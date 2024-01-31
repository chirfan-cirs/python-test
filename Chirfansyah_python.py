full_name = "CHIRFANSYAH"
email = "Chirfansyah2@gmail.com"

CleansingPhoneNumber = "Test 1"

# def clean_phone_number(phone):
#     '''
#     Function to clean the phone number
#
#     Parameters
#     ----------
#     phone : list
#         The raw sample of phone data
#
#     Returns
#     -------
#     phone_clean : list
#         The clean sample of phone data
#     '''
#
#     phone_clean = []
#     for num in phone:
#         num = ''.join(filter(str.isdigit, num.replace(' ', '')))
#
#         if num.startswith('0'):
#             num = '62' + num[1:]
#
#         if not num.startswith('62'):
#             num = '62' + num
#
#         if 11 <= len(num) <= 14:
#             phone_clean.append(num)
#         else:
#             phone_clean.append('Invalid number')
#     return phone_clean
#
#
# # Test Case 1
# phone = [
#     '82123321123',
#     '082321123321',
#     '+6282-456-654-456',
#     '+62 82 789 987 789',
#     '14045',
#     '82145-451-145'
# ]
#
# phone_clean = clean_phone_number(phone)
# print(phone_clean)


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


CalculateTstatistics = "Test 2"

# def calculate_t_statistics(n, avg1, avg2, sd):
#     sp = sd/(n ** 0.5)
#     t = (avg1 - avg2) / (sp*(2 ** 0.5))
#     return t



oop = "Test 3"

class Data:
    def __init__(self):
        self.data = []
        self.size = 0

    def read_data(self, data):
        self.data = data
        self.size = len(data)

    def find_total(self):
        return sum(self.data)

    def find_average(self):
        return sum(self.data) / self.size

# # Test Case 1
# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_data = Data()
# my_data.read_data(data)
# print(my_data.data)
# print(my_data.size)
# print(my_data.find_total())
# print(my_data.find_average())


# # Test Case 2
# data = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# my_data = Data()
# my_data.read_data(data)
# print(my_data.data)
# print(my_data.size)
# print(my_data.find_total())
# print(my_data.find_average())