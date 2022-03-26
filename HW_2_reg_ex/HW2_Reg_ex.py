from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
def get_list_from_phonebook(file_name):
  phonebook = []
  with open(file_name, encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    phonebook.append(contacts_list[0])
    for line in contacts_list[1:]:
      fio = re.findall('\w+', str(line[:3]))
      lastname = fio[0]
      firstname = fio[1]
      if len(fio) > 2:
        surname = fio[2]
      else:
        surname = ''
      tel = re.sub(r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(-|\s*)(\d{3})-*(\d{2})-*(\d{2})\s\(*доб.\s(\d{4})\)*', r'+7(\4)\7-\8-\9 доб.\10', line[5])
      tel = re.sub(r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(-|\s*)(\d{3})-*(\d{2})-*(\d{2})', r'+7(\4)\7-\8-\9', tel)
      new_line = []
      new_line.extend([lastname, firstname, surname, line[3], line[4], tel, line[6]])
      phonebook.append(new_line)
  return phonebook
def get_correction_phonebook():  #корректируем записную книгу, убирая дубли, и записываем в CSV файл
  phonebook = get_list_from_phonebook("phonebook_raw.csv")
  final_phonebook = []
  help_dict = {}  #создаем словарь для хранеия данных по типу Фамилия:Номер списка
  final_phonebook.append(phonebook[0])
  help_dict[phonebook[0][0]] = 0
  n = 0   #счетчик цикла, он же номер списка из phonebook
  for data in phonebook[1:]:
    if data[0] not in help_dict:
      n += 1
      help_dict[data[0]] = n
      final_phonebook.append(data)
    else:
      for i in range(len(data)):
        if data[i] != final_phonebook[help_dict[data[0]]][i]:
          if final_phonebook[help_dict[data[0]]][i] == '':
            final_phonebook[help_dict[data[0]]][i] = data[i]
        else:
          continue
  pprint(final_phonebook)
  with open("phonebook.csv", "w", encoding="utf-8",) as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_phonebook)
if __name__ == '__main__':
  get_correction_phonebook()





