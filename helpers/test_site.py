"""
This script runs a selenium bot with test_site() to test our website.
The method has 2 parameters: maxUsers (max # users) and lag (page load time).
Running test_site(200,2) will run 200 test users with a 2s lag between pages.
"""

#load dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

def test_site(maxUsers=200,lag=2):
    """
    The method has 2 parameters: maxUsers (max # users) and lag (page load time).
    Running test_site(200,2) will run 200 test users with a 2s lag between pages.
    """
    url = "http://www.newtest-env.ut3hmfea6v.us-east-2.elasticbeanstalk.com/"
    parties = ["Republicans", "Democrats"]
    opinions = ["support", "oppose"]

    user = 1
    while user <= maxUsers:
        try:
            #Create new Chrome session
            driver = webdriver.Chrome("/usr/local/bin/chromedriver") #Mac location
            driver.implicitly_wait(10) #if load fails in 10s, give error
            driver.get(url)
            time.sleep(lag) #load login page for <lag> seconds

            #select user's political party
            party = random.choice(parties) #choose Dem or Rep
            selectParty = driver.find_element_by_xpath("//select[@name='political_stand']/option[text()='{}']".format(party)).click()

            #enter TurkID and login
            inputID = driver.find_element_by_name("mTurk_code")
            inputID.send_keys('test' + str(user))
            inputID.send_keys(Keys.ENTER)

            #select consent
            time.sleep(lag) #load consent page for <lag> seconds
            selectConsent = driver.find_element_by_id('myCheck').click()
            submitConsent = driver.find_element_by_id('myButton').click()

            #select instructions
            time.sleep(lag) #load consent page for <lag> seconds
            selectInstruct = driver.find_element_by_id('myCheck').click()
            submitInstruct = driver.find_element_by_id('myButton').click()

            #evaluate policies
            policy = 1
            while policy <= 20:
                time.sleep(lag) #load policy page for <lag> seconds
                opinion = random.choice(opinions) #choose support or oppose
                submitOpinion = driver.find_element_by_name(opinion).click()
                policy += 1

            #end Selenium Chrome session
            driver.quit()
        except:
            driver.quit()

        #update user index and repeat loop through max users
        user += 1
