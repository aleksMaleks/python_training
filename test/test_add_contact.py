# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name="first1", header="middle1", footer="last1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name="", header="", footer=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


# def is_element_present(self, how, what):
#     try: self.wd.find_element(by=how, value=what)
#     except NoSuchElementException as e: return False
#     return True
#
# def is_alert_present(self):
#     try: self.wd.switch_to_alert()
#     except NoAlertPresentException as e: return False
#     return True
