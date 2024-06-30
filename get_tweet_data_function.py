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
    
def selenuim(my_usernames, my_account_emails, my_passwords, twitter_list, 
             short_sleep_time, long_sleep_time, desired_data_amount, save_dirPath, fileName, fileHeader):

    for i, twitter in enumerate(twitter_list[0:]):
        print(i, twitter)
    
        # changing account
        index = i%(len(my_usernames))
        my_username=my_usernames[index]
        my_account_email=my_account_emails[index]
        my_password=my_passwords[index]
    
        if (i!=0) and (i % 5 == 0):
            time.sleep(long_sleep_time)
        else:
            time.sleep(short_sleep_time)

        chrome_options = Options()
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_experimental_option("detach", True)
    
        # setting the options & going to website 
        chrome_driver = webdriver.Chrome(options=chrome_options)
        # open the browser and maximize the window
        chrome_driver.maximize_window()

        chrome_driver.get('https://twitter.com/i/flow/login')
        # chrome_driver.get('https://www.reddit.com/login/')
    


        # some issue with twitter's flow login page - https://stackoverflow.com/questions/73748693/twitter-logging-automatically-by-using-the-selenium-module-unable-to-locate-ele
        username = WebDriverWait(chrome_driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="text"]'))
        )
        time.sleep(3) # attempt to scroll again 

        username.send_keys(my_account_email) # Email

        ## find element using xpath /html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div
        login_button = chrome_driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        chrome_driver.execute_script("arguments[0].click();", login_button)

        # verification of username 
        verify_username = WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="text"]'))
        )
        verify_username.send_keys(my_username) # @username
        verify_login_button = chrome_driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div')
                                                         #'/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')

        # Wait for 10 seconds before clicking the login button
        chrome_driver.execute_script("arguments[0].click();", verify_login_button)

       
        time.sleep(10)

        my_password_input = WebDriverWait(chrome_driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="password"]'))
        )
        my_password_input.send_keys(my_password)
        time.sleep(3) # attempt to scroll again 

        # log in button second
        login_button_second = chrome_driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
                                                         #'/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        chrome_driver.execute_script("arguments[0].click();", login_button_second)


        search_input = WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input'))
                                        #'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input'))
        )
 
        # search_input = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        # search_input.send_keys(f'(@{twitter}) min_replies:5 min_faves:10 lang:en until:2023-04-01 since:2022-09-01 -filter:retweets -filter:replies')
        search_input.send_keys(f' (from:{twitter})  lang:en until:2024-02-24 since:2022-02-10 -filter:replies')#高階搜尋

        search_input.send_keys(Keys.RETURN)

        latest_tab = WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a'))   
        )                                        
        chrome_driver.execute_script("arguments[0].click();", latest_tab)


        # chrome_driver.execute_script('window_scrollTo(0, document.body.scrollHeight);')

        # help from : https://stackoverflow.com/questions/70379706/driver-find-elements-by-xpath-divdata-testid-tweet-gives-no-output
        # getting a list of cards that contains the tweet cards 
        tweet_data = []
        tweet_ids = set()
        last_position = chrome_driver.execute_script("return window.pageYOffset;")
        scrolling = True
        try:
            while scrolling:
        
                if WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]'))):
                    cards = chrome_driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
        
                if len(cards) > 0:
                    # only care about the last 15 items 
                    for card in cards:
                        data = get_tweet_data(card)
                        
                        if data:
                            tweet_id = ''.join(str(item) for item in data)
                            if tweet_id not in tweet_ids:
                                tweet_ids.add(tweet_id)
                                tweet_data.append(data)
                else:
                    # Print text in red
                    raise NoSuchElementException('No cards were found')
                scrollAttempt = 0
                while True:
                    # check scroll position
                    chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
                    time.sleep(3)
                    currentPosition = chrome_driver.execute_script("return window.pageYOffset;")
                    if last_position == currentPosition:
                        scrollAttempt += 1
                
                        # end of scroll region 
                        if scrollAttempt >= 3:
                            scrolling = False
                            break
                        else:
                            time.sleep(5) # attempt to scroll again 
                    else:
                        last_position = currentPosition
                        break
            chrome_driver.quit()
            
        # saving the tweet 
            fileName = twitter+'_'+fileName
            with open(f'{save_dirPath+fileName}.csv','w',newline='', encoding='utf-8') as f:
                #fileHeader = header
                writer = csv.writer(f)
                writer.writerow(fileHeader)
                writer.writerows(tweet_data)
        except Exception as e:
            print(f"No data: {e}")            
            chrome_driver.quit()
            continue

