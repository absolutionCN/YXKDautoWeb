import time

import page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from Base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class Base:

    def __init__(self, driver):
        log.info("[base]: 正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    # 查找元素方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        try:
            log.info("[base]:正在定位{}元素，默认定位超时时间为：{}".format(loc, timeout))
            return WebDriverWait(self.driver,
                                 timeout=timeout,
                                 poll_frequency=poll).until(lambda x: x.find_element(*loc))
        except Exception as e:
            print("没有查到对应的元素 % s" % e)

    # 查找元素方法封装
    def base_finds(self, loc, timeout=30, poll=0.5):
        try:
            log.info("[base]:正在定位{}元素，默认定位超时时间为：{}".format(loc, timeout))
            return WebDriverWait(self.driver,
                                 timeout=timeout,
                                 poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        except Exception as e:
            print("没有查到对应的元素 % s" % e)


    # 点击元素 方法封装
    def base_click(self, loc):
        log.info("[base]:正在对{}元素实行点击事件".format(loc))
        self.base_find(loc).click()

    # 点击元素 方法封装二
    # 使用send_keys(Keys.ENTER)模拟click()事件
    def base_send_keys(self, loc):
        log.info("[base_send_keys]对：{}元素使用send_keys模拟事件点击".format(loc))
        self.base_find(loc).send_keys(Keys.ENTER)

    # 输入元素方法封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        log.info("[base]: 正在对:{}元素实行清空".format(loc))
        el.click()
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本信息方法封装
    def base_get_text(self, loc):
        log.info("[base]: 正在获取：{}元素文本值".format(loc))
        print('获取文本信息封装 % s' % self.base_find(loc).get_attribute('innerHTML'))
        return self.base_find(loc).get_attribute('innerHTML')

    # 截图 方法封装
    def base_get_image(self):
        log.info("[base]:断言出错,调用截图")
        self.driver.get_screenshot_as_file(r"./image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S") + "报错信息"))

    # 正常截图进行封装
    def base_get_info_image(self):
        log.info("[base]:截图查看信息")
        self.driver.get_screenshot_as_file(r"./image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S") + "wlt截图信息"))

    # 判断元素是否存在 方法封装business_batch_management
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=2)
            log.info("[base]:{}元素查找成功，存在页面".format(loc))
            return True  # 返回true 元素存在
        except:
            log.info("[base]:{}元素查找失败, 不存在当前页面".format(loc))
            return False  # 返回false元素不存在

    # 回到首页
    '''
    待定
    '''

    def base_index(self):
        self.driver.get(page.URL)

    # 切换frame表单方法
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 切换窗口方法
    def base_swtich_window(self, title):
        self.driver.switch_to.window(self.base_title_get_handle(title))

    # 根据title获取指定窗口句柄
    def base_title_get_handle(self, title):
        # 遍历 所有窗口句柄
        for handle in self.driver.window_handles:
            # 切换窗口目的：获取当前窗口title
            self.driver.switch_to.window(handle)
            # 判断当前窗口title是否等于要获取的title
            if self.driver.title == title:
                # 条件成立 返回当前窗口句柄
                return handle

    # 选择下拉框select
    def base_select_option(self, loc, value):
        log.info("[base]:{}元素查找，对：{}元素进行选择".format(loc, value))
        self.select = Select(self.base_find(loc))
        self.select.select_by_index(value)

    # 将滚动条滚动到页面底部 针对整个html页面
    def base_sliding_down(self):
        js = "var q=document.documentElement.scrollTop=10000"
        return self.driver.execute_script(js)

    # 将滚动条滚动到页面顶部 针对整个html页面
    def base_sliding_up(self):
        js = "var q=document.documentElement.scrollTop=0"
        return self.driver.execute_script(js)

    # 将滚动条滑动到页面底部 针对的是整个body页面
    def base_sliding_body_down(self):
        js = "var q=document.body.scrollTop=10000"  # documentElement表示获取body节点元素
        return self.driver.execute_script(js)

    # 将滚动条滑动到页面底部 针对整个body页面
    def base_sliding_body_up(self):
        js = "var q=document.body.scrollTop=0"  # documentElement表示获取body节点元素
        return self.driver.execute_script(js)

    # 向后退
    def base_page_back(self):
        self.driver.back()

    # 向前进
    def base_page_forward(self):
        self.driver.forword()

    # 获取当前网页的网址
    def base_get_page_url(self):
        return self.driver.current_url
