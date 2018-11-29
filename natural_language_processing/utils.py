import random
import re
from collections import defaultdict, Counter

from natural_language_processing.data import data, documents
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests


def plot_resumes():
    """Word Clouds"""

    def text_size(total):
        return 8 + total / 200 * 20

    for word, job_popularity, resume_popularity in data:
        plt.text(job_popularity, resume_popularity, word,
                 ha='center',
                 va='center',
                 size=text_size(job_popularity + resume_popularity))

    plt.xlabel("Popularity on Job Postings")
    plt.ylabel("Popularity on Resumes")
    plt.axis([0, 100, 0, 100])
    plt.xticks([])
    plt.yticks([])
    plt.show()


"""n-grams Model"""


def fix_unicode(text):
    return text.replace(u"\u2019", "'")


def get_document():
    url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    content = soup.find("div", "article-body")  # find article-body div
    regex = r"[\w']+|[\.]"  # matches a word or a period

    document = []

    for paragraph in content("p"):
        words = re.findall(regex, fix_unicode(paragraph.text))
        document.extend(words)

    return document


def generate_using_bigrams(transitions):
    current = "."  # this means the next word will start with a sentence
    result = []
    while True:
        next_word_candidates = transitions[current]  # bigrams (current, _)
        current = random.choice(next_word_candidates)  # choose one at random
        result.append(current)  # append it to results
        if current == ".":
            return " ".join(result)  # if "." we're done


def generate_using_trigrams(starts, transitions):
    current = random.choice(starts)  # choose a random starting word
    prev = "."
    result = [current]
    while True:
        next_word_candidates = transitions[(prev, current)]
        next = random.choice(next_word_candidates)

        prev, current = current, next
        result.append(current)  # append it to results
        if current == ".":
            return " ".join(result)  # if "." we're done


"""Grammars"""


def is_terminal(token):
    return token[0] != "_"


def expand(grammar, tokens):
    for i, token in enumerate(tokens):

        # skip over terminals
        if is_terminal(token): continue

        # if we get here, we found a non-terminal token
        # so we need to choose a replacement at random
        replacement = random.choice(grammar[token])

        if is_terminal(replacement):
            tokens[i] = replacement
        else:
            tokens = tokens[:i] + replacement.split() + tokens[(i + 1):]

        # now call expand on the new list of tokens
        return expand(grammar, tokens)

    # if we get here we had all terminals and are done
    return tokens


def generate_sentence(grammar):
    return expand(grammar, ["_S"])


"""Gibbs Sampling"""


def roll_a_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def direct_sample():
    d1 = roll_a_die()
    d2 = roll_a_die()
    return d1, d1 + d2


def random_y_given_x(x):
    return x + roll_a_die()


def random_x_given_y(y):
    if y <= 7:
        return random.randrange(1, y)
    else:
        return random.randrange(y - 6, 7)


def gibbs_sampling(num_iters=100):
    x, y = 1, 2
    for _ in range(num_iters):
        x = random_x_given_y(y)
        y = random_y_given_x(x)
    return x, y


def compare_distributions(num_samples=1000):
    counts = defaultdict(lambda: [0, 0])
    for _ in range(num_samples):
        counts[gibbs_sampling()][0] += 1
        counts[direct_sample()][1] += 1
    return counts


"""Topic Modelling"""


def sample_from(weights):
    """returns i with probability weights[i] / sum(weights)"""
    total = sum(weights)
    rnd = total * random.random()  # uniform between 0 and total
    for i, w in enumerate(weights):
        rnd -= w  # return the smallest i such
        if rnd <= 0:  # weights[0] + ... + weights[i] >=rnd
            return i


K = 4

document_topic_counts = [Counter() for _ in documents]
# print(document_topic_counts)
topic_word_counts = [Counter() for _ in range(K)]
topic_counts = [0 for _ in range(K)]
document_lengths = [len(d) for d in documents]

distinct_words = set(word
                     for document in documents
                     for word in document)

W = len(distinct_words)
D = len(documents)


def p_topic_given_document(topic, d, alpha=0.1):
    """the fraction of words in document 'd'
    that are assigned to 'topic' (plus some smoothing)"""
    return ((document_topic_counts[d][topic] + alpha) / (document_lengths[d] + K * alpha))


def p_word_given_topic(word, topic, beta=0.1):
    """the fraction of words in document 'd'
    that are assigned to 'topic' (plus some smoothing)"""
    return ((topic_word_counts[topic][word] + beta) / (topic_counts[topic] + W * beta))


def topic_weight(d, word, k):
    """given a document and a word in that document,
    return the weight for the k-th topic"""
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)


def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k)
                        for k in range(K)])


random.seed(0)
document_topics = [[random.randrange(K) for word in document]
                   for document in documents]

for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1

for iter in range(1000):
    for d in range(D):
        for i, (word, topic) in enumerate(zip(documents[d], document_topics[d])):
            # remove this word/topic from the counts
            # so that it doesn't influence the weights
            document_topic_counts[d][topic] -= 1
            topic_word_counts[topic][word] -= 1
            topic_counts[topic] -= 1
            document_lengths[d] -= 1

            # choose a new topic based on the weights
            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic

            # and now add it back to the counts
            document_topic_counts[d][new_topic] += 1
            topic_word_counts[topic][word] += 1
            topic_counts[topic] += 1
            document_lengths[d] += 1
