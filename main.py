import requests
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import datetime
links_list=[]
hello=[]
#current path
absolute_path = os.path.abspath(__file__)
Pathway= os.path.dirname(absolute_path)
File_path = Pathway.replace('\\','\\\\')
s = Service(str(File_path) + '\\chromedriver.exe')

#todays date
def TodayDate():
    Current= datetime.datetime.now()
    CurrentDate= f'{Current.month}/{Current.day}/{Current.year}'
    return CurrentDate

def remove_duplicates(links_list):
    links_list=list(list(dict.fromkeys(links_list)))
    #print(links_list)

    return links_list

def google_search(word,TodayDate=TodayDate()):
    #activate browser
    browser = webdriver.Chrome(service=s)
    #request
    browser.get('https://www.google.com')
    time.sleep(2)
    print('******PROCESSING PAGE********')
    #pick the selector
    search_input= browser.find_element(By.NAME,'q')
    #input
    search= str(word)
    search_input.send_keys(search)
    time.sleep(1)
    print('******PROCESSING PAGE********')
    #ENTER GOOGLE SEARCH -property must be 'input[type="submit"]'
    search_button= browser.find_element(By.CSS_SELECTOR,'input[class="gNO89b"]')
    time.sleep(2)
    search_button.click()
    time.sleep(1)
    #tool option
    Search_tools= browser.find_element(By.CLASS_NAME,'t2vtad')
    time.sleep(0.5)
    Search_tools.click()
    print('******PROCESSING PAGE********')
    time.sleep(0.3)
    #click on timeline
    Search_Time = browser.find_element(By.CLASS_NAME,'gTl8xb')
    Search_Time.click()
    print('******PROCESSING PAGE********')
    time.sleep(0.2)
    #click on custom range
    Search_customrange=browser.find_element(By.CSS_SELECTOR,'span[role="menuitem"]')
    print('******PROCESSING PAGE********')
    time.sleep(0.5)
    Search_customrange.click()
    #time from time to
    Search_fromRange=browser.find_element(By.CSS_SELECTOR,'input[id="OouJcb"]')
    #time from
    Search_fromRange.send_keys('04/09/2019')
    #time to Search

    Search_toRange=browser.find_element(By.CSS_SELECTOR,'input[id="rzG2be"]')
    Search_toRange.send_keys(TodayDate)
    print('******PROCESSING PAGE********')
    time.sleep(0.5)
    #click go button in custom range
    Search_goRange=browser.find_element(By.CSS_SELECTOR,'g-button')
    Search_goRange.click()
    print('******PROCESSING PAGE********')
    time.sleep(0.5)
    #starting link siphon FROM SEARCH RESULTS
    #links_list=[]
    #GET ALL HREF LINKS IN 'A' ANCHORS
    def linkSiphon():
        # GRAB THE WHOLE SEARCH SECTION
        results = browser.find_elements(By.CSS_SELECTOR, 'div[id="search"]')
        # GRAB ALL 'A' ANCHORS
        link = results[0].find_elements(By.TAG_NAME, 'a')
        print('******PROCESSING PAGE********')
        for item in link:
            href = item.get_attribute('href')
            if 'search?q' in href:
                pass
            elif 'watch?v' in href:
                pass
            elif 'google.com/search?' in href:
                pass
            elif 'google.com/websearch/answer' in href:
                pass
            else:
                links_list.append(href)
                remove_duplicates(links_list)
        return links_list
    linkSiphon()
    time.sleep(2)
    #repeat process but keep going next page
    while True:
        try:
            next = browser.find_element(By.ID,'pnnext')
            next.click()
            time.sleep(8)
            #link siphon again on new page
            linkSiphon()
        except:
            print("No more pages left")
            break

google_search('sdsdsdsdsds')
print(links_list)
