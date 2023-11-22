from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from selenium.webdriver.chrome.options import Options



def my_function(value):
    
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # 设置浏览器的User-Agent
    chrome_options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.13(0x17000d21) NetType/WIFI Language/zh_CN")

    # 启动谷歌浏览器
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(400, 600)

    # 打开网页
    url = "https://ykt.ihelp.com.cn:9098/?bankcode=34252302"
    driver.get(url)
    try:
        # 等待section.content下的第一个button可见并点击
        time.sleep(1)
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'section.content button'))
        )
        button.click()
        # print("    点击惠农政策成功")

        # 等待ul.zc-list下的第15个li标签可见并点击
        time.sleep(1)
        li_15 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.zc-list li:nth-child(15)'))
        )
        li_15.click()
        # print("    点击宣城成功")

        # 等待第二个class为shaixuan-item的元素可见并点击
        time.sleep(1)
        shaixuan_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.shaixuan-item:nth-child(2)'))
        )
        shaixuan_item.click()
        # print('    点击区县成功')

        # 等待第二个class为van-popup和van-popup--bottom的元素可见
        time.sleep(1)
        van_popup = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.van-popup.van-popup--bottom'))
        )

        # 找到它下面的class为van-radio--horizontal的第三个元素并点击
        time.sleep(1)
        radio3 = van_popup.find_elements(By.CSS_SELECTOR, '.van-radio--horizontal')[2]
        radio3.click()
        # print('    点击广德成功')

        time.sleep(1)

        # 等待zc-list下的第三个li标签加载完成
        third_li = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.zc-list li:nth-child({value})'))
        )
        updated_text = third_li.text.replace('\n', ';').replace(' ', ';')
        # print(f'        {updated_text}')  # 输出重新渲染后的li标签文本，换行和空格替换为分号

        # 等待第三个li元素可见并点击
        time.sleep(1)
        third_li = WebDriverWait(driver, 200).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'.zc-list li:nth-child({value})'))
        )
        third_li.click()

        # print("    点击列表成功")

    finally:
        # 等待一段时间（例如5秒）
        time.sleep(3)
        driver.implicitly_wait(5)
        # 关闭浏览器
        driver.quit()

# 循环1000次
for i in range(0,200):
    # 生成1到3之间的随机等待时间
    wait_time = random.uniform(0.5, 0.6)
    
    # 传入值为1000/42的余数加一
    input_value = i % 2 + 1
    
    # 调用函数
    my_function(input_value)
    print(f"第{i+1}次运行成功时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    # 随机等待时间
    time.sleep(wait_time)

print("-----------运行结束-----------")