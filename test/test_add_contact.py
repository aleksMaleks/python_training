# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Group(name="first1", header="middle1", footer="last1"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Group(name="", header="", footer=""))
    app.session.logout()

# def is_element_present(self, how, what):
#     try: self.wd.find_element(by=how, value=what)
#     except NoSuchElementException as e: return False
#     return True
#
# def is_alert_present(self):
#     try: self.wd.switch_to_alert()
#     except NoAlertPresentException as e: return False
#     return True
