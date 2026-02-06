import time

class TestRegister:
    def test_reg(self,browser_setup):
        browser_setup.find_element("xpath","//a[text()='Register']").click()
        time.sleep(2)
    def test_gender(self,browser_setup):
        browser_setup.find_element("id","gender-female").click()
        time.sleep(2)
    def test_fname(self,browser_setup):
        browser_setup.find_element("id","FirstName").send_keys("Sanchita")
        time.sleep(2)
    def test_lname(self,browser_setup):
        browser_setup.find_element("id","LastName").send_keys("Ramesh")
        time.sleep(2)
    def test_email(self,browser_setup):
        browser_setup.find_element("id","Email").send_keys("sanchi123@gmail.com")
        time.sleep(2)
    def test_password(self,browser_setup):
        browser_setup.find_element("id","Password").send_keys("JeonSanchita")
        time.sleep(2)
    def test_confirmPassword(self,browser_setup):
        browser_setup.find_element("id","ConfirmPassword").send_keys("JeonSanchita")
        time.sleep(2)
    def test_clickRegister(self,browser_setup):
        browser_setup.find_element("id","register-button").click()
        time.sleep(2)