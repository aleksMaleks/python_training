# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string


# def is_alert_present(wd): # пример взят из урока
#     try:
#         wd.switch_to_alert().text
#         return True
#     except:
#         return False

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " # *10 убрал генерацию лишних пробелов так как с ними некоторые тесты падают, а еще не создается группа со знаком ' (string.punctuation + )
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# первый вариант
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(2)
]

# второй вариант
# testdata = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
#    pass
     old_groups = app.group.get_group_list()
     app.group.create(group)
#    app.session.logout() # эмуляция аварийного завершения сессии
     assert len(old_groups) + 1 == app.group.count()
     new_groups = app.group.get_group_list()
     old_groups.append(group)
     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




# def is_element_present(self, how, what):
#     try: self.wd.find_element(by=how, value=what)
#     except NoSuchElementException as e: return False
#     return True
#
# def is_alert_present(self):
#     try: self.wd.switch_to_alert()
#     except NoAlertPresentException as e: return False
#     return True

