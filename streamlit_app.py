import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def run_selenium():
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 使用无头模式
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 设置webdriver服务
    webdriver_service = Service(ChromeDriverManager().install())

    # 创建一个Selenium driver实例
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # 访问一个网页
    driver.get("https://www.example.com")

    # 找到一个元素并获取其文本
    element = driver.find_element(By.TAG_NAME, "h1")
    element_text = element.text

    # 关闭driver
    driver.quit()

    return element_text

# 在Streamlit应用中运行Selenium并显示结果
st.write(run_selenium())
