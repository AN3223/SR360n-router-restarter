from selenium import webdriver

TIMER_LENGTH = 900  # 15 minutes
PASSWORD = '1999'
SLEEP_TIME = 5


def restart_router():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    try:
        driver.get('http://admin:{}@192.168.1.1/admin/'.format(PASSWORD))
        driver.get('http://192.168.1.1/admin/resetrouter.html')
        selector = 'body > p > input[type="button"]'
        driver.find_element_by_css_selector(selector).click()
    finally:
        driver.close()


if __name__ == '__main__':
    restart_router()
