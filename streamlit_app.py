from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 设置Chrome选项
options = Options()
options.add_argument('--headless')  # 无头模式
options.add_argument('--disable-gpu')  # 禁用GPU
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 设置WebDriver路径
s = '/usr/bin/chromedriver'
webdriver_service = Service(s)

# 创建WebDriver实例
driver = webdriver.Chrome(service=webdriver_service, options=options)
driver.get('https://s.weibo.com/')
