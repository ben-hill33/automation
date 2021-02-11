import re


def valid_phone(path):
    file_to_write = './assets/phone-num-extracted.txt'
    regex = r'[(]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})'

    with open(path) as potential_contact:
        file = potential_contact.read()

    phone = set(re.findall(regex, file))
    mo_phone = list(phone)
    mo_phone.sort()
    if mo_phone:
        print(len(mo_phone), 'phone numbers collected!')
    else:
        print('No phone numbers found.')
    phone_num = ''

    for i in mo_phone:
        number_list = '-'.join(i)
        phone_num += number_list + '\n'

    with open(file_to_write, 'w+') as pho_file:
        pho_file.write(phone_num)


if __name__ == "__main__":
    file_to_read = './assets/potential-contacts.txt'
    result = valid_phone(file_to_read)
    print(result)
