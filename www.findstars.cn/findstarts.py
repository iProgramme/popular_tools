import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import requests

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开页面
url = 'https://www.findstars.cn/search'
driver.get(url)

# 模拟滚动加载五次
scroll_pause_time = 1  # 滚动加载的间隔时间
scroll_count = 0

while scroll_count < 5:
    scroll_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script(f'window.scrollTo(0, {scroll_height});')
    time.sleep(scroll_pause_time)
    new_scroll_height = driver.execute_script('return document.body.scrollHeight')

    if new_scroll_height == scroll_height:
        scroll_count += 1

    scroll_height = new_scroll_height

# 获取包含数据的页面内容
page_source = driver.page_source

# 使用 BeautifulSoup 解析页面内容
soup = BeautifulSoup(page_source, 'html.parser')

# 找到前 100 个 href 以 "/detail/" 开头的 a 标签
a_tags = soup.select('a[href^="/detail/"]')[:100]

# 创建一个列表来存储匹配的数据
data = []

# 遍历 a 标签，获取相应的页面并解析
for a_tag in a_tags:
    href = a_tag['href']
    detail_url = f'https://www.findstars.cn{href}'

    # 发送 HTTP GET 请求获取详细页面内容
    detail_response = requests.get(detail_url)
    detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

    # 查找 class 为 'w-[calc(100%-50px)]' 和 class 为 'text-#999999' 的数据
    w_data = detail_soup.find(class_='w-[calc(100%-50px)]')
    text_data = detail_soup.find_all(class_='text-#999999')

    if w_data:
        w_text = w_data.get_text(strip=True)
    else:
        w_text = ''

    if text_data and len(text_data) > 3:
        size = text_data[1].get_text(strip=True)
        number = text_data[2].get_text(strip=True)
        time = text_data[3].get_text(strip=True)
        MC = text_data[4].get_text(strip=True)
    else:
        size = ''
    
    data.append({'名称': w_text, '大小': size, '人数': number, '预估时间': time, 'MC评分': MC})

    # 打印每条数据
    print(f'名称:{w_text},大小:{size},人数:{number},预估时间:{time},MC评分:{MC}')

    
# 生成 DataFrame
df = pd.DataFrame(data)


# 保存为 Excel 文件
excel_file = 'data.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

# 关闭浏览器
driver.quit()

print('数据已保存到 data.xlsx 文件。')
