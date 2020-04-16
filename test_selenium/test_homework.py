import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHomework:
    def setup_method(self, method):
        browser = os.getenv("browser", "").lower()
        print(browser)

        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "safari":
            self.driver = webdriver.Safari()
        elif browser == "headless":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1280,1696")
            self.driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.ChromeOptions()
            options.debugger_address = "localhost:9222"  # 复用一个已经打开的浏览器
            self.driver = webdriver.Chrome(options=options)

        self.driver.set_window_size(1680, 972)
        self.driver.implicitly_wait(5)

    # 作业1：进入testerhome，访问社团，访问霍格沃兹测试学院，访问最顶部的第一个帖子。把代码贴到回复里。
    def test_homework_one(self):
        url = "https://testerhome.com"
        self.driver.get(url)
        # self.driver.minimize_window()
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
        self.driver.find_element(By.CSS_SELECTOR, "div.topic:first-of-type div.title a").click()  # 第一个帖子链接

    # 作业2：进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围。把代码贴到回复里。
    def test_homework_two(self):
        url = "https://testerhome.com"
        self.driver.get(url)
        element1 = (By.LINK_TEXT, "MTSC2020 中国互联网测试开发大会议题征集")
        element2 = (By.CSS_SELECTOR, "div.toc-container button")
        element3 = (By.LINK_TEXT, "征集议题范围")
        self.driver.find_element(*element1).click()
        self.driver.find_element(*element2).click()
        self.driver.find_element(*element3).click()

    # 作业3：企业微信自动添加成员，需要复用已经登录的chrome，需要debugger address，代码贴到回复里
    def test_homework_three(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.set_window_size(1680, 972)
        self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        self.driver.find_element(By.ID, "username").send_keys("1")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("2")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".member_edit_sec:nth-child(1) .ww_label:nth-child(2) > .ww_radio").click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13200000000")
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .js_btn_save").click()

    def teardown_method(self, method):
        self.driver.quit()
