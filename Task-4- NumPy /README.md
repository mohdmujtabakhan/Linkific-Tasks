# NumPy Cheat Sheet

## Import NumPy

```python
import numpy as np
```

---

## Array Creation

```python
np.array()
np.zeros()
np.ones()
np.arange()
np.linspace()
```

### Examples

```python
np.array([1, 2, 3])

np.zeros((3,3))

np.ones((2,4))

np.arange(1,11)

np.linspace(0,1,5)
```

---

## Array Information

```python
arr.ndim
arr.shape
arr.size
arr.dtype
```

### Examples

```python
arr = np.array([1,2,3,4,5])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

---

## Indexing & Slicing

```python
arr[0]
arr[-1]
arr[1:5]
arr[:3]
arr[-3:]
matrix[1,2]
```

### Examples

```python
arr = np.array([10,20,30,40,50])

print(arr[0])
print(arr[-1])
print(arr[1:4])
```

---

## Mathematical Operations

```python
a + b
a - b
a * b
a / b

arr + 10
arr - 10
arr * 2
arr / 2
```

### Examples

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## Statistical Operations

```python
np.sum()
np.mean()
np.std()
np.max()
np.min()
np.median()
```

### Examples

```python
arr = np.array([15,7,22,3,18])

print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.max(arr))
print(np.min(arr))
```

---

## Array Manipulation

```python
arr.reshape()
arr.flatten()
arr.transpose()
np.concatenate()
np.append()
np.insert()
np.delete()
```

### Examples

```python
arr = np.arange(12)

arr.reshape(3,4)

arr.flatten()
```

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

np.concatenate((a,b))
```

---

## Broadcasting

```python
arr + 10

a + b
a - b
a * b
a / b
```

### Example

```python
a = np.array([[1],
              [2],
              [3]])

b = np.array([10,20,30])

print(a + b)
```

Output:

```text
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```

---

## Random Number Generation

```python
np.random.rand()
np.random.randn()
np.random.randint()
np.random.seed()
```

### Examples

```python
np.random.rand(5)

np.random.randint(1,100,10)

np.random.randint(1,50,(3,3))
```

---



---

## Learning Outcome

After completing this task, I learned:

- NumPy array creation and manipulation
- Indexing and slicing techniques
- Mathematical and statistical operations
- Reshaping and broadcasting
- Random number generation
- Efficient numerical computing using NumPy
