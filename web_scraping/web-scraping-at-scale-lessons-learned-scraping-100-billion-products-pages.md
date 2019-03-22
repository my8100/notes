### **:link: Source**: [https://blog.scrapinghub.com/web-scraping-at-scale-lessons-learned-scraping-100-billion-products-pages](https://blog.scrapinghub.com/web-scraping-at-scale-lessons-learned-scraping-100-billion-products-pages)

FOR E-COMMERCE DATA SCIENTISTS: LESSONS LEARNED SCRAPING 100 BILLION PRODUCTS PAGES
===================================================================================

 [July 02, 2018](https://blog.scrapinghub.com/web-scraping-at-scale-lessons-learned-scraping-100-billion-products-pages)
 [Ian Kerins](https://blog.scrapinghub.com/author/ian-kerins)
 [11 Comments](https://blog.scrapinghub.com/web-scraping-at-scale-lessons-learned-scraping-100-billion-products-pages#comments-listing)

-   [What's Important When Scraping At Scale?](#whats-important-when-scraping-at-scale)
-   [Challenge #1 - Sloppy and Always Changing Website Formats](#challenge-1---sloppy-and-always-changing-website-formats)
    -   [No Easy Solution](#no-easy-solution)
-   [Challenge 2: Scalable Architecture](#challenge-2-scalable-architecture)
    -   [Separate Product Discovery From Product Extraction](#separate-product-discovery-from-product-extraction)
    -   [Allocate More Resources To Product Extraction](#allocate-more-resources-to-product-extraction)
-   [Challenge 3: Maintaining Throughput Performance](#challenge-3-maintaining-throughput-performance)
    -   [Crawling Efficiency](#crawling-efficiency)
-   [Challenge 4: Anti-Bot Countermeasures](#challenge-4-anti-bot-countermeasures)
    -   [Proxies](#proxies)
    -   [Beyond Proxies](#beyond-proxies)
-   [Challenge 5: Data Quality](#challenge-5-data-quality)
-   [Wrapping Things Up](#wrapping-things-up)

Web scraping can look deceptively easy these days. There are numerous open-source libraries/frameworks, visual scraping tools and data extraction tools that make it very easy to scrape data from a website. However, when you want to scrape websites at scale things start to get very tricky, very fast.

In this series of articles, we will share with you the lessons we've learned scraping over 100 billion product pages since 2010, give you an in-depth look at the challenges you will face when extracting product data from e-commerce stores at scale and share with you some of the best practices to address those challenges.

In this article, the first of the series, we will give you a overview of the main challenges you will face scraping product data at scale and the lessons Scrapinghub has learned from scraping 100 billion product pages.

Founded in 2010, Scrapinghub is one of the leading data extraction companies and the author of Scrapy, the most robust and popular web scraping framework available today. Currently, Scrapinghub scrapes over 8 billion pages per month (3 billion of which are product pages) for many of the largest e-commerce companies in the world.

For those of you who are interested in scraping the web at scale but are wrestling with the decision of whether or not you should build up a dedicated web scraping team in-house or outsource it to a dedicated web scraping firm then be sure to check out our free guide, [**Enterprise Web Scraping: A Guide to Scraping the Web at Scale**](https://info.scrapinghub.com/enterprise-web-scraping-scraping-at-scale-1).

**What's Important When Scraping At Scale?**
--------------------------------------------

Unlike your standard web scraping application, scraping e-commerce product data at scale has a unique set of challenges that make web scraping vastly more difficult.

At its core, these challenges can be boiled down to two things: **speed** and **data quality**.

**从本质上讲，这些挑战可以归结为两个方面：速度和数据质量。**

As time is usually a limiting constraint, scraping at scale requires your crawlers to scrape the web at very high speeds without compromising data quality. This need for speed makes scraping large volumes of product data very challenging.

![web scraping product data scale - sloppy code](https://user-gold-cdn.xitu.io/2019/3/21/1699e52253cb54cf?w=600&h=300&f=jpeg&s=42924)

**Challenge #1 - Sloppy and Always Changing Website Formats**
-------------------------------------------------------------

It might be obvious and it might not be the sexiest challenge, but sloppy and always changing website formats is by far the biggest challenge you will face when extracting data at scale. Not necessarily because of the complexity of the task, but the time and resources you will spend dealing with it.

If you have spent any length of time building crawlers for e-commerce stores you'll know that there is a epidemic of sloppy code on e-commerce stores. There's more to it than HTML well-formedness or the occasional character encoding problem. We've run into all sorts of colorful issues over the years - misused HTTP response codes, broken JavaScripts, or misuse of Ajax:

**爬虫过程中所遇到的各种各样的问题——错误使用 HTTP 响应代码，异常的 JavaScripts 代码，以及滥用 Ajax：**

-   Stores that remove pages when they discontinue products and suddenly begin to return 200 response codes on its 404 error handler after a website upgrade.
-   Improperly escaped JSON data that break javascript on some pages (e.g. 'b0rk'd'), resulting in you needing to scrape that data using regular expressions.
-   Stores that abuse Ajax calls so much that you can only get the information you're after by either rendering the page (resulting in much slower crawls) or mimicking the API calls (resulting in more development effort).

Sloppy（稀松的；马虎的；凌乱的）code like this can make writing your spider a pain, but can also make visual scraping tools or automatic extraction tools unviable.

When scraping at scale, not only do you have to navigate potentially hundreds of websites with sloppy code, you will also have to deal with constantly evolving websites. A good rule of thumb is to expect your target website to make changes that will break your spider (drop in data extraction coverage or quality) every 2-3 months.

**一个好的经验法则是预期目标网站每2-3个月会发生改变，而导致爬虫的数据提取覆盖率或质量的下降。**

That mightn't sound like too big a deal but when you are scraping at scale, those incidents really add up. For example, one of Scrapinghub's larger e-commerce projects has ~4,000 spiders targeting about 1,000 e-commerce websites, meaning they can experience 20-30 spiders failing per day.

Variations in website layouts from regional and multilingual websites, A/B split testing and packaging/pricing variants also create a world of problems that routinely break spiders.

### **No Easy Solution**

Unfortunately, there is no magic bullet that will completely solve these problems. A lot of the time it just a matter of committing more resources to your project as you scale. To take the previous project as a example again, that project has a team of full-time 18 crawl engineers and 3 dedicated QA engineers to ensure the client always has reliable data feed.

With experience however, your team will learn to create ever more robust spiders that can detect and deal with quirks（怪异模式）in your target websites format.

Instead of having multiple spiders for all the possible layouts a target website might use, it is best practice to have only one product extraction spider that can deal with all the possible rules and schemes used by different page layouts. The more configurable your spiders are the better.

**最佳做法是只使用一个爬虫专门用于产品信息提取，该爬虫能够处理目标网站的各种页面布局所使用的所有可能的规则和图式/方案，且可以灵活配置，而不是使用多个爬虫处理目标网站所可能使用的不同布局。**

Although these practices will make your spiders more complex (some of our spiders are thousands of lines long), it will ensure that your spiders are easier to maintain.
**这些实践做法虽然会导致爬虫代码更复杂（可能多达数千行），但确保了代码易于维护。**

![earthquake-taipei-101-640x640](https://user-gold-cdn.xitu.io/2019/3/21/1699e5225af88c63?w=600&h=400&f=jpeg&s=47307)

**Challenge 2: Scalable Architecture**
--------------------------------------
**可扩展架构**

The next challenge you will face is building a crawling infrastructure that will scale as the number of requests per day increases, without degrading in performance.

When extracting product data at scale a simple web crawler that crawls and scrapes data serially just won't cut it. Typically, a serial web scraper will make requests in a loop, one after the other, with each request taking 2-3 seconds to complete.

This approach is fine if your crawler is only required to make < 40,000 requests per day (request every 2 seconds equals 43,200 request per day). However, past this point you will need to transition to a crawling architecture that will allow you to scrape millions of requests per day with no decrease in performance.

As this topic warrants a article onto itself, in the coming weeks we will publish a dedicated article discussing the how to design and build your own high throughput scraping architecture. However, for the remainder of this section we will discuss some of the higher level principles and best practices.

**将发表一篇专门的文章，讨论如何设计和构建高吞吐量抓取架构。**

As we've discussed, speed is key when it comes to scraping product data at scale. You need to ensure that you can find and scrape all the required product pages in the time allotted (often one day). To do this you need to do the following:

### **Separate Product Discovery From Product Extraction**

To scrape product data at scale you need to separate your product discovery spiders from your product extraction spiders.

**为了大规模爬取产品数据，必须将用于在产品目录中提取产品链接的爬虫和用于提取产品信息的爬虫区分开来**

The goal of the product discovery spider should be for it to navigate to the target product category (or "shelf") and store URLs of the products in that category for the product extraction spiders. As the product discovery spider adds product URLs to the queue the product extraction spiders scrape the target data from that product page.

This can be accomplished with the aid of a crawl frontier such as [Frontera](https://github.com/scrapinghub/frontera), the open source crawl frontier developed by Scrapinghub. While Frontera was originally designed for use with Scrapy, it's completely agnostic and can be used with any other crawling framework or standalone project. In this guide, we share how you can [use Frontera to scrape at scale](http://frontera.readthedocs.io/en/latest/topics/cluster-setup.html).

### **Allocate More Resources To Product Extraction**

As each product category "shelf" can contain anywhere from 10 to 100 products and extracting product data is more resource heavy than extracting a product URL, discovery spiders typically run faster than product extraction spiders. When this is the case, you need to have multiple extraction spiders for every discovery spider. A good rule of thumb is to create a separate extraction spider for each ~100,000 page bucket.

**应该为用于提取产品信息的爬虫分配更多的资源，如每100K网页分配一个单独的提取爬虫。**

![sp02-vettel](https://user-gold-cdn.xitu.io/2019/3/21/1699e522ecb814a6?w=599&h=337&f=jpeg&s=32937)

**Challenge 3: Maintaining Throughput Performance**
---------------------------------------------------

Scraping at scale can easily be compared to Formula 1 where you goal is to shave every unnecessary gram of weight from your car and squeeze that last fraction of a horsepower from the engine all in the name of speed. The same is true for web scraping at scale.

When extracting large volumes of data you are always on the lookout for ways to minimise the request cycle time and maximise your spiders performance of the available hardware resources. All in the hope that you can shave a couple milliseconds off each request.

To do this your team will need to develop a deep understanding of the web scraping framework, proxy management and hardware you are using so you can tune them for optimal performance. You will also need to focus on:

### **Crawling Efficiency**

When scraping at scale you should always be focused on solely extracting the exact data you need in as few requests as possible. Any additional requests or data extraction slow the pace at which you can crawl a website. Keep these tips in mind when designing your spiders:

**应始终专注于用尽可能少的请求来达到提取所需数据的目标。**

-   Only use a headless browsers, such as Splash or Puppeteer, to render javascript as a last resort. Rendering javascript with a headless browser whilst crawling is very resource intensive and severely impacts the speeds at which you can crawl. 将使用无头浏览器渲染 javascript 作为最后的手段
-   If you can get the data you need from the shelf page (e.x. Product names, price, ratings, etc.) without requesting each individual product page, then don't request the product pages. 善用产品目录页面
-   Don't request or extract images unless you really have to. 如非必要，不要请求或提取图片

![Web scraping at scale - bot detection](https://user-gold-cdn.xitu.io/2019/3/21/1699e5225b0addee?w=600&h=400&f=jpeg&s=57084)

**Challenge 4: Anti-Bot Countermeasures**
-----------------------------------------
**对抗反爬虫**

If you are scraping e-commerce sites at scale you are guaranteed to run into websites employing anti-bot countermeasures.

For most smaller websites their anti-bot countermeasures will be quite basic (ban IPs making excess requests). However, larger e-commerce websites such as Amazon, etc. make use of sophisticated anti-bot countermeasures such as Distil Networks, Incapsula, or Akamai, that make extracting data significantly more difficult.

### **Proxies**
**大规模爬取的首要需求，代理外包**

With that in mind the first and most essential requirement for any project scraping product data at scale is to use proxy IPs. **When scraping at scale you will need a sizeable list of proxies, and will need to implement the necessary IP rotation, request throttling, session management and blacklisting logic to prevent your proxies from getting blocked.**

Unless, you have or are willing to commit a sizeable team to manage your proxies you should outsource this part of the scraping process. There are a huge number of proxy services available who provide varying levels of service.

**However, our recommendation is to go with a proxy provider who can provide a single endpoint for proxy configuration and hide all the complexities of managing your proxies.** Scraping at scale is resource intensive enough without trying to reinvent the wheel by developing and maintaining your own internal proxy management infrastructure.

This is the approach most of the large e-commerce companies use. A number of the worlds largest e-commerce companies use [Crawlera](https://scrapinghub.com/crawlera), the smart downloader developed by Scrapinghub, that completely outsource their proxy management. When your crawlers are making 20 million requests per day, it makes much more sense to focus on analysing the data not managing proxies.

### **Beyond Proxies**
**反爬虫逆向**

Unfortunately, just using a proxy service won't be enough to ensure you can evade bot countermeasures on larger e-commerce websites. More and more websites are using sophisticated anti-bot countermeasures that monitor your crawlers behaviour to detect that it isn't a real human visitor.

Not only do these anti-bot countermeasures make scraping e-commerce sites more difficult, overcoming them can significantly dent your crawlers performance if done incorrectly.

**A large proportion of these bot countermeasures use javascript to determine if the request is coming from a crawler or a human (Javascript engine checks, font enumeration, WebGL and Canvas, etc.).**

However as mentioned previously, when scraping at scale you want to limit your usage of scriptable headless browsers such as Splash or Puppeteer, that render any javascript on the page as they are very heavy on resources and slow the speed at which you can scrape a website.

This means that to ensure you can achieve the necessary throughput from your spiders to deliver daily product data **you often need to painstakingly reverse engineer the anti-bot countermeasures used on the site and design your spider to counteract them without using a headless browser.**

**Challenge 5: Data Quality**
-----------------------------

From a data scientists perspective the most important consideration of any web scraping project is the quality of the data being extracted. Scraping at scale only makes this focus on data quality even more important.

When extracting millions of data points every single day, it is impossible to manually verify that all your data is clean and intact. It is very easy for dirty or incomplete data to creep into your data feeds and disrupt your data analysis efforts.

This is especially true when scraping products on multiple versions of the same store (different languages, regions, etc.) or separate stores.

Outside of a careful QA process during the design phase of the building the spider, where the code of the spider is peer reviewed and tested to ensure that it is extracting the desired data in the most reliable way possible. **The best method of ensuring the highest possible data quality is the development of a automated QA monitoring system.**

As part of any data extraction project you need to plan and develop a monitoring system that will alert you of any data for inconsistencies and spider errors. At Scrapinghub we've developed machine learning algorithms designed to detect:

-   **Data Validation Errors** - Every data item has a defined data type and values that follow a consistent pattern. Our data validation algorithms will flag to the projects QA team any data items that are inconsistent with what is to expected for that data type, from which point the data is manually checked and alert verified or been flagged as a error.
-   **Product Variation Errors** -  When scraping the same product data from multiple versions of the same website (different languages, regions, etc.) it is possible that variable and supposedly fixed values such as product weight or dimensions can vary. This can be the result of a websites anti-bot countermeasures giving one or more of your crawlers **falsified（伪造的） information**. Again, you need to have algorithms in place to identify and flag any occurrences such as this.
-   **Volume Based Inconsistencies** - Another key monitoring script is one that detects any abnormal variations in the number of records returned. This could signify that there have been changes made to the website or that your crawler is being fed falsified information.
-   **Site Changes** - Structural changes happening to the target websites is the main reason why crawlers break. This is monitored by our dedicated monitoring system, quite aggressively. **The tool performs frequent checks on the target site to make sure nothing has changed since the previous crawl.** If changes are found, it sends out notifications for the same.

All of which we will discuss in a later article dedicated to automated quality assurance.

**Wrapping Things Up**
----------------------

As you have seen scraping product data at scale creates its own unique set of challenges. Hopefully, this article has made you more aware of the challenges you will face and how you should go about solving them.

However, this is just the first article in this series so if you are interested in reading the next articles as soon as they are published be sure to sign up to our email list.

For those of you who are interested in scraping the web at scale but are wrestling with the decision of whether or not you should build up a dedicated web scraping team in-house or outsource it to a dedicated web scraping firm then be sure to check out our guide, **[E](https://info.scrapinghub.com/enterprise-web-scraping-build-inhouse-or-outsource)[nterprise Web Scraping: Build In-House or Outsource](https://info.scrapinghub.com/enterprise-web-scraping-build-inhouse-or-outsource)**.

[![New call-to-action](https://user-gold-cdn.xitu.io/2019/3/21/1699e5225e06bef7?w=1500&h=785&f=jpeg&s=89645)](https://blog.scrapinghub.com/cs/c/?cta_guid=15b13819-b573-4985-8941-093bfcdc3377&placement_guid=421a097a-aaa9-4d4a-9db3-0f8630a76792&portal_id=4367560&canon=https%3A%2F%2Fblog.scrapinghub.com%2Fweb-scraping-at-scale-lessons-learned-scraping-100-billion-products-pages&redirect_url=APefjpF4eN9Q_hH0PpJCVTZgNwojrTuHQNd9wz7q3R4qu2z64KFmTivJfS209TImZB3qkXu82MFvvy5J31JFzZuSTjz6N2aqCIgPMe842s4DoLQEHLADi_YqYZ6anl775grfDn6Z3nmWXItBGtHwKxV9WEHElDxqhXV2kMNmvdSeM1g4HF5UOKt3NOozIdXUg3ykVAga7b_-Nb4Y1CYHSB5PaR2EyqecOxe1ItioGUVC2T-Bho-JA1wCYHbbCY5BD6RTs-Rm9KqJ5W6-V0gzPkxJQe0TYx65IjrBlZYvNnWTJSQPma_vZ3Y&click=20d0962c-2dc2-47da-ac01-6e41bf00855e&hsutk=76a92f1991dbe4ba72bcc2e275cf16aa&pageId=5925219067&__hstc=234333761.76a92f1991dbe4ba72bcc2e275cf16aa.1525929391471.1542738283183.1553139143315.14&__hssc=234333761.1.1553139143315&__hsfp=3861380900)

At Scrapinghub we specialize in turning unstructured web data into structured data. If you would like to learn more about how you can use web scraped product data in your business then feel free to [contact our sales team,](https://scrapinghub.com/enterprise-solutions) who will talk you through the services we offer startups right through to Fortune 100 companies.

At Scrapinghub we always love to hear what our readers think of our content and any questions you might. So please leave a comment below with what you thought of the article and what you are working on.
