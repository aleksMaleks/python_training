
assert(True)
#assert(False), 'Test'

# if __debug__:
#         if not passed:
#             raise AssertionError('Not passed')


# assert(2 + 2 == 5, "Houston we've got a problem")
# assert 2 + 2 == 5, "Houston we've got a problem"



from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost/litecart/admin')
driver.find_element_by_css_selector("[name=username]").send_keys("admin")
driver.find_element_by_css_selector("[name=password]").send_keys("admin")
driver.find_element_by_name("login").click()

#links = driver.find_elements_by_css_selector("#app- a")

linksCount = len(driver.find_elements_by_css_selector("#app- a"))

# for 1 in range i:






