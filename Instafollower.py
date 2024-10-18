import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class InstaFollower:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username, password, link):
        self.driver.get(link)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.NAME, "username"))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.NAME, "password"))
        ).send_keys(password, Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "div._a9-z button:nth-of-type(2)"))
        ).click()

    def find_followers(self, insta_account):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Search"]'))
        ).click()
        search = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search input']"))
        )
        search.send_keys(insta_account, Keys.ENTER)
        account = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, f'a[href="/{insta_account}/"]'))
        )
        account.click()
        followers = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, f'a[href="/{insta_account}/followers/"]'))
        )
        followers.click()

    def follow(self):
        try:
            pop_up_window = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div'
                                                          '/div/''div/div[2]/div/div/div[3]'))
            )
            time.sleep(2)

            print('pop up window found')
        except Exception as e:
            print(f'error locating the pop-up window:{str(e)}')
            return
        while True:
            try:
                pop_up_window = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.XPATH,
                                                    '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div'
                                                    '/div[2]/div/div/div[3]'))
                )

                follow_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class, '_acan') and contains"
                                                                     "(@class, '_acap') and contains(@class, '_acas') "
                                                                     "and contains(@class, '_aj1-') and "
                                                                     "contains(@class, '_ap30')]")

                if not follow_buttons:
                    print('No follow buttons found exiting')
                    break

                for button in follow_buttons:
                    try:
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                        WebDriverWait(self.driver, 10).until(
                            ec.element_to_be_clickable((By.XPATH,
                                                        "//button[contains(@class, '_acan') and contains(@class, "
                                                        "'_acap') and contains(@class, '_acas') and contains(@class, "
                                                        "'_aj1-') and contains(@class, '_ap30')]"))
                        )
                        self.driver.execute_script("arguments[0].click();", button)
                        time.sleep(1)
                    except Exception as e:
                        print(f"Error clicking the button: {str(e)}")
                        continue
            except Exception as e:
                print(f"Error locating follow buttons: {str(e)}")
                break
            try:
                pop_up_window = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.XPATH,
                                                    '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div'
                                                    '/div[2]/div/div/div[3]'))
                )
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',
                                           pop_up_window)
            except Exception as e:
                print(f"Error scrolling the pop-up window: {str(e)}")
                break
            time.sleep(2)

    def close(self):
        self.driver.quit()
