import pytest

from natural_language_processing.spam_classifier import (
    SAMPLE_LABELS,
    SAMPLE_MESSAGES,
    predict_message,
    train_classifier,
)


def test_classifier_returns_accuracy_and_model():
    model, accuracy = train_classifier(SAMPLE_MESSAGES, SAMPLE_LABELS)

    assert model is not None
    assert 0.0 <= accuracy <= 1.0


def test_classifier_predicts_spam_and_ham():
    model, _ = train_classifier(SAMPLE_MESSAGES, SAMPLE_LABELS)

    assert predict_message(model, "You won a free prize!") == "spam"
    assert predict_message(model, "Please send me the class notes.") == "ham"


def test_mismatched_messages_and_labels_raise_error():
    with pytest.raises(ValueError, match="same length"):
        train_classifier(["hello"], ["ham", "spam"])


def test_too_few_messages_raise_error():
    with pytest.raises(ValueError, match="at least four"):
        train_classifier(["hello", "hi", "bye"], ["ham", "ham", "spam"])
