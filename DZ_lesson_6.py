# Задача - 1. В настольной игре Скрабл

word = input()
di_eng = {1:'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
di_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ' }
word_value = 0
for i in word:
    for j in di_eng.values():
        if i.upper() in j:
            for key, value in di_eng.items():
                if value == j:
                    word_value += key
    for j in di_ru.values():
        if i.upper() in j:
            for key, value in di_ru.items():
                if value == j:
                    word_value += key
print(word_value)

# Задача - 2. Email-адреса
# Данные об email-адресах студентов хранятся в словаре:
# Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен.

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
list = []
for i in emails.values():
       for j in i:
              for key, value in sorted(emails.items()):
                     if j in value:
                            a = (j + '@' + key)
                            list.append(a)
list = sorted(list)
for i in list:
       print(i)
