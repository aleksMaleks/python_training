# -*- coding: utf-8 -*-

from model.group import Group


def test_add_contact(app):
    app.contact.create(Group(name="first1", header="middle1", footer="last1"))

def test_add_empty_contact(app):
    app.contact.create(Group(name="", header="", footer=""))

# def is_element_present(self, how, what):
#     try: self.wd.find_element(by=how, value=what)
#     except NoSuchElementException as e: return False
#     return True
#
# def is_alert_present(self):
#     try: self.wd.switch_to_alert()
#     except NoAlertPresentException as e: return False
#     return True
