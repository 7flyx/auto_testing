# 用selenuim框架，自动抓取西南大学研招网上的拟录取名单
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\Administrator\AppData\Roaming\Python\Python310\site-packages\selenium\webdriver\chrome\chromedriver.exe')
driver.get("http://ceie.swu.edu.cn/info/1058/4870.htm")
time.sleep(2)
tbody = driver.find_element_by_xpath('//*[@id="vsb_content"]/div/div/table/tbody')
# tbody.find_element_by_css_selector('p > span')
# print(type(tbody))
tr = tbody.find_elements_by_tag_name('tr')

ans = []

# print(type(tr))
for item in tr:
    td = item.find_elements_by_tag_name('td')
    list = []
    for person in td:
        # print(person.find_element_by_css_selector('p > span').text)
        list.append(person.find_element_by_css_selector('p > span').text)
    ans.append(list)

with open('C:\\Users\Administrator\Desktop\\2024年电信院拟录取名单.csv', 'w') as f:
    for list in ans:
        for item in list:
            f.write(str(item) + ' ')
        f.write('\n')
    print('写入成功')

driver.quit()
# driver.close() 二者都是差不多的，但是quit()~会自动清除产生的缓存
