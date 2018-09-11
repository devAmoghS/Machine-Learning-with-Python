import glob
import re
from collections import Counter
import random
from naive_bayes_classifier.naivebayesclassifier import NaiveBayesClassifier


def split_data(data, prob):
    """split data into fractions [prob, 1 - prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results


def get_subject_data(path):

    data = []

    # regex for stripping out the leading "Subject:" and any spaces after it
    subject_regex = re.compile(r"^Subject:\s+")

    # glob.glob returns every filename that matches the wildcarded path
    for fn in glob.glob(path):
        is_spam = "ham" not in fn

        with open(fn, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                if line.startswith("Subject:"):
                    subject = subject_regex.sub("", line).strip()
                    data.append((subject, is_spam))

    return data


def p_spam_given_word(word_prob):
    word, prob_if_spam, prob_if_not_spam = word_prob
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)


def train_and_test_model(path):

    data = get_subject_data(path)
    random.seed(0)      # just so you get the same answers as me
    train_data, test_data = split_data(data, 0.75)

    classifier = NaiveBayesClassifier()
    classifier.train(train_data)

    classified = [(subject, is_spam, classifier.classify(subject))
              for subject, is_spam in test_data]

    counts = Counter((is_spam, spam_probability > 0.5) # (actual, predicted)
                     for _, is_spam, spam_probability in classified)

    print(counts)

    classified.sort(key=lambda row: row[2])
    spammiest_hams = list(filter(lambda row: not row[1], classified))[-5:]
    hammiest_spams = list(filter(lambda row: row[1], classified))[:5]

    print("\nspammiest_hams", spammiest_hams)
    print("\nhammiest_spams", hammiest_spams)

    words = sorted(classifier.word_probs, key=p_spam_given_word)

    spammiest_words = words[-5:]
    hammiest_words = words[:5]

    print("\nspammiest_words", spammiest_words)
    print("\nhammiest_words", hammiest_words)


if __name__ == "__main__":
    train_and_test_model(r"data/*/*")
