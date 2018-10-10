from model.group import Group


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Group(name="test7777"))
    app.contact.delete_first_contact()

