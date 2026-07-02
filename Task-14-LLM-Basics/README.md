## Task-14: LLM Basics and Prompt Engineering

## Project Overview

This project introduces the fundamentals of Large Language Models (LLMs) and Prompt Engineering. It demonstrates how to interact with an LLM using the Groq API, understand prompt design techniques, calculate token usage and API cost, and build a reusable prompt template library.

The project also includes practical exercises on summarization, information extraction, text generation, reasoning, and cost calculation using different prompting techniques.

---

## Objectives

- Understand Large Language Models (LLMs)
- Learn Prompt Engineering concepts
- Connect to an LLM using the Groq API
- Compare different prompting techniques
- Perform common NLP tasks using prompts
- Calculate API token usage and estimated cost
- Build a reusable prompt template library

---

## Technologies Used

- Python 3.11
- Jupyter Notebook
- Groq API
- Llama 3.3 70B Versatile Model
- VS Code

---

## Project Structure

```
Task-14-LLM-Basics/
│
├── llm-basics.ipynb
├── prompt-engineering.ipynb
├── cost-calculation.ipynb
├── README.md
└── prompt_templates/
    ├── text summarization.txt
    ├── text extraction.txt
    ├── text generation.txt
    └── text reasoning.txt
```

---

## Concepts Covered

- Large Language Models (LLMs)
- Tokens
- Context Window
- Temperature
- System Prompt
- User Prompt
- Zero-shot Prompting
- Few-shot Prompting
- Chain-of-Thought Prompting

---

## LLM API Integration

The notebook connects to the Groq API using an API key and sends prompts to the Llama 3.3 70B Versatile model to generate responses.

---

## Prompt Engineering Techniques

### Zero-shot Prompting

The model performs a task without any examples.

Example:

- Summarize an article
- Extract information
- Answer questions

---

### Few-shot Prompting

The model is provided with examples before solving the actual task.

Examples help improve response accuracy and consistency.

---

### Chain-of-Thought Prompting

The model explains each reasoning step before providing the final answer.

Used for:

- Mathematical calculations
- Logical reasoning
- Decision making
- Problem solving

---

## Prompt Engineering Exercises

The notebook includes practical examples of:

- Text Summarization
- Information Extraction
- Text Generation
- Reasoning Tasks

More than 20 prompt examples are included.

---

## Prompt Template Library

A reusable prompt library is created containing templates for:

- Text Summarization
- Information Extraction
- Text Generation
- Text Reasoning

These templates can be reused in future LLM projects.

---

## Token Cost Calculation

The project demonstrates how LLM providers charge based on token usage.

Formula:

```
Total Tokens = Input Tokens + Output Tokens

Cost = (Total Tokens / 1,000,000) × Price per Million Tokens
```

Several practical examples are included to estimate API usage cost.

---

## Files Included

### llm-basics.ipynb

Contains:

- Groq API integration
- Sending prompts
- Receiving model responses
- LLM fundamentals

---

### prompt-engineering.ipynb

Contains:

- Zero-shot prompting
- Few-shot prompting
- Chain-of-Thought prompting
- Summarization examples
- Information extraction examples
- Generation prompts
- Reasoning prompts
- Prompt comparison

---

### cost-calculation.ipynb

Contains:

- Token calculation examples
- Cost estimation examples
- API pricing explanation

---

### prompt_templates

Contains reusable prompt templates saved as text files.

---

## Learning Outcomes

After completing this task, I learned how to:

- Work with Large Language Models
- Use the Groq API
- Design effective prompts
- Compare prompting techniques
- Perform multiple NLP tasks
- Estimate API costs using token calculations
- Build a reusable prompt library

---

## Future Improvements

- Build a chatbot using LangChain
- Add conversation memory
- Use Retrieval-Augmented Generation (RAG)
- Connect PDFs for question answering
- Develop document summarization applications
- Build AI assistants using LLMs

---

## Author

**Mohammed Mujtaba Khan**

Artificial Intelligence and Machine Learning
