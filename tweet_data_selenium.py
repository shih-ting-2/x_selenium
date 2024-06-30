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

# 請提供帳號密碼資訊
my_account_emails = ['futaba@gmail.com','c311706017@nycu.edu.tw', 'intheclocktown@gmail.com' ]  #帳號/email
my_usernames = ['futaba','c311706017','town'] # 暱稱  
my_passwords = ['*****','*****','*****']  #密碼
# 請提供想要爬取的帳號列表
twitter_list = ['MbiyuEliud', 'koeche646', 'anericod']
# 請提供dataset的儲存位置
save_dirPath = ''

short_sleep_time = 10  
long_sleep_time = 500 
desired_data_amount = 300
fileName = '' 
fileHeader = ['username','handle','postDate','textresponding','reply','retweets','likes']

selenuim(my_usernames, my_account_emails, my_passwords, twitter_list, 
             short_sleep_time, long_sleep_time, desired_data_amount, save_dirPath, fileName, fileHeader)

