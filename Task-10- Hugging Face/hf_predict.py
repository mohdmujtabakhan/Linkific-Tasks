from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis"
)

text = input("Enter text: ")

result = classifier(text)

print(result)