from sklearn.decomposition import NMF, LatentDirichletAllocation
from preprocess import tfidf, tf
num_topics = 20

# Run NMF
nmf = NMF(n_components=num_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

# Run LDA
lda = LatentDirichletAllocation(n_topics=num_topics, max_iter=5, learning_method='online', learning_offset=50, random_state=0).fit(tf)
