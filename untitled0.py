from selenium import webdriver

import time


driver = None





def click(address):
    path = driver.find_element_by_xpath(address)
    path.click()



driver = webdriver.Edge('msedgedriver.exe')
driver.get("https://dining.postech.ac.kr/weekly-menu/")
time.sleep(1)


f = open("newFile.txt",'w')

for day in range(0,7):
    for meal in range(1,4):
        click('''//*[@id="day-{}"]'''.format(day))
        xpath = driver.find_element_by_xpath('''//*[@id="data-{}"]/div/div[{}]/div/div/div[2]/div/div'''.format(day,meal))
        menu = xpath.text
        f.write(menu + '\n')
        print(menu)

    



f.close()
driver.close()

