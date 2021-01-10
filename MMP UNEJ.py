# import requests
# import webbrowser as wb

# #wb.open('https://sso.unej.ac.id/cas/login?service=https%3A%2F%2Fmmp.unej.ac.id%2Flogin%2Findex.php')
# payload = {
#     'username': "USERNAME",
#     "password": "PASSWORD",
#     "execution": "e22600de-66bd-4b5b-b98f-3186108d402b_ZXlKaGJHY2lPaUpJVXpVeE1pSjkucTFKU3dQRERuNzVucit6a2hUUGZURmlBS3F2eVRaa2lLRnRRTVIzUDQ2RWZkMjJxVEZ6MWJ6RHlZT0NzQVZlLzVHbnQ0MzdFRkoySjQ4cFpXOWRNYUIrelVza3ZJclRaOVZ2c0RqeU8yQXNsSU9wV3RpbFZFdkFRUzVoR25NQXVGc3BHRGFSTExNdzJGbHBKVzhBY3ZZWHJ0ZFRzV1RTUmtJUGlPWHYwSjJHc1BqYVd0SkRUNkMvUnNvb0E4Y2toMlF2dEd0WmRZKzY4Mm5ERzdwdE43YmxCbjltUnpHSm9kWEMvY1ZYUG1pdFV4NHJWeUh2S2NMODJiRlVJK0p2Mi8va1M0elhyZ0JJYWhVNzEvdUZHQ2xkSUdJMW9rTEszN3hJcnptQWhXbHRmWGowOUhoSFhOaXVrNUxNdyt6T3VNVkx5MlRZajZsVlV5RG9XM2tzeVljTWdFV0ljcVBWODg1Yk5udjljbWlYalBlcHFhNTdvM3dSeDMrVUh2aGdvQ0ljTnZWV280L2VnSmo4WnlMdVFEUGpDd01uYmRWSlpJd2lBTjlBOFA3YTR5VVYzdTJXL0V3QUl2Z0FKYlJXVUtvSEpRMEQ4dmRNbXVXVHZDYXpOaFVTSGFJamwxUUhyL3N5S1hPREkzcGlGRmxROFRTSFhjbXp4SVVNWE5aZWsvK0pUUlRZM29PeWtJbVhoWDM5bVFyQ0FCcE9NaXlmQ29zYUNlVzFTKzNzRjVibHpnVGRMbGw1bWlVM2RsSnR3ZmN6eVg0RGxLd2NHRlJIYnJ4anVWOEhheWwyYUlub0RpSmRkYkFLeDVORjhzeDRTOXI1cjhKQVhDNUw5ZFRiSzZscFZRQXl0VnhoVVAvT1MwdGwyKzJ5cWk0MWdRbmx3VDNVR1ZkQkFPU2Z6MDlzYitnODE5UEJEN3lHUjE3dUtMZXZlRVJoSS9JV3p6VXljbnkwak1uQUZBZjc3S012OE9jU08xNm16WFNjK1FMMkZzUnBWSUJOeW41a1pudnZmMUh4c3BUMkprakR5WXViV0NLQlhzdi9wUHd1TVJxb0hVOUIzZmp0aTRwV25yYi8vMUtHTDdQR1NTL0FWN2lpc3hPV0gwZFEwMGdSSXI3WDZwWTd6MTMzOWlRd1Ayb0FUT2ZUZ2ZMTjNCS2lrcEU0eVA4dTExYnpBV2ZyUmRNMnpnZ29rc250ZllHSHQycnNXN1ZaVU5jRHM5N2RNNnBtNlJRZmRiOGRNdU1iR2RLSkVzUGpobUk1MFl1TTRLMmpTS1BrYm9YYXlVUnlDOCtBaytyZ1pMZ1pPbThRaWtsSWpWeThheDJVQ09OZUFsVDJWMUJtOE43YkFscEJFVTZ5NVRxVWhrd2VMWk5BTmM0OVErcW53eWVHZ3dneFNqRWpINTFQNHdPeDM3dXRHWVZjRUkvVzJDMHJpaEtsenVvNnk1dEVzY3hiL3JkSGdHdm1nQ3l0MERCYkdWZFo2RlUrT3JmVWpQU0Q3OHEvcHlrRXBoMk0yRVovWHYzYXpzd2dPY2RmY1dHODUzenpSdkJYbDFhTEFlZVJBMElwd01WMDZuVzdRcVZXNnRLS3lIVy9yTHlHUzRaYUx2eFM1dlVOZWdEd0xKdUtGZGlvVEdTakdLK1daL2NjNXg0cGorWVRobFBrYWVmYXVSNmhGTnlCNzUvZzRveGFqSjhDNHdIS0QxYW9pWExta3htVWxGYi9kYS81ZmZpZno3K1dKbE1yTGQ3dXVOVS9aRUYzVkVmbFo5T2VNUEgzZ0psamVRcTdoTW55cHUxMU9XZ3lQeW0zNFd1Y0Z5cDEreW9Bd0dyOHdVLy8vdE1LOFFaQmhuUjNCZks3VWswQlpReXdkcGtLY2M3U3VyTzdrZFpQK3pURElpR0M2cjJ1MnJ5bnhwOXNhQmMzbjJIWWZJc04yM2dFRG1XM2g5STZ1TmluNzd0T2hVeGhHUjMrWklhS1gzNjN2eUZmYXhDV1FMdWVMQUpQQXZZTXZxczNUVnhuOFpXeXRBcDA1L0Ruajl1VmJRQjJVMnFUalFmYWxqZE13NzVsZTdMdk8yK1YvMlhrZWFkaUN0MzZyeE9WeklIcmpzRUxJMHFUUmhBTVFoS21Hb3Z1WEgwYklDZ2grdjVxaWI2cnh6L0l4bjJQMG9UNHl6cGRjZXNBTnlxNXBiTmJWS2pLd2dTVlNudUw1KytTWWNEMXlNWUd2eUJFQ1FpMEVVTVVoRHJNMkxsL0NTb2hmcE9QQlVXSzRRVkRrNDBuaXFVVEd0Z0p4SFJWSktUQWdQdnRTb1V2N3g1b3FXNmUwR3A3UzhkR25VZnhiVE05SFd4dmdZbDIzNnk5bFN0djZIZjduTWVLNEdHYlBpZ3NWVUJ4d0F6TjdnTnczc0llMFR3M2owSmFobTBRUWtiREpQQ2dRTEF5ZFM0R2ErM29BcVlBeXg5SVltREhQSXVlUjRvbU1maG0rRTRta3kwb0FnY21nY0xqbXZxUmozRWpURzIrY1drMHZ3OUFEVCtWaUNobUYvU3U4RzFWSVBWN3NBcVluK0FQOTd5UXBLY2tQWFVZV3UyZXJ6QXdsVUlHTFJydTRRbkQ3dmdaYnRLQ2txb2hhcTNuM2lSRDNSYThEN0ZHd1dwZlEyUVRNd1A1eW5HVUV0cXAvTmtjbEZmbXEvYm5SZTN5dEtUcU5tb2FVS3ZibEFrWkFPcUFpV0JlNjFDTTZjaVBpOEpGYWdMZHR2N0NxNGdrbE1SK3VwWE1uZVdWWmhLWHdnZU5uQ0d0Vm81RkR3b2dtQXdYeDBqQVNJd3FDditaaXY0djdNZmhtOWV1eml4cHJ4bGlwTSt5R0YydGhkZTA5TEEvdVlvb0t6ekNWNW5JbFQ4RGRPTWtQUndmZ3o3cE8wNVRtdkFkOG5sSUV4MEtHdWQyclBwNVJzdlU0SlNjVFNRYlM2cnVqcUJTWE5HU0MxTG92L1p2SmlPclJIS0l3NDhmUHk0WHcxeEx2YlQ2THlUTTA2WU90VWtUelJsbWY1Y0xwc0NISTJGbVNUTjNhOWhJRkVzVmpZY2poNCszSDRxV1g3bi9OakJGcEdOU0JubGZsaXRyUk1DSkIxZEppV3pkMy93cDgvako3cTNSamp5R1YvQlcwL0RGcEVBWlZmdzN5aG5OZnh6M05TTi8rcE1rbFRCMHpTTlJrRFFzemN2aWI5OHFIcmZDeXpKa0VnQ050ZVc3ZklIK0FjbGRBZVlLbHdWUUZXdUhCeHV6ZkFRcTFFZi9yUUpNdnpsOERZN1pXNVFsV0l3OUU3d2RyZUZVRmNHMWlNc2xhVWhMTGwzeDdYUnlVOCtRYUVLQ2pDM2JkNFU0OVZ5Rm41SnBhYnE5NWgzVUhjajN2L0tuNUZ4bXVsdWVSV3RXdnA0Q1NDZFZ6Y0JnckYwTUlMUXVrV0ZTWVJuSEdqaVhvbnYzbXJhQnVvc0l3ZllBUTRuZlIwa3Q1VlpLMitaelpxUFFRblJ3eXhnTVVlOXRrSU9PRG9nbXptcllRRXlFWkw0bFcrNGxKTDF2ZmFrSHVJQ09MQzhjTG9VSXZROGl6enNySmR1L0V4clNzMzZuejlsbW5tY203K1NzOXJuazRHQmtQMlpqdUFCRFNyc2NHWXg1K0h0ZURvLzY1ZER2czBxWlArOUdUREllbWZjNEJzODlmdDd3Qlc4cytxRDVYUHJNcnYrbU8zT2EwdURMS0V2S1RFUVRzNGI4SGxFQjJldXduNWNRbnBvY2s4cjVXaEJRdDJ3TWw3ZDJ1WUxaN2RsdzlJL21kclRscHY2K1hYdzE4ejVBMzFOUlFOWGRnME9jUGE2VkFJUWkwVU9rL0RHdGhqbVp0eDdFbXl5VlhEb0t3NjdZaDVNMFNuaStGcVorV2FvQW1jL2FiVTJqTnM1VzYxdzVBeHJXcUJlWGVBQ2QrL0E9PS5KWjVmQlVCRWV0bGxvb3A5cnFLc01BQWJWY0h4b3hWSzBQNVRHSEZlR1Jta1Y5eVVGVnNxZV9CeVNhWDN6c2RvM3BYeEQwMnZoVGU5NTNUbzVsRTNHZw==",
#     "_eventId": "submit",
#     "geolocation": "",
#     "submit": "LOGIN"
# }
# headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
# def test():
#   with requests.Session() as s:
#       p = s.post('https://sso.unej.ac.id/cas/login?service=https%3A%2F%2Fkawanda.unej.ac.id%2Fapps%2Fuser_cas%2Flogin/',data=payload)
#       print(p.text)
# test()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

class UnejLog:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        #app for automate with chrome
        self.driver = webdriver.Chrome('Chrome Web Driver PATH')

        #close browser
    def closeBrowser(self):
        self.driver.close()

        #login sister dashboard
    def login(self):
        driver = self.driver
        #visit login form and redirect to mmp
        driver.get("https://sso.unej.ac.id/cas/login?service=https%3A%2F%2Fmmp.unej.ac.id%2Flogin%2Findex.php")
        time.sleep(2)
        # login_button = driver.find_element_by_xpath("//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]") #//a[@href='/accounts/login/?source=auth_switcher']
        # login_button.click()
        # time.sleep(2)
        #put the username & password to field
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']") #//input[@name='username']
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")	#//input[@name='password']
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    #present in mmp
    def attendance(self):
    	time.sleep(2)
    	driver = self.driver
    	click_button = lambda: driver.find_element_by_xpath('//a[@data-type="event"]').click()	#//span[@aria-label="Like"] #/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[1]/div[2]/section[1]/span[1]/button/svg/path
    	click_button()
    	time.sleep(5)
    	Present_button = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/a')
    	Present_button.click()

#main program
if __name__ == "__main__":

    #put your account here
    username = "USERNAME"
    password = "PASSWORD"

    sister = UnejLog(username, password)
    sister.login()
    sister.attendance()
#use browser=======================================
# import requests
# from webbot import Browser
# import time
# from selenium import webdriver
# web = Browser()
# time.sleep(3)
# web.go_to('https://sso.unej.ac.id/cas/login?service=https%3A%2F%2Fmmp.unej.ac.id%2Flogin%2Findex.php')
# time.sleep(2)
# web.type('USERNAME',into='username')
# web.type('PASSWORD',into='password')
# web.click('LOGIN',classname='button')

#==================================
# payload = {
#     'sessid': '63205'
#     'sesskey': 'iYUIjrAptO'
#     'sesskey': 'iYUIjrAptO'
#     '_qf__mod_attendance_student_attendance_form': '1'
#     'mform_isexpanded_id_session': '1'
#     'status': '224201'
#     'submitbutton': 'Save+changes'
# }
# headers = {'Host': 'mmp.unej.ac.id'
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
# 'Accept-Language': 'en-US,en;q=0.5'
# 'Accept-Encoding': 'gzip, deflate, br'
# 'Referer': 'https://mmp.unej.ac.id/mod/attendance/attendance.php?sessid=63205&sesskey=iYUIjrAptO'
# 'Content-Type': 'application/x-www-form-urlencoded'
# 'Content-Length': '166'
# 'Origin': 'https://mmp.unej.ac.id'
# 'Connection': 'keep-alive'
# 'Cookie': '_ga=GA1.3.55500459.1584802855; _gid=GA1.3.63662980.1587573148; MoodleSessionsite=ng7j23afbvrbhetra2kan1mbdn'
# 'Upgrade-Insecure-Requests': '1'
# 'TE': 'Trailers'}
# def test():
#   with requests.Session() as s:
#       p = s.post('https://mmp.unej.ac.id/mod/attendance/attendance.php',data=payload)
#       print(p.text)
# test()
