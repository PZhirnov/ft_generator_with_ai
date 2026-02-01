from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field, validator, field_validator
from datetime import datetime, date

# Модель для компонента формы
class Component(BaseModel):
    type: str = Field(..., description="Тип компонента (input, select, checkbox, etc.)")
    name: str = Field(..., description="Имя компонента (должно соответствовать полю в dataModel)")
    label: str = Field(..., description="Отображаемое название поля")
    required: Optional[bool] = Field(False, description="Обязательность заполнения")
    options: Optional[List[Dict[str, Any]]] = Field(None, description="Опции для select, radio и т.д.")
    validation: Optional[Dict[str, Any]] = Field(None, description="Правила валидации")
    props: Optional[Dict[str, Any]] = Field(None, description="Дополнительные свойства компонента")

    @field_validator('type')
    def validate_type(cls, v):
        allowed_types = ['text', 'number', 'email', 'password', 'textarea', 
                        'select', 'checkbox', 'radio', 'date', 'file', 'hidden']
        if v not in allowed_types:
            raise ValueError(f'Тип компонента должен быть одним из: {allowed_types}')
        return v

# Модель для формы редактирования/создания
class EditForm(BaseModel):
    title: str = Field(..., description="Заголовок формы")
    components: List[Component] = Field(..., description="Список компонентов формы")
    layout: Optional[str] = Field('vertical', description="Расположение элементов (vertical, horizontal)")
    submit_text: Optional[str] = Field('Сохранить', description="Текст кнопки отправки")
    cancel_text: Optional[str] = Field('Отмена', description="Текст кнопки отмены")
    width: Optional[str] = Field('100%', description="Ширина формы")

    @field_validator('layout')
    def validate_layout(cls, v):
        if v not in ['vertical', 'horizontal', 'grid']:
            raise ValueError('Layout должен быть vertical, horizontal или grid')
        return v

# Модель для формы списка
class ListForm(BaseModel):
    columns: List[Dict[str, Any]] = Field(..., description="Колонки таблицы")
    page_size: Optional[int] = Field(10, ge=1, le=100, description="Количество элементов на странице")
    searchable: Optional[bool] = Field(True, description="Возможность поиска")
    sortable: Optional[bool] = Field(True, description="Возможность сортировки")
    actions: Optional[List[Dict[str, Any]]] = Field(None, description="Действия (редактировать, удалить и т.д.)")
    filters: Optional[List[Dict[str, Any]]] = Field(None, description="Фильтры для списка")

    @field_validator('columns')
    def validate_columns(cls, v):
        if not v:
            raise ValueError('Список колонок не может быть пустым')
        for column in v:
            if 'field' not in column or 'header' not in column:
                raise ValueError('Каждая колонка должна содержать field и header')
        return v

# Модель для поля dataModel
class FieldModel(BaseModel):
    type: str = Field(..., description="Тип данных поля")
    required: Optional[bool] = Field(False, description="Обязательность поля")
    default: Optional[Any] = Field(None, description="Значение по умолчанию")
    max_length: Optional[int] = Field(None, ge=0, description="Максимальная длина для строк")
    min_value: Optional[Union[int, float]] = Field(None, description="Минимальное значение для чисел")
    max_value: Optional[Union[int, float]] = Field(None, description="Максимальное значение для чисел")
    pattern: Optional[str] = Field(None, description="Регулярное выражение для валидации строк")
    enum: Optional[List[Any]] = Field(None, description="Допустимые значения")

    @field_validator('type')
    def validate_field_type(cls, v):
        allowed_types = ['string', 'integer', 'float', 'boolean', 'date', 
                        'datetime', 'array', 'object', 'email']
        if v not in allowed_types:
            raise ValueError(f'Тип поля должен быть одним из: {allowed_types}')
        return v

# Основная модель
class ApplicationModel(BaseModel):
    editForm: EditForm = Field(..., description="Форма редактирования/создания записи")
    listForm: ListForm = Field(..., description="Форма отображения списка записей")
    dataModel: Dict[str, FieldModel] = Field(..., description="Модель данных")
    components: Optional[List[Component]] = Field(None, description="Дополнительные компоненты")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Дополнительные метаданные")
    version: Optional[str] = Field('1.0.0', description="Версия конфигурации")

    @field_validator('dataModel')
    def validate_data_model_consistency(cls, v, values):
        """Проверка согласованности dataModel с компонентами форм"""
        if 'editForm' in values:
            edit_form = values['editForm']
            for component in edit_form.components:
                if component.name not in v:
                    raise ValueError(f'Компонент {component.name} отсутствует в dataModel')
        return v

    class Config:
        schema_extra = {
            "example": {
                "editForm": {
                    "title": "Создание пользователя",
                    "components": [
                        {
                            "type": "text",
                            "name": "username",
                            "label": "Имя пользователя",
                            "required": True
                        }
                    ]
                },
                "listForm": {
                    "columns": [
                        {"field": "id", "header": "ID"},
                        {"field": "username", "header": "Имя пользователя"}
                    ]
                },
                "dataModel": {
                    "username": {
                        "type": "string",
                        "required": True,
                        "max_length": 50
                    }
                }
            }
        }
