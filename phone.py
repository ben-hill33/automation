import pyperclip
import re
import shutil


file_to_read = './assets/potential-contacts.txt'
file_to_write = 'phone-num-extracted.txt'

delimiter_in_file = [',', ';']


def validate_phone(str_phone):
    phone_pattern = r'^(\d{10})(?:\s|$)'
    compile_obj = re.compile(phone_pattern)
    match_obj = compile_obj.search(item_line)

    if re.match(match_obj, str_phone):
        return True
    return False


def write_file(list_data):
    file = open(file_to_write, 'w+')
    str_data = ''
    for item in list_data:
        str_data = str_data + item + '\n'
    file.write(str_data)


list_phone = []

file = open(file_to_read, 'r')
list_line = file.readlines()

for item_line in list_line:
    item = str(item_line)
    for delimiter in delimiter_in_file:
        item = item.replace(str(delimiter), ' ')
    word_list = item.split()
    for word in word_list:
        if(validate_phone(word)):
            list_phone.append(word)

if list_phone:
    unique_phone = set(list_phone)
    print(len(unique_phone), 'phone numbers collected!')
    write_file(unique_phone)
else:
    print('No numbers founds.')


# file.close()

# delimiter_in_file = [',', ';']


# matches phone number pattern
# phone_regex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?                # area code
#     (\s|-|\.)?                        # separator
#     (\d{3})                           # first 3 digits
#     (\s|-|\.)                         # separator
#     (\d{4})                           # last 4 digits
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
#     )''', re.VERBOSE | re.IGNORECASE)

# file = open(file_to_read, 'r')

# list_line = file.readlines()

# print(list_line)
# mo = phone_regex.search(list_line)

# phone_number = '-'.join([mo.group(2), mo.group(4), mo.group(6)])
# if mo.group(10) != '':
#     phone_number += ' x' + mo.group(10)

# print(phone_number)


# print(mo)


# text = str(pyperclip.paste())
# matches = []
# for groups in phone_regex.findall(text):
#   phone_num = '-'.join([groups[1], groups[3], groups[5]])
#   if groups[8] != '':
#     phone_num += ' x' + groups[8]
#   matches.append(phone_num)

# if len(matches) > 0:
#   pyperclip.copy('\n'.join(matches))
#   print('Copied to the clipboard: ')
#   print('\n'.join(matches))
# else:
#   print('No phone numbers found.')

# if __name__ == "__main__":
