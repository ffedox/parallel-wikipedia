# A semi-automatic approach to parallel corpora extraction from the Wikipedia

This repository contains the software developed for the pilot project of the Profession-Based Research course. The main task of the project was to identify in-domain Wikipedia articles in English and Italian, in order to extract a parallel corpus.

## Contents

1. [Parallel_corpus_creation.ipynb](https://github.com/ffedox/pbr/blob/main/parallel_corpus_creation.ipynb):
2. Parallel_corpus_script.py:
3. Report:

## Data

The extracted corpus is available in .xlsx and .tmx format. 

## Getting the code

You can download a copy of all the files in this repository by cloning the
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
7. If you want to use a GPU: Install [PyTorch](https://pytorch.org/) <br />
`pip install torch` <br />
