import pytest

from model.group import Group


#@pytest.mark.skip(reason="no way of currently testing this") # для отключение теста
def test_modification_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modification_first_group\
        (Group(name="name mod1", header="header mod1", footer="footer mod1")) # my test!!!

