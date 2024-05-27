import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#크롬 드라이버 생성
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#웹사이트 접속
driver.get("https://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=https://www.g2b.go.kr:8340/search.do?category=TGONG&kwd=ISO27001")

#요소 찾기
sleep(5)

iframe_element = driver.find_element(By.ID, "sub")
print(iframe_element)
popup = driver.find_element(By.XPATH, '/html')#.is_displayed()

#iframe_element = driver.find_element(By.ID, "bodyFrame")
print(popup)
#driver.switch_to.frame("sub")
#driver.switch_to.frame("bodyFrame")
#popup = driver.find_element(By.XPATH, '//*[@id="epDialog"]').is_displayed()
#print(popup)
#element = driver.find_element(By.NAME, 'q')

#요소에 키워드 넣기(검색)
#element.send_keys('send word')

#검색
#element.submit()
time.sleep(5)

#브라우저 종료
driver.quit()



