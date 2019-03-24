**:link: Source**: [https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking](https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking)

Asynchronous programming. Blocking I/O and non-blocking I/O
===========================================================

Wed Feb 06 2019 | ☕ 9 minute read

![Asynchronous programming. Blocking I/O and non-blocking I/O](https://mirror-gold-cdn.xitu.io/-temp/15532523869591122b?w=2732&h=2048&f=jpeg&s=160334)

-   [Blocking I/O](#blocking-io)
-   [Non-blocking I/O](#non-blocking-io)
-   [Multitasking](#multitasking)
    -   [Separate processes](#separate-processes)
    -   [Threads(OS )](#threadsos-)
-   [Conclusion](#conclusion)

This is the first post of a series about **asynchronous programming**（[eɪ'sɪŋkrənəs] 异步编程）. The whole series tries to answer the simple question: "What is asynchrony?".

At first, when I just started **digging into**（[dɪɡ] 深入钻研） the question - I thought that I know what it is. It turned out that I didn't know a clue about（**do not have a clue about** 对...一无所知/毫无线索） what asynchrony is all about. So, let's find out!

Whole series:

-   [Asynchronous programming. Blocking I/O and non-blocking I/O](https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking)
-   [Asynchronous programming. Cooperative multitasking](https://luminousmen.com/post/asynchronous-programming-cooperative-multitasking)
-   [Asynchronous programming. Await the Future](https://luminousmen.com/post/asynchronous-programming-await-the-future)
-   [Asynchronous programming. Python3.5+](https://luminousmen.com/post/asynchronous-programming-python3.5)

In this post, we will be talking about networking but you can easily map it to other input/output(I/O) operation, for example, **change sockets to file descriptors**（文件描述符）. And this is the explanation not focusing on any specific programming language although the examples will be in Python(what can I say --- I love Python).

* * * * *

In client-server applications, when a client makes a request to a server, the server processes the request and sends back a response. For this to happen, both the client and the server first need to establish a connection with one another and **that's where the sockets come into play**（发挥作用的地方）. **Both the client and the server has to bind itself to a socket at the end and the server starts listening to its socket for the client to make a request.**

客户端和服务器都必须将自己绑定到套接字：
1. 服务器开始监听其套接字：s.bind((host, port))    s.listen(5)
2. 客户端发出请求：s.connect((host, port))
3. 服务器接受并建立连接：conn, addr = s.accept()

![client-server application](https://user-gold-cdn.xitu.io/2019/3/22/169a5d5f7353d61d?w=2732&h=2048&f=jpeg&s=118612)

If you look at the ratio of processor speed and network connectivity, the differences are a couple of **orders of magnitude**（数量级）. It turns out that if our application uses I/O, then the CPU doesn't do anything most of the time, that type of applications called **I/O-bound**（I/O 绑定/密集型）. For applications which require high performance, this is **a major roadblock** as other activities and other I/O operations are kept waiting --- it turns out these systems are all **slackers**（怠惰的人）.

**There are 3 options for organizing I/O: *blocking*, *non-blocking* and *asynchronous*.** The last one does not work with the networking, so, there are 2 options for us --- blocking and non-blocking.

Blocking I/O
------------

Consider this option on the example of UNIX(POSIX) [BSD sockets](https://en.wikipedia.org/wiki/Berkeley_sockets)(in Windows all the same --- the calls will be different, but the logic is the same).

With blocking I/O, when a client makes a request to connect to the server, **the socket that handles that connection is blocked until there is some data to read, or the data is fully written. Until the operation is complete server can't do anything else but wait.** From this follows the simplest conclusion: within a single execution thread, we cannot serve more than one connection. By default, TCP sockets are placed in a blocking mode.

处理来自 client 的连接的 socket 将阻塞 server 主进程/主线程，除非出现可读数据或直到数据已经接收完毕。 

Simple example on Python, client:

```
import socket

sock = socket.socket()

host = socket.gethostname()
sock.connect((host, 12345))

data = b"Foo Bar" *10*1024 # Send a lot of data to be sent
assert sock.send(data) # Send data till true
print("Data sent")

```

And the server:

```
import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

s.bind((host, port))
s.listen(5)

while True:
	conn, addr = s.accept()
	data = conn.recv(1024)  # block until there is some data to read, or the data is fully written.	
	while data:
		print(data)
		data = conn.recv(1024)  # block until there is some data to read, or the data is fully written.
	print("Data Received")
	conn.close()
	break

```

You'll notice that the server keeps on printing our message "". This will go on and on till all the data is sent. In the above code, the "Data Received" message will not be printed for while because the client has to send a huge amount of data, which will take time, and until then the socket **will get blocked**.

What's going on here? The `send()` method will try to transmit all the data to the server, while the **write buffer** on the client will keep getting the data. **When the buffer becomes empty, the kernel will wake the process up again to get the next chunk of data that is to be transferred.** In short, your code will block and it will not let anything else proceed.

Now to fulfill **[concurrent](https://luminousmen.com/post/concurrency-and-parallelism-are-different)** requests with this approach we need to have multiple threads, that is we need to allocate a new thread for each client connection. We will talk about that in a minute.

Non-blocking I/O
----------------

But there is a second option --- **non-blocking I/O**. From the wording, the differences are obvious --- instead of blocking, any operation from the client perspective is completed immediately. **Non-blocking I/O means a request is queued straight away and the function returns. The actual I/O is then processed at some later point.**

Go back to our example with some changes in client:

```
import socket

sock = socket.socket()

host = socket.gethostname()
sock.connect((host, 12345))
sock.setblocking(0) # Now setting to non-blocking mode

data = b"Foo Bar" *10*1024
assert sock.send(data)
print("Data sent")

```

Now, if we run this code, you'll notice that the program will run for a small time, it will print "Data sent" and terminate.

What's going on here? Here the client did not send all the data. When we make a socket non-blocking by calling `setblocking(0)`, it will never wait for the operation to complete. So when we call the `send()` method, it will put as much data in the buffer as possible and return.

With this option, we can perform several I/O operations with different sockets from one thread at the same time. But, since it is not known whether the socket is ready for I/O operation, we would have to contact each socket with the same question and, in fact, spin in an endless loop.

To get rid of this inefficient loop a **polling readiness mechanism**（轮询准备状态的机制） is needed, where we could poll readiness of all the sockets, and they tell us which of them are ready for new I/O operation or not. When any of sockets are ready, we would perform queued operations, after which we could go back to blocking state, waiting for the sockets that are ready for next I/O operation again.

There are several mechanisms for polling readiness, they differ in performance and details, but usually, details are hidden "under the hood" and are not visible to us.

**Keywords to search:**

Notifications:

-   Level Triggering (state)
-   Edge Triggering (state changed)

Mechanics:

-   `select()`, `poll()`
-   `epoll()`, `kqueue()`
-   `EAGAIN`, `EWOULDBLOCK`

Multitasking
------------

So, our goal is to manage multiple clients concurrently. How can we ensure the simultaneous processing of multiple requests?

There are several options:

### Separate processes

![client-server application](https://user-gold-cdn.xitu.io/2019/3/24/169af22504ee360a?w=2732&h=2048&f=jpeg&s=148403)

The easiest and historically the first approach is to process each request in a separate process. This is good because we can use the same blocking I/O API. If the process suddenly crashes, it will only affect the operations that processed in this one particular process, but not any others.

*Minus*（负面的，缺点） --- **difficult communication**. Formally, there is almost nothing in common between processes, and any *nontrivial*（非凡的，不容易的） communication that we want to organize requires *additional efforts*（额外的努力） to synchronize access, etc. Also at any given point in time, there can be multiple processes just waiting for the client requests and that is just a waste of resources.

Let's look on how this work in practice: **usually the first process(main process/master process) starts, it does, for example, listen, then it spawns some set of processes（[spɔn] 产卵，衍生一系列进程）as workers, each of whom can accept on the same socket and waits for incoming connections.** As soon as an incoming connection appears, one of the processes is occupied --- it receives this connection, processes it from beginning to the end, closes the socket, and is again ready to fulfill the next request. Variations are possible --- the process can be generated for each incoming connection or they are all started in advance, etc. This may affect the performance characteristics, but now it is not so important for us.

Examples of such systems:

-   Apache `mod_prefork`;

-   FastCGI for those who most often run PHP;（[wiki/FastCGI](https://en.wikipedia.org/wiki/FastCGI)：Instead of creating a new process for each request, FastCGI uses persistent processes to handle a series of requests.） 

-   Phusion Passenger for those who write on Ruby on Rails;

-   PostgreSQL.

### Threads(OS )

Another approach is to use [Operating System](https://en.wikipedia.org/wiki/Operating_system)(OS) threads. Within one process, we spawn multiple threads. Blocking I/O also can be used, because only one thread will be blocked. OS itself manages threads, it is able to scatter them between processors.（操作系统负责管理线程，使之分布于多个处理器） **Threads are lighter than processes**. *In essence*（['esəns] 本质上）, this means that we can generate more threads on the same system. **We can hardly run 10 thousand processes, but 10 thousand threads can be easy.** Not that it will be effective, but, nevertheless, they are somewhat more lightweight.

On the other hand, there is **no isolation**（[.aɪsə'leɪʃ(ə)n] 隔离
）, i.e. if some kind of crash occurs, it will crash not only one particular thread but the whole process. **And the biggest difficulty is that the process memory where threads are working is shared between the threads.** We have shared resource --- memory, which means that there is a **need to synchronize access**. And the issue of synchronization of access to shared memory --- it is the simplest case, but, for example, there may be a connection to the database, or a pool of connections to the database, which is common to all threads inside the application that processes incoming connections. To synchronize access to a resource is difficult to conduct correctly.

There are some problems:

1.  First of all --- it is possible **[deadlocks](https://en.wikipedia.org/wiki/Deadlock)** during the synchronization process. A deadlock occurs when a process or thread enters a waiting state because a requested system resource is held by another waiting process, which in turn is waiting for another resource held by another waiting process;

2.  **Insufficient synchronization**, when we have competitive access to shared data. Roughly speaking, two threads change data simultaneously and spoils them. Such programs are harder to debug, not all bugs appear immediately. For example, the famous [GIL](https://en.wikipedia.org/wiki/Global_interpreter_lock) --- Global Interpreter Lock --- is one of the easiest ways to make a multi-threaded application. When using GIL we say that all data structures, all our memory is protected by just one lock on the whole process. *It would seem that this means that*（这似乎意味着） multithreaded execution is impossible because only one thread can be executed, there is only one lock, and someone has captured it, all the others cannot work. Yes, this is true, but remember that **most of the time we do not do any computations on threads, but network I/O operations, so at the moment when a blocking I/O operation is accessed, GIL goes down, the thread resets and in fact switching to another thread that is ready for execution.** Therefore, from the backend point of view, using GIL may not be so bad. Using GIL is *scary*（可怕的，吓人的） when you try to multiply a matrix in several threads --- this is *pointless*（无意义的） because only one thread will be executed at a time(it's not totally true, but this is another story).

Conclusion
----------

Blocking methods execute synchronously --- you run application and it's operations executing straight after calls.

Non-blocking methods execute asynchronously --- you run application and the non-blocking operations returns right away, but the actual work is stating later.

There are several approaches in implementation of multitasking: threads and processes.

In the next post we will be talking about **cooperative multitasking**（[koʊ'ɑp(ə)rətɪv]
协作式多任务） and its implementations.