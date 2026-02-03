from core.models.json_schema import ApplicationModel
from pydantic import BaseModel, Field, ValidationError, ConfigDict

# Пример JSON данных
json_data = {
    "editForm": {
        "title": "Создание задачи",
        "components": [
            {
                "type": "text",
                "name": "title",
                "label": "Заголовок задачи",
                "required": True
            },
            {
                "type": "textarea",
                "name": "description",
                "label": "Описание",
                "required": False
            },
            {
                "type": "select",
                "name": "status",
                "label": "Статус",
                "options": [
                    {"value": "pending", "label": "В ожидании"},
                    {"value": "in_progress", "label": "В процессе"},
                    {"value": "completed", "label": "Завершено"}
                ]
            }
        ]
    },
    "listForm": {
        "columns": [
            {"field": "id", "header": "ID"},
            {"field": "title", "header": "Заголовок"},
            {"field": "status", "header": "Статус"}
        ],
        "page_size": 20,
        "actions": [
            {"name": "edit", "label": "Редактировать"},
            {"name": "delete", "label": "Удалить"}
        ]
    },
    "dataModel": {
        "title": {
            "type": "string",
            "required": True,
            "max_length": 100
        },
        "description": {
            "type": "string",
            "required": False,
            "max_length": 500
        },
        "status": {
            "type": "string",
            "enum": ["pending", "in_progress", "completed"]
        }
    }
}

# Валидация данных
try:
    model = ApplicationModel(ConfigDict(json_schema_extra=json_data))
    print("Данные валидны!")
except Exception as e:
    print(f"Ошибка валидации: {e}")
