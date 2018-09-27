

from model.group import Group


def test_modification_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first_group(Group(name="mod1", header="mod1", footer="mod1"))
    app.session.logout()
