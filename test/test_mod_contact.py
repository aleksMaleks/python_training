

from model.group import Group


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Group(name="new name1"))


def test_modify_contact_header(app):
    app.contact.modify_first_contact(Group(header="new header1"))
