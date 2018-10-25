from model.contact import Contact
import re


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
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)

    def create(self, contact_data):
        wd = self.app.wd
        self.return_to_home()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact_data)
        # submit contcat creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cashe = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        # init contact modification
        wd.find_element_by_xpath("(//img[@alt='Edit'])[" + str(index+1) + "]").click() # еще можно css=img[alt="Edit"]
        # fill contact form
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cashe = None


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        #  select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_css_selector("input[value=Delete]").click()
        wd.switch_to_alert().accept()
#        wd.get("http://localhost/addressbook/index.php")
        self.contact_cashe = None

    def return_to_home_page(self): # этот переход проверять не нужно, так как он должен всегда выполняться иначе сайт работает не верно
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def return_to_home(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click() # можно так
#            wd.find_element_by_css_selector("a[href='./']").click() # а можно и так

    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.return_to_home()
            self.contact_cashe = []
            """ ниже мой вариант кода """
            # for element in wd.find_elements_by_name("entry"):
            #     cells = element.find_elements_by_tag_name("td")
            #     id = element.find_element_by_name("selected[]").get_attribute("value")
            #     self.contact_cashe.append(Contact(lastname= cells[1].text, firstname= cells[2].text, id = id))
            """ ниже код из урока - 5_2_splitting_strings.mp4 """
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                #self.contact_cashe.append(Contact(lastname=lastname, firstname=firstname, id=id))

                self.contact_cashe.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cashe)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")[7]
        cells.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")[6]
        cells.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

