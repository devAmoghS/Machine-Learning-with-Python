from network_analysis.data import users
from network_analysis.utils import eigenvector_centralities, page_rank

if __name__ == '__main__':

    print("Betweenness Centrality")
    for user in users:
        print(user["id"], user["betweenness_centrality"])
    print()

    print("Closeness Centrality")
    for user in users:
        print(user["id"], user["closeness_centrality"])
    print()

    print("Eigenvector Centrality")
    for user_id, centrality in enumerate(eigenvector_centralities):
        print(user_id, centrality)
    print()

    print("PageRank")
    for user_id, pr in page_rank(users).items():
        print(user_id, pr)