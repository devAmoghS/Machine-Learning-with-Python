from decision_trees.data import inputs
from decision_trees.utils import partition_entropy_by, build_tree_id3, classify

if __name__ == "__main__":

    for key in ['level', 'lang', 'tweets', 'phd']:
        print(key, partition_entropy_by(inputs, key))
    print()

    senior_inputs = [(input, label)
                     for input, label in inputs if input["level"] == "Senior"]

    for key in ['lang', 'tweets', 'phd']:
        print(key, partition_entropy_by(senior_inputs, key))
    print()

    print("building the tree")
    tree = build_tree_id3(inputs)
    print(tree)

    print("Junior / Java / tweets / no phd", classify(tree,
                                                      {"level": "Junior",
                                                       "lang": "Java",
                                                       "tweets": "yes",
                                                       "phd": "no"}))

    print("Junior / Java / tweets / phd", classify(tree,
                                                   {"level": "Junior",
                                                    "lang": "Java",
                                                    "tweets": "yes",
                                                    "phd": "yes"}))

    print("Intern", classify(tree, {"level": "Intern"}))
    print("Senior", classify(tree, {"level": "Senior"}))
