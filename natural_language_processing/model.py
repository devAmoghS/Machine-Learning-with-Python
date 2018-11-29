from natural_language_processing.data import grammar, documents
from natural_language_processing.utils import generate_sentence, topic_word_counts, document_topic_counts

if __name__ == '__main__':
    # plot_resumes()

    # document = get_document()

    # bigrams = zip(document, document[1:])       # gives us precisely the pairs of consecutive elements of document
    # bigrams_transitions = defaultdict(list)
    # for prev, current in bigrams:
    #     bigrams_transitions[prev].append(current)

    # trigrams = zip(document, document[1:], document[2:])
    # trigrams_transitions = defaultdict(list)
    # starts = []
    #
    # for prev, current, next in trigrams:
    #     if prev == ".":             # if previous word is a period
    #         starts.append(current)  # then this is start word
    #
    #     trigrams_transitions[(prev, current)].append(next)
    #
    # print(generate_using_trigrams(starts, trigrams_transitions))

    # print(generate_sentence(grammar=grammar))

    for k, word_counts in enumerate(topic_word_counts):
        for word, count in word_counts.most_common():
            if count > 0:
                print(k, word, count)

    topic_names = ["Big Data and programming languages",
                   "databases",
                   "machine learning",
                   "statistics"]

    for document, topic_counts in zip(documents, document_topic_counts):
        for topic, count in topic_counts.most_common():
            if count > 0:
                print(topic_names[topic], count)
        print()

