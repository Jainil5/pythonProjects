# Import module
from selenium import webdriver

# Create object
driver = webdriver.Chrome()

# Assign URL
url = "https://www.geeksforgeeks.org/"

# Fetching the Url
driver.get(url)

