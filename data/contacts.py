from model.contact import Contact


# см урок 6_3_ddt.mp4
constant = [
    Contact(firstname="firstname111", middlename="middlename111", lastname="lastname111"),
    Contact(firstname="firstname222", middlename="middlename222", lastname="lastname222")
]


# убрали этот код в уроке 6_5_dynamic_test_generation.mp4
# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " " # из за пробелов иногда тест падает!
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# testdata = [Contact(firstname="", middlename="", lastname="")] + [
#     Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20))
#     for i in range(2)
# ]

