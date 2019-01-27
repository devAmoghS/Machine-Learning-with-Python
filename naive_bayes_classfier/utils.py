import math
import re
from collections import defaultdict


def tokenise(message):
    """Tokenise message into distinct words"""
    message = message.lower()                       # convert to lowercase
    all_words = re.findall("[a-z0-9']+", message)   # extract the words
    return set(all_words)                           # remove duplicates


def count_words(training_set):
    """training set consists of parts (meesage, is_spam)"""
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokenise(message):
            counts[word][0 if is_spam else 1] += 1
    return counts


def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    """Turn the word_counts into a list of triplets: w, p(w|spam) and p(w|~spam)"""
    return [(w,
            (spam + k)/(total_spams + 2 * k),
            (non_spam + k)/(total_non_spams + 2 * k))
             for w, (spam, non_spam) in counts.items()]


def spam_probability(word_probs, message):
    """assigns word probabilities to messages"""
    message_words = tokenise(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    # iterate through each word in our vocabulary
    for word, prob_if_spam, prob_if_not_spam in word_probs:

        # if "word" appears in the message,
        # add the log probability of seeing it
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)

        # if the "word" doesn't appear in the message
        # add the log probability of not seeing it
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)

    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

