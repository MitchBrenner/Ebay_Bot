# class for calculating cosine similarity
import math


class CosineSimilarity:
    threshold = 0.5

    # return a tokenized list for the given string str
    def tokenize(str):
        return str.lower().split()

    # return a vectorized list for the given str and vocab
    def vectorize(str, vocab):
        vector = []
        for word in vocab:
            if word in str:
                vector.append(1)
            else:
                vector.append(0)
        return vector

    # return the dot product between two vectors
    def dotproduct(vector1, vector2):
        return sum(x * y for x, y in zip(vector1, vector2))

    # return the magnitude of a vector
    def magnitude(vector):
        return math.sqrt(sum([num**2 for num in vector]))

    # uses all the functions to calculate the cosine similarity
    def calc_cosine_similarity(string1, string2):
        str1 = CosineSimilarity.tokenize(string1)
        str2 = CosineSimilarity.tokenize(string2)
        # the vocab is the unique set of words between the two strings
        vocab = set(str1 + str2)

        # get vectors for each string
        vec1 = CosineSimilarity.vectorize(str1, vocab)
        vec2 = CosineSimilarity.vectorize(str2, vocab)
        # print(vec1)
        # print(vec2)

        # get dot product of the two vectors
        dot_product = CosineSimilarity.dotproduct(vec1, vec2)
        # print("dot: ", dot_product)

        # get magnitude of each vector
        mag1 = CosineSimilarity.magnitude(vec1)
        mag2 = CosineSimilarity.magnitude(vec2)
        # print("mag1: ", mag1)
        # print("mag2: ", mag2)

        # get cosine similarity
        return dot_product / (mag1 * mag2)

    # this method returns if it's above the threshold and the similarity value
    @staticmethod
    def is_similar(str1, str2):
        val = CosineSimilarity.calc_cosine_similarity(str1, str2)
        return (val >= CosineSimilarity.threshold, val)


# str1 = (
#     "SportDOG SportHunter SD-825X Dog Remote Trainer 1/2 Mile Range Training Collar F"
# )
# str2 = "SportDOG SD-825X 1/2 MILE Remote Trainer Collar SHOCK Hunting 825x Duck DOG"

# str3 = "Hello World"
# str4 = "Hello"
# print(CosineSimilarity.is_similar(str1, str2))
