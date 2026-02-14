
list_of_keys = ["access_level", "age"]
my_first_dictionary={
    "name":"John",
    "email":"john@ecorp.com",
    "access_level":5,
    "age":28,
}
for index in range(len(list_of_keys)):
    deleted_item = my_first_dictionary.pop(list_of_keys[index])
print(my_first_dictionary)