# Model Performance and Accuracy Metrics

## Model Evaluation

The Movie Review Sentiment Analysis model was evaluated using standard classification metrics to measure its ability to correctly classify movie reviews as Positive or Negative.

### Accuracy Score

Accuracy measures the percentage of correctly classified reviews.

Formula:

Accuracy = Correct Predictions / Total Predictions

Model Accuracy:

**XX%** *(Replace with your actual accuracy score)*

Example:

If the model correctly predicts 890 reviews out of 1000 reviews:

Accuracy = 890 / 1000 = 89%

This indicates that the model correctly classified 89% of the movie reviews.

---

## Precision

Precision measures how many reviews predicted as Positive were actually Positive.

Higher precision indicates fewer false positive predictions.

---

## Recall

Recall measures how many actual Positive reviews were correctly identified by the model.

Higher recall indicates fewer missed positive reviews.

---

## F1-Score

F1-Score is the harmonic mean of Precision and Recall.

It provides a balanced measure when both Precision and Recall are important.

---

## Interpretation of Results

The model achieved good performance on the IMDb Movie Review dataset. TF-IDF was used to convert text into numerical features, and Logistic Regression was used as the classification algorithm.

The evaluation metrics indicate that the model can effectively distinguish between Positive and Negative movie reviews. Higher values of Accuracy, Precision, Recall, and F1-Score demonstrate the model's ability to perform sentiment classification reliably.

---

## Example Predictions

Input Review:

"This movie was absolutely amazing and enjoyable."

Prediction:

Positive

Input Review:

"Worst movie ever. Waste of time."

Prediction:

Negative

---

## Conclusion

The Movie Review Sentiment Analysis system successfully classified movie reviews using Natural Language Processing techniques. Text preprocessing, TF-IDF feature extraction, and Logistic Regression classification enabled the model to achieve strong sentiment prediction performance on unseen reviews.
