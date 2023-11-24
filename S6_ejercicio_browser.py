
# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define the browser and login details
browser = 'browser'
login = 'login'

# Open the browser
driver = webdriver.Chrome(executable_path=r'path_to_chromedriver')

# Navigate to the login page
driver.get('https://www.example.com/login')

# Locate the login input field
login_input = driver.find_element_by_name('login')

# Enter the login details
login_input.send_keys(login)

# Locate the password input field
password_input = driver.find_element_by_name('password')

# Enter the password details
password_input.send_keys('password')

# Locate the login button
login_button = driver.find_element_by_name('submit')

# Click the login button