

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
#        self.return_to_home()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.header)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.footer)
        # submit contcat creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def modification_first_contact(self, group):
        wd = self.app.wd
#        self.return_to_home()
        # init contact modification
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click() # еще можно css=img[alt="Edit"]
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.header)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.footer)
        # submit contcat modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()


    def delete_first_contact(self):
        wd = self.app.wd
#        self.return_to_home()
        #  select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
#        wd.get("http://localhost/addressbook/index.php")

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    # def return_to_home(self):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector("a[href='./']").click()


