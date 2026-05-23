# Proper Noun and Pronoun Remover

A Python NLP tool for removing proper nouns and pronouns from plain text files.

## Overview

This project uses NLTK part-of-speech tagging to identify and remove proper nouns and pronouns from a text file. It can be used as a preprocessing step for text analysis tasks where names, personal references, or character-specific markers should be reduced.

## Features

- Reads a plain `.txt` file
- Tokenizes text with NLTK
- Tags each token by part of speech
- Removes proper nouns and pronouns
- Saves the cleaned text to a new file

## Removed POS Tags

- `NNP` — proper noun, singular
- `NNPS` — proper noun, plural
- `PRP` — personal pronoun
- `PRP$` — possessive pronoun
- `WP` — wh-pronoun
- `WP$` — possessive wh-pronoun

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
Downlaod required NLTK data:
```python
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
```

## How to Run
```bash
python proper_noun_pronoun_remover.py
```
You will be prompted for:
1. The input `.txt` file path
2. The output `.txt` filename

## Skills Demonstrated
* Python scripting
* Natural language processing
* Part-of-speech tagging
* Text pre-processing
* Corpus cleaning
* File handling

## Limitations
This script depends on automated POS tagging, so results may not be perfect. Names, pronouns, and ambiguous words may occasionally be missed or incorrectly removed depending on context.

## Future Improvements
* Add command-line arguments
* Preserve punctuation spacing more cleanly
* Export removed words separately
* Add summary statistics
* Support batch processing for folders of `.txt` files
