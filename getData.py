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
def get_creator_data(card):
    # # username , getting the first span tag after the current tag
    username = card.find_element(By.XPATH,'.//span').text 
    # print("Username: " + username + "\n")
    # twitter handle 

    creator_page = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/a')))
    #/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/a
    chrome_driver.execute_script("arguments[0].click();", creator_page)
    
    if WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]'))):
       
     # Get the introduction, number of following, number of follower of this user
        intro_element = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div/span')))
        following_element = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span')))
        follower_element = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span')))
        
        intro = intro_element.text 
        following = following_element.text 
        follower = follower_element.text 
        
        print(intro,following,follower)
    user_bg = (intro,following,follower)
    return user_bg
