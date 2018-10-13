from model.contact import Contact



def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test7777"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="new name1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_header(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test7777"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="new header1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
