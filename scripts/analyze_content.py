#!/usr/bin/env python

import sys
import re
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
import unicodedata
from unidecode import unidecode


def preprocess_text(text):
    """
    Preprocesses the given text by tokenizing, normalizing, and removing non-alphanumeric characters.

    Parameters:
    - text (str): The input text to be preprocessed.

    Returns:
    - list: A list of processed tokens.
    """
    tokens = word_tokenize(text.lower())

    # Use unidecode to handle non-ASCII characters and normalize
    tokens = [unidecode(token) for token in tokens]

    # Remove remaining non-alphanumeric characters and extra spaces
    tokens = [token for token in tokens if token.isalnum()]

    return tokens


def analyze_content(processed_headlines):
    """
    Analyzes the content of processed headlines and generates a DataFrame with word frequencies.

    Parameters:
    - processed_headlines (list): A list of processed headlines, where each headline is represented as a list of tokens.

    Returns:
    - pd.DataFrame: A DataFrame with columns 'Word' and 'Frequency' representing word frequencies.
    """
    processed_text = [
        word for sublist in processed_headlines for word in sublist]
    word_frequency = Counter(processed_text)
    word_frequency_df = pd.DataFrame(
        list(word_frequency.items()), columns=['Word', 'Frequency'])
    word_frequency_df = word_frequency_df.sort_values(
        by='Frequency', ascending=False)
    return word_frequency_df


def main():
    """
    The main function reads processed headlines from a file, performs analysis, and saves the result to a CSV file.
    """
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
