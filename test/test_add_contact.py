# -*- coding: utf-8 -*-
import random
import string
import pytest
from model.contact import Contact

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " # из за пробелов иногда тест падает!
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20))
    for i in range(2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


