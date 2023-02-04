# A semi-automatic approach to parallel corpora extraction from the Wikipedia

This repository contains the software developed for the pilot project of the Profession-Based Research course. The main task of the project was to identify in-domain Wikipedia articles in English and Italian in order to extract a parallel corpus.

## Contents

1. [Parallel_corpus_creation.ipynb](https://github.com/ffedox/pbr/blob/main/parallel_corpus_creation.ipynb): our semi-automatic pipeline for the extraction of parallel corpora from Wikipedia. 
2. [Parallel_corpus_script.py](https://github.com/ffedox/pbr/blob/main/parallel_corpus_script.py): a Python script that can be used to extract parallel articles from the command line.
3. [Text_cleaning.ipynb](https://github.com/ffedox/pbr/blob/main/text_cleaning.ipynb): preprocessing options for cleaning the corpus (removing duplicate sentences, removing newlines etc.).
4. Report: written report providing a detailed overview of the proposed solution and the thought process behind it.

## Data

The extracted corpus is available in [.xlsx](https://docs.google.com/spreadsheets/d/1wj0yUTVTfIckiWAGbxc0-M3sVBfNDDWn/edit?usp=sharing&ouid=116503555824878479100&rtpof=true&sd=true) and [.tmx](https://drive.google.com/file/d/1MbHsMEtkw-DKAKQWyPXqa_6yrmmpxmJx/view?usp=sharing) format. 

## Getting the code

A copy of all the files can be downloaded by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/ffedox/pbr

## Setup and installation
1. Install [Pandas](https://pandas.pydata.org/) <br />
`pip install pandas` <br />
2. Install [Numpy](https://numpy.org/) <br />
`pip install numpy` <br />
3. Install [Scipy](https://scipy.org/) <br />
`pip install scipy` <br />
4. Install [NLTK](https://www.nltk.org/) <br />
`pip install nltk` <br />
5. Download punkt from [NLTK](https://www.nltk.org/nltk_data/) (for tokenizing the texts into sentences) <br />
`python3 -m nltk.downloader punkt` <br />
5. Install [Wikipedia-API](https://github.com/martin-majlis/Wikipedia-API) <br />
`pip install wikipedia-api` <br />
6. Install [Sentence-Transformers](https://github.com/UKPLab/sentence-transformers) <br />
`pip install sentence-transformers` <br />
7. To use a GPU: Install [PyTorch](https://pytorch.org/) <br />
`pip install torch` <br />
 
