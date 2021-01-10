from selenium import webdriver
from time import sleep



class bot():
    def __init__(self):
        self.driver = webdriver.Chrome('Chrome Web Driver PATH')

    def login(self):
        self.driver.maximize_window()
        self.driver.get('https://tinder.com')
        sleep(2)


        loginbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').text
        if 'PHONE' in loginbtn:
            moreoption = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button').click()
            fblogin = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button').click()
        else:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()
        sleep(2)

        workspace = self.driver.window_handles[0]
        popup = self.driver.window_handles[1]
        self.driver._switch_to.window(popup)

        sleep(2)

        email_fb = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_fb.send_keys('EMAIL')
        passwd_fb = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwd_fb.send_keys('PASSWORD')

        loing_fb = self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
        sleep(3)

        self.driver.switch_to.window(workspace)

        sleep(2)


        allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow.click()

        sleep(1)


        enable = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable.click()

        sleep(1)

        acc_cookie = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        acc_cookie.click()

        sleep(1)
        nothanks = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        nothanks.click()
        sleep(1)

    def like(self):
        sleep(2)

        like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()
        sleep(1)

    def sendmsg(self):
        textbox = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        textbox.send_keys('Hey Cutie')
        sleep(2)
        sendmsg = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
        sendmsg.click()
        sleep(2)


b = bot()
b.login()

for i in range(50):
    try:
        b.like()
    except :
        b.sendmsg()
