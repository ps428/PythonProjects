# Name Permutation and Meanings

A Python tool that finds the meaning of names and generates all possible permutations of given letters to create new names.

## What It Does

This tool has two main functions:

1. **Find the meaning of existing names** by querying online dictionary resources
2. **Generate new name ideas** by creating all possible permutations of a set of letters

## How It Works

### Name Meaning Lookup

The program uses web scraping to find the meanings of names:

1. It connects to dictionary.com to search for the meaning of the name
2. It extracts definitions from the HTML response
3. It cleans and formats the definitions for display

### Name Permutation Generator

The program can also help you brainstorm new names:

1. Enter a set of letters (e.g., "ALEY")
2. The program generates all possible permutations of these letters (ALEY, ALYE, AELY, etc.)
3. You can then check the meanings of any interesting combinations

## Usage

```
python meaning.py
```

When running the program, you can:
- Enter a single name to find its meaning
- Enter a set of letters to generate all permutations
- View the definitions of each name or permutation

## Requirements

- Python 3.x
- urllib (included in standard library)
- re (included in standard library)
