#!/usr/bin/env python

"""
Script to preprocess headlines by tokenizing, removing stopwords, and punctuation.

Requirements:
- NLTK: pip install nltk
"""
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from scrape_headlines import scrape_and_save_headlines


def preprocess_text(text):
    """
    Preprocess a given text by tokenizing, removing stopwords, and punctuation.

    Parameters:
    - text (str): The input text.

    Returns:
    - list: List of processed tokens.
    """
    # Tokenize
    tokens = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    tokens = [token for token in tokens if token not in stop_words]

    return tokens


def read_headlines_from_file(file_path='data/headlines.txt'):
    """
    Read headlines from a file.

    Parameters:
    - file_path (str): The path to the file containing headlines. Default is 'data/headlines.txt'.

    Returns:
    - list: List of headlines.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        headlines = [line.strip() for line in file.readlines()]
    return headlines


def preprocess_and_save_headlines(headlines, output_file='data/processed_headlines.txt'):
    """
    Preprocess a list of headlines by tokenizing, removing stopwords, and punctuation,
    and save the processed headlines to a text file.

    Parameters:
    - headlines (list): List of headlines.
    - output_file (str): The path to the file to save processed headlines. Default is 'data/processed_headlines.txt'.
    """
    # Preprocess headlines using the imported function from preprocess.py
    processed_headlines = [preprocess_text(headline) for headline in headlines]

    # Filter out empty documents
    processed_headlines = [doc for doc in processed_headlines if doc]

    # Check if there are still processed headlines after filtering
    if not processed_headlines:
        print("No processed headlines after filtering. Check the preprocessing steps.")
    else:
        # Save processed headlines to a text file
        output_path = os.path.join(os.getcwd(), output_file)
        with open(output_path, 'w', encoding='utf-8') as file:
            for processed_headline in processed_headlines:
                file.write(' '.join(processed_headline) + '\n')

        print(f"Processed headlines saved to {output_path}")


# URL of the news website
news_url = 'https://www.wsj.com/politics/elections'

# Uncomment the line below to re-scrape headlines
# scrape_and_save_headlines(news_url)

# Read headlines from the file
headlines_file_path = 'data/headlines.txt'
headlines = read_headlines_from_file(headlines_file_path)

# Call the function to preprocess and save to 'data/processed_headlines.txt'
preprocess_and_save_headlines(headlines)
