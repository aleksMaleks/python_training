

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.header)
        self.change_field_value("lastname", contact.footer)

    def create(self, contact_data):
        wd = self.app.wd
        self.return_to_home()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact_data)
        # submit contcat creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        # init contact modification
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click() # еще можно css=img[alt="Edit"]
        # fill contact form
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()


    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home()
        #  select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
#        wd.get("http://localhost/addressbook/index.php")

    def return_to_home_page(self): # этот переход проверять не нужно, так как он должен всегда выполняться иначе сайт работает не верно
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def return_to_home(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/"):
            wd.find_element_by_link_text("home").click() # можно так
#            wd.find_element_by_css_selector("a[href='./']").click() # а можно и так


    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements_by_name("selected[]"))




