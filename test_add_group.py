# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application

# def is_alert_present(wd): # пример взят из урока
#     try:
#         wd.switch_to_alert().text
#         return True
#     except:
#         return False


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="asdf", header="asdf", footer="asdfsdf"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


# def is_element_present(self, how, what):
#     try: self.wd.find_element(by=how, value=what)
#     except NoSuchElementException as e: return False
#     return True
#
# def is_alert_present(self):
#     try: self.wd.switch_to_alert()
#     except NoAlertPresentException as e: return False
#     return True

