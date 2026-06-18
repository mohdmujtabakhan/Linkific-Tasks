# Regex Cheat Sheet for Python

## What is Regex?

Regex (Regular Expression) is a sequence of characters used to search, match, validate, and manipulate text patterns.

Python provides regex support through the built-in `re` module.

```python
import re
```

---

# Common Regex Symbols

| Pattern | Meaning                           | Example Match |
| ------- | --------------------------------- | ------------- |
| `.`     | Any character except newline      | a, b, 1       |
| `\d`    | Any digit (0-9)                   | 5             |
| `\D`    | Any non-digit                     | A, #          |
| `\w`    | Word character (a-z, A-Z, 0-9, _) | Python123     |
| `\W`    | Non-word character                | @, #          |
| `\s`    | Whitespace (space, tab, newline)  | " "           |
| `\S`    | Non-whitespace                    | A, 1          |
| `^`     | Start of string                   | ^Hello        |
| `$`     | End of string                     | World$        |

---

# Character Sets

| Pattern    | Meaning           |
| ---------- | ----------------- |
| `[abc]`    | Match a, b, or c  |
| `[A-Z]`    | Uppercase letters |
| `[a-z]`    | Lowercase letters |
| `[0-9]`    | Digits            |
| `[A-Za-z]` | Any alphabet      |
| `[^abc]`   | Not a, b, or c    |

---

# Frequently Used Regex Patterns

## Email Address

Pattern:

```regex
\S+@\S+\.\S+
```

Example:

```text
support@gmail.com
admin@yahoo.com
```

---

## Phone Number (10 Digits)

Pattern:

```regex
\d{10}
```

Example:

```text
9876543210
9123456789
```

---

## Date (DD/MM/YYYY)

Pattern:

```regex
\d{2}/\d{2}/\d{4}
```

Example:

```text
15/06/2026
```

---

## Date (YYYY-MM-DD)

Pattern:

```regex
\d{4}-\d{2}-\d{2}
```

Example:

```text
2026-06-15
```

---

## URL

Pattern:

```regex
https?://\S+
```

Example:

```text
https://google.com
https://github.com
```

---

## Hashtag

Pattern:

```regex
#\w+
```

Example:

```text
#Python
#MachineLearning
```

---

## Username (@ Mention)

Pattern:

```regex
@\w+
```

Example:

```text
@mujtaba
@john
```

---

## Extract Numbers

Pattern:

```regex
\d+
```

Example:

```text
123
456
789
```

---

# Data Cleaning Patterns

## Remove Special Characters

Pattern:

```regex
[^a-zA-Z0-9 ]
```

Example:

Before:

```text
Hello!!! @Python###
```

After:

```text
Hello Python
```

---

## Remove Extra Spaces

Pattern:

```regex
\s+
```

Replace with:

```python
re.sub(r'\s+', ' ', text)
```

Before:

```text
Python      is      awesome
```

After:

```text
Python is awesome
```

---

# Validation Patterns

## Email Validation

```regex
^[\w\.-]+@[\w\.-]+\.\w+$
```

Valid:

```text
test@gmail.com
```

Invalid:

```text
test@gmail
```

---

## Indian Mobile Number Validation

```regex
^[6-9]\d{9}$
```

Valid:

```text
9876543210
```

Invalid:

```text
1234567890
```

---

# Common Regex Functions in Python

## Find All Matches

```python
re.findall(pattern, text)
```

Returns all matching values.

---

## Find First Match

```python
re.search(pattern, text)
```

Returns the first match.

---

## Match from Beginning

```python
re.match(pattern, text)
```

Checks only from the start of the string.

---

## Replace Text

```python
re.sub(pattern, replacement, text)
```

Used for text cleaning.

Example:

```python
re.sub(r'[^a-zA-Z0-9 ]', '', text)
```

---

# Quick Tips

* Use `r""` before regex patterns to create raw strings.
* Test regex patterns on small text samples first.
* Use `findall()` for extraction tasks.
* Use `sub()` for data cleaning tasks.
* Use `match()` or `search()` for validation tasks.

---

## Conclusion

Regex is a powerful tool for:

* Extracting information
* Cleaning text data
* Validating inputs
* Preprocessing datasets for machine learning and data analysis
