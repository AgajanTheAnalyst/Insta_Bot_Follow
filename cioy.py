def follow(self):
    usernames = set()
    try:
        pop_up_window = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div'
                                                      '/div/''div/div[2]/div/div/div[3]'))
        )
        time.sleep(5)

        print('pop up window found')
    except Exception as e:
        print(f'error locating the pop-up window:{str(e)}')
        return
    while True:
        num_of_username = len(usernames)
        users_in_window = pop_up_window.find_elements(By.CSS_SELECTOR, 'div button')
        print(f'Number of users found in : {len(users_in_window)}')
        for users in users_in_window:
            username = users.text
            if username and username not in usernames:
                usernames.add(username)
                print(f'processing user: {username}')
                try:
                    follow_button = users.find_element(By.XPATH, './/following-sibling::button[text()="Follow"]')
                    if follow_button:
                        follow_button.click()
                        print(f'followed user:{username}')
                        time.sleep(1)
                except Exception as e:
                    print(f'error while trying to follow {users.text} " {str(e)}')

        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', pop_up_window)
        current_scroll_position = self.driver.execute_script('return arguments[0].scrollTop',
                                                             pop_up_window)
        print(f'Scrolled to position:{current_scroll_position}')
        time.sleep(1)
        num_of_username_after = len(usernames)
        if num_of_username == num_of_username_after:
            print("No new usernames found, stop scrolling")
            break
    print(f"Total usernames followed:{len(usernames)}")
