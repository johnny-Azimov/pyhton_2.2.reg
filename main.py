from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

#TODO 1: выполните пункты 1-3 ДЗ
# ваш код
result = {}
name_pattern = re.compile(r'(^[А-ЯЁ][а-яё]*)\s?\,?(([А-Я][а-яё]*)\s?\,?([А-Я][а-яё]*)?)\,?$')
phone_pattern = re.compile(r'(\+7|8)\s?\(?(495|812)\)?\-?\s?(\d{3})\-?(\d{2})\-?(\d{2})(\s?\(?(доб.)\s?(\d+)\)?)?')

name_sub = r'\1,\3,\4,'
key_sub = r'\1,\3'
phone_sub = r' +7(\2)\3-\4-\5 \6\7'
keys = contacts_list[0]

for item in contacts_list[1:]:
        name = name_pattern.sub(name_sub, ''.join(item[:2])).split(',')
        item[0] = name[0]
        item[1] = name[1]
        item[2] = name[2]
        item[5] = phone_pattern.sub(phone_sub, item[5])
        key = (item[1], item[0])
        data = result.setdefault(key, {
        })
        count = 0
        for elem in keys:
            data[elem] = data.get(elem) or item[count]
            result[key] = data
            count += 1

#TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf8') as f:
  datawriter = csv.writer(f, delimiter=',', lineterminator='\n\n')
  datawriter.writerows(elem.values() for elem in result.values())
  # Вместо contacts_list подставьте свой список
  datawriter.writerows([keys])
