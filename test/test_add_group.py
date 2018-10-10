# -*- coding: utf-8 -*-

from model.group import Group

# def is_alert_present(wd): # пример взят из урока
#     try:
#         wd.switch_to_alert().text
#         return True
#     except:
#         return False


def test_add_group(app):
    app.group.create(Group(name="asdf", header="asdf", footer="asdfsdf"))
#    app.session.logout() # эмуляция аварийного завершения сессии


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


# def is_element_present(self, how, what):
#     try: self.wd.find_element(by=how, value=what)
#     except NoSuchElementException as e: return False
#     return True
#
# def is_alert_present(self):
#     try: self.wd.switch_to_alert()
#     except NoAlertPresentException as e: return False
#     return True

