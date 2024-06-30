# 使用selenium套件取得X資料

## 程式說明
- 取得創作者發布的貼文 get_tweet_data
  ![image](https://github.com/shih-ting-2/x_selenium/assets/174265450/aa5b64cf-47c6-4f87-a75d-e2b2d314ceda)

- 取得創作者的簡介get_creator_data
  ![image](https://github.com/shih-ting-2/x_selenium/assets/174265450/91cfeaf9-ea46-443e-8349-86d20ab81d1b)

## 程式執行環境設定

1. 引用[selenium套件](https://selenium-python.readthedocs.io/locating-elements.html)
2. [安裝webdriver](https://googlechromelabs.github.io/chrome-for-testing/ )，並將exe檔和code放置於同一個目錄中。注意，**伺服器版本要和webdriver執行檔版本一致(例如122.XX.XX)**
3. 記得在程式裡給定帳號、密碼、要爬取的帳號(twitter_list) 

### 爬取X資料時常見問題
- 網頁更新之後，程式抓不到輸入框的位置，發生錯誤:
    - 修改程式碼，透過full xpath去定位網頁中的某元素。(# F12>>選取想要抓的區域>>在開發工具處code右鍵>>copy xpath)
- 輸入帳號密碼失敗:
    - 建議等畫面都跑出來再讓爬重按按鈕，可以設定sleep time，避免程式卡住
- 被X視為不明登入行為，登入失敗:
    - 同一帳號登入太頻繁，會被鎖帳，可以多辦幾隻帳號輪流登入

