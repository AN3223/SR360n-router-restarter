from selenium import webdriver
import time
import datetime
import os


def main():
    timer_length = 900  # 15 minutes
    password = 'admin'  # this is the default password, change it to your own if you've set one

    base_time = time.time()
    strikes = 0

    while True:
        try:
            current_time_formatted = datetime.datetime.now().strftime('%I:%M %p')

            if not ping():
                strikes += 1
                print('Internets are down at {}'.format(current_time_formatted))
            else:
                print('Internets are operational at {}'.format(current_time_formatted))

            if time_passed(base_time, timer_length):  # runs at the end of the timer
                if strikes >= (timer_length / 60) * 0.4:  # restarts the router if it was down 40% of the time or more
                    restart_router(password)
                    print('Router restarted at {}'.format(datetime.datetime.now().strftime('%I:%M %p')))
                print()
                base_time = time.time()
                strikes = 0

            time.sleep(60)
            
        except KeyboardInterrupt:
            print('Restarting...')
            restart_router(password)
            base_time = time.time()
            strikes = 0
            print('Router force restarted at {}'.format(datetime.datetime.now().strftime('%I:%M %p')))


def ping(server_ip='8.8.8.8'):
    command = 'ping'
    response = os.system('{} {} >nul'.format(command, server_ip))
    if response == 0:
        return 1  # successful ping
    else:
        return 0  # failure


def restart_router(password):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    try:
        driver.get('http://admin:{}@192.168.1.1/admin/'.format(password))
        driver.get('http://192.168.1.1/admin/resetrouter.html')
        selector = 'body > p > input[type="button"]'
        driver.find_element_by_css_selector(selector).click()
    finally:
        driver.close()


def time_passed(oldepoch, amount_of_time):
    return time.time() - oldepoch >= amount_of_time


main()
