from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime



def run_driver(run_func,*args):
    driver = create_browser()
    # driver = create_browser_chrome()
    val = run_func(driver,*args)
    driver.quit()
    return val

def custom_location_firefox(options):
    options.binary_location = r'C:\Users\dhaval.atul.pantojee\AppData\Local\Mozilla Firefox\firefox.exe'
    return options

def create_browser():
    driver_options = webdriver.FirefoxOptions()
    # driver_options.add_argument('--headless')
    driver_options = custom_location_firefox(driver_options)
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False) 
    driver = webdriver.Firefox(executable_path='C:\\test_attempt\\geckodriver.exe',firefox_profile=profile, options=driver_options)
    driver.maximize_window()
    return driver

def create_browser_chrome():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver = webdriver.Chrome(options=driver_options)
    driver.maximize_window()
    return driver

def run_func_in_new_tab(driver,func,*args):
    current_window_handle = driver.current_window_handle
    current_window_handles = driver.window_handles
    open_new_blank_tab(driver)
    new_window_handles = driver.window_handles
    new_tab_handle = list(set(new_window_handles)-set(current_window_handles))[0]
    driver.switch_to.window(new_tab_handle)
    # Run this function
    func(driver,*args)
    # Close the Tab
    driver.close()
    # Switch to the original Tab
    driver.switch_to.window(current_window_handle)

def open_new_blank_tab(driver):
    driver.execute_script("window.open('')")

def dummy_func(*args):
    print(*args)
    sleep(1)

def log(sentence,openmode='a'):
    with open('logfile.log',openmode) as logfile:
        timestamp = '['+datetime.now().isoformat()+'] '
        logfile.write(timestamp + sentence.strip()+'\n')


if __name__ == '__main__':
    # Opens new firefox automated browser with dummy_func and arguments as 1,2,3
    # run_driver(dummy_func,1,2,3)
    pass