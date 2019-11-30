import random


class account:
    account_mail = "emailer5k+addaddress@gmail.com"
    account_mail_failed = "emailer5k+addressfailed@gmail.com"
    account_mail_edit = "emailer5k+editaddress@gmail.com"
    account_mail_missing = "emailer5k+missingaddress@gmail.com"
    account_mail_change = "emailer5k+changedata@gmail.com"
    account_mail_affiliate = "emailer5k+affiliate@gmail.com"
    account_mail_newsletter = "emailer5k+newsletter@gmail.com"
    account_address_book = 'Address Book'
    account_add_address = 'New Address'
    account_fname = '//*[@id="input-firstname"]'
    account_lname = '//*[@id="input-lastname"]'
    account_company = '//*[@id="input-company"]'
    account_address1 = '//*[@id="input-address-1"]'
    account_address2 = '//*[@id="input-address-2"]'
    account_city = '//*[@id="input-city"]'
    account_postcode = '//*[@id="input-postcode"]'
    account_region_select = '//*[@id="input-zone"]/option[text()="Conwy"]'
    account_submit = 'input.btn-primary'
    account_success = 'div.alert-success'
    account_failed = 'div.alert-warning'
    account_missing = 'div.text-danger'
    account_delete = 'a.btn-danger'
    account_address_edit = 'a.btn-info'
    account_edit = 'Edit Account'
    account_edit_phone = '//*[@id="input-telephone"]'
    account_affiliate = 'Edit your affiliate information'
    account_affiliate_tax = '//*[@id="input-tax"]'
    account_newsletter = 'Newsletter'
    account_newsletter_1 = '//input[@value="1"]'
    account_newsletter_0 = '//input[@value="0"]'

    account_data = "Tester"
    account_data_postcode = "12345"
    account_data_random = str(random.randint(0, 99999))
    account_added_text = "Your address has been successfully added"
    account_deleted_text = "Your address has been successfully deleted"
    account_last_address_text = "Warning: You must have at least one address!"
    account_edit_address_text = "Your address has been successfully updated"
    account_missing_text = "First Name must be between 1 and 32 characters!"
    account_updated = "Success: Your account has been successfully updated."
    account_newsletter_text = "Success: Your newsletter subscription has been successfully updated!"

