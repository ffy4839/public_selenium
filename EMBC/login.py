from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytesseract
from PIL import Image,ImageEnhance
import os


url = 'https://wxys.vs-gascloud.com/ygp/login/goLogin.do'
class main():
    def __init__(self,url):
        self.url = url
        self.login = EMBClogin()
        #打开浏览器
        self.open()

    def run(self):
        print(self.driver.title)
        #获取登录界面句柄
        login_handle = self.driver.current_window_handle
        #登录
        self.login.login(self.driver)
        #切换登录后界面
        self.switch2main_window(login_handle)
        print(self.driver.title)

        self.quit()

    def switch2main_window(self,login_handle):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != login_handle:
                self.driver.switch_to(handle)

    def open(self):
        # 打开浏览器
        driver = webdriver.Chrome(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
        driver.get(self.url)
        driver.implicitly_wait(10)
        # 浏览器最大化
        driver.maximize_window()
        self.driver = driver

    def quit(self):
        input('按键退出')
        self.driver.quit()


class EMBClogin():
    def __init__(self):
        self.img_path = (os.getcwd() + os.path.sep + '{}.png')

    def login(self, driver):
        self.get_driver(driver)
        #获取元素
        username_element = self.driver.find_element(By.XPATH,'//*[@id="workCode"]')
        password_element = self.driver.find_element(By.XPATH,'//*[@id="password"]')
        imgcode_element = self.driver.find_element(By.XPATH,'//*[@id="autherCode"]')
        img_element = self.driver.find_element(By.XPATH, '//*[@id="authImage"]')
        submit_element = self.driver.find_element(By.XPATH,'//*[@id="submit"]')

        #登录
        username_element.clear()
        password_element.clear()
        imgcode_element.clear()
        username_element.send_keys('cpglb')
        password_element.send_keys('12345678')

        self.submit_login(img_element, imgcode_element, submit_element)

        return self.driver

    def get_driver(self, driver):
        self.driver = driver

    def submit_login(self, img_element, imgcode_element, submit_element,times = 1):

        # login_handle = self.driver.current_window_handle
        for i in range(times):
            code = self.get_code(img_element)
            imgcode_element.send_keys(code)
            submit_element.click()
            #
            # try:
            #     WebDriverWait(self.driver, 20).until(
            #         EC.presence_of_element_located(
            #             ((By.XPATH,'/html/body/div[5]/div[3]/div/button'))
            #         )
            #     )
            #     self.driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/button').submit()
            # except Exception as e:
            #     print(e)
            #     break

            if i == (times-1):
                self.driver.quit()
                assert '验证码获取解析错误'


    def switch_window_choose(self, num):
        all_windows = self.driver.window_handles
        self.driver.switch_to(all_windows[num-1])

    def switch_window_new(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to(all_windows[-1])

    def switch_window_init(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to(all_windows[0])

    def get_code(self, img_element,times = 50):
        # 获取验证码
        for i in range(times):
            code = self.img_code()
            if len(code) == 4:
                print(i, code)
                return code
            img_element.click()
            if i == times-1:
                self.driver.quit()
                assert '验证码获取位数错误'


    def img_code(self):
        #截屏
        self.driver.save_screenshot(self.img_path.format('imgs_00'))
        img = Image.open(self.img_path.format('imgs_00'))
        #选取验证码
        img.crop((637,324,766,363)).save(self.img_path.format('imgs_01'))

        imgcode = Image.open(self.img_path.format('imgs_01'))

        sharp_img = ImageEnhance.Contrast(imgcode).enhance(2.0)
        sharp_img.load()

        time.sleep(1)
        sharp_img.save(self.img_path.format('imgs_02'))
        #解析
        code = ''
        for i in range(3):
            code = pytesseract.image_to_string(sharp_img)
            code.replace(' ','')
            if code:
                break

        return code




if __name__ == '__main__':
    main = main(url)
    main.run()


