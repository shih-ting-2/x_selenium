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
