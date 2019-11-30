from selenium.webdriver.common.by import By

from conftest import services


class login:
    login_url = "http://tutorialsninja.com/demo/index.php?route=account/login"
    login_mail_input = '//*[@id="input-email"]'
    login_pwd_input = '//*[@id="input-password"]'
    login_submit = 'input.btn-primary'
    login_my_acc = '//*[@id="content"]/h2[1]'
    login_alert = 'div.alert'
    login_logout = 'Logout'
    login_forgotten_pwd = 'Forgotten Password'
    login_pwd_change = 'Password'
    pwd_change_input_confirm = '//*[@id="input-confirm"]'
    pwd_change_submit = '//input[@type="submit"]'
    logout_success = '//*[@id="content"]/p[1]'

    login_mail = "emailer5k+login@gmail.com"
    login_pwd = "12345"
    login_fail_mail = "failed@fail.co"
    login_fail_pwd = "34231"
    login_fail_msg = "Warning: No match for E-Mail Address and/or Password."
    login_success = "My Account"
    login_forgotten_msg_alert = "Warning: The E-Mail Address was not found in our records, please try again!"
    login_forgotten_msg_success = "An email with a confirmation link has been sent your email address."
    logout_success_text = "You have been logged off your account. It is now safe to leave the computer."

    pwd_change_mail = "emailer5k+pwdchange@gmail.com"
    pwd_change_default_pass = "12345"
    pwd_change_changed_pass = "54321"
    pwd_change_success = "Success: Your password has been successfully updated."

    def check_login(self):
        services.send_keys_by_xpath(self, login.login_pwd_input, login.login_pwd)

        services.assert_and_click(self, By.CSS_SELECTOR, login.login_submit)

        services.assert_text(self, By.XPATH, login.login_my_acc, login.login_success)

    def check_logout(self):
        services.assert_and_click(self, By.LINK_TEXT, login.login_logout)

        services.assert_text(self, By.XPATH, login.logout_success, login.logout_success_text)
