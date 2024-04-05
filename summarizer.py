import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
from pypdf import PdfReader 

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    list1 = [0] * len(all_words)
    list2 = [0] * len(all_words)
 
    # For the First Sentence
    for w in sent1:
        if w in stopwords:
            continue
        list1[all_words.index(w)] += 1
 
    # For the First Sentence
    for w in sent2:
        if w in stopwords:
            continue
        list2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(list1, list2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(file_name, top_n=5):
    # nltk.download("stopwords")
    stop_words = stopwords.words('english')

    # Step 1 - Read text from pdf 
    reader = PdfReader(file_name) 
    summarize_text = []
  
    # getting number of pages in pdf file 
    length = len(reader.pages)
    # getting all the pages and summarizing one by one
    for i in range(1,length):
        page = reader.pages[i] 
        text = page.extract_text()
        article = text.split(". ")
        article = [text.replace(u'\xa0', u' ') for text in article]
        sentences = []

        for sentence in article:
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))

    # Step 2 - Generate Similary Martix across sentences
        sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
        scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
        ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
        # print("Indexes of top ranked_sentence order are ", ranked_sentence)    

        for i in range(int(len(ranked_sentence)/top_n)):
            summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Output the summarize text and saving it in a .txt file
    summarize_text = [text.replace("\n", " ") for text in summarize_text]
    summary = "\n".join(summarize_text)
    print(f"SummarizedText : \n", ". ".join(summarize_text))
    with open(f"Summarized.txt", "w", encoding="utf-8") as output:
        output.write(summary)


if __name__=="__main__":
    file_name = input("Enter the path of pdf file:")
    generate_summary(file_name, 3)