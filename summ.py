import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def generate_summary(input_text):
    text = """{}""".format(input_text)  # Wrap the input_text in triple quotes
    # Tokenizing the text
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the score of each word
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentence_value = dict()

    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    sum_values = 0
    for sentence in sentence_value:
        sum_values += sentence_value[sentence]

    # Average value of a sentence from the original text
    average = int(sum_values / len(sentence_value))

    # Storing sentences into our summary
    summary = ''
    for sentence in sentences:
        if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
            summary += " " + sentence

    return summary

# Example usage
# input_text = """
#     Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. It involves the development of algorithms and models that enable computers to understand, interpret, and generate human-like text. NLP has various applications, including machine translation, sentiment analysis, chatbots, and text summarization.

#     The NLTK library in Python provides tools and resources for working with human language data. In this example, we'll use NLTK to create a simple extractive text summarization function. The function will tokenize the input text, create a frequency table for words, assign scores to sentences based on word frequency, calculate an average score for sentences, and generate a summary by selecting sentences with scores higher than 1.2 times the average.

#     Let's test the summarization function with this example input. Keep in mind that this is a basic extractive summarization approach and may not capture all nuances of the original text.
# """
# print("summary is:")
# print(generate_summary(input_text))
