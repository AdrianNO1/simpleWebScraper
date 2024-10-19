from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

def get_html(url, use_selenium=False, debug=False):
    def write_to_file(html, filename="output.html"):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html)

    if not use_selenium:
        try:
            response = requests.get(url)
            response.raise_for_status()
            if debug:
                write_to_file(response.text)
            return (response.text, None)
        except requests.RequestException as e:
            print(f"Error fetching URL with requests: {e}")
            return (None, e)
    else:
        try:
            # Set up Chrome options
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

            driver = webdriver.Chrome(options=options)

            driver.get(url)
            
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            html = driver.page_source

            if debug:
                write_to_file(html)
            
            return (html, None)
        except Exception as e:
            print(f"Error fetching URL with Selenium: {e}")
            return (None, e)
        finally:
            driver.quit()


if __name__ == "__main__":
    debug = True

    html = get_html("https://socialblade.com/youtube/channel/UCVun3IyFIh6AsEMV11zlVHg", use_selenium=True)

    html, error = html["html"], html["error"]

    if debug:
        if html:
            with open("output.html", "w", encoding="utf-8") as file:
                file.write(html)
            print("Success!")
        if error:
            print(f"Error: {error}")