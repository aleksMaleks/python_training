import pytest

from model.group import Group


@pytest.mark.skip(reason="no way of currently testing this")
def test_modification_first_group(app):
    app.group.modification_first_group(Group(name="mod1", header="mod1", footer="mod1"))
