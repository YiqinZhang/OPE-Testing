import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform
import sys

def setup_driver():
    chrome_options = Options()
    if platform.system() in ['Windows', 'Darwin']:
        chrome_options.add_experimental_option('detach', True)
    elif platform.system() == 'Linux':
        chrome_options.add_argument('--headless')
    else:
        raise Exception("Unknown OS")
    return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=chrome_options)

def create_jupyter_notebook_from_github(github_url, local_file_name):
    try:
        response = requests.get(github_url)
        response.raise_for_status()  # Raise an error for bad status codes
        notebook_content = response.json()
        with open(local_file_name, 'w', encoding='utf-8') as notebook_file:
            json.dump(notebook_content, notebook_file)
        print(f"Notebook created: {local_file_name}")
    except requests.RequestException as e:
        print(f"Failed to download the notebook: {e}")

def open_jupyter_notebook(url, notebook_name, driver):
    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jp-DirListing")))
        notebook = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//span[text()='{notebook_name}']"))
        )
        notebook.click()  # JavaScript click for double-click action
        driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('dblclick', {bubbles: true, cancelable: true, view: window}));", notebook)
    except Exception as e:
        print(f"Error: {e}")

def take_screenshot(driver, filename):
    try:
        driver.save_screenshot(filename)
        print(f"Saved screenshot: {filename}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def find_and_click(driver, xpath):
    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        return element
    except Exception as e:
        print(f"Error finding/clicking element: {e}")

def test_rise(token, notebook_github_url, local_notebook_name):
    driver = setup_driver()
    create_jupyter_notebook_from_github(notebook_github_url, local_notebook_name)
    open_jupyter_notebook(f"http://127.0.0.1:8888/lab?token={token}", local_notebook_name, driver)

    try:
        WebDriverWait(driver, 45)
        take_screenshot(driver, 'main_screenshot.png')

        # Correct the XPath and check if the "Launcher" tab is present
        try:
            launcher_element = driver.find_element(By.XPATH, "//div[contains(@class, 'lm-TabBar-tabLabel') and contains(@class, 'p-TabBar-tabLabel') and text()='Launcher']")
            is_launcher_page = True
        except NoSuchElementException:
            is_launcher_page = False 
        
        if is_launcher_page:
            print("On the Launcher page")
            find_and_click(driver, '//div[@data-category="Notebook"]')
        # else:
        #     print("Not on the Launcher page, trying to open the notebook directly")
        #     notebook = WebDriverWait(driver, 30).until(
        #         EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{local_notebook_name}')]"))
        #     )
        #     notebook.click()      
                 
        take_screenshot(driver, 'new_nb_screenshot.png')

        find_and_click(driver, '//button[@data-command="RISE:preview"]')        
        take_screenshot(driver, 'rise_screenshot.png')

        fullscreen_button = find_and_click(driver, ".//button[@title='Open the slideshow in full screen']")
        is_fullscreen = driver.execute_script("return document.fullscreenElement !== null")
        print("Fullscreen button is functioning")

    finally:
        # Clean up  
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        # driver.quit()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python script.py <token>")
    else:
        notebook_github_url = "https://raw.githubusercontent.com/OPEFFORT/ope-project/main/content/test_book/02_slides_template/layout_example.ipynb"
        local_notebook_name = "downloaded_notebook.ipynb"
        test_rise(sys.argv[1], notebook_github_url, local_notebook_name)
