# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.add_group import testdata # constant as testdata # см урок 6_3_ddt.mp4

# def is_alert_present(wd): # пример взят из урока
#     try:
#         wd.switch_to_alert().text
#         return True
#     except:
#         return False


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

