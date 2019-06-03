import random
from collections import deque
from functools import partial

from helpers.linear_algebra import dot, get_row, get_column, shape, make_matrix, magnitude, scalar_multiply, distance
from network_analysis.data import users, friendships, endorsements

for user in users:
    user["friends"] = []

# and populate it
for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i


def shortest_paths_from(from_user):

    # a dictionary from "user_id" to *all* shortest paths to that user
    shortest_paths_to = {from_user["id"]: [[]]}

    # a queue of (previous_user, next user) that we need to check
    # starts out with all the pairs (from_user, friend_of_from_user)
    frontier = deque((from_user, friend)
                     for friend in from_user["friends"])

    # keep going until we empty the deque
    while frontier:

        prev_user, user = frontier.popleft()    # remove the user who is first in the queue
        user_id = user["id"]

        # because of the way we are adding to the queue,
        # necessarily we already know some shortest paths to prev_user
        paths_to_prev_user = shortest_paths_to[prev_user["id"]]
        new_paths_to_user = [path + [user_id] for path in paths_to_prev_user]

        # it is possible we already know a shortest path
        old_paths_to_user = shortest_paths_to.get(user_id, [])

        # what is the shortest path tot here that we have seen so far ?
        if old_paths_to_user:
            min_path_length = len(old_paths_to_user[0])
        else:
            min_path_length = float('inf')

        # only keep paths that are not too long and are actually new
        new_paths_to_user = [path
                             for path in new_paths_to_user
                             if len(path) <= min_path_length
                             and path not in old_paths_to_user]

        shortest_paths_to[user_id] = old_paths_to_user + new_paths_to_user

        # add never-seen neighbors to the frontier
        frontier.extend((user, friend)
                        for friend in user["friends"]
                        if friend["id"] not in shortest_paths_to)

    return shortest_paths_to


for user in users:
    user["shortest_paths"] = shortest_paths_from(user)

for user in users:
    user["betweenness_centrality"] = 0.0

for source in users:
    source_id = source["id"]
    for target_id, paths in source["shortest_paths"].items():
        if source_id < target_id:       # don't double count
            num_paths = len(paths)      # how many shortest paths?
            contrib = 1 / num_paths     # contribution to centrality

            for path in paths:
                for id in path:
                    if id not in [source_id, target_id]:
                        users[id]["betweenness_centrality"] += contrib


def farness(user):
    """the sum of the lengths of the shortest paths to each other user"""
    return sum(len(paths[0])
               for paths in user["shortest_paths"].values())


for user in users:
    user["closeness_centrality"] = 1 / farness(user)

"""Eigenvector Centrality"""


def matrix_product_entry(A, B, i, j):
    return dot(get_row(A, i), get_column(B, j))


def matrix_multiply(A, B):
    n1, k1 = shape(A)
    n2, k2 = shape(B)

    if k1 != n2:
        raise ArithmeticError("incompatible shapes!")

    return make_matrix(n1, k2, partial(matrix_product_entry, A, B))


def vector_as_matrix(v):
    """returns the vector v (represented as a list) as a n x 1 matrix"""
    return [[v_i] for v_i in v]


def vector_from_matrix(v_as_matrix):
    """returns the n x 1 matrix as a list of values"""
    return [row[0] for row in v_as_matrix]


def matrix_operation(A, v):
    v_as_matrix = vector_as_matrix(v)
    product = matrix_multiply(A, v_as_matrix)
    return vector_from_matrix(product)


def find_eigenvector(A, tolerance=0.00001):
    guess = [random.random() for _ in A]

    while True:
        result = matrix_operation(A, guess)
        length = magnitude(result)
        next_guess = scalar_multiply(1/length, result)

        if distance(guess, next_guess) < tolerance:
            return next_guess, length   # eigenvector, eigenvalue
        guess = next_guess


def entry_fn(i, j):
    return 1 if (i, j) in friendships or (j, i) in friendships else 0


n = len(users)
adjacency_matrix = make_matrix(n, n, entry_fn)
eigenvector_centralities, _ = find_eigenvector(adjacency_matrix)

"""Directed Graphs and PageRank"""
for user in users:
    user["endorses"] = []       # add one list to track outgoing endorsements
    user["endorsed_by"] = []    # and another to track endorsements

for source_id, target_id in endorsements:
    users[source_id]["endorses"].append(users[target_id])
    users[target_id]["endorsed_by"].append(users[source_id])

endorsements_by_id = [(user["id"], len(user["endorsed_by"]))
                      for user in users]

sorted(endorsements_by_id,
       key=lambda pair: pair[1],
       reverse=True)


def page_rank(users, damping=0.85, num_iters=100):

    # initially distribute PageRank evenly
    num_users = len(users)
    pr = {user["id"]: 1 / num_users for user in users}

    # this is the small fraction of PageRank
    # that each node gets each iteration
    base_pr = (1 - damping) / num_users

    for _ in range(num_iters):
        next_pr = {user["id"]: base_pr for user in users}
        for user in users:
            # distribute PageRank to outgoing links
            links_pr = pr[user["id"]] * damping
            for endorsee in user["endorses"]:
                next_pr[endorsee["id"]] += links_pr / len(user["endorses"])

        pr = next_pr

    return pr