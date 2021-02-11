import re


def valid_email(path):
    file_to_write = './assets/email-extracted.txt'
    regex = r'\w+[._]*\w+@\w+[-]*\w+\.(?:com|org|info|net|biz)'

    with open(path) as potential_contact:
        file = potential_contact.read()

    email = set(re.findall(regex, file))
    mo_email = list(email)
    mo_email.sort()
    if mo_email:
        print(len(mo_email), 'emails collected!')
    else:
        print('No emails found.')

    email_list = ''
    for email in mo_email:
        email_list += email + '\n'

    with open(file_to_write, 'w+') as e_file:
        e_file.write(email_list)


if __name__ == "__main__":
    file_to_read = './assets/potential-contacts.txt'
    result = valid_email(file_to_read)
    print(result)


# Commented out code works also but it's not mine. It also prints alphabetically which is neat but I was having trouble integrating that into my solution
# Maybe come back through when you have more time

# file_to_read = './assets/potential-contacts.txt'
# file_to_write = 'email-extracted.txt'


# delimiter_in_file = [',', ';']


# def validate_email(str_email):
#     if re.match("(.*)@(.*).(.*)", str_email):
#         return True
#     return False


# def write_file(list_data):
#     file = open(file_to_write, 'w+')
#     str_data = ''
#     for item in list_data:
#         str_data = str_data + item + '\n'
#     file.write(str_data)


# list_email = []

# file = open(file_to_read, 'r')

# list_line = file.readlines()

# for item_line in list_line:
#     item = str(item_line)
#     for delimiter in delimiter_in_file:
#         item = item.replace(str(delimiter), ' ')
#     word_list = item.split()
#     for word in word_list:
#         if(validate_email(word)):
#             list_email.append(word)

# if list_email:
#     unique_email = set(list_email)
#     print(len(unique_email), 'emails collected!')
#     write_file(unique_email)
# else:
#     print("No email found.")
