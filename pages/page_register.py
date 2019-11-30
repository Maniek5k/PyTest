import random


class register:
    register_url = "http://tutorialsninja.com/demo/index.php?route=account/login"
    register_btn = "div.well > a.btn-primary"
    register_fname = '//*[@id="input-firstname"]'
    register_lname = '//*[@id="input-lastname"]'
    register_mail = '//*[@id="input-email"]'
    register_phone = '//*[@id="input-telephone"]'
    register_pwd = '//*[@id="input-password"]'
    register_pwd_conf = '//*[@id="input-confirm"]'
    register_checkbox = 'agree'
    register_submit = 'div.pull-right > input.btn-primary'
    register_success_h1 = '//*[@id="content"]/h1'
    register_success_continue = 'div.pull-right'
    register_logout = 'Logout'
    register_alert = 'div.alert'

    register_data_mail = str(random.randint(0, 99999)) + "@testmail.test"
    register_data_fname = "Tester"
    register_data_lname = "Testowy"
    register_data_pwd = "12345"
    register_data_phone = "123123123"
    register_policy = "Warning: You must agree to the Privacy Policy!"
