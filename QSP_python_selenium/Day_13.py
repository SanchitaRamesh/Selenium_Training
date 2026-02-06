############## 05/01/2026 #############
import time
from time import sleep

from selenium import webdriver

ch_open = webdriver.ChromeOptions()
ch_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(ch_open)

