# import requests
# from webbot import Browser
# import time
# from selenium import webdriver

# # driver = webdriver.Firefox('C:\\Users\\Phanatagama\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\selenium\\webdriver\\firefox\\geckodriver.exe')
# # # Go to your page url
# # driver.get('https://sso.unej.ac.id/cas/login?service=https%3A%2F%2Fkawanda.unej.ac.id%2Fapps%2Fuser_cas%2Flogin/')
# # # Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
# # button_element = driver.findElements(By.type('submit'))
# # button_element.click()

# web = Browser()
# time.sleep(2)
# web.go_to('https://instagram.com')
# time.sleep(1)
# web.type('phanatagama_',into='username')
# web.type('osingcoder2',into='password')
# web.click('Log In')
# time.sleep(5)
# web.click(xpath='/html/body/div[4]/div/div/div[3]/button[2]')
# for i in range(10):
# 	web.click(xpath='//*[@id="react-root"]/section/main/section/div/div[2]/div/article[{}]/div[2]/section[1]/span[1]/button/svg'.format(i))
# 	web.scrolly(200)
# 	time.sleep(1)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('C:/Users/Phanatagama/Downloads/chromedriver.exe')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        # login_button = driver.find_element_by_xpath("//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]") #//a[@href='/accounts/login/?source=auth_switcher']
        # login_button.click()
        # time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']") #//input[@name='username']
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")	#//input[@name='password']
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)
       # login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]') #//a[@href='/accounts/login/?source=auth_switcher']
       # login_button.click()
       # time.sleep(2)


    def like_photo(self, hashtag):
        time.sleep(3)
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
     
        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs 
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                komentar = ['Follback ya', 'follback dong', 'like back & follback ya', 'ditunggu follbacknya', 'follow balik ya', 'follback kak']
                komen = random.choice(komentar)
                time.sleep(random.randint(2, 4))
                follow = lambda: driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button").click()    
                print('sukses follow')
                follow()
                time.sleep(1)
                comment = lambda: driver.find_element_by_xpath('//textarea[@placeholder="Add a comment…"]') #//input[@name='username']
                comment().click()
                comment().send_keys(komen)
                comment().send_keys(Keys.RETURN)
                print('komentar sukses gan')
                time.sleep(1)
                like_button = lambda: driver.find_element_by_xpath('//span[@class="fr66n"]').click()    #//span[@aria-label="Like"] #/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[1]/div[2]/section[1]/span[1]/button/svg/path
                print('like akal akalann sukses')
                like_button()
                time.sleep(1)
                
                # for second in reversed(range(0, random.randint(18, 28))):
                #     print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                #                     + " | Sleeping " + str(second))
                #     time.sleep(1)
            except Exception as e:
            	print('gagal semua njer')
            	time.sleep(3)
            	# like_button = lambda: driver.find_element_by_xpath('//span[@class="fr66n"]').click()	#//span[@aria-label="Like"] #/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[1]/div[2]/section[1]/span[1]/button/svg/path
            	# print('like akal akalann sukses')
            	# like_button().click()
            finally:
                # comment = lambda: self.driver.find_element_by_xpath('//textarea[@placeholder="Add a comment…"]') #//input[@name='username']
                # comment().click()
                # comment().send_keys(komen)
                # comment().send_keys(Keys.RETURN)
                print('kampret')
                time.sleep(2)
            unique_photos -= 1

if __name__ == "__main__":

    username = "USERNAME"
    password = "PASSWORD"

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ['lfl', 'like4like', 'likeforlikes', 'f4f', 'followforfollow', 'follow4follow', 's4s', 'like4likes', 'likeforfollow']
    

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            # 
            time.sleep(2)
            ig.like_photo(tag)
        except Exception:
            print('you has been death :v')
            pass
            # ig.closeBrowser()
            # time.sleep(60)
            # ig = InstagramBot(username, password)
            # ig.login()
