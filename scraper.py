from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PATH = "C:\Program Files (x86)\chromedeiver.exe"
vid_links = []
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@ESPNFC")

title = driver.title
# find the element

# using an explicit wait


wait = WebDriverWait(driver, timeout = 2000)

# elements = driver.find_elements(by=By.ID, value="thumbnail")
elements = wait.until(EC.presence_of_all_elements_located((By.ID, "thumbnail")))
# element_info = element.get_attribute('href')

driver.execute_script("scrollBy(0, window.innerHeight)")
for element in elements:
    
    driver.execute_script("arguments[0].scrollIntoView()", element)
    href = element.get_attribute('href')
    # print(href)
    vid_links.append(href)



vid_links.pop(0)
vid_links.pop(26)
# vid_links = [link for link in vid_links if link != 'None']
print(vid_links)

driver.quit()
## read from file and append to an array



# f = open("file.txt", "r")
# print(f.read)


with open("file.txt", 'w') as file:
    # Iterate over the list and write each element to a new line in the file
    for link in vid_links:
        file.write(str(link) + '\n')



