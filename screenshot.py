import os
from selenium import webdriver

# 创建 Chrome 浏览器驱动
chrome_options = webdriver.ChromeOptions()
# 无头模式，不弹出浏览器窗口
chrome_options.add_argument('--headless')
# 设置浏览器窗口大小，可根据需要调整
chrome_options.add_argument('--window-size=1920x1080')
# 设置 ChromeDriver 路径，请替换为您的 ChromeDriver 路径
# Windows下请自行指定路径  driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

# 定义要截取的网址列表
websites = [
    'https://www.findstars.cn/search',
    # 'https://www.example.com',
    # 'https://www.anotherwebsite.com',
    # 添加更多网址
]

# 遍历网址列表，截取截图并保存到本地
for website in websites:
    driver.get(website)
    title = driver.title  # 获取网页标题
    domain = website.split('//')[1].split('/')[0]  # 提取二级域名
    screenshot_path = os.path.join(domain, f'{title}.png')

    # 创建保存文件的目录（如果不存在）
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

    driver.save_screenshot(screenshot_path)
    print(f'网站标题: {title}, 保存路径: {screenshot_path}')

# 关闭浏览器驱动
driver.quit()
