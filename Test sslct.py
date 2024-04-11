from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser
browser = webdriver.Chrome()  # You need to have Chrome webdriver installed and accessible in PATH

# Open a website
browser.get("https://example.com")

# Find an element by its ID and interact with it
element = browser.find_element_by_id("some_id")
element.click()  # Click on the element
element.send_keys("Some text to input")  # Input text into the element

# Find an element by its class name and interact with it
element = browser.find_element_by_class_name("some_class")
element.click()

# Find an element by its XPath and interact with it
element = browser.find_element_by_xpath("//input[@name='username']")
element.send_keys("username")

# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()


# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()

# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()


# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()


# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()


# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()
# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()


# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()


# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()


# Find an element by its CSS selector and interact with it
element = browser.find_element_by_css_selector("input[type='password']")
element.send_keys("password")

# Wait for an element to be clickable
try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "some_id"))
    )
    element.click()
except:
    print("Element not found or clickable within 10 seconds")

# Close the browser
browser.quit()
