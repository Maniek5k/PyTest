# This repository contains tests of http://tutorialsninja.com/demo/ website.

All tests are written using PyTest framework, also tests includes custom info logging about every step.

Tests are run by PyTest automatically (to run just enter /tests folder and type in terminal: pytest)

# At current state following tests are available:

- Login - success
- Login - failed (no user/pwd not match)
- Login - forgotten password
- Register
- Register - checkbox missing
- Search test (success + failed in one test)
- Checkout
- Return ordered product
- Add to wishlist - success
- Add to wishlist - failed, you have to be logged in
- Add to basket
- Add to basket - failed (select option required)
- Add to basket - reorder previously ordered product
- Add Gift Card to basket
- Contact form test
- Contact form (wrong mail & message too short tests)
- Account Tests:
    - Add address
    - Missing address
    - Affiliate account changes
    - Change customer data
    - At least one address required
    - Newsletter
    - Password change