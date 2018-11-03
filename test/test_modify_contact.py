import  random
from model.contact import Contact


#@pytest.mark.skip(reason="no way of currently testing this") # это нужно для отключение теста
def test_modify_contact_name(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test7777"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact = Contact(firstname="new firstname1")
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(random_contact.id, contact)
#    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_header(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(middlename="test7777"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(middlename="new middlename1"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
