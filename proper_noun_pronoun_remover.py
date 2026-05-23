"""
Remove proper nouns and pronouns from text files.

This script uses NLTK part-of-speech tagging to remove selected POS categories,
including proper nouns and pronouns, from a plain text file.
"""

from pathlib import Path

import nltk


REMOVED_TAGS = {
    "NNP",   # proper noun, singular
    "NNPS",  # proper noun, plural
    "PRP",   # personal pronoun
    "PRP$",  # possessive pronoun
    "WP",    # wh-pronoun
    "WP$",   # possessive wh-pronoun
}


def remove_proper_nouns_and_pronouns(text):
    """Return text with proper nouns and pronouns removed."""
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)

    kept_words = [
        word
        for word, tag in tagged_tokens
        if tag not in REMOVED_TAGS
    ]

    return " ".join(kept_words)


def main():
    """Run the remover workflow."""
    input_path = Path(input("Enter input .txt file path: ").strip())
    output_path = Path(input("Enter output .txt filename: ").strip())

    if not input_path.exists():
        print("Error: input file does not exist.")
        return

    text = input_path.read_text(encoding="utf-8")
    cleaned_text = remove_proper_nouns_and_pronouns(text)

    output_path.write_text(cleaned_text, encoding="utf-8")

    print(f"Saved cleaned text to {output_path}")


if __name__ == "__main__":
    main()
