import re

heads = """
-   What's Important When Scraping At Scale?
-   Challenge #1 - Sloppy and Always Changing Website Formats

    -   No Easy Solution
-   Challenge 2: Scalable Architecture

    -   Separate Product Discovery From Product Extraction
    -   Allocate More Resources To Product Extraction
-   Challenge 3: Maintaining Throughput Performance

    -   Crawling Efficiency

-   Challenge 4: Anti-Bot Countermeasures

    -   Proxies
    -   Beyond Proxies
-   Challenge 5: Data Quality
-   Wrapping Things Up
"""

# What's Important When Scraping At Scale? -> whats-important-when-scraping-at-scale
for head in re.split(r'\n', heads):
    if head.strip():
        start = re.search('\w', head).start()
        prefix = head[:start]
        head_ = head[start:]
        fragment = re.sub(r'[^\w-]', '', head_.lower().replace(' ', '-'))
        print("%s[%s](#%s)" % (prefix, head_, fragment))


# -   [What's Important When Scraping At Scale?](#whats-important-when-scraping-at-scale)
# -   [Challenge #1 - Sloppy and Always Changing Website Formats](#challenge-1---sloppy-and-always-changing-website-formats)
    # -   [No Easy Solution](#no-easy-solution)
# -   [Challenge 2: Scalable Architecture](#challenge-2-scalable-architecture)
    # -   [Separate Product Discovery From Product Extraction](#separate-product-discovery-from-product-extraction)
    # -   [Allocate More Resources To Product Extraction](#allocate-more-resources-to-product-extraction)
# -   [Challenge 3: Maintaining Throughput Performance](#challenge-3-maintaining-throughput-performance)
    # -   [Crawling Efficiency](#crawling-efficiency)
# -   [Challenge 4: Anti-Bot Countermeasures](#challenge-4-anti-bot-countermeasures)
    # -   [Proxies](#proxies)
    # -   [Beyond Proxies](#beyond-proxies)
# -   [Challenge 5: Data Quality](#challenge-5-data-quality)
# -   [Wrapping Things Up](#wrapping-things-up)
