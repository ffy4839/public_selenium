from selenium import webdriver
from selenium.webdriver.common.by import By

import time



url = 'http://192.168.18.27:8081/sgp/login/goLogin.html'

class main():
    def __init__(self, url):
        self.open(url)

    def run(self):
        self.login()

        self.close()

    def open(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)
        # 浏览器最大化
        driver.maximize_window()
        self.driver = driver

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

        time.sleep()
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != login_handle:
                self.driver.switch_to(handle)


    def close(self):
        input('按键退出')
        self.driver.quit()


if __name__ == '__main__':
    m = main(url)
    m.run()

