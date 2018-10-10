

from model.group import Group


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Group(name="test7777"))
    app.contact.modify_first_contact(Group(name="new name1"))


def test_modify_contact_header(app):
    if app.contact.count() == 0:
        app.contact.create(Group(name="test7777"))
    app.contact.modify_first_contact(Group(header="new header1"))
