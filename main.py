from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

'''ss = raw_input("Enter the subject:")'''
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)
driver.get('https://calendar.google.com')
time.sleep(5)

ele = driver.find_element_by_id("identifierId")

ele.send_keys("18bce014@nirmauni.ac.in")

driver.find_element_by_css_selector("#identifierNext > div > button").click()
time.sleep(5)
ele1 = driver.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")

ele1.send_keys("159632478anik")

driver.find_element_by_css_selector("#passwordNext > div > button").click()
time.sleep(10)

driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[2]/div[3]/div/div/div[1]/div").click()

s1=driver.find_element_by_xpath("//*[@id='gs_lc50']/input[1]")

s1.send_keys("Maths")

driver.find_element_by_xpath("//*[@id='aso_search_form_anchor']/button[4]").click()
time.sleep(5)
s2=driver.find_element_by_xpath("//*[@id='YPCqFe']/div[2]/div/div/div/div/div[2]/div[1]")

action = ActionChains(driver)

action.double_click(s2).perform()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='xRTCIn']/div/div/div[1]/div[1]/div/div[1]/a").click()
time.sleep(10)

current_tab=driver.window_handles[1]
driver.switch_to.window(current_tab)

vod=driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div").click()

mic =driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div").click()




driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()


time.sleep(15)

driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button").click()