
# Text Summarizer

Sometimes reading long texts is tedious and time-consuming. Keeping this in mind, this Natural Language Processing (NLP) project aims to summarize PDF documents utilizing NLTK for stopword removal, generating a similarity graph and matrix using NetworkX, and saving the summarized content into a text file. The project offers a streamlined approach to summarize large textual data into concise summaries, enhancing readability and comprehension.

## Project Components:

### PDF Document Parsing:

The project facilitates parsing PDF documents, extracting textual content for subsequent processing.

### Stopword Removal using NLTK:

Utilizing the NLTK library, stopwords are removed from the extracted text. Stopwords, common words like "the", "is", etc., are filtered out as they do not contribute significantly to the meaning of the text.

### Similarity Graph Generation:

NetworkX is employed to construct a similarity graph based on the text content. This graph represents relationships between different sections or sentences within the document.

### Similarity Matrix Construction:

NetworkX is also utilized to generate a similarity matrix, providing a numerical representation of the relationships between different parts of the text.

### Text Summarization:

Leveraging the generated similarity graph and matrix, the project summarizes the document, condensing its contents into a more concise form.

### Output to Text File:

The summarized content is saved into a text file for easy access and reference.

## Instruction to Usage

Write the path of the pdf file that you want to summarize or write only the name if that pdf file is in the same folder. Adjust the value of the second parameter given to the function **generate_summary** to control the length of summarized text. You will find your summarized text in **Summarized.txt** file.

Now enjoy the summarized text.

## Dependencies
- **Python 3.x**
- **NLTK (Natural Language Toolkit)**
- **NetworkX**


## Deployment

To use the project, run the following command in the folder where you want to get the project.

```bash
  git clone git@github.com:anamfatima1304/TextSummarizer.git
```
Now play around with the model and enjoy.


## Installation

To run this project, you should have python istalled on your computer. Also install all the required packages by running the command in command prompt:

```bash
  pip install -r requirements.txt
```
  
## Contributing

Contributions are always welcome!

Find out an Error or give any suggestion to improve the project.

If you want to add any new features, make a pull request.

ThankYou for your attention.

**Happy Coding**
