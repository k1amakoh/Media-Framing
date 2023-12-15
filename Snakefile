# Define input and output files
news_url = "https://www.wsj.com/politics/elections"
headlines_file = “data/headlines.txt"
processed_headlines_file = “data/processed_headlines.txt"
analyze_headlines_file = “data/analysis_result.csv"
lda_model_file = "lda_model_20topics.model"
visualization_file = "output/wordcloud.png"

# Step 1: Scrape Headlines
rule scrape_headlines:
    """
    Rule to scrape headlines from a news website.
    """
    output: headlines_file
    shell: "python scripts/scrape_headlines.py --url {news_url} --output {output}"

# Step 2: Preprocess Headlines
rule preprocess_headlines:
    """
    Rule to preprocess headlines.
    """
    input: headlines_file
    output: processed_headlines_file
    shell: "python scripts/preprocess_headlines.py --input {input} --output {output}"

# Step 3: Analyze Headlines
rule analyze_headlines:
    """
    Rule to analyze processed headlines.
    """
    input: processed_headlines_file
    shell: "python scripts/analyze_content.py --input {input}"

# Step 4: LDA Modeling
rule train_lda:
    """
    Rule to train an LDA model.
    """
    input: processed_headlines_file
    output: lda_model_file
    shell: "python scripts/lda_model.py --input {input} --output {output}"

# Step 5: Test LDA Model
rule test_lda:
    """
    Rule to test the LDA model.
    """
    input: lda_model_file
    shell: "python scripts/test_model.py --input {input}"

# Step 6: Visualize LDA Model
rule visualize_lda:
    """
    Rule to visualize topics in headlines.
    """
    input: processed_headlines_file
    output: visualization_file
    shell: "python scripts/visualize_topics.py --input {input} --output {output}"
# Define a rule to clean up intermediate files
rule clean:
    """
    Rule to clean up intermediate files.
    """
    shell: "rm -f {headlines_file} {processed_headlines_file} {lda_model_file} {visualization_file}"

# Define a rule to run all steps
rule all:
    """
    Rule to run all steps.
    """
    input: headlines_file, processed_headlines_file, lda_model_file, visualization_file