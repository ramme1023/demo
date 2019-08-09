from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir","path with /")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("pdfjs.disabled", True)



driver = webdriver.Firefox(firefox_profile=profile,executable_path = 'C:\Selemium\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get("https://getbootstrap.com/docs/4.3/getting-started/download/")
driver.find_element_by_xpath("//p[4]//a[1]").click()
print ("Completed")
