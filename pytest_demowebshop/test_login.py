import time

class TestLogin:
    def test_login(self,browser_setup):
        browser_setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self,browser_setup):
        browser_setup.find_element('id', 'Email').send_keys('sanchi123@gmail.com')
        time.sleep(1)

    def test_login_pwd(self,browser_setup):
        browser_setup.find_element('id', 'Password').send_keys('JeonSanchita')
        time.sleep(1)