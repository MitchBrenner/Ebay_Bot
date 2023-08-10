# Ebay_Bot

## **This project involves the extraction of data from eBay listings highlighting the most popular listings.**

The project uses Selemnium to web scrape information from eBay. It specifically gethers listing titles from a chosen category. Following this, an algorithm utilizing cosine similarity is utilized to determine the similarity between different listings, helping categorize whether they represent the same product. The program keeps track of occurrences of each unique listing. This data is then presented in an organized Excel sheet using the openpyxl library. This sheet provides a clear overview of the frequency of every listing.
