# Media-Framing

#Motivation
The media plays a unique role in shaping public opinion and setting the agenda. This project identifies the tone used to report the 2024 U.S. elections in the Wall Street Journal. It is important to examine how the media report relevant events such as elections. Electorates form their judgments about an election based on the information received from the media. Therefore, the overarching question guiding this project is: "How does the media frame the U.S. Elections?"

#Workflow
The workflow is automated using the Snakemake workflow. To activate this automatic process, there is a Snakefile that contains the six-step process of this project (scrape headlines, process headlines, analyze headlines, topic modeling using the Latent Dirichlet Allocation (LDA) technique, testing the functions created and visualizing the model output. 

Second, the scripts folder contains all the scripts needed to run the Snakefile - analyze_content.py, lda_modeling.py, preprocess_headlines.py, scrape_headlines.py, test_model.py, and visualize_topics.py.

Third, the data folder contains the saved data derived from running the abovementioned scripts in the workflow. For example, the headlines.txt is derived whenever the scrape_headlines.py script is run. This .txt file will aggregate all the headlines on the website at that given time. Hence, it is important to highlight that .txt is a fluid file and it is bound to change depending on when the scraping process takes place. Also, this is likely to impact the output throughout the process. Other data files include analysis_results.csv,lda_model_20topics.model, and processed_headlines.txt.

Fourth, the output folder contains the visualization derived from the data folder. The main visualization includes the most common words used in the headlines. To show this, I plotted some word clouds and bar graphs to highlight these. 

#Findings
This is a light version of the main project. Preliminary results from this project suggest that the incumbent, Joe Biden currently receives more media coverage, especially in WSJ. On the other hand, the major opponent, Donald Trump receives the most coverage among the opposing contenders. I expect that this is likely to shift even as the campaigns intensify and political parties select their candidates.  
