import streamlit as st
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Options for Chrome driver
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_experimental_option("detach", True)

@st.cache_resource
def get_driver():                     
    s = r"chrome-win64\chromedriver.exe"
    s = Service(s) 
    return webdriver.Chrome(service=s)

weibo_url = 'https://s.weibo.com/'
driver = get_driver()
                
driver.get(weibo_url)
time.sleep(30)

data = []
st.session_state.keyword="日本核污水"
date ='2023-09-01-0:2023-11-08-23'
for i in range(1, 50):
    try:
        w_url = f"https://s.weibo.com/weibo?q={st.session_state.keyword}&timescope=custom:{date}&Refer=g&sudaref=s.weibo.com&page={i}"
        driver.get(w_url)
        driver.implicitly_wait(10)
        blogs = driver.find_elements(By.XPATH, "//div[@class='main-full']//div[@class='card-wrap']")
        if blogs:
            for blog in blogs:
                publish_time = blog.find_element(By.CSS_SELECTOR, "div.from> a:nth-child(1)").text
                up_name = blog.find_element(By.CSS_SELECTOR, ".name").text
                try:
                    blog_url = blog.find_element(By.CSS_SELECTOR, "div.from> a:nth-child(1)").get_attribute('href')
                except:
                    blog_url = 'NULL'
                data.append({"发布者": up_name, "发布时间": publish_time, "博客url链接": blog_url})
        else:
            st.warning('爬取失败')
    except:
        st.warning('一共爬取了'+str(i-1)+'页,'+'页数' + str(i) + '不存在')
        break
driver.close()

df = pd.DataFrame(data)
