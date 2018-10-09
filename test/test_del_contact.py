from model.group import Group


def test_delete_first_contact(app):
    app.contact.delete_first_contact()

