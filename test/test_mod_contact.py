

from model.group import Group


def test_modification_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_first_contact(Group(name="mod1", header="mod1", footer="mod1"))
    app.session.logout()

