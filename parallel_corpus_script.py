from sentence_transformers import models, SentenceTransformer
from nltk.tokenize import sent_tokenize
from json import JSONDecodeError
import wikipediaapi
import pandas as pd
import numpy as np
import scipy
import nltk

page_titles = []
page_texts_it = []

def get_it_articles(category, page_titles, page_texts_it):

  wiki_wiki = wikipediaapi.Wikipedia('it')
  cat = wiki_wiki.page(category)   

  for p in cat.categorymembers.values():
    if p.namespace == wikipediaapi.Namespace.MAIN:
      page_titles.append(p.title)
      page_texts_it.append(p.text)

category = input("Enter a Category from the IT Wiki like this -> Categoria:Nome_categoria  ")

print("Retrieving IT articles...")

get_it_articles(category, page_titles, page_texts_it)

page_texts_en = []

def get_langlinks(page, page_texts_en):

        langlinks = page.langlinks

        for k in sorted(langlinks.keys()):
            v = langlinks[k]

        try:
          page_en = page.langlinks['en']
          page_texts_en.append(page_en.text)

        except KeyError:
          page_texts_en.append(str('No match'))
          
        except JSONDecodeError:
           page_texts_en.append(str('No match'))

def get_en_articles(page_titles, page_texts_en):

  for title in page_titles:

    wiki_wiki = wikipediaapi.Wikipedia('it')
    page = wiki_wiki.page(str(title))
    get_langlinks(page, page_texts_en)

print("Retrieving EN articles...")

get_en_articles(page_titles, page_texts_en)

comparable_corpus = pd.DataFrame(np.column_stack([page_texts_en, page_texts_it]), 
                               columns=['en', 'it'])

comparable_corpus = comparable_corpus[comparable_corpus['en'].str.contains('No match')==False].reset_index(drop=True)

print("Comparable corpus extracted.")

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return comparable_corpus.to_excel('comparable_corpus.xlsx')
    if reply[0] == 'n':
        pass
    else:
        pass

yes_or_no('Export the comparable corpus to Excel?') 

print("Loading the Sentence-BERT model...")

model = SentenceTransformer('distiluse-base-multilingual-cased')

parallel_sentences_en = []
parallel_sentences_it = []

def extract_parallel_sents(comparable_corpus, parallel_sentences_en, parallel_sentences_it):

  closest_n = 1

  for en, it in zip(comparable_corpus.en.values, comparable_corpus.it.values): # Looping throuth the texts in the comparable corpus

    corpus = sent_tokenize(en)
    queries = sent_tokenize(it)

    corpus_embeddings = model.encode(corpus)
    query_embeddings = model.encode(queries)

    for query, query_embedding in zip(queries, query_embeddings):
      
      distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]

      results = zip(range(len(distances)), distances)
      results = sorted(results, key=lambda x: x[1])

      for idx, distance in results[0:closest_n]:
        if 1-distance > 0.8: # Similarity threshold
          parallel_sentences_it.append(query)
          parallel_sentences_en.append(corpus[idx].strip())

print("Extracting parallel sentences...")

extract_parallel_sents(comparable_corpus, parallel_sentences_en, parallel_sentences_it)

parallel_corpus = pd.DataFrame(np.column_stack([parallel_sentences_en, parallel_sentences_it]), 
                               columns=['en', 'it'])

def yes_or_no_2(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return parallel_corpus.to_excel('parallel_corpus.xlsx')
    if reply[0] == 'n':
        pass
    else:
        pass

yes_or_no_2('Export the parallel corpus to Excel?') 