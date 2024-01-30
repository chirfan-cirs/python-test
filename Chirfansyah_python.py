full_name = "CHIRFANSYAH"
email = "Chirfansyah2@gmail.com"


def clean_phone_number(phone):
    '''
    Function to clean the phone number

    Parameters
    ----------
    phone : list
        The raw sample of phone data

    Returns
    -------
    phone_clean : list
        The clean sample of phone data
    '''

    phone_clean = []
    for num in phone:
        num = ''.join(filter(str.isdigit, num))
        if len(num) == 11 or num.startswith('62'):
            phone_clean.append(num)
        else:
            phone_clean.append('Invalid number')
    return phone_clean


# Test Case 1
phone = [
    '82123321123',
    '082321123321',
    '+6282-456-654-456',
    '+62 82 789 987 789',
    '14045',
    '82145-451-145'
]

phone_clean = clean_phone_number(phone)
print(phone_clean)

#
# #Test Case 2
# phone = [
#     '82432234432',
#     '+62 82 32',
#     '14032',
#     '082 234 432 234'
# ]
#
# phone_clean = clean_phone_number(phone)
# print(phone_clean)
