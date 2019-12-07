class contact:
    contact_link = 'Contact Us'
    contact_name = '//*[@id="input-name"]'
    contact_mail = '//*[@id="input-email"]'
    contact_message = '//*[@id="input-enquiry"]'
    contact_submit = '//input[@type="submit"]'
    contact_success = '//*[@id="content"]/h1'
    contact_danger = 'div.text-danger'

    contact_data_name = "Tester"
    contact_data_mail = "tester@test.te"
    contact_data_message = "This is test message longer than 10 characters"
    contact_data_short_message = "Nope!"
    contact_success_text = "Contact Us"
    contact_danger_mail_text = "E-Mail Address does not appear to be valid!"
    contact_danger_msg_text = "Enquiry must be between 10 and 3000 characters!"
