import json
from tkinter.font import names
from typing import Optional, Dict, Any, List

# Типы данных в поле
data_type_dict = {
    'DateField': 'Дата/Время',
    'Date': 'Дата',
    'TextField': 'Текстовый',
    'NumberField': 'Числовой',
    'CheckboxField': 'Логический',
    'Other': 'Текстовый'
}


class ObJFromJsonBftPlatform:
    data_model: Dict[str, Any] = {}
    edit_form: List[Dict[str, Any]] = []

    def __init__(self, json_data: Dict[str, Any]):
        self.json_data: Dict[str, Any] = json_data

    def get_data_model(self):
        self.data_model = self.json_data['dataModel']
        return self.data_model

    def get_edit_form(self):
        self.edit_form = self.json_data['editForm']['components']
        return self.edit_form


class RowInResultTableForScreenForm:
    def __init__(self, row: Dict[str, Any]):
        self.row = row
        self.number = row['number']
        self.required_field = '-'
        self.data_type = '-'
        # задаем имя поля по label или title для записей табличной части
        name_field_from_row = '-'
        if row.get('label'):
            name_field_from_row = row['label']
        if row.get('title'):
            name_field_from_row = row['title']
        name_for_type_row_dict = {
            "FormSections": "Основное окно ЭФ",
            "FormSection": "Вкладка",
            "FormTable": "Табличная часть",
            "Details": "Раздел",
            "FieldGroup": "Группа полей"
        }
        self.type_row_name = name_for_type_row_dict.get(row.get('type'))
        if self.type_row_name:
            name_field_from_row = f'{self.type_row_name} {f"{chr(34)}{row.get('title')}{chr(34)}" if row.get('title') else ""}'
        else:
            self.type_row_name = 'Поле'
            self.required_field = "Да" if row.get('required') else "Нет"
            self.data_type = data_type_dict.get(row.get('type')) if row.get('type') else '-'
        self.name_field = name_field_from_row
        self.system_field_name = row.get('dataField') if row.get('dataField') else '-'

    def __str__(self):
        return f'{self.number}|{self.type_row_name}|{self.name_field}|{self.system_field_name}|{self.data_type}|-|{self.required_field}|!!ToDo: Добавить описание|{json.dumps(self.row, ensure_ascii=False)}'


data_type_data_model_dict = {
    'DATE': 'Дата',
    'STRING': 'Текстовый',
    'INT': 'Числовой',
    'BOOLEAN': 'Логический',
    'REFERENCE': 'Ссылка на ОП',
    'ATTACH': 'Приложенный файл',
    'OTHER': 'Текстовый'
}


class RowInResultTableForDataModel:
    def __init__(self, row: Dict[str, Any]):
        self.row = row
        self.number = row['number']
        self.required_field = '-'
        self.data_type = '-'
        # задаем имя поля по label или title для записей табличной части
        name_field_from_row = '-'
        if row.get('displayName'):
            name_field_from_row = row['displayName']

        name_for_type_row_dict = {
            "LIST": "Вложенный список",
        }
        self.type_row_name = name_for_type_row_dict.get(row.get('dataType'))
        if self.type_row_name:
            name_field_from_row = f'{self.type_row_name} {f"{chr(34)}{row.get('displayName')}{chr(34)}" if row.get('displayName') else ""}'
        else:
            self.type_row_name = 'Поле'
            self.required_field = "Да" if row.get('required') else "Нет"
            self.data_type = data_type_data_model_dict.get(row.get('dataType')) if row.get('dataType') else '-'
        self.name_field = name_field_from_row
        self.system_field_name = row.get('name') if row.get('name') else '-'

    def __str__(self):
        return f'{self.number}|{self.type_row_name}|{self.name_field}|{self.system_field_name}|{self.data_type}|-|{self.required_field}|!!ToDo: Добавить описание|{json.dumps(self.row, ensure_ascii=False)}'
