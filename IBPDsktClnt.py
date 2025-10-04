from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time, os
from winotify import Notification

username="soham.bhattacharya@bega.com.au"
password="Masterda@123"
options = Options()
options.add_argument("--headless")
#driver = webdriver.Edge()
driver = webdriver.Edge(options=options)
driver.get("https://my303715.scmibp1.ondemand.com/ui#IBPPlanningModelPlanningArea-manage")
time.sleep(5)
driver.find_element(By.ID, "j_username").send_keys(username)
time.sleep(2)
driver.find_element(By.ID, "j_password").send_keys(password)
time.sleep(2)
driver.find_element(By.XPATH, '//button[@id="logOnFormSubmit"]').click()
time.sleep(60)

for i in range (100):
	i=i+1
	idpath='//*[@id="__identifier0-__clone'+str(i)+'-link"]'
	statuspath='//*[@id="application-IBPPlanningModelPlanningArea-manage-component---worklist--activeCell-__clone'+str(i)+'-text"]'
	try:
		PlanID=driver.find_element(By.XPATH,idpath)
		status=driver.find_element(By.XPATH,statuspath)
		print(PlanID.text,"==>",status.text)

		if status.text== 'Inactive':
			toast = Notification(app_id="IBP Notification",
                         title='Inactive PlanID in IBP',
                        msg="{text} is inactive in IBP".format(
                             text=PlanID.text),
                             duration="short",
                        icon=r"C:\Users\Public\efccicon.png")
			toast.show()
	except Exception as es:
		break
