##########################
# Finding Key Connectors #
##########################

# dictionary of each user and their id
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

# friendship data as a list of tuples
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# assign empty list to each user
for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])  # add i as a friend of j
    users[j]["friends"].append(users[i])  # add j as a friend of i


def number_of_friends(user):
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users
print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)


###############################
# Data Scientist You May Know #
###############################


def friends_of_friend_ids_bad(user):
    return [foaf["id"]
            for friend in user["friends"]  # for each of user's friend
            for foaf in friend["friends"]]  # for each of their friends


print(friends_of_friend_ids_bad(users[0]))  # Data Scientists Hero may know

from collections import Counter


def not_the_same(user, other_user):
    # Two users are not same if they have different ids
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    # other_user is not a friend if he is not in user["friends"]
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]  # for each of my friends
                   for foaf in friend["friends"]  # count *their* friends
                   if not_the_same(user, foaf)  # who aren't me
                   and not_friends(user, foaf))  # and aren't my friends


print(friends_of_friend_ids(users[3]))  # Data Scientists Chi may know

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


from collections import defaultdict

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

print(user_ids_by_interest)

interests_by_user_ids = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_ids[user_id].append(interest)

print(interests_by_user_ids)


def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_ids[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


print(most_common_interests_with(users[6]))

###########################
# Salaries and Experience #
###########################
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

from matplotlib import pyplot as plt


def make_chart_salaries_by_tenure():
    tenures = [tenure for salary, tenure in salaries_and_tenures]
    salaries = [salary for salary, tenure in salaries_and_tenures]
    plt.scatter(tenures, salaries)
    plt.xlabel("Years Experience")
    plt.ylabel("Salary")
    plt.show()


salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print(average_salary_by_bucket)


#################
# Paid Accounts #
#################


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


#######################
# Topics of Interests #
#######################

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in str(interest).lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
