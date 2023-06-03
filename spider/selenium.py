import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 定义并启动Chrome
driver = webdriver.Chrome()

# 连接调试
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
driver = webdriver.Chrome(options=options)

# 访问网站
driver.get("https://")

# 获取网页源码
html = driver.page_source

# 查找
def find(xpath):
    while True:
        try:
            driver.find_element(By.XPATH, xpath)
        except:
            time.sleep(0.1)
        else:
            break

# 点击
def click(xpath):
    while True:
        try:
            driver.find_element(By.XPATH, xpath).click()
        except:
            time.sleep(0.1)
        else:
            break

# 输入
def write(xpath, content):
    while True:
        try:
            driver.find_element(By.XPATH, xpath).send_keys(content)
        except:
            time.sleep(0.1)
        else:
            break

# 按键
def press(xpath, key):
    # key -> Keys.ESCAPE
    # key -> Keys.ENTER
    while True:
        try:
            driver.find_element(By.XPATH, xpath).send_keys(key)
        except:
            time.sleep(0.1)
        else:
            break
