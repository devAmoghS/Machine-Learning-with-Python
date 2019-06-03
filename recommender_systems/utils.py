import math
from collections import defaultdict

from helpers.linear_algebra import dot


def cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))


def make_user_interest_vector(interests, user_interests):
    return [1 if interest in user_interests else 0
            for interest in interests]


def most_similar_users_to(user_similarities, user_id):
    pairs = [(other_user_id, similarity)
             for other_user_id, similarity in
             enumerate(user_similarities[user_id])
             if user_id != other_user_id and similarity > 0]

    return sorted(pairs, key=lambda pair: pair[1], reverse=True)


def most_similar_interests_to(interest_similarities, interest_id, unique_interests):
    pairs = [(unique_interests[other_interest_id], similarity)
             for other_interest_id, similarity in
             enumerate(interest_similarities[interest_id])
             if interest_id != other_interest_id and similarity > 0]

    return sorted(pairs, key=lambda pair: pair[1], reverse=True)


def user_based_suggestions(user_similarities, users_interests, user_id, include_current_interests=False):
    suggestions = defaultdict(float)
    for other_user_id, similarity in most_similar_users_to(user_similarities, user_id):
        for interest in users_interests[other_user_id]:
            suggestions[interest] += similarity

    suggestions = sorted(suggestions.items(), key=lambda pair: pair[1], reverse=True)

    if include_current_interests:
        return suggestions
    else:
        return [(suggestion, weight)
                for suggestion, weight in suggestions
                if suggestion not in users_interests[user_id]]


def item_based_suggestions(interest_similarities, users_interests, user_interest_matrix, unique_interests, user_id, include_current_interests=False):
    suggestions = defaultdict(float)
    for interest_id, is_interested in enumerate(user_interest_matrix[user_id]):
        if is_interested == 1:
            for interest, similarity in most_similar_interests_to(interest_similarities, interest_id, unique_interests):
                suggestions[interest] += similarity

    suggestions = sorted(suggestions.items(), key=lambda pair: pair[1], reverse=True)

    if include_current_interests:
        return suggestions
    else:
        return [(suggestion, weight)
                for suggestion, weight in suggestions
                if suggestion not in users_interests[user_id]]

