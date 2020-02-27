class checkout:
    checkout_mail = "emailer5k+order@gmail.com"
    checkout_pwd = "12345"
    checkout_return_email = "emailer5k+return@gmail.com"
    checkout_btn = 'Checkout'
    checkout_payment = '//*[@id="button-payment-address"]'
    checkout_shipping = '//*[@id="button-shipping-address"]'
    checkout_shipping_method = '//*[@id="button-shipping-method"]'
    checkout_payment_method = '//*[@id="button-payment-method"]'
    checkout_alert_checkbox = 'div.alert'
    checkout_checkbox = 'agree'
    checkout_confirm = '//*[@id="button-confirm"]'
    checkout_order_placed = '//*[@id="content"]/h1'
    checkout_placed_title = "Your order"

    checkout_alert_msg = "Warning: You must agree to the Terms & Conditions!\n×"
    checkout_order_placed_msg = "Your order has been placed!"

    return_button = 'a.btn-danger'
    return_necessary_option = 'div.text-danger'
    return_radio = 'return_reason_id'
    return_submit = 'input.btn-primary'
    return_success = '// *[ @ id = "content"] / p[2]'

    return_option_text = "You must select a return product reason!"
    return_success_text = "You will be notified via e-mail as to the status of your request."
