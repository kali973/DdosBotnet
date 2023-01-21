import time

from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from tinydb import TinyDB

# Create a new TinyDB database
db = TinyDB('dbScrapingBeguinFr.json')

options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# URL de connexion
login_url = "https://le-beguin.fr/login/"

# Initialize a webdriver
driver = webdriver.Chrome(chrome_options=options)

# Open the login page
driver.get(login_url)

# Find the login form and fill in the username and password
username_field = driver.find_element(By.NAME, "email")
username_field.send_keys("steeve.co@orange.fr")
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Tmax500_t")
submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

# Submit the form
submit_button.click()
target_url_template_rescu = "https://le-beguin.fr/member/790591/profil/show/75374"

# Check if login was successful
if "Welcome" in driver.page_source:
    print("Login success")

    # Open the target page
    target_url_template = "https://le-beguin.fr/member/790591/profil/show/{}"
    for i in range(417892, 838761):
        target_url = target_url_template.format(i)
        driver.get(target_url)
        if "Login success" in driver.page_source:
            # Parse the HTML with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            name = soup.find("li", class_="breadcrumb-item active")
            print(name.text)
            # Find all elements with class "col-md-6"
            col_md_6 = soup.find_all("div", class_="col-md-6")

            for element in col_md_6:
                for li in element.find_all("li"):
                    # Insert the data into the TinyDB
                    db.insert({"content": li.text.encode("utf-8").decode()})

    else:
        print("Login failed")

# Close the browser
driver.quit()
