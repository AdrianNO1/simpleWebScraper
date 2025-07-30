from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

def get_html(url, use_selenium=False, debug=False, wait_until_fully_loaded=False):
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
            options.add_argument("--enable-unsafe-swiftshader")
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

            driver = webdriver.Chrome(options=options)

            driver.get(url)
            
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            if wait_until_fully_loaded:
                timeout = 30
                WebDriverWait(driver, timeout).until(lambda d: d.execute_script('return document.readyState') == 'complete')

                # wait 5 extra seconds to let extra content load, like web requests
                try:
                    WebDriverWait(driver, 5).until(lambda d: 0)
                except Exception as e:
                    pass
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

    html, error = get_html("https://reise.skyss.no/planner/travel-plans?timetype=DEPARTURE&service-modes=airportbus,bus,carferry,expressbus,others,passengerboat,train,tram&min-transfer=2&walk-speed=normal&from=eyJkZXNjIjoiU29saGVpbXNnYXRlbiAxNSwgQmVyZ2VuIiwiaWQiOiIyNTY5NzU5MjgiLCJsb2Mi%0D%0AOiI2MC4zNzcwNDY4ODYwMTc3Miw1LjMzNTk2NDQzNjc2MzAwNiIsIm1vZGVzIjpudWxsLCJ0eXBl%0D%0AIjoiYWRkcmVzcyJ9&to=eyJkZXNjIjoiTWFyaWtvdmVuIFDDuHlsbywgQXNrw7h5IiwiaWQiOiJOU1I6U3RvcFBsYWNlOjMy%0D%0ANDgzIiwibG9jIjoiNjAuMzk2OTA0LDUuMTc0NDAyIiwibW9kZXMiOlsiQnVzIl0sInR5cGUiOiJz%0D%0AdG9wZ3JvdXAifQ%3D%3D", use_selenium=True)

    if debug:
        if html:
            with open("output.html", "w", encoding="utf-8") as file:
                file.write(html)
            print("Success!")
        if error:
            print(f"Error: {error}")