from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass


import pandas as pd 
import time 
import csv

def get_tweet_data(card):
    # # username , getting the first span tag after the current tag
    username = card.find_element(By.XPATH,'.//span').text 

    handle = card.find_element(By.XPATH,'.//span[contains(text(),"@")]').text 

    try:
        postDate = card.find_element(By.XPATH, './/time').get_attribute('datetime')
    except NoSuchElementException:
    # Handle the missing element, e.g., set a default value or skip this data point
        postDate = None
        return
    # content of tweet 
    responding = card.find_element(By.XPATH, './/div[2]/div[2]/div[2]').text
    # print("Responding: " + responding + "\n")
    
    # reply
    if card.find_element(By.CSS_SELECTOR,'div[data-testid="reply"]').text is not None:
        reply = card.find_element(By.CSS_SELECTOR,'div[data-testid="reply"]').text
        # print("Reply " + reply + "\n")
    else:
        reply = 'None'
        # print("Reply: 0\n")
    
    # retweet 
    if card.find_element(By.CSS_SELECTOR,'div[data-testid="retweet"]').text is not None:
        retweets = card.find_element(By.CSS_SELECTOR,'div[data-testid="retweet"]').text
        # print("Retweets: " + retweets + "\n")
    else: 
        retweets = 'None'
        # print("Retweets: 0\n")
    
    # likes 
    if card.find_element(By.CSS_SELECTOR,'div[data-testid="like"]').text is not None:
        likes = card.find_element(By.CSS_SELECTOR,'div[data-testid="like"]').text
        # print("Likes: " + likes + "\n")
    else:
        likes = 'None'
        # print("Likes: 0\n")
    
    tweet = (username,handle,postDate,responding,reply,retweets,likes)
    return tweet
