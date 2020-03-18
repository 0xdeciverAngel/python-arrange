from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://www.youtube.com/watch?v=Y-v-GPkha7s")
#找到輸入框
while(1):
    time.sleep(2)
    element = driver.find_element_by_id('video-title')
    element.click()

print(element)

# #輸入內容
# element.send_keys("hello world");
# #提交表單
# element.submit();
# #driver.close()
# html_source = driver.page_source
# print (html_source)