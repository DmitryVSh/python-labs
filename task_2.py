# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, delimiter=","):
    set_str1 = set(str1.split(delimiter))
    set_str2 = set(str2.split(delimiter))

    common_participants = sorted(set_str1 & set_str2)
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

# Проверка функции с разделителем "|"
common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")

# Вывод результата
print("Общие участники:", common)
