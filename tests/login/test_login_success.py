from conftest import Base
from conftest import services
from pages.page_login import login


class TestLoginSuccess(Base):
    def test_login_success(self):
        self.driver.get(login.login_url)

        services.send_keys_by_xpath(self, login.login_mail_input, login.login_mail)

        login.check_login(self)

        login.check_logout(self)
