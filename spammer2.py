from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
log = input("login :")
pas = input("password :")
message = input("message :")
PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=PATH,options=chrome_options)
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys(log)
driver.find_element_by_id("pass").send_keys(pas)
driver.find_element_by_css_selector("button[data-cookiebanner='accept_button']").click()
driver.find_element_by_css_selector("button[type='submit']").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "mount_0_0")))
driver.get("https://www.facebook.com/me/friends")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "sjgh65i0")))
for i in range(500):
    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
src = driver.page_source
soup = BeautifulSoup(src,"html.parser")
lista_id=[]
for i in soup.findAll("a",attrs={"aria-hidden":"true","role":"link","tabindex":"-1"}):
	if "php?id" in i["href"]:
		lista_id.append(i["href"].split("=")[1])
	else:
		lista_id.append(i["href"].split("/")[3])

for item in lista_id:
    driver.get("https://m.facebook.com/" + item)
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "page")))
    driver.find_elements_by_css_selector("a[role='button']")[3].click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR , "textarea[placeholder='Napisz wiadomość...']")))
    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_css_selector("textarea[placeholder='Napisz wiadomość...']").send_keys(message)
    driver.find_element_by_css_selector("button[value='Wyślij']").click()
    print(str(lista_id.index(item)+1)+"/"+str(len(lista_id))+"wysłanych wiadomości")
    time.sleep(2)
