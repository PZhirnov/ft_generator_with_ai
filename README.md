# Генерация ФТ по данным JSON объектов БФТ.Платформы


Описание структуры проекта
prompt-generator/
├── config/
│   ├── __init__.py
│   ├── settings.py          # Основные настройки проекта
│   ├── template_config.py   # Конфигурация шаблонов
│   └── logging_config.py    # Настройка логирования
├── core/
│   ├── __init__.py
│   ├── models/              # Модели данных
│   │   ├── __init__.py
│   │   ├── json_schema.py   # Pydantic-схемы для JSON
│   │   └── prompt.py        # Модель промпта
│   ├── processors/          # Обработчики данных
│   │   ├── __init__.py
│   │   ├── json_loader.py   # Загрузка и валидация JSON
│   │   ├── template_engine.py # Движок шаблонов (Jinja2)
│   │   └── context_builder.py # Построение контекста
│   └── validators/          # Валидаторы
│       ├── __init__.py
│       ├── json_validator.py
│       └── template_validator.py
├── templates/
│   ├── __init__.py
│   ├── system/              # Системные промпты
│   │   ├── architecture.j2
│   │   ├── components.j2
│   │   └── documentation.j2
│   ├── code/                # Шаблоны для генерации кода
│   │   ├── backend.j2
│   │   ├── frontend.j2
│   │   └── api.j2
│   └── validation/          # Шаблоны для валидации
│       └── validation_rules.j2
├── data/
│   ├── input/              # Входные JSON файлы
│   │   ├── applications/
│   │   ├── components/
│   │   └── workflows/
│   ├── output/             # Сгенерированные промпты
│   │   ├── prompts/
│   │   └── logs/
│   └── schemas/            # JSON-схемы для валидации
│       ├── application_schema.json
│       ├── component_schema.json
│       └── workflow_schema.json
├── services/
│   ├── __init__.py
│   ├── prompt_service.py   # Основной сервис генерации
│   ├── file_service.py     # Работа с файлами
│   └── cache_service.py    # Кэширование промптов
├── cli/
│   ├── __init__.py
│   ├── commands.py         # CLI команды
│   └── interface.py        # Интерфейс командной строки
├── api/
│   ├── __init__.py
│   ├── endpoints.py        # FastAPI/Flask эндпоинты
│   ├── models.py           # API модели
│   └── dependencies.py     # Зависимости API
├── utils/
│   ├── __init__.py
│   ├── helpers.py          # Вспомогательные функции
│   ├── formatters.py       # Форматирование вывода
│   └── constants.py        # Константы проекта
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_json_loader.py
│   │   ├── test_template_engine.py
│   │   └── test_prompt_service.py
│   ├── integration/
│   │   └── test_generation_flow.py
│   ├── fixtures/
│   │   └── sample_data.py
│   └── conftest.py
├── scripts/
│   ├── init_project.py     # Инициализация проекта
│   ├── batch_generate.py   # Пакетная генерация
│   └── validate_inputs.py  # Валидация входных данных
├── docs/
│   ├── templates.md        # Документация шаблонов
│   └── examples.md         # Примеры использования
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── README.md
└── main.py                 # Точка входа


Основные модули и их назначение:
1. config/ - Конфигурация
settings.py - основные настройки (пути, параметры)
template_config.py - настройка шаблонов и переменных

2. core/ - Ядро приложения
models/ - Pydantic-модели для JSON объектов low-code платформы
processors/ - обработчики:

json_loader.py - загрузка и парсинг JSON
template_engine.py - движок шаблонов (Jinja2)
context_builder.py - подготовка контекста для подстановки
validators/ - валидация входных данных

3. templates/ - Шаблоны промптов
system/ - системные промпты (архитектура, документация)
code/ - шаблоны для генерации кода

Используется Jinja2-синтаксис: {{ variable_name }}

4. data/ - Данные
input/ - входные JSON файлы
output/ - сгенерированные промпты
schemas/ - JSON-схемы для валидации

5. services/ - Бизнес-логика
prompt_service.py - основной сервис генерации
file_service.py - управление файлами
cache_service.py - кэширование результатов

6. cli/ - Командный интерфейс
Для запуска генерации из командной строки

7. api/ - REST API
Для интеграции с другими системами

8. utils/ - Вспомогательные утилиты
9. tests/ - Тесты
10. scripts/ - Вспомогательные скрипты
Пример кода основных компонентов: