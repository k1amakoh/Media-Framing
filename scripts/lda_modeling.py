#!/usr/bin/env python
"""
Script to perform LDA (Latent Dirichlet Allocation) modeling on a corpus.

Requirements:
- Gensim: pip install gensim
"""
import sys
import os
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from analyze_content import analyze_content


def train_lda_model(processed_headlines, num_topics=20, passes=30):
    """
    Train an LDA model using processed headlines.

    Parameters:
    - processed_headlines (list): List of processed headlines.
    - num_topics (int): Number of topics for the LDA model.
    - passes (int): Number of passes for LDA model training.

    Returns:
    - gensim.models.LdaModel: Trained LDA model.
    """
    # Create a dictionary and corpus for Topic Modeling
    dictionary = Dictionary(processed_headlines)
    corpus = [dictionary.doc2bow(doc) for doc in processed_headlines]

    # Train the LDA model
    lda_model = LdaModel(corpus, num_topics=num_topics,
                         id2word=dictionary, passes=passes)

    # Print the perplexity
    perplexity = lda_model.log_perplexity(corpus)
    print(f"Model perplexity: {perplexity}")

    return lda_model


def save_lda_model(lda_model, filename="lda_model.model"):
    """
    Save the trained LDA model to a file.

    Parameters:
    - lda_model (gensim.models.LdaModel): Trained LDA model.
    - filename (str): Filepath to save the model.
    """
    # Get the absolute path for the current directory
    current_directory = os.getcwd()

    # Create the absolute path for saving the model
    absolute_path = os.path.join(current_directory, filename)

    lda_model.save(absolute_path)
    print(f"LDA model saved to {absolute_path}")


def print_topics(lda_model, num_words=5):
    """
    Print topics and their top words.

    Parameters:
    - lda_model (gensim.models.LdaModel): Trained LDA model.
    - num_words (int): Number of top words to display for each topic.
    """
    topics = lda_model.print_topics(num_words=num_words)
    for topic in topics:
        print(f"Topic {topic[0]}: {topic[1]}")


def main():
    # Set the default file path
    default_filepath = "data/processed_headlines.txt"

    # Use the provided file path or the default one
    filename = sys.argv[1] if len(sys.argv) == 2 else default_filepath

    # Read processed headlines from the specified file
    with open(filename, 'r') as file:
        processed_headlines = [line.strip().split()
                               for line in file.readlines()]

    # Train the LDA model with 10 topics
    lda_model = train_lda_model(processed_headlines, num_topics=20)

    # Save the LDA model with an absolute path
    save_filename = "lda_model_20topics.model"
    save_lda_model(lda_model, save_filename)

    # Print topics
    print_topics(lda_model)


if __name__ == "__main__":
    main()
