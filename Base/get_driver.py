from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import page


class GetDriver:
    driver = None

    # 获取driver
    @classmethod
    def get_dirver(cls):
        if cls.driver is None:
            # 获取driver
            # cls.driver = webdriver.Firefox()  # 火狐
            # chrome_options = Options()
            # chrome_options.add_argument('--headless')
            cls.driver = webdriver.Chrome()  # 谷歌
            # 最大化浏览器
            cls.driver.maximize_window()
            # 设置隐式等待
            # cls.driver.implicitly_wait(30)
            # 打开url
            cls.driver.get(page.URL)
        # 返回driver
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空操作
            cls.driver = None


class GetSecondDriver:
    driver = None

    # 获取driver
    @classmethod
    def get_Custonmer_dirver(cls):
        if cls.driver is None:
            # 获取driver
            # cls.driver = webdriver.Firefox()  # 火狐
            # chrome_options = Options()
            # chrome_options.add_argument('--headless')
            cls.driver = webdriver.Chrome()  # 谷歌
            # 最大化浏览器
            cls.driver.maximize_window()
            # 设置隐式等待
            # cls.driver.implicitly_wait(30)
            # 打开url
            cls.driver.get(page.URL_CUSTOMER)
        # 返回driver
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空操作
            cls.driver = None


if __name__ == '__main__':
    GetDriver().quit_driver()
    GetSecondDriver().quit_driver()
