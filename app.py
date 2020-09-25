from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
log = input("login :")
pas = input("password :")
message = input("message :")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys(log)
driver.find_element_by_id("pass").send_keys(pas)
driver.find_element_by_id("u_0_d").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "mount_0_0")))
driver.get("https://www.facebook.com/me/friends")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "sjgh65i0")))
lista_objektow = driver.find_elements_by_class_name("agehan2d")
lista_id = []
for item in range(len(lista_objektow)):
    if lista_objektow[item].get_attribute("href") != None and lista_objektow[item].get_attribute("href") != "https://www.facebook.com/":
        if "id" in lista_objektow[item].get_attribute("href"):
            lista_id.append(lista_objektow[item].get_attribute("href").split("=")[1])
        else:
            lista_id.append(lista_objektow[item].get_attribute("href").split("/")[3])
lista_id.pop(0)
for item in lista_id:
    print(str(lista_id.index(item)+1)+"/"+str(len(lista_id))+"messages sent")
    driver.get("https://m.facebook.com/" + item)
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "page")))
    driver.find_elements_by_css_selector("a[role='button']")[3].click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "composerInput")))
    driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_id("composerInput").send_keys(message)
    driver.find_element_by_name("send").click()


