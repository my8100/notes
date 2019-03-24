**:link: Source**: [https://blog.scrapinghub.com/web-scraping-gdpr-compliance-guide](https://blog.scrapinghub.com/web-scraping-gdpr-compliance-guide)

GDPR COMPLIANCE FOR WEB SCRAPERS: THE STEP-BY-STEP GUIDE
========================================================
The EU General Data Protection Regulation (GDPR) 欧盟通用数据保护条例


 [July 25, 2018 ](https://blog.scrapinghub.com/web-scraping-gdpr-compliance-guide) [Ian Kerins](https://blog.scrapinghub.com/author/ian-kerins) [2 Comments](https://blog.scrapinghub.com/web-scraping-gdpr-compliance-guide#comments-listing)

-   [Step 1: Are You Scraping Personal Data?](#step-1-are-you-scraping-personal-data)
-   [Step 2: Are Your Scraping the Personal Data Of EU Residents?](#step-2-are-your-scraping-the-personal-data-of-eu-residents)
-   [Step 3: Do You Have A Lawful Reason to Scrape Their Personal Data?](#step-3-do-you-have-a-lawful-reason-to-scrape-their-personal-data)
    -   [Consent](#consent)
    -   [Legitimate Interest](#legitimate-interest)
-   [Step 4: Assess The Personal Data Being Scraped](#step-4-assess-the-personal-data-being-scraped)
    -   [Reason #1: Prevent the Scraping of Sensitive Data](#reason-1-prevent-the-scraping-of-sensitive-data)
    -   [Reason #2: Minimise the Extent of The Data Extraction](#reason-2-minimise-the-extent-of-the-data-extraction)
    -   [Reason #3: Ensure Personal Data Is Used For Legitimate Business Purposes](#reason-3-ensure-personal-data-is-used-for-legitimate-business-purposes)
-   [Step 5: Ensure The Correct Data Retention And Access Policies Are In Place](#step-5-ensure-the-correct-data-retention-and-access-policies-are-in-place)
-   [Step 6: Make Sure Your Residential IPs Are GDPR Compliant](#step-6-make-sure-your-residential-ips-are-gdpr-compliant)
-   [Old Web Scraping Projects](#old-web-scraping-projects)
-   [Conclusion](#conclusion)

Unless you've been living under a rock for the past few months you know that the EU's General Data Protection Regulation (GDPR) is upon us.

It is the most **comprehensive**（全面的） data protection law ever been introduced, fundamentally changing the way companies can use the personal data of their customers and **prospects**（潜在用户）.

There are countless articles and guides about how GDPR will affect your company's marketing efforts, lead generation, etc. and the changes you'll need to make to ensure your company is in full **compliance with**（遵守） the law.

**But when it comes to web scraping....nothing.**

Which is strange given that web scraping has traditionally been the backbone of many companies marketing, lead generation and market intelligence efforts.

To shed some light on this **grey area**（灰色地带）, I sat down with Sanaea Daruwalla, Head of Legal at Scrapinghub, to get her insights on how Scrapinghub ensures our clients are scraping personal data in a GDPR **compliant**（[kəm'plaɪənt] 兼容，(与一系列规则)符合的） way.

In this guide I will share with you:

-   How GDPR is going to impact web scraping (**Answer**: **unless you have the person's explicit consent（明确同意） it is now illegal to scrape a EU residents personal data under GDPR**).
-   The exact **decision making process**（决策过程） Sanaea uses when evaluating the GDPR compliance of a web scraping project, and
-   Answer the most **pressing**（紧迫的） questions web scrapers have about GDPR compliance.

Before we get started though, I want to highlight a quick **disclaimer**（免责声明）.

**Disclaimer**: I am not a lawyer, and the recommendations in this guide **do not constitute legal advice**（不构成法律意见）. Our Head of Legal is a lawyer, but she's not your lawyer, so none of her opinions or recommendations in this guide constitute legal advice from her to you. The commentary and recommendations outlined below are based on Scrapinghub's experience helping our clients (startups to Fortune 100's) maintain GDPR compliance whilst scraping 7 billion web pages per month. If you want assistance with your specific situation then you should consult a lawyer.

**Now with the technicalities out of the way**（抛开技术细节？！）, let's talk about how you should **evaluate**（评估） your web scraping project for GDPR compliance.

**Step 1: Are You Scraping Personal Data?**
-------------------------------------------

This is the very first and most obvious question you should be asking yourself when you are **instigating**（教唆,挑起,煽动,怂恿） a web scraping project.

**The General Data Protection Regulation, or GDPR as it is more commonly known, only applies to personal data.** Which is defined as any **personally identifiable information (PII)**（个人身份信息） that could be used to directly or indirectly identify a specific individual. Examples of personal data include a person's:

-   Name
-   Physical Address
-   Email Address
-   Phone Number
-   Credit Card Details
-   Bank Details
-   IP Address
-   Date of Birth
-   Employment Info
-   Social Security Number
-   Medical Information
-   Video/Audio Recording

**If you aren't scraping personal data, then GDPR does not apply.** However, if you are scraping personal data then move to step 2.

![gdpr-compliance-web-scraping-eu-residents](https://user-gold-cdn.xitu.io/2019/3/22/169a44063d624663?w=599&h=345&f=jpeg&s=65312)

**Step 2: Are Your Scraping the Personal Data Of EU Residents?**
----------------------------------------------------------------

If you are scraping personal data then the next question you need to ask yourself is whether or not you are scraping the personal data of EU citizens or residents (note that the GDPR actually covers the EEA, which includes all EU countries, plus Iceland, Liechtenstein, and Norway, so it's a bit broader than just the EU).

**GDPR is an EEA specific regulation, so it only applies to EU citizens.** If you are scraping the personal information of residents of other countries (ex. US, Canada, Australia, etc.) then GDPR may not apply. You just need to **comply with**（[kəm'plaɪ] 遵守） the data protection laws **in the jurisdiction**（司法管辖权；管辖区） that you scraping personal data from.

![gdpr-compliance-web-scraping-consent](https://user-gold-cdn.xitu.io/2019/3/22/169a4406344f1538?w=600&h=400&f=jpeg&s=17326)

**Step 3: Do You Have A Lawful Reason to Scrape Their Personal Data?**
----------------------------------------------------------------------

Ok, now we are starting to get into **the nuts and bolts**（螺母和螺丝
the basic details of a job or activity） of GDPR. We now know we are scraping personal data and there will be EU citizens affected. The next question we need to ask yourselves is:

*Do we have a lawful reason to scrape the personal data of these EU citizens?*

Under GDPR to use or hold the personal data of any EU citizen a company must comply with one or more of the following legal reasons for storing or using their personal data, otherwise they will be in breach of the regulation. The five types of lawful reasons are:

-   **Consent** - the data subject (person whose data we have) consented to us having their data.
-   **Contract** - the personal data is required for performance of a contract with the data subject.
-   **Compliance** - necessary for compliance with a legal obligation.
-   **Vital Interest, Public Interest, or Official Authority** - typically only applicable for state run bodies where access to personal data is in the public's interest.
-   **Legitimate Interest** - necessary for our legitimate interests.

When a client comes to Scrapinghub looking to scrape the personal data of EU residents we **take it on a case by case basis**（根据具体情况进行处理，a case-by-case 个案） because it is vital that you can prove that you have a lawful reason to scrape that data.

The most common legal reasons in the case of web scraping are **legitimate interest**（[lə'dʒɪtəmət] 合法权益） and **consent**（ [kən'sent] 同意，允许）.

First, let's take a look at consent...

### **Consent**

For most web scrapers, demonstrating that you have consent from the individual to scrape their personal data will be the main (and often only) method in which you can lawfully scrape the personal data from EU residents.

Prior to the commencement of GDPR, there was a lot of discussion within the web scraping community on whether an EU resident had to **implicitly**（隐式） give their consent for companies to scrape their personal data if it was available on public websites (no login required to see the data).

The argument was that by uploading personal data to a public site you are giving consent for that data to be viewed and stored by 3rd parties.

However, after in-depth review of this argument by Sanaea (Head of Legal at Scrapinghub) and external legal experts contracted by Scrapinghub we concluded that this interpretation of the regulations wasn't compliant with GDPR.

**As a result, to scrape the personal data of EU residents you now need to demonstrate（演示，证明） that you have the explicit consent（明确同意） of the individual before scraping their personal data.**

A lot of web scrapers mightn't like this position, but after a careful review of all the guidance documents provided by the commission Scrapinghub believes that adopting this policy is the only one that is guaranteed to prevent you and your company **falling foul to**（fall foul [faʊl] of sb/sth (因做错事或不法行为)与…发生麻烦） GDPR.

Obviously, this interpretation of the GDPR regulations will significantly curtail（[kɜr'teɪl]
缩短；限制；减缩） most web scraping projects focused on extraction of the personal information of EU residents for lead generation, market analysis, etc.

However, it will still enable some companies to scrape the personal data of EU citizens if they have obtained their explicit content to do so. An example of this would be companies like Mint.com, where users give Mint consent to log into their online banking accounts and retrieve their banking transactions so that they can be tracked and displayed in a more user friendly format on Mint.com.

Next, we'll look at using "legitimate interest" as the your lawful reason for scraping the personal data of EU citizens.

### **Legitimate Interest**

The other likely lawful reason available to web scrapers is if they can demonstrate they have a legitimate interest in scraping/storing/using this personal data.

Although this lawful reason is viable for web scrapers, for most companies it will be very difficult for them to demonstrate that they have a legitimate interest in scraping someone's personal data.

In most cases, only governments, **law enforcement agencies**（执法部门）, etc. will have what would be **deemed**（ [diːm] 认为，视为） a to have a legitimate interest in scraping the personal data of its citizens as they will typically be scraping people's personal data for the **public good**（公共利益）.

![gdpr-compliance-web-scraping-personal data](https://user-gold-cdn.xitu.io/2019/3/22/169a440630549c58?w=599&h=291&f=jpeg&s=30187)

**Step 4: Assess The Personal Data Being Scraped**
--------------------------------------------------

As mentioned in Step 3, when a client approaches Scrapinghub looking to scrape the publicly available personal data of EU residents we take it on a case by case basis and work with the client to ensure that this data is being extracted in a GDPR compliant manner.

During this stage not only do we look at the companies lawful reason for scraping personal data we also look at the type of personal data they want to extract, the **extent**（ [ɪk'stent] 程度，范围） of the **proposed**（[prə'poʊz] 提议，求婚） data collection and how they plan to use the data post extraction.

There are a number of reasons for taking this approach:

### **Reason #1: Prevent the Scraping of Sensitive Data**

Under the GDPR regulation, there are certain types of data that are classed as "sensitive" . These include any type of personal data that could indicate a person's:

-   Racial or ethnic origin
-   Political opinions
-   Religious or philosophical beliefs
-   Trade union membership
-   Genetic data
-   Biometric data for the purpose of uniquely identifying a natural person
-   Data concerning health or a natural person's sex life and/or sexual orientation

**Scraping sensitive data means that you are subject to（受…制约） additional rules and require specific consent to be given for this data to be scraped and stored.** Therefore, unless you have clear explicit consent and legitimate reason to scrape this data you should avoid scraping it.

### **Reason #2: Minimise the Extent of The Data Extraction**

A important part of GDPR is that companies should only store and process as much data as is required to successfully accomplish a given task.

Given web scrapings ability to extract large quantities of data from a website there is sometimes the desire to capture as much data as possible as it might be useful in the future. Obviously, this **mindset**（思维方式） isn't **in line with**（与...相符） the new GDPR regulations.

As a result, when Scrapinghub is evaluating a scraping project we often work with client companies to minimise the amount of personal data they extract from a website and to define **retention periods**（[rɪ'tenʃ(ə)n] 保留期限） to ensure they comply with GDPR. You should adopt a similar evaluation process for your own scraping projects to ensure you comply with GDPR's minimisation requirements.

### **Reason #3: Ensure Personal Data Is Used For Legitimate Business Purposes**

Even if you can argue that you have a legitimate interest in this data or have the users consent to extract and store their personal data, under GDPR you need to have a clear and legal reason for doing so and be able to demonstrate that it will be used for legitimate business purposes.

If the proposed scraping project doesn't **raise any red flags**（发出危险信号） after being evaluated on these **criteria**（[kraɪ'tɪriən] 标准，准则） then we will generally **commence**（ [kə'mens] 开始，着手） the scraping project.

**Step 5: Ensure The Correct Data Retention And Access Policies Are In Place**
------------------------------------------------------------------------------

As outlined in Step 3, the reason a web scraper is allowed to scrape personal data from a website under GDPR is either because you have their explicit consent or you can demonstrate that you have a legitimate interest in scraping/storing their data.

However, you also need to ensure that the data subjects have been made aware of your data protection and privacy policy and make sure you comply with their **Data Subject Access Rights (DSAR)**（数据主体访问权限）, including their right to **withdraw**（[wɪð'drɔ] 撤回） consent, request a copy of their data, or request deletion of their data.

If consent is withdrawn, or a DSAR is received to delete personal data, then the company who scraped this data must either delete or **anonymize**（[ə'nɒnɪmaɪz] 使匿名化） this personal data because you no longer have a legal basis to hold it.

**Finally, so your web scraping project is just about ready to go but the last thing you need to check off your list is ensuring your proxies are GDPR compliant, specifically any residential（ [.rezɪ'denʃ(ə)l] 住宅的） proxies you might be using.**

![gdpr-compliance-web-scraping-residential-IPs](https://user-gold-cdn.xitu.io/2019/3/22/169a44063a99cecc?w=599&h=407&f=png&s=195995)

**Step 6: Make Sure Your Residential IPs Are GDPR Compliant**
-------------------------------------------------------------

As the GDPR regulation defines IP addresses as personally identifiable information you need to ensure that any EU residential IPs you use as proxies are GDPR compliant.

This means that you need to ensure that the owner of that residential IP has given their explicit consent for their home or mobile IP to be used as a web scraping proxy.

If you own your own residential IPs then you will need to handle this consent yourself. However, **if you are obtaining residential proxies from a 3rd party provider then you need to ensure that they have obtained consent and are in compliance with GDPR prior to using the proxy for your web scraping project**

**Old Web Scraping Projects**
-----------------------------

That is everything you need to know about any future web scraping projects, however, what does GDPR mean for personal data that you may have extracted from websites previously?

Luckily for us you just need to use **the same process as outlined（概述） above** to ensure the GDPR compliance of any old web scraping projects:

1.  **Audit**（ ['ɔːdɪt] 审查） your databases for any personal data you obtained via web scraping.
2.  Determine if this personal data belongs to EU residents.
3.  If there is personal data belonging to EU residents then determine if you had a lawful reason for scraping and storing it.
4.  If you didn't have a lawful reason for scraping and storing this data then you must delete or anonymise this personal data.
5.  If you did have a lawful reason for scraping and storing this data, then ensure that you've put in the **adequate**（ ['ædəkwət] 充分的） data subject access request requirements and retention policies to maintain compliance.
6.  If this data is still publically available, you should determine 1) do you still need all or part of this data to carry out your business processes or 2) if this data contains sensitive data. If you don't need this data or if it contains sensitive information then delete it.

**Conclusion**
--------------

GDPR is perhaps **the most impactful**（最具影响力的） data protection law ever passed, and it will change the way data is extracted from websites forever.

If you are considering commencing a web scraping project for your business that might extract personal data from public websites and you want to ensure it is GDPR compliant, then [don't hesitate to reach out to us](https://scrapinghub.com/enterprise-solutions). Our engineering team of 60+ crawl engineers and data scientists can build a custom web scraping solution for your specific needs.

[![New call-to-action](https://user-gold-cdn.xitu.io/2019/3/21/1699e5225e06bef7?w=1500&h=785&f=jpeg&s=89645)](https://blog.scrapinghub.com/cs/c/?cta_guid=15b13819-b573-4985-8941-093bfcdc3377&placement_guid=421a097a-aaa9-4d4a-9db3-0f8630a76792&portal_id=4367560&canon=https%3A%2F%2Fblog.scrapinghub.com%2Fweb-scraping-gdpr-compliance-guide&redirect_url=APefjpFJkgurx29mOUAy2-QFXAJqawsCuVpACL_-YG0ZU7Utnj_D1sjBvyajV22UgN1zNPw_aPFvFAUf7FtBg09FP5t3w14MMciODVNKWatk3BHZWwuND163kdY3rZxaQ7whCHVgFzp9vRZZU5PRTY_SsmeIlJwZlj4uuZqOy2qKYcZGxEFwNcI&click=b1ba5962-6211-42d4-a8e6-9a6d2ae6c978&hsutk=28f116b4a60ffb08af50ef5427a9e576&utm_referrer=https%3A%2F%2Fblog.scrapinghub.com%2Fweb-scraping-at-scale-lessons-learned-scraping-100-billion-products-pages&pageId=5951738506&__hstc=234333761.28f116b4a60ffb08af50ef5427a9e576.1553238692582.1553238692582.1553238692582.1&__hssc=234333761.1.1553238692583&__hsfp=3861380900)

If you're interested in web scraping and interested in joining a 100% team of some of the leading web scraping experts then be sure to [check out our jobs page](https://scrapinghub.com/jobs). We're growing fast and need people like you to help turn the web into useful data.
