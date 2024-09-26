import logging
import time
import pickle
import random
import csv
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(filename='kardashian_problems(15).log', encoding='utf-8', level=logging.DEBUG)

with open('data/kardashian_jenner_urls_jan_1_2024_to_july_31_2024_mediacloud.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    urls = [line[-1] for line in reader][1:]
    
def get_people_in_article(url):
    """
    Given a URL (string) of a TMZ article, 
    return a list of the names of the people (as strings) whose TMZ pages are linked in the article. 
    You can handle invalid URLs within this function or in the for loop below, 
    but make sure you're handling them!
    """
    #my_url = random.choice(urls)
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    
    people_in_article = []
    try:
        for text_line in soup.find_all('p'):
            a_tag = text_line.find_all('a')
            for tag in a_tag:
                href = tag.get('href')
                if 'https://www.tmz.com/people/' in href:
                    people_in_article.append(href.split('/')[-2])

    except requests.ConnectionError as e: 
        print('connection error')
        print(e)
        logging.debug('is this thing on?')
    
    except Exception as e:
        print('other error')
        print(e)
        logging.debug('is this thing on?')
    
    
    
    
    return people_in_article

lists_of_people = []
for url in random.sample(urls, 15):
    lists_of_people.append(get_people_in_article(url))
    time.sleep(7)
    
pickle.dump(lists_of_people, open('lists_of_people(15).pkl', 'wb'))