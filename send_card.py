import names
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
#import time

ser = Service(r"webdrivers/chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('headless') # run the browser in the background
driver = webdriver.Chrome(service=ser, options=op)

website = "https://give.cincinnatichildrens.org/site/SPageNavigator/ValentinesDay.html"

# get the ID's of each form element
first_name_input = '2199_1_4266'
last_name_input = '2199_2_4267'
email_input = '2199_3_4268'
email_confirm_input = '2199_4_4269'
state_input = '2199_5_4270'
marketing_choice_input = '2199_7_4272_2'
card_to_send_input = '2199_8_4273'
submit_input = 'ACTION_SUBMIT_SURVEY_RESPONSE'

# list of state names and select a random choice
state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
state = random.choice(state_names)

# select random first and last names
first_name = names.get_first_name()
last_name = names.get_last_name()

# create a pseudo email for the form
faux_email = first_name + '.' + last_name + '@gmail.com'

# select from one of the card choices available
card_choices = [
    "You make the world more colorful", 
    "You're Magic!", 
    "You amaze me!", 
    "Love you with all of my art!",
    "You are my sunshine, Valentine!",
    "You OTTER know, I think you're very spe-SHELL!"
]
card_choice = random.choice(card_choices)

# visit website
driver.get(website)

# fill out the form
driver.find_element(By.ID, first_name_input).send_keys(first_name)
driver.find_element(By.ID, last_name_input).send_keys(last_name)
driver.find_element(By.ID, email_input).send_keys(faux_email)
driver.find_element(By.ID, email_confirm_input).send_keys(faux_email)
driver.find_element(By.ID, state_input).send_keys(state)
driver.find_element(By.ID, marketing_choice_input).click()
driver.find_element(By.ID, card_to_send_input).send_keys(card_choice)

#wait a few seconds to mimic user interaction
#time.sleep()

# use click action, submit does not work
driver.find_element(By.ID, submit_input).click()

# if the page is redirected to the donate page, it worked
redirect_url = driver.current_url

if "https://give.cincinnatichildrens.org/site/Donation2" in redirect_url:
    print("Valentine Sent!")
