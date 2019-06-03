from functools import partial

from recommender_systems.data import users_interests
from recommender_systems.utils import make_user_interest_vector, cosine_similarity, most_similar_users_to, \
    user_based_suggestions, most_similar_interests_to, item_based_suggestions

if __name__ == '__main__':
    unique_interests = sorted(list({interest
                                    for user_interests in users_interests
                                    for interest in user_interests}))

    print("unique interests")
    print(unique_interests)

    user_interest_matrix = map(partial(make_user_interest_vector, unique_interests), users_interests)

    user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
                          for interest_vector_j in user_interest_matrix]
                         for interest_vector_i in user_interest_matrix]

    print(most_similar_users_to(user_similarities, 0))

    print(user_based_suggestions(user_similarities, users_interests, 0))

    # item-based
    interest_user_matrix = [[user_interest_vector[j]
                             for user_interest_vector in user_interest_matrix]
                            for j, _ in enumerate(unique_interests)]

    interest_similarities = [[cosine_similarity(user_vector_i, user_vector_j)
                              for user_vector_j in interest_user_matrix]
                             for user_vector_i in interest_user_matrix]

    print(most_similar_interests_to(interest_similarities, 0, unique_interests))

    print(item_based_suggestions(interest_similarities, users_interests, user_interest_matrix, unique_interests, 0))