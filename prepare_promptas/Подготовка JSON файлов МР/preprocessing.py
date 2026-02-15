import json
import csv
from pprint import pprint
from pathlib import Path

from pydantic_core.core_schema import model_schema

from models import *
from utils import *

# Файл для обработки
file_name = "260215_ALL_MOSREESTR.json"
file_dir = "data"
path_file_input = Path(file_dir, file_name)

# Файл с результатами
file_result_edit_form = f"[edit_form]_{file_name.replace('.', '_')}.csv"
file_result_data_model = f"[data_model]_{file_name.replace('.', '_')}.csv"
file_result_dir = "results"
path_file_output_edit_form = Path(file_result_dir, file_result_edit_form)
path_file_output_data_model = Path(file_result_dir, file_result_data_model)

# Структура данных
model_schema_dict = {
    "edit_form": RowInResultTableForScreenForm,
    "data_model": RowInResultTableForDataModel
}


with open(path_file_input, "r", encoding="utf-8") as file:
    load_dict = json.load(file)

obj_from_json = ObJFromJsonBftPlatform(load_dict)

data_model = obj_from_json.get_data_model()
edit_form = obj_from_json.get_edit_form()

result_rows = []

filter_list_type = ['Col', 'Row', 'Spacer']
filter_row_with_fields = ['deleteCascadeEnable', ]


def data_in_node(select_model, node_dict, number=""):
    select_obj_model_for_data_in_row = model_schema_dict.get(select_model)
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
            use_obj = not (True in list(map(lambda x: x in node.keys(), filter_row_with_fields)))

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
            result_rows.append(select_obj_model_for_data_in_row(print_node_row))
        for item in list_node_for_recursion:
            data_in_node(select_model, item, num_str)





print('---------- ДАННЫЕ EDIT_FORM ---------------------')
data_in_node(select_model='edit_form', node_dict=edit_form)
print(*result_rows, sep='\n')
save_to_csv(path_file_output=path_file_output_edit_form, result_rows=result_rows)

print('---------- ДАННЫЕ DATA_MODEL ---------------------')
result_rows = []
data_in_node(select_model='data_model', node_dict=[data_model, ])
print(*result_rows, sep='\n')
save_to_csv(path_file_output=path_file_output_data_model, result_rows=result_rows)
