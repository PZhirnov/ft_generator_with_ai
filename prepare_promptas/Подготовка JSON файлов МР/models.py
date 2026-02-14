from typing import Optional, Dict, Any, List


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
        self.number = round(row['number'])
        self.display_name_field_on_screen = row['label']
        self.system_field_name = row['dataField']





