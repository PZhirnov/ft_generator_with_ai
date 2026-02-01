Ты системный аналитик. Пиши ответ согласно инструкции. Придерживайся выводимой структур и формата предоставления ответа.
Формат входной информации:
Тебе передан в анализ json-файл описания сложного объекта приложения low-code платформы.

```json
{
  "editForm": {
    "layout": {
      "verticalLayout": true
    },
    "components": [
      {
        "name": "formSection1",
        "type": "FormSection",
        "style": "{justify-content: center}",
        "title": "Свойства документа",
        "children": [
          {
            "name": "details1",
            "type": "Details",
            "style": "{width:70%; margin-left: 15%}\n",
            "title": "Общие сведения",
            "compact": true,
            "bordered": true,
            "children": [
              {
                "name": "row17",
                "type": "Row",
                "gutter": 8,
                "children": [
                  {
                    "name": "col21",
                    "type": "Col",
                    "children": [
                      {
                        "name": "subjectFullNameField",
                        "type": "ReferenceField",
                        "label": "Клиент",
                        "readOnly": false,
                        "dataField": "subject",
                        "addAllowed": true,
                        "fetchFields": "fullName,inn,cpp,mosCode,unc,srpsCode",
                        "displayField": "fullName",
                        "refAppObject": {
                          "entity": "AppObject",
                          "id": "reference.subject",
                          "displayName": "Экономические субъекты"
                        },
                        "refreshAllowed": false,
                        "onlySystemFilters": false
                      }
                    ]
                  }
                ]
              },
              {
                "name": "row18",
                "type": "Row",
                "gutter": 8,
                "children": [
                  {
                    "name": "col22",
                    "span": 8,
                    "type": "Col",
                    "children": [
                      {
                        "name": "clientINNField",
                        "rows": 2,
                        "type": "TextField",
                        "label": "ИНН",
                        "maxRows": 2,
                        "readOnly": true,
                        "dataField": "subject.inn"
                      }
                    ]
                  },
                  {
                    "name": "col23",
                    "span": 8,
                    "type": "Col",
                    "children": [
                      {
                        "name": "clientKPPField",
                        "rows": 2,
                        "type": "TextField",
                        "label": "КПП",
                        "maxRows": 2,
                        "readOnly": true,
                        "dataField": "subject.cpp"
                      }
                    ]
                  },
                  {
                    "name": "col41",
                    "span": 8,
                    "type": "Col",
                    "children": [
                      {
                        "name": "row20",
                        "type": "Row",
                        "children": [
                          {
                            "name": "textField3",
                            "rows": 2,
                            "type": "TextField",
                            "label": "ОГРН",
                            "maxRows": 2,
                            "disabled": false,
                            "readOnly": true
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "name": "row19",
                "type": "Row",
                "gutter": 8,
                "children": [
                  {
                    "name": "col39",
                    "span": 8,
                    "type": "Col",
                    "children": [
                      {
                        "name": "textField1",
                        "rows": 2,
                        "type": "TextField",
                        "label": "УНК",
                        "maxRows": 2,
                        "readOnly": true,
                        "dataField": "subject.unc"
                      }
                    ]
                  },
                  {
                    "name": "col24",
                    "span": 8,
                    "type": "Col",
                    "children": [
                      {
                        "name": "clientOKATOField",
                        "rows": 2,
                        "type": "TextField",
                        "label": "Код по МР",
                        "maxRows": 2,
                        "readOnly": true,
                        "dataField": "subject.mosCode"
                      }
                    ]
                  },
                  {
                    "name": "col40",
                    "span": 8,
                    "type": "Col",
                    "children": [
                      {
                        "name": "textField2",
                        "rows": 2,
                        "type": "TextField",
                        "label": "Код СР",
                        "maxRows": 2,
                        "readOnly": true,
                        "dataField": "subject.srpsCode"
                      }
                    ]
                  }
                ]
              }
            ],
            "collapsible": true,
            "headerBordered": true
          },
          {
            "name": "details2",
            "type": "Details",
            "style": "{width:70%; margin-left: 15%}\n",
            "title": "Уполномоченные лица",
            "compact": true,
            "bordered": true,
            "children": [
              {
                "name": "authorizedPersonInfoField",
                "type": "TableField",
                "listForm": {
                  "dataColumns": [
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
                      "title": "СНИЛС",
                      "isMask": false,
                      "dataType": "STRING",
                      "sortable": true,
                      "dataField": "snils",
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
                    },
                    {
                      "title": "Электронная почта",
                      "isMask": false,
                      "dataType": "STRING",
                      "sortable": true,
                      "dataField": "email",
                      "filterable": true,
                      "notGroupable": true,
                      "hideFilterOptions": false,
                      "rememberLastValues": false
                    },
                    {
                      "title": "Изменен",
                      "isMask": false,
                      "dataType": "STRING",
                      "sortable": true,
                      "dataField": "modified",
                      "filterable": true,
                      "notGroupable": true,
                      "hideFilterOptions": false,
                      "rememberLastValues": false
                    },
                    {
                      "title": "Создан",
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
                      "title": "Заблокирован",
                      "isMask": false,
                      "dataType": "STRING",
                      "sortable": true,
                      "dataField": "isBlock",
                      "filterable": true,
                      "notGroupable": true,
                      "hideFilterOptions": false,
                      "rememberLastValues": false
                    }
                  ],
                  "deleteCascadeEnable": false
                },
                "readOnly": false,
                "dataField": "authorizedPersonInfo",
                "suppressCollapse": true
              }
            ],
            "expandable": false,
            "collapsible": true,
            "headerBordered": true
          }
        ]
      }
    ]
  },
  "listForm": {
    "mode": "SPLIT",
    "dataColumns": [
      {
        "title": "Наименование Клиента",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "subject",
        "filterable": true,
        "captionField": "fullName",
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "ИНН",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "subject.inn",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "КПП",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "subject.cpp",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "ОГРН/ОГРНИП",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "subject.ogrn",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "УНК",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "subject.unc",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "Код МР",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "subject.mosCode",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "Код СР",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "subject.srpsCode",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "Статус",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "state.code",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "Изменен",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "modified",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      },
      {
        "title": "Создан",
        "isMask": false,
        "dataType": "STRING",
        "sortable": true,
        "dataField": "created",
        "filterable": true,
        "notGroupable": true,
        "hideFilterOptions": false,
        "rememberLastValues": false
      }
    ],
    "deleteCascadeEnable": false
  },
  "constUuid": "9a10a6f8-1086-4bea-8aff-63acfc380afd",
  "dataModel": {
    "isView": false,
    "tableName": "PAAUTHORIZEDPERSONDOC",
    "dataFields": [
      {
        "name": "name",
        "static": true,
        "dataType": "STRING",
        "required": true,
        "fetchMode": "NORMAL",
        "calculated": false,
        "displayName": "Наименование",
        "dataConstraint": {},
        "hideFilterOptions": false
      },
      {
        "name": "subject",
        "hidden": true,
        "static": true,
        "dataType": "REFERENCE",
        "fetchMode": "NORMAL",
        "calculated": false,
        "displayName": "Экономические субъекты",
        "refAppObject": {
          "entity": "AppObject",
          "id": "reference.subject",
          "displayName": "Экономические субъекты"
        },
        "dataConstraint": {},
        "hideFilterOptions": false
      },
      {
        "name": "authorizedPersonInfo",
        "static": true,
        "dataType": "REFLIST",
        "fetchMode": "NORMAL",
        "displayName": "Уполномоченное лицо",
        "refAppObject": {
          "entity": "AppObject",
          "id": "pa.authorizedPersonInfo",
          "displayName": "Уполномоченное лицо"
        },
        "dataConstraint": {},
        "hideFilterOptions": false
      }
    ],
    "displayName": {
      "displayFields": "name"
    },
    "displayTooltip": {},
    "isFullTextSearch": false,
    "greenplumReplicatedOption": true
  },
  "extProperties": {},
  "reportTemplates": [],
  "editForms": []
}
```

Формат выходной таблицы:
Необходимо вывести описание структуры в табличном виде со следующими столбцами:
Условный номер поля, Наименование поля/элемента, Атрибут, Формат атрибута, Размерность поля, Обязательность поля, Описание.
Основная часть структуры таблицы задается описание компонентов в теге components в элементе "editForm" со следующими
правилами:

1. Элемент с типом в поле "type" указанным "FormSection" выводится в отдельной строке таблицы с названием из "title" с
   использованием следующего шаблона "Блок полей {{title}}". Элемент является группирующий и должен иметь группирующий
   порядковый номер, который будет использоваться для вывода дочерних элементов.
2. Вложенные элементы "type" со значением "Details" выводятся в отдельной строке таблицы с названием из "title" с
   использованием следующего шаблона "Блок полей {{title}}"
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

5. Размерность поля при отображении на экранной форме определи самостоятельно в зависимости от типа данных или назначения поля, если его длинна может быть тобой определена исходя из его назначения. 
При этом учитывай следующее:
```
− Ограничение количества символов в поле ЭФ. 
− При описании полей с плавающими значениями перед максимальным значением количества допустимых символов на ЭФ добавлять знак «<» (меньше) либо «<=» (меньше равно)
− Ставить «б/о» (без ограничений) если поле неограниченной длины (адаптивное).
− Ставить «−» для интерактивных элементов.
```
6. 
6. В колонке описание выводи ключевые свойства поля, которые позволяет однозначно его идентифицировать в системе.
7. Если дочерний элемент имеет "type" = "TableField", то вывести одной строкой наименование в формате "Табличная часть".
   Наименование поля принять по значению элемента "title" а имя атрибута по данным "dataField". Формат поля определить
   по рекомендациям выше. 
8. Табличную часть заполнить описанием полей в соответствии с рекомендациями выше. 

