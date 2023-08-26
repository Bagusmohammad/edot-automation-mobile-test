from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import unittest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.mobileby import MobileBy

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "11"
caps["appium:deviceName"] = "sdk_gphone_arm64"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:appPackage"] = "com.pmaapp.ehashtag"
caps["appium:appActivity"] = "com.pmaapp.ehashtag.MainActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
caps['autoGrantPermissions'] = True

#xpath
skip_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView'
skip2_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]'
close_banner_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[2]'
ecommerce_page_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View/android.view.View[2]'
ecommerce_page_tittle = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView'
search_commerce_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.CircleView'
search_bar_commerce_classname = 'android.widget.EditText'
momments_filter_search_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
list_momments_search = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'
momments_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
try:
  button_skip = WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH, skip_xpath))
  ).click()
except TimeoutException:
  logger.error("Error: Cannot Tap Button Skip")

try:
  button_skip2 = WebDriverWait(driver,10).until(
      EC.visibility_of_element_located((By.XPATH, skip2_xpath))
  ).click()
except TimeoutException:
  logger.error("Error: Cannot Tap Button Skip 2")

try:
  button_close_banner = WebDriverWait(driver,10).until(
      EC.visibility_of_element_located((By.XPATH, close_banner_xpath))
  ).click()
except TimeoutException:
  logger.error("Error: Cannot Tap Button Close Banner")

try:
  button_commerce_page = WebDriverWait(driver,10).until(
      EC.visibility_of_element_located((By.XPATH, ecommerce_page_xpath))
  ).click()
except TimeoutException:
  logger.error("Error: Cannot Tap Button Commerce Page")

try:
  commerce_page_tittle = WebDriverWait(driver,10).until(
      EC.presence_of_element_located((By.XPATH, ecommerce_page_tittle))
  )
except TimeoutException:
  logger.error("Error: Commerce Page Doesnt Appeared")

try:
  button_search = WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH, search_commerce_xpath))
  ).click()
except TimeoutException:
  logger.error("Error: Button Search Error")

try:
  momments_filter = WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.XPATH, momments_filter_search_xpath))
  ).click()
except TimeoutException:
  logger.error("Error: Button Search Error")
time.sleep(3)
try:
  button_search_bar = WebDriverWait(driver,10).until(
      EC.visibility_of_element_located((By.CLASS_NAME, search_bar_commerce_classname))
  ).send_keys("KPOP")
except TimeoutException:
  logger.error("Error: Search Bar Error")

try:
  button_search_bar = WebDriverWait(driver,10).until(
      EC.visibility_of_element_located((By.CLASS_NAME, search_bar_commerce_classname))
  ).click()
except TimeoutException:
  logger.error("Error: Search Bar Error")
time.sleep(3)
driver.press_keycode(66);

try:
  list_momments = WebDriverWait(driver, 10).until(
      EC.visibility_of_all_elements_located((By.XPATH, list_momments_search))
  )
except TimeoutException:
  logger.error("Error: Momments Doesnt Appeared")

try:
  momments = WebDriverWait(driver,10).until(
      EC.visibility_of_element_located((By.XPATH, momments_xpath))
  ).click()
except TimeoutException:
  logger.error("Error: Momments Error")

time.sleep(10)
logger.success("Search Momments Test Case has been Tested")
driver.quit()