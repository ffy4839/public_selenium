from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import json
import os



url = 'http://192.168.18.27:8081/sgp/login/goLogin.html'

def json_write(data):
    with open('cookies.json', 'w') as f:
        json.dump(data, f)

def json_read(filename='cookies.json'):
    filePath = os.getcwd() + os.path.sep + filename
    if not os.path.exists(filePath):
        return None
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)

def data_save(data,fileName):
    filePath = '{}.txt'.format(fileName)
    with open(filePath,'w') as f:
        f.write(data)


class main():
    def __init__(self, url):
        self.open(url)

    def run(self):
        if not self.cookiesLogin():
            self.login()

        self.quir_driver()

    def open(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)
        # 浏览器最大化
        driver.maximize_window()
        self.driver = driver


    def cookiesLogin(self):
        url = 'http://192.168.18.27:8081/sgp/login/goMain.html'
        cookies = json_read('cookies.json')
        if cookies:
            self.driver.delete_all_cookies()
            for i in cookies: self.driver.add_cookie(i)
            self.driver.get(url)
            return True

    def login(self):
        login_handle = self.driver.current_window_handle
        usernamee = self.driver.find_element(By.XPATH,
                    '//*[@id="box"]/div[3]/ul/li[1]/span/input[1]')
        passworde = self.driver.find_element(By.XPATH,
                    '//*[@id="box"]/div[3]/ul/li[2]/span/input[1]')
        submite = self.driver.find_element(By.XPATH,
                    '//*[@id="submit"]')


        usernamee.clear()
        passworde.clear()
        # submite.clear()

        usernamee.send_keys('999')
        passworde.send_keys('99999')
        submite.click()

        time.sleep(5)
        all_windows = self.driver.window_handles
        print(all_windows)
        for handle in all_windows:
            if handle != login_handle:
                self.driver.switch_to.window(handle)

        data_save(self.driver.current_url,'mainUrl')
        print(self.driver.title)
        cookies = self.driver.get_cookies()
        print(cookies)
        json_write(cookies)
        print(self.driver.current_url)


    def quir_driver(self):
        input('按键退出')
        self.driver.quit()


if __name__ == '__main__':
    m = main(url)
    m.run()

