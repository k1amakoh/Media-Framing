#!/usr/bin/env python
"""
Script to visualize topics in headlines.

Requirements:
- Gensim: pip install gensim
- Matplotlib: pip install matplotlib
- Seaborn: pip install seaborn
- WordCloud: pip install wordcloud
"""

import os
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from preprocess_headlines import preprocess_text


def visualize_wordcloud(processed_headlines, save_dir):
    """
    Generate a word cloud and bar graph from the processed headlines.

    Parameters:
    - processed_headlines (list): List of processed headlines.
    - save_dir (str): Directory to save visualization outputs.
    """
    # Concatenate all processed headlines into a single text
    all_headlines_text = ' '.join([' '.join(tokens)
                                  for tokens in processed_headlines])

    # Generate WordCloud
    wordcloud = WordCloud(
        width=800, height=400, background_color='white').generate(all_headlines_text)

    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud for Processed Headlines')

    # Save the word cloud as a PNG file
    wordcloud_path = os.path.join(save_dir, 'wordcloud.png')
    plt.savefig(wordcloud_path)
    plt.show()

    # Most common words in the headlines
    # Preprocess the headlines
    processed_tokens = preprocess_text(all_headlines_text)

    # Count the frequency of each word
    word_counts = Counter(processed_tokens)

    # Get the most common words and their frequencies
    top_words = word_counts.most_common(20)

    # Extract words and frequencies for plotting
    words, frequencies = zip(*top_words)

    # Plot a bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 20 Most Common Words in Headlines')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the bar graph as a PNG file
    bar_graph_path = os.path.join(save_dir, 'bar_graph_headlines.png')
    plt.savefig(bar_graph_path)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    # Set the default file path
    default_filepath = "data/processed_headlines.txt"

    # Use the provided file path or the default one
    filename = sys.argv[1] if len(sys.argv) == 2 else default_filepath

    # Read headlines from a file or any other source
    with open(filename, 'r', encoding='utf-8') as file:
        headlines = [line.strip() for line in file.readlines()]

    # Specify the output directory
    output_dir = "output"

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Preprocess headlines
    processed_headlines = [preprocess_text(headline) for headline in headlines]

    # Visualize the word cloud and most common words
    visualize_wordcloud(processed_headlines, output_dir)
