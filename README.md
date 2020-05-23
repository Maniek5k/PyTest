[![Build Status](https://travis-ci.org/Maniek5k/PyTest.svg?branch=master)](https://travis-ci.org/Maniek5k/PyTest)

# This repository contains tests of http://tutorialsninja.com/demo/ website.

All tests are written using PyTest framework, also tests includes custom info logging about every step.

Tests are run by PyTest automatically (to run just enter /tests folder and type in terminal: pytest)

Whole repository is meant to be built automatically by Travis-CI (on staging branch) and then deployed on merge to master branch as Docker Image. 

# Whole repository is available as DOCKER IMAGE!

To run it you need to run command, having your docker installed:
    docker run maniek5k/pytest

This will download DOCKER image and run tests automatically, so you can see main functionality and test results without needing to download this repository and running it by yourself (all necessary packages like Chrome, ChromeDriver, Selenium are included). So it's working out-of-the-box solution for testing!

Additionally, you can run spearate tests using Docker bash:
sudo docker run -it maniek5k/pytest /bin/bash
Then just CD to tests folder:
cd /usr/src/pytest-selenium/tests/
Then you can run tests per folder, in example:
pytest login
Or enter any of folder and run tests separately.

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