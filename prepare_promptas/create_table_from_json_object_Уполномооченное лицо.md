Ты системный аналитик. Пиши ответ согласно инструкции. Придерживайся выводимой структур и формата предоставления ответа.
Формат входной информации:
Тебе передан в анализ json-файл описания сложного объекта приложения low-code платформы.

```json
{
    "rules": [],
    "actions": [],
    "objects": [],
    "editForm": {
        "layout": {
            "maxWidth": 1904,
            "minWidth": 1904,
            "maxHeight": 1008,
            "minHeight": 1008,
            "verticalLayout": true
        },
        "components": [
            {
                "name": "formSections",
                "type": "FormSections",
                "children": [
                    {
                        "name": "mainSection",
                        "type": "FormSection",
                        "title": "Основные сведения",
                        "children": [
                            {
                                "name": "row612",
                                "type": "Row",
                                "gutter": 8,
                                "children": [
                                    {
                                        "name": "col1512",
                                        "type": "Col",
                                        "children": [
                                            {
                                                "name": "details1",
                                                "type": "Details",
                                                "title": "Основыне сведения",
                                                "compact": true,
                                                "bordered": true,
                                                "children": [
                                                    {
                                                        "name": "row1",
                                                        "type": "Row",
                                                        "gutter": 8,
                                                        "children": [
                                                            {
                                                                "name": "col1",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "lastNameField",
                                                                        "rows": 2,
                                                                        "type": "TextField",
                                                                        "label": "Фамилия",
                                                                        "maxRows": 2,
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "secondName",
                                                                        "verticalLayout": true
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "col3",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "firstNameField",
                                                                        "rows": 2,
                                                                        "type": "TextField",
                                                                        "label": "Имя",
                                                                        "maxRows": 2,
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "firstName",
                                                                        "verticalLayout": true
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "col5",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "patronymicField",
                                                                        "rows": 2,
                                                                        "type": "TextField",
                                                                        "label": "Отчество",
                                                                        "maxRows": 2,
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "patronymic",
                                                                        "verticalLayout": true
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "row2",
                                                        "type": "Row",
                                                        "gutter": 8,
                                                        "children": [
                                                            {
                                                                "name": "col7",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "snilsField",
                                                                        "rows": 2,
                                                                        "type": "TextField",
                                                                        "label": "СНИЛС",
                                                                        "maxRows": 2,
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "snils",
                                                                        "verticalLayout": true
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "col8",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "jobTitleField",
                                                                        "rows": 2,
                                                                        "type": "TextField",
                                                                        "label": "Должность",
                                                                        "maxRows": 2,
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "position",
                                                                        "verticalLayout": true
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "col10",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "emailField",
                                                                        "rows": 2,
                                                                        "type": "TextField",
                                                                        "label": "Электронная почта",
                                                                        "maxRows": 2,
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "email",
                                                                        "verticalLayout": true
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "row3",
                                                        "type": "Row",
                                                        "gutter": 8,
                                                        "children": [
                                                            {
                                                                "name": "col11",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "textField1",
                                                                        "rows": 2,
                                                                        "type": "TextField",
                                                                        "label": "Номер телефона",
                                                                        "maxRows": 2,
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "phone"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "row4",
                                                        "type": "Row",
                                                        "gutter": 8,
                                                        "children": [
                                                            {
                                                                "name": "col12",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "modifiedField",
                                                                        "type": "TimestampField",
                                                                        "label": "Изменен",
                                                                        "children": [],
                                                                        "readOnly": true,
                                                                        "required": false,
                                                                        "dataField": "modified"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "col13",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "createdField",
                                                                        "type": "TimestampField",
                                                                        "label": "Создан",
                                                                        "children": [],
                                                                        "readOnly": true,
                                                                        "required": true,
                                                                        "dataField": "created"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "row5",
                                                        "type": "Row",
                                                        "gutter": 8,
                                                        "children": [
                                                            {
                                                                "name": "col14",
                                                                "span": 8,
                                                                "type": "Col",
                                                                "children": [
                                                                    {
                                                                        "name": "isBlockedField",
                                                                        "type": "CheckboxField",
                                                                        "label": "Заблокирован",
                                                                        "children": [],
                                                                        "readOnly": false,
                                                                        "required": true,
                                                                        "dataField": "isBlock",
                                                                        "labelSpan": 1,
                                                                        "labelPosition": "LEFT"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ],
                                                "headerBordered": true
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "formSection1",
                        "type": "FormSection",
                        "title": "Сертификаты",
                        "children": [
                            {
                                "name": "row6",
                                "type": "Row",
                                "gutter": 8,
                                "children": [
                                    {
                                        "name": "col15",
                                        "type": "Col",
                                        "children": [
                                            {
                                                "name": "details2",
                                                "type": "Details",
                                                "title": "Сертификаты",
                                                "compact": true,
                                                "bordered": true,
                                                "children": [
                                                    {
                                                        "name": "asugfPaRecordAttachmentField1",
                                                        "type": "AsugfPaRecordAttachmentField",
                                                        "marks": [
                                                            {
                                                                "mark": {
                                                                    "entity": "Mark",
                                                                    "id": 2,
                                                                    "name": "Документ в формате PDF"
                                                                }
                                                            }
                                                        ],
                                                        "children": [],
                                                        "addAllowed": true
                                                    }
                                                ],
                                                "collapsible": true,
                                                "headerBordered": true
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "formSection2",
                        "type": "FormSection",
                        "title": "МЧД",
                        "children": [
                            {
                                "name": "row61",
                                "type": "Row",
                                "gutter": 8,
                                "children": [
                                    {
                                        "name": "col151",
                                        "type": "Col",
                                        "children": [
                                            {
                                                "name": "details21",
                                                "type": "Details",
                                                "title": "МЧД",
                                                "compact": true,
                                                "bordered": true,
                                                "children": [
                                                    {
                                                        "name": "asugfPaRecordAttachmentField11",
                                                        "type": "AsugfPaRecordAttachmentField",
                                                        "marks": [
                                                            {
                                                                "mark": {
                                                                    "entity": "Mark",
                                                                    "id": 2,
                                                                    "name": "Документ в формате PDF"
                                                                }
                                                            }
                                                        ],
                                                        "children": [],
                                                        "addAllowed": true
                                                    }
                                                ],
                                                "collapsible": true,
                                                "headerBordered": true
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "formSection3",
                        "type": "FormSection",
                        "title": "Полномочия",
                        "children": [
                            {
                                "name": "row611",
                                "type": "Row",
                                "gutter": 8,
                                "children": [
                                    {
                                        "name": "col1511",
                                        "type": "Col",
                                        "children": [
                                            {
                                                "name": "details211",
                                                "type": "Details",
                                                "title": "Полномочия",
                                                "compact": true,
                                                "bordered": true,
                                                "children": [
                                                    {
                                                        "name": "authorityField",
                                                        "type": "TableField",
                                                        "children": [],
                                                        "listForm": {
                                                            "filters": [],
                                                            "cellStyles": [],
                                                            "dataColumns": [
                                                                {
                                                                    "title": "Наименование",
                                                                    "isMask": false,
                                                                    "dataType": "STRING",
                                                                    "sortable": true,
                                                                    "dataField": "name",
                                                                    "filterable": true,
                                                                    "notGroupable": true,
                                                                    "hideFilterOptions": false,
                                                                    "rememberLastValues": false
                                                                },
                                                                {
                                                                    "title": "Действует с",
                                                                    "isMask": false,
                                                                    "dataType": "STRING",
                                                                    "sortable": true,
                                                                    "dataField": "startDateTime",
                                                                    "filterable": true,
                                                                    "notGroupable": true,
                                                                    "hideFilterOptions": false,
                                                                    "rememberLastValues": false
                                                                },
                                                                {
                                                                    "title": "Действует по",
                                                                    "isMask": false,
                                                                    "dataType": "STRING",
                                                                    "sortable": true,
                                                                    "dataField": "endDateTime",
                                                                    "filterable": true,
                                                                    "notGroupable": true,
                                                                    "hideFilterOptions": false,
                                                                    "rememberLastValues": false
                                                                },
                                                                {
                                                                    "title": "Создано",
                                                                    "isMask": false,
                                                                    "dataType": "STRING",
                                                                    "sortable": true,
                                                                    "dataField": "created",
                                                                    "filterable": true,
                                                                    "notGroupable": true,
                                                                    "hideFilterOptions": false,
                                                                    "rememberLastValues": false
                                                                },
                                                                {
                                                                    "title": "Примечание",
                                                                    "isMask": false,
                                                                    "dataType": "STRING",
                                                                    "sortable": true,
                                                                    "dataField": "note",
                                                                    "filterable": true,
                                                                    "notGroupable": true,
                                                                    "hideFilterOptions": false,
                                                                    "rememberLastValues": false
                                                                }
                                                            ],
                                                            "deleteCascadeEnable": false
                                                        },
                                                        "readOnly": false,
                                                        "dataField": "authority",
                                                        "suppressCollapse": true
                                                    }
                                                ],
                                                "collapsible": true,
                                                "headerBordered": true
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "contentWidthMax": 1200,
                "contentWidthMin": 1200
            }
        ]
    },
    "listForm": {
        "filters": [],
        "cellStyles": [],
        "dataColumns": [
            {
                "title": "Наименование",
                "isMask": false,
                "dataType": "STRING",
                "sortable": true,
                "dataField": "name",
                "filterable": true,
                "notGroupable": true,
                "hideFilterOptions": false,
                "rememberLastValues": false
            },
            {
                "title": "Фамилия",
                "isMask": false,
                "dataType": "STRING",
                "sortable": true,
                "dataField": "secondName",
                "filterable": true,
                "notGroupable": true,
                "hideFilterOptions": false,
                "rememberLastValues": false
            },
            {
                "title": "Имя",
                "isMask": false,
                "dataType": "STRING",
                "sortable": true,
                "dataField": "firstName",
                "filterable": true,
                "notGroupable": true,
                "hideFilterOptions": false,
                "rememberLastValues": false
            },
            {
                "title": "Отчество",
                "isMask": false,
                "dataType": "STRING",
                "sortable": true,
                "dataField": "patronymic",
                "filterable": true,
                "notGroupable": true,
                "hideFilterOptions": false,
                "rememberLastValues": false
            },
            {
                "title": "Должность",
                "isMask": false,
                "dataType": "STRING",
                "sortable": true,
                "dataField": "position",
                "filterable": true,
                "notGroupable": true,
                "hideFilterOptions": false,
                "rememberLastValues": false
            }
        ],
        "deleteCascadeEnable": false
    },
    "constUuid": "b9194e66-08c9-4f33-8ff6-12dbcb41821e",
    "dataModel": {
        "isView": false,
        "triggers": [],
        "tableName": "PAAUTHORIZEDPERSONINFO",
        "dataFields": [
            {
                "name": "name",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "required": true,
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Наименование",
                "dataConstraint": {
                    "inputMaskChars": []
                },
                "hideFilterOptions": false
            },
            {
                "name": "authorizedPersonDoc",
                "static": true,
                "children": [],
                "dataType": "REFERENCE",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Уполномоченные лица",
                "refAppObject": {
                    "entity": "AppObject",
                    "id": "pa.authorizedPersonList",
                    "displayName": "Список уполномоченных лиц"
                },
                "dataConstraint": {
                    "inputMaskChars": []
                },
                "hideFilterOptions": false
            },
            {
                "name": "authority",
                "static": true,
                "children": [],
                "dataType": "REFLIST",
                "fetchMode": "NORMAL",
                "displayName": "Полномочия",
                "refAppObject": {
                    "entity": "AppObject",
                    "id": "pa.authority",
                    "displayName": "Полномочия"
                },
                "dataConstraint": {},
                "hideFilterOptions": false
            },
            {
                "name": "secondName",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Фамилия",
                "dataConstraint": {
                    "inputMaskChars": []
                },
                "hideFilterOptions": false
            },
            {
                "name": "firstName",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Имя",
                "dataConstraint": {
                    "inputMaskChars": []
                },
                "hideFilterOptions": false
            },
            {
                "name": "patronymic",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Отчество",
                "dataConstraint": {
                    "inputMaskChars": []
                },
                "hideFilterOptions": false
            },
            {
                "name": "snils",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "СНИЛС",
                "dataConstraint": {},
                "hideFilterOptions": false
            },
            {
                "name": "position",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Должность",
                "dataConstraint": {
                    "inputMaskChars": []
                },
                "hideFilterOptions": false
            },
            {
                "name": "email",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Электронная почта",
                "dataConstraint": {},
                "hideFilterOptions": false
            },
            {
                "name": "isBlock",
                "static": true,
                "children": [],
                "dataType": "BOOLEAN",
                "required": true,
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Заблокирован",
                "defaultValue": false,
                "dataConstraint": {},
                "defaultValueMode": "CONST",
                "hideFilterOptions": false
            },
            {
                "name": "phone",
                "static": true,
                "children": [],
                "dataType": "STRING",
                "fetchMode": "NORMAL",
                "calculated": false,
                "displayName": "Номер телефона",
                "dataConstraint": {},
                "hideFilterOptions": false
            }
        ],
        "displayName": {
            "displayFields": "secondName"
        },
        "displayTooltip": {},
        "dataFieldGroups": [],
        "validationRules": [],
        "isFullTextSearch": false,
        "greenplumReplicatedOption": true
    },
    "editForms": [],
    "extProperties": {
        "properties": []
    },
    "dictNativeKeys": [],
    "reportTemplates": [],
    "signedDataSetting": []
}
```

Формат выходной таблицы:
Необходимо вывести описание структуры в табличном виде со следующими столбцами:
Условный номер поля, Наименование поля/элемента, Атрибут, Формат атрибута, Размерность поля, Обязательность поля,
Описание, Примечание.
Основная часть структуры таблицы задается описание компонентов в теге components в элементе "editForm" со следующими
правилами:

1. Элемент с типом в поле "type" указанным "FormSection" выводится в отдельной строке таблицы с названием из "title" с
   использованием следующего шаблона "Блок полей "{{title}}"". Элемент является группирующий и должен иметь группирующий
   порядковый номер, который будет использоваться для вывода дочерних элементов.
2. Вложенные элементы "type" со значением "Details" выводятся в отдельной строке таблицы с названием из "title" с
   использованием следующего шаблона "Блок полей "{{title}}""
3. Далее выводить описание полей в строку, описанные во вложенных объектах, учитывая следующие правила:
   3.1 Если поле имеет тип "type"="ReferenceField", то наименование поля брать из элемента "label", а имя атрибута из "
   displayField".
   3.2 Если поле имеет тип "type" предназначено для конкретных типов данных (текстовое поле, числовое, дата, дата/время
   и т.д.), то наименование поля принимается из "label", а наименование атрибута из "dataField". Если значение в поле
   получается через ссылку на другой объект, то показать имя поля в формате "Ссылка:{{dataField}}"
4. Формат атрибута определи в зависимости от ожидаемого формата в поле "type" согласно рекомендациям следующего json:

```json
[
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (integer)",
    "Описание": "Отрицательное или положительное целое число от -2147483648 до +2147483647",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (positiveinteger)",
    "Описание": "Положительное целое число",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (negativeinteger)",
    "Описание": "Отрицательное целое число",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (nonpositiveinteger)",
    "Описание": "Нуль или отрицательное целое число",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (nonnegativeinteger)",
    "Описание": "Нуль или положительное целое число",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (long)",
    "Описание": "64-битовое целое число со знаком",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (short)",
    "Описание": "16-битовое целое число со знаком",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (decimal)",
    "Описание": "Число, содержащее дробную часть",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (float)",
    "Описание": "Число с плавающей запятой стандартной точности",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (double)",
    "Описание": "Число с плавающей запятой двойной точности",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Числовой",
    "Форматы": "Числовой (numeric)",
    "Описание": "Вещественное число с фиксированной точностью, которая настраивается в параметрах точность (m) (общее количество цифр) и масштаб (n) (количество цифр после запятой). Этот тип применяется для чисел, где важна точность, например для хранения денежных сумм.",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Текстовый",
    "Форматы": "Текстовый (string)",
    "Описание": "Символьная строка переменной длины",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Текстовый",
    "Форматы": "Строка (varchar)",
    "Описание": "Строка переменной длины, которая настраивается в параметре (n), но не длиннее (n).",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Текстовый",
    "Форматы": "Строка (text)",
    "Описание": "Строка неограниченной и переменной длины",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Время",
    "Форматы": "Время (time)",
    "Описание": "Время дня (часы/минуты/секунды/миллисекунды)",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Время",
    "Форматы": "Дата/Время (DateTime)",
    "Описание": "День и время (эквивалент SQL-типа TIMESTAMP)",
    "Размерность": "всегда =19 знаков"
  },
  {
    "Тип данных ЧТЗ": "Время",
    "Форматы": "Дата (date)",
    "Описание": "Год/месяц/день",
    "Размерность": "всегда =10 знаков"
  },
  {
    "Тип данных ЧТЗ": "Время",
    "Форматы": "Время (Timestamp)",
    "Описание": "Дата и время",
    "Размерность": "всегда =19 знаков"
  },
  {
    "Тип данных ЧТЗ": "Логический",
    "Форматы": "Логический тип (boolean)",
    "Описание": "Значение TRUE/FALSE",
    "Размерность": "всегда =1 знак"
  },
  {
    "Тип данных ЧТЗ": "Данные",
    "Форматы": "Данные (byte)",
    "Описание": "Один байт данных со знаковым битом",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Данные",
    "Форматы": "Данные (base64Binary)",
    "Описание": "Двоичные данные по основанию 64",
    "Размерность": "разная"
  },
  {
    "Тип данных ЧТЗ": "Идентификатор",
    "Форматы": "Идентификатор (uuid)",
    "Описание": "128-битное значение, генерируемое специальным алгоритмом. Записывается в виде 32 шестнадцатеричных цифр, разделённых на несколько групп.",
    "Размерность": "разная"
  }
]
```

5. Размерность поля при отображении на экранной форме определи самостоятельно в зависимости от типа данных или
   назначения поля, если его длинна может быть тобой определена исходя из его назначения.
   При этом учитывай следующее:

```
− Ограничение количества символов в поле ЭФ. 
− При описании полей с плавающими значениями перед максимальным значением количества допустимых символов на ЭФ добавлять знак «<» (меньше) либо «<=» (меньше равно)
− Ставить «б/о» (без ограничений) если поле неограниченной длины (адаптивное).
− Ставить «−» для интерактивных элементов.
- Также используй рекомендуемые ограничения для следующих полей:
УНК: <=6
Код МР: <=10
Код СР (или сводного реестра): <=10
```

6. Поле "Обязательность заполнения" заполнять учитывая следующующее:

```
− Ставить «Да», если поле обязательно для заполнения!!!!
− Ставить «Нет».
− Ставить «−» для интерактивных элементов.
```

7. В колонку "Описание" выводи информацию о поле, учитывая следующие рекомендации к содержанию:

```
1.Название поля, если есть или атрибута:
− обязательно русское название атрибута/поля/ элемента пользовательского интерфейса
- название поля показывается без указания типа - поле, элемент и т.д. 
2.Правило заполнения поля/атрибута (только для поля /атрибута)
Варианты описания:
− «Заполняется вручную».
− «Заполняется вручную выбором значений из ___» (справочника и пр.).
− «Заполняется автоматически значением, рассчитанным как ___, (описание формулы). Заполняется при ____ (описание события)».
− «Заполняется автоматически значением атрибута ЭД ____ (название ЭД). Заполняется при ____ (описание события)».
− «Заполняется автоматически значением элемента/атрибута элемента ____ (название элемента/атрибута элемента) файла формата ___ (название формата файла) ЭД ____ (название ЭД), полученного из ___ (наименование внешней системы) /загруженного при ____ (описание события)».
− «Заполняется автоматически значением поля ___ (название поля) блока ____ (название блока при наличии) вкладки ____ (название вкладки при наличии) ЭФ ____ (название ЭФ)» (при заполнении атрибута из поля ЭФ).
3.Редактирование атрибута (только для поля /атрибута)
− «Доступно/недоступно для редактирования» (расписать правило при наличии особенностей доступности к редактированию)
4.Предназначение элемента (только для элементов пользовательского интерфейса)
5.Условие (-я) отображения поля/элемента (только для полей/элементов пользовательского интерфейса) при наличии. 
```

8. В колонке "Примечание" описание выводи ключевые свойства поля, которые позволяет однозначно его идентифицировать в
   системе. Добавляй исходный фрагмент json струкутры для поля в блоке кода.
9. Если дочерний элемент имеет "type" = "TableField", то вывести одной строкой наименование в формате "Табличная часть".
   Наименование поля принять по значению элемента "title" а имя атрибута по данным "dataField". Формат поля определить
   по рекомендациям выше.
10. Табличную часть заполнить описанием полей в соответствии с рекомендациями выше. 

