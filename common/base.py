import pytest

from common.helpers import find_element_by_test_id


@pytest.mark.usefixtures("driver_init")
class Login:

    def test_login(self, url, fb_username, fb_password):

        self.driver.get(url=url)

        find_element_by_test_id(self.driver, "royal_email").send_keys(fb_username)
        find_element_by_test_id(self.driver, "royal_pass").send_keys(fb_password)
        find_element_by_test_id(self.driver, "royal_login_button").click()

        assert find_element_by_test_id(self.driver, "facebar_root").is_displayed(), \
            "Facebook homepage was not loaded as expected"
