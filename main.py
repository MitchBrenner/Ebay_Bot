from ebay_scraper.ebay import Ebay
import time

with Ebay() as bot:
    keywords = "Dog Collar"
    bot.launch("https://www.ebay.com/sch/ebayadvsearch")
    bot.search(keywords=keywords)
    bot.get_report(keywords)
