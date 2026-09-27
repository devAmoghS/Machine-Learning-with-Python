"""Classify short messages as spam or ham using TF-IDF and a linear SVM."""

from typing import Sequence

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


SAMPLE_MESSAGES = [
    "Congratulations, you won a free vacation. Click now!",
    "Claim your cash prize by visiting this link.",
    "Urgent offer: receive a free gift card today.",
    "You have been selected for a limited-time reward.",
    "Win money now by replying to this message.",
    "Exclusive deal! Buy now and save 90 percent.",
    "Can you send me the meeting notes?",
    "I will call you after class.",
    "Please remember to submit the homework.",
    "Are we still meeting for lunch tomorrow?",
    "The report is attached to this email.",
    "Thank you for helping me with the project.",
]

SAMPLE_LABELS = [
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "spam",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
    "ham",
]


def build_classifier() -> Pipeline:
    """Create a TF-IDF and linear-SVM classification pipeline."""
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
            ("classifier", LinearSVC(random_state=42)),
        ]
    )


def train_classifier(
    messages: Sequence[str],
    labels: Sequence[str],
    test_size: float = 0.25,
    random_state: int = 42,
) -> tuple[Pipeline, float]:
    """Train the classifier and return the model and test accuracy."""
    if len(messages) != len(labels):
        raise ValueError("messages and labels must have the same length")
    if len(messages) < 4:
        raise ValueError("at least four labeled messages are required")

    x_train, x_test, y_train, y_test = train_test_split(
        list(messages),
        list(labels),
        test_size=test_size,
        random_state=random_state,
        stratify=labels,
    )

    model = build_classifier()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, float(accuracy)


def predict_message(model: Pipeline, message: str) -> str:
    """Predict whether one message is spam or ham."""
    return str(model.predict([message])[0])


def main() -> None:
    """Train the example classifier and display predictions."""
    model, accuracy = train_classifier(SAMPLE_MESSAGES, SAMPLE_LABELS)

    print(f"Test accuracy: {accuracy:.2f}")

    examples = [
        "You won a free prize. Click this link now!",
        "Could you send me the class notes?",
    ]

    for message in examples:
        print(f"{predict_message(model, message)}: {message}")


if __name__ == "__main__":
    main()


