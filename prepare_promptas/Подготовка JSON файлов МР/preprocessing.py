import json
from pprint import pprint

from models import *

with open("all.json", "r", encoding="utf-8") as file:
    load_dict = json.load(file)

obj_from_json = ObJFromJsonBftPlatform(load_dict)

data_model = obj_from_json.get_data_model()
edit_form = obj_from_json.get_edit_form()

result_rows = []

filter_list_type = ['Col', 'Row']
filter_row_with_fields = ['deleteCascadeEnable',]

def data_in_node(node_dict, number=""):
    pos = 0
    for node in node_dict:
        if len(node.keys()) == 1: break
        type_node = node.get('type')
        pos += 1
        print_node_row = {}
        list_node_for_recursion = []
        # если объект то проверяем наличие полей фильтруемых
        use_obj = True
        if type(node_dict):
            use_obj = not(True in list(map(lambda x: x in node.keys(), filter_row_with_fields)))


        if number:
            num_str = f'{number}.{pos}'
        else:
            num_str = f'{pos}'
        if type_node in filter_list_type and use_obj:
            num_str = number
        print_node_row['number'] = num_str
        for key, value in node.items():
            if type(value) not in [list, dict]:
                print_node_row[key] = value
            if type(value) in [list, dict]:
                list_node_for_recursion.append(value if type(value) == list else [value, ])
        # Выводим только поля с атрибутами
        if type_node not in filter_list_type and use_obj:
            result_rows.append(print_node_row)
        # print('-----------------------------------------------')
        for item in list_node_for_recursion:
            data_in_node(item, num_str)


data_in_node(edit_form)
print(*result_rows, sep='\n')

# data_in_node([data_model, ])
# print(*result_rows, sep='\n')


# pprint(
#     edit_form, indent=1
# )
