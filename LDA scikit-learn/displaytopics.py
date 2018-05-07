from nmf_lda_scikitlearn import nmf, lda
from preprocess import tfidf_feature_names, tf_feature_names


def display_topics(model, feature_names, num_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print("".join([feature_names[i]
          for i in topic.argsort()[:-num_top_words - 1:-1]])
        )


num_top_words = 10
display_topics(nmf, tfidf_feature_names, num_top_words)
display_topics(lda, tf_feature_names, num_top_words)
