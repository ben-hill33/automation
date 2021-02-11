import re
import os

file_to_read = './assets/potential-contacts.txt'
file_to_write = 'email-extracted.txt'

delimiter_in_file = [',', ';']


def validate_email(str_email):
    if re.match("(.*)@(.*).(.*)", str_email):
        return True
    return False


def write_file(list_data):
    file = open(file_to_write, 'w+')
    str_data = ''
    for item in list_data:
        str_data = str_data + item + '\n'
    file.write(str_data)


list_email = []

file = open(file_to_read, 'r')

list_line = file.readlines()

for item_line in list_line:
    item = str(item_line)
    for delimiter in delimiter_in_file:
        item = item.replace(str(delimiter), ' ')
    word_list = item.split()
    for word in word_list:
        if(validate_email(word)):
            list_email.append(word)

if list_email:
    unique_email = set(list_email)
    print(len(unique_email), 'emails collected!')
    write_file(unique_email)
else:
    print("No email found.")


if __name__ == "__main__":
    validate = validate_email
    print(validate)
