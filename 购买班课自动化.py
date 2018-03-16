from selenium import webdriver
import time
import threading
import unittest
from selenium.webdriver.common.action_chains import ActionChains


def login(f):
    def inner():
        driver = f()
        driver.get("http://xiaobao.gn100.com/tw.main.login")

        driver.find_element_by_class_name("stu_mobile").clear()
        driver.find_element_by_class_name("stu_mobile").send_keys("18310836536")
        driver.find_element_by_class_name("stu_pwd").clear()
        driver.find_element_by_class_name("stu_pwd").send_keys("111111")
        time.sleep(3)

        driver.find_element_by_class_name("fs16").click()

        driver.quit()
    return inner

@login
def login_chrome():
    driver = webdriver.Chrome()
    return driver

@login
def login_firefox():
    driver = webdriver.Firefox()
    return driver

threads = []

t1 = threading.Thread(target=login_chrome)
threads.append(t1)

t2 = threading.Thread(target=login_firefox)
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("ok")


