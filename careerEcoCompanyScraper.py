from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains as AC

fname = "career.csv"
f = open(fname, "w", encoding="utf-8")
f.write("Company Name,Company Info")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = "https://www.careereco.com/Fair/FairOrganizations?fairId=c4d16387-80ba-4751-8471-abf00141644b"

driver.get(url)
degree_search = driver.find_element_by_id("employerTable")
fullXPath = "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/table/tbody"
list = driver.find_element_by_xpath(fullXPath)

def formattedQuery(q):
    y = " ".join([s.strip() for s in q.splitlines()])
    return y[80:]

def getStuff(x):

    goodCompanies = []
    time.sleep(1)
    for i in range(x):
        #companyList = []
        good = False

        for j in range(4):
            nextPath = "//tr[" + str(i+1) + "]/td[" + str(j+1) + "]"
            companyInfo = list.find_element_by_xpath(nextPath)

            if j == 1 and "Mechanical" in companyInfo.text:
                good = True

            if good and j == 3 and "Intern" in companyInfo.text:
                    goodCompanies.append(i)
                    #print(companyInfo.text)

    for i in goodCompanies:
        nextPath = "//tr[" + str(i+1) + "]/td[1]"
        companyInfo = list.find_element_by_xpath(nextPath)
        nameInfo = companyInfo.text
        companyInfo.find_element_by_css_selector("a[href*='javascript']").click()

        #time.sleep(3)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        newInfo = driver.find_element_by_id("tabs-1")
        newInfo = formattedQuery(newInfo.text)
        f.write("\n" + nameInfo + "," + newInfo)
        nameInfo = nameInfo + "  \n " + newInfo
        print(nameInfo)
        print("\n\n")

        driver.switch_to.default_content()
        driver.find_element_by_link_text("Close").click()
getStuff(49)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/a[@title='Go to the next page']").click()

getStuff(49)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/a[@title='Go to the next page']").click()

getStuff(27)

print(driver.title)

#degree_search.send_keys("bachelor")

time.sleep(10)
driver.quit()