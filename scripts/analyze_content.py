#!/usr/bin/env python

import sys
import re
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
import unicodedata
from unidecode import unidecode


def preprocess_text(text):
    tokens = word_tokenize(text.lower())

    # Use unidecode to handle non-ASCII characters and normalize
    tokens = [unidecode(token) for token in tokens]

    # Remove remaining non-alphanumeric characters and extra spaces
    tokens = [token for token in tokens if token.isalnum()]

    return tokens


def analyze_content(processed_headlines):
    processed_text = [
        word for sublist in processed_headlines for word in sublist]
    word_frequency = Counter(processed_text)
    word_frequency_df = pd.DataFrame(
        list(word_frequency.items()), columns=['Word', 'Frequency'])
    word_frequency_df = word_frequency_df.sort_values(
        by='Frequency', ascending=False)
    return word_frequency_df


def main():
    # Specify the default file path
    default_filename = 'data/processed_headlines.txt'

    # Try to read processed headlines from the default file
    try:
        with open(default_filename, 'r', encoding='utf-8') as file:
            processed_headlines = [preprocess_text(
                line.strip()) for line in file.readlines()]

        processed_headlines = [doc for doc in processed_headlines if doc]

        if not processed_headlines:
            print(
                "No processed headlines after filtering. Check the preprocessing steps.")
        else:
            print("Processed headlines after filtering empty documents:",
                  processed_headlines)

            result = analyze_content(processed_headlines)

            save_filename = "data/analysis_result.csv"
            result.to_csv(save_filename, index=False)
            print(f"Analysis result saved to {save_filename}")

    except FileNotFoundError:
        print(
            f"Error: {default_filename} not found. Check the file path or run the preprocess script.")


if __name__ == "__main__":
    main()
