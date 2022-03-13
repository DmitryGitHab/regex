# читаем адресную книгу в формате CSV в список contacts_list
import csv
from pprint import pprint
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list[1])

class People:
    instances = []

    def __init__(self, first_name, second_name, third_name='', phone=''):
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name
        self.phone = phone
        self.__class__.instances.append(self)

    def __str__(self):
        return (f'Фамилия: {self.first_name}\nИмя: {self.second_name}\n'
                f'Отчество: {self.third_name}\nТелефон: {self.phone}')

# TODO 1: выполните пункты 1-3 ДЗ


people_list = People.instances


pattern_phone = r'(8|\+7)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_phone = r'+7(\2)\3-\4-\5 \6\7'
pattern_FCs = r'^(\w+)[,\s]?(\w+)(,|\s)?(\w+)?'
sub_FCs = r"\1,\2,\4"


new_contacts_list = []
for i in contacts_list:
    line = ','.join(i[0:3])
    true_name = re.sub(pattern_FCs, sub_FCs, line)
    true_phone = re.sub(pattern_phone, sub_phone, i[5])
    result = true_name.split(',') + true_phone.split(',')
    new_contacts_list.append(result)

check_list = []
for i in range(len(new_contacts_list)):
    temp_list = [new_contacts_list[i][0], new_contacts_list[i][1]]
    # print(temp_list)
    if i == 0:
        man_name = 'man_' + str(i)
        globals()[man_name] = People(first_name=new_contacts_list[i][0], second_name=new_contacts_list[i][1],
                                     third_name=new_contacts_list[i][2], phone=new_contacts_list[i][-1])
        # print('has been added => ' + man_name)
        check_list.append(temp_list)

    if temp_list in check_list:
        pass
    else:
        man_name = 'man_' + str(i)
        globals()[man_name] = People(first_name=new_contacts_list[i][0], second_name=new_contacts_list[i][1],
                                     third_name=new_contacts_list[i][2], phone=new_contacts_list[i][-1])
        # print('has been added => ' + man_name)
        check_list.append(temp_list)


contacts_list = []
print(people_list)
for i in people_list:
    new_list = [i.first_name, i.second_name, i.third_name, i.phone]
    contacts_list.append(new_list)
print(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)



# if __name__ == '__main__':
#     # print('PyCharm')