# Text Similarity Calculator

A Python implementation of cosine similarity to measure how similar two texts are to each other.

## What is Cosine Similarity?

Cosine similarity is a metric used to determine how similar two documents are regardless of their size. Mathematically, it measures the cosine of the angle between two vectors in a multi-dimensional space.

The mathematical formula is:
```
Cosine Similarity = (A·B) / (||A|| × ||B||)
```
Where:
- A·B is the dot product of vectors A and B
- ||A|| and ||B|| are the magnitudes (or norms) of vectors A and B

## How This Program Works

1. **Input**: The program takes two text strings as input.

2. **Text Processing**:
   - Converts the texts to lowercase
   - Splits them into individual words
   - Creates frequency matrices for each word in both texts

3. **Vector Creation**:
   - Each unique word becomes a dimension in our vector space
   - The frequency of each word becomes its magnitude in that dimension

4. **Similarity Calculation**:
   - Calculates the dot product of the two word frequency vectors
   - Calculates the magnitudes of both vectors
   - Computes the cosine similarity using the formula above

5. **Output**: Returns a similarity score between 0 and 1
   - 1 means the texts are identical
   - 0 means they have nothing in common
   - Values in between indicate partial similarity

## Usage

Run the program and input two texts when prompted:

```
python cosine.py
```

Example:
```
Text 1: Julie loves me more than Linda loves me
Text 2: Jane likes me more than Julie loves me
```

The program will display:
- The words and their frequencies in each text
- The dot product calculation
- The final cosine similarity score
