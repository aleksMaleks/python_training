from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
#        self.return_to_home()
        self.group_cashe = None


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
#        self.return_to_home()
        self.group_cashe = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        #        self.return_to_home()
        self.group_cashe = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
#        self.return_to_home()
        self.group_cashe = None

    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        #        self.return_to_home()
        self.group_cashe = None

    #     def modification_first_group(self, new_group_data): # my test!!!
#         wd = self.app.wd
#         self.open_groups_page()
#         self.select_first_group()
#         # open modification form
#         wd.find_element_by_name("edit").click()
#         # fill group form
#         self.fill_group_form(new_group_data)
#         # submit group creation
#         wd.find_element_by_name("update").click()
#         self.return_to_groups_page()
# #        self.return_to_home()
#         self.group_cashe = None

    def return_to_groups_page(self): # этот переход проверять не нужно, так как он должен всегда выполняться иначе сайт работает не верно
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    # def return_to_home(self): # перенес эту проверку в contact.py
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector("a[href='./']").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cashe = None

    def get_group_list(self):
        if self.group_cashe is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cashe = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cashe.append(Group(name=text, id=id))
        return list(self.group_cashe)


