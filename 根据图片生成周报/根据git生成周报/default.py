
from flask import Flask, jsonify, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

app = Flask(__name__, static_folder='/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    request_type = request.args.get('request')
    if request_type == 'cas':
        chrome_options = Options()
        # Perform web automation with Selenium
        driver = webdriver.Chrome()  # You need to have ChromeDriver installed
        driver.get("http://172.16.0.191:6010/pqc/cas-web/commits/branch/ybw")

        try:
            # Wait until the username field is present
            username_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user_name"))
            )
            
            # Fill in username and password
            username_element.send_keys("yubowen")
            password_element = driver.find_element(By.ID, "password")
            password_element.send_keys("5266632311ybw")

            # Click the login button
            login_button = driver.find_element(By.CLASS_NAME, "green")
            login_button.click()

            # Wait for the page to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "tbody"))
            )

            # Extract and process data from the table
            table_rows = driver.find_elements(By.XPATH, "//tbody/tr")
            result_data = []

            for row in table_rows:
                columns = row.find_elements(By.TAG_NAME, "td")
                if (
                    columns[0].text == "喻博文"
                    and "Merge" not in columns[2].text
                    and "天" in columns[3].text
                ):
                    result_data.append(columns[2].text)

        finally:
            driver.quit()

        return jsonify(result_data)

    return jsonify({"error": "Invalid request type"})

if __name__ == '__main__':
    app.run(debug=True)
