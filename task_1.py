# TODO Напишите функцию для поиска индекса товара
def find_item_index(items_list, item):
    try:
        # индекс первого вхождения элемента
        return items_list.index(item)
    except ValueError:
        # Если товар не найден в списке
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
