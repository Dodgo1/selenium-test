import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

def check_tab_column(tab_number:int,column_number:int):
    """
    :args
    tab_number:int - number of a tab, clickable from 1-8
    column_number:int - number of a column if such exists (tab 1 = 0-6)

    :return list of bools if clicked link has <html>
    """
    os.environ['WDM_LOCAL'] = '1'
    os.environ['WDM_LOG_LEVEL'] = '0'
    TITLE_STR = 'https://pwsz.edu.pl/'
    # options = Options()
    # options.add_argument()
    # start DRIVER
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(TITLE_STR)
    driver.maximize_window()
    with driver:
        nav_tabs_li_elements = driver.find_element(By.XPATH,'//*[@id="navbar"]/div[2]/div/ul').find_elements(By.XPATH,'*') # 9 - tabs
        # open tab so content could be read
        nav_tabs_li_elements[tab_number].click()
        row = nav_tabs_li_elements[tab_number].find_element(By.CLASS_NAME,"row")
        columns_list = row.find_elements(By.CLASS_NAME,"col")
        li_elements_list = columns_list[column_number].find_elements(By.TAG_NAME,"li")
        # hide tab for compatibility
        nav_tabs_li_elements[tab_number].click()
        content_dict = {}
        for i,elem in enumerate(li_elements_list):
            try:
                nav_tabs_li_elements = driver.find_element(By.XPATH,'//*[@id="navbar"]/div[2]/div/ul').find_elements(By.XPATH,'*') # 9 - tabs
                # open tab so content could be read, it has to be updated, otherwise StaleElementReferenceException
                # Previous list is used just for number of tabs, new one each iteration for right webelements
                nav_tabs_li_elements[tab_number].click()
                row = nav_tabs_li_elements[tab_number].find_element(By.CLASS_NAME,"row")
                columns_list = row.find_elements(By.CLASS_NAME,"col")
                li_elements_list = columns_list[column_number].find_elements(By.TAG_NAME,"li")
                # click new element each iteration
                li_elements_list[i].click()
                html = driver.find_element(By.TAG_NAME,"html")
                content_dict[i] = bool(html.text)
            except StaleElementReferenceException:
                # if link transfers to different page go back to pages in browser history and repeat
                driver.back()
                driver.back()
                nav_tabs_li_elements = driver.find_element(By.XPATH,'//*[@id="navbar"]/div[2]/div/ul').find_elements(By.XPATH,'*') # 9 - tabs
                nav_tabs_li_elements[tab_number].click()
                row = nav_tabs_li_elements[tab_number].find_element(By.CLASS_NAME,"row")
                columns_list = row.find_elements(By.CLASS_NAME,"col")
                li_elements_list = columns_list[column_number].find_elements(By.TAG_NAME,"li")
                li_elements_list[i].click()
                html = driver.find_element(By.TAG_NAME,"html")
                content_dict[i] = bool(html.text)
        return content_dict

def test_tab_1_0():
    content_dict = check_tab_column(1,0)
    for i,value in content_dict.items():
        assert value

def test_tab_1_1():
    content_dict = check_tab_column(1,1)
    for i,value in content_dict.items():
        assert value
    
def test_tab_1_2():
    content_dict = check_tab_column(1,2)
    for i,value in content_dict.items():
        assert value

def test_tab_1_3():
    content_dict = check_tab_column(1,3)
    for i,value in content_dict.items():
        assert value

        
