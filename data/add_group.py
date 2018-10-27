from model.group import Group
import random
import string


# см урок 6_3_ddt.mp4
constant = [
    Group(name="name111", header="header111", footer="footer111"),
    Group(name="name222", header="header222", footer="footer222")
]


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

