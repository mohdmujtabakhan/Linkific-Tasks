# Hugging Face NLP Practice

## Overview

This project demonstrates the use of Hugging Face pre-trained transformer models for various Natural Language Processing (NLP) tasks. The objective is to understand transfer learning and how pre-trained models can be used to solve NLP problems without training models from scratch.

## Tasks Implemented

### 1. Sentiment Analysis

Predicts whether a text expresses a positive or negative sentiment.

Model Used:

* distilbert-base-uncased-finetuned-sst-2-english

### 2. Question Answering

Answers questions based on a given context.

Model Used:

* distilbert-base-cased-distilled-squad

### 3. Text Generation

Generates text based on a user-provided prompt.

Model Used:

* gpt2

### 4. Named Entity Recognition (NER)

Identifies entities such as people, organizations, and locations.

Model Used:

* dslim/bert-base-NER

### 5. Text Summarization

Generates concise summaries from long text.

Model Used:

* sshleifer/distilbart-cnn-12-6

## Project Structure

Day10-HuggingFace/

├── huggingface-practice.ipynb

├── hf_predict.py

├── README.md

└── saved_model/

## Day 9 vs Day 10 Comparison

| Feature               | Day 9 Custom Model  | Day 10 Hugging Face Model |
| --------------------- | ------------------- | ------------------------- |
| Model                 | Logistic Regression | DistilBERT                |
| Feature Extraction    | TF-IDF              | Transformer Embeddings    |
| Training Required     | Yes                 | No                        |
| Dataset Required      | Yes                 | No                        |
| Accuracy              | Moderate            | High                      |
| Context Understanding | Limited             | Better                    |
| Development Time      | More                | Less                      |

## Simple Prediction Script

The project includes a Python script named `hf_predict.py` which performs sentiment analysis using a Hugging Face pre-trained model.

Run:

python hf_predict.py

Enter text when prompted and the model will predict the sentiment.

## Model Serialization

Model serialization is demonstrated using:

* save_pretrained()
* from_pretrained()

This allows models and tokenizers to be saved locally and loaded later without downloading them again.

## Libraries Used

* transformers
* torch
* huggingface_hub

## Installation

pip install transformers torch

## Conclusion

This project demonstrates how Hugging Face transformer models can be used for multiple NLP tasks including sentiment analysis, question answering, text generation, named entity recognition, and text summarization. Pre-trained models provide powerful NLP capabilities with minimal training effort and are widely used in modern AI applications.
