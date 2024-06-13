import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to check if HTTP server is running and wait if not
def wait_for_httpd(url, timeout=60):
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("HTTP server is up.")
                break
        except requests.ConnectionError:
            print("HTTP server is not yet up. Retrying.")

        if time.time() - start_time > timeout:
            raise Exception("Timed out waiting for HTTP server to start.")
        time.sleep(5)  # Wait 5 seconds and retry

# Read the public IP address from /tmp/ip_address.txt
with open('/tmp/ip_address.txt', 'r') as file:
    public_ip = file.read().strip()

# Construct the URL for Redmine
target_url = f"http://{public_ip}:9100"

# Check if HTTP server is running
wait_for_httpd(target_url)

# Set up headless Firefox options
options = Options()
options.headless = True

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Now that we've confirmed the server is up, we can proceed to access the page
driver.get(target_url)

# Wait for a specific element to be loaded
wait = WebDriverWait(driver, 60)

# Get the width and height of the page's body
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# Set the window size to the page's body size
driver.set_window_rect(width=w, height=h)

# Save a screenshot of the page
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./screenshot.png")
driver.save_screenshot(filename)

# Quit the driver
driver.quit()
