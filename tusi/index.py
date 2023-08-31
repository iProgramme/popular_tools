from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开网页
driver.get("https://tusi.art")
# 打开新的标签页
# driver.execute_script("window.open('https://www.baidu.com', '_blank');")

# 切换到新打开的标签页
# driver.switch_to.window(driver.window_handles[-1])

# 打开第二个网页
# driver.get("https://www.baidu.com")

try:
    # 显式等待页面加载完成
    wait = WebDriverWait(driver, 30)  # 最多等待10秒
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "vi-button__wrap")))
    print("页面加载完成")

    # 点击第二个 class 为 vi-button__wrap 的按钮
    second_button = driver.find_elements(By.CLASS_NAME, "vi-button__wrap")[1]
    second_button.click()
    print("点击第二个按钮")

    time.sleep(10)
    # 查找输入框并输入内容
    input_wrap = driver.find_elements(By.CLASS_NAME, "vi-input__input-wrap")[1]
    input_box = input_wrap.find_elements(By.TAG_NAME, "input")[0]
    input_box.send_keys("手机号todo")
    print("输入内容")

    # 点击 class 为 w-118 的按钮
    w_118_button = driver.find_elements(By.CLASS_NAME, "w-118")[0]
    w_118_button.click()
    print("点击 w-118 按钮")

    # 等待用户输入
    input_wrap_2 = driver.find_elements(By.CLASS_NAME, "vi-input__input-wrap")[2]
    input_box_2 = input_wrap_2.find_elements(By.TAG_NAME, "input")[0]
    while len(input_box_2.get_attribute("value")) < 6:
        time.sleep(1)
    print("等待用户输入完毕")

    # 点击第七个 class 为 vi-button__wrap 的按钮
    seventh_button = driver.find_elements(By.CLASS_NAME, "mt-24")[1]
    seventh_button.click()
    print("点击第七个按钮")

    time.sleep(10)

    # 点击在线生图
    seventh_button = driver.find_elements(By.CLASS_NAME, "vi-button__wrap")[0]
    seventh_button.click()

    # 等待 10 分钟
    time.sleep(600)
    print("等待 10 分钟")

except Exception as e:
    print("发生异常:", e)

finally:
    # 关闭浏览器
    driver.quit()
