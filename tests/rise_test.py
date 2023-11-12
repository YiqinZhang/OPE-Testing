from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager, ChromeType
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

def find_element_and_click(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.click()
        return element
    except NoSuchElementException as e:
        print(f"Error finding or clicking element: {e}")
        return None


def take_screenshot(driver, filename):
    try:
        driver.save_screenshot(filename)
        print(f"Saved screenshot: {filename}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def test_rise_extension(token):
    driver = setup_driver()
    url = f"http://127.0.0.1:8888/lab?token={token}"

    try:
        driver.get(url)
        driver.implicitly_wait(45)
        # Main actions and interactions
        take_screenshot(driver, 'main_screenshot.png')
        find_element_and_click(driver, '//div[@data-category="Notebook"]')
        take_screenshot(driver, 'new_nb_screenshot.png')

        find_element_and_click(driver, '//button[@data-command="RISE:preview"]')
        take_screenshot(driver, 'rise_screenshot.png')

        toolbar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='lm-Widget jp-Toolbar' and @role='navigation']")))
        if toolbar:
            fullscreen_button = toolbar.find_element(By.XPATH, ".//button[@title='Open the slideshow in full screen']")
            fullscreen_button.click()
            is_fullscreen = driver.execute_script("return document.fullscreenElement !== null")
            print("Fullscreen button is functioning: ", is_fullscreen)
        else:
            print("Toolbar not found")

        print("RISE Extension is working!")
    except Exception as e:
        print(f"An error occurred during test: {e}")
    finally:
        # Clean up
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python script.py <token>")
    else:
        test_rise_extension(sys.argv[1])