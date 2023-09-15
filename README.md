# Ebay_Bot

### **This project involves the extraction of data from eBay listings highlighting the most popular listings.**

The project uses Selenium to web scrape information from eBay. It specifically gethers listing titles from a chosen category. Following this, an algorithm utilizing cosine similarity is used to determine the similarity between different listings, helping categorize whether they represent the same product. The program keeps track of occurrences of each unique listing. This data is then presented in an organized Excel sheet using the openpyxl library. This sheet provides a clear overview of the frequency of every listing.

## Cosine Similarity

Cosine similarity is a mathematical metric used to measure the similarity between two vectors, often representing documents, texts, or other high-dimensional data points. It assesses the cosine of the angle between the vectors, disregarding their magnitude and focusing solely on their orientations relative to each other.

In the context of text analysis, like comparing listing titles, each vector component typically represents the frequency or presence of a specific term in the text. The cosine similarity formula calculates the dot product of the vectors and divides it by the product of their magnitudes, resulting in a value between -1 and 1. A value closer to 1 indicates higher similarity, while a value closer to -1 indicates dissimilarity.

Cosine similarity is particularly useful when comparing documents or texts because it highlights the thematic or conceptual similarity rather than exact word matches. This property makes it effective for tasks like information retrieval, recommendation systems, and clustering, where the emphasis is on understanding content relationships rather than literal matching.
