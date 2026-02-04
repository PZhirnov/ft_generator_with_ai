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

Предв. проработка  основных компонентов:
core/models/json_schema.py:
```python
from pydantic import BaseModel
from typing import List, Dict, Optional

class LowCodeComponent(BaseModel):
    name: str
    type: str
    properties: Dict[str, str]
    events: Optional[List[str]] = None
    data_bindings: Optional[Dict] = None

class LowCodeApplication(BaseModel):
    name: str
    components: List[LowCodeComponent]
    workflows: List[Dict]
    data_sources: Optional[List[Dict]] = None

```

core/processors/template_engine.py:
```python
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from typing import Dict, Any

class TemplateEngine:
    def __init__(self, templates_dir: str):
        self.env = Environment(
            loader=FileSystemLoader(templates_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        try:
            template = self.env.get_template(template_name)
            return template.render(**context)
        except TemplateNotFound:
            raise ValueError(f"Template {template_name} not found")
```
services/prompt_service.py:
```python
from core.processors.json_loader import JsonLoader
from core.processors.template_engine import TemplateEngine
from core.processors.context_builder import ContextBuilder

class PromptService:
    def __init__(self, config: Dict):
        self.json_loader = JsonLoader()
        self.template_engine = TemplateEngine(config['templates_dir'])
        self.context_builder = ContextBuilder()
    
    def generate_prompt(
        self, 
        json_path: str, 
        template_name: str
    ) -> str:
        # Загрузка JSON
        json_data = self.json_loader.load(json_path)
        
        # Построение контекста
        context = self.context_builder.build(json_data)
        
        # Рендеринг шаблона
        prompt = self.template_engine.render(template_name, context)
        
        return prompt
```
templates/code/backend.j2:
```python
На основе low-code конфигурации приложения "{{ application.name }}" 
сгенерируйте backend код.

Описание компонентов:
{% for component in application.components %}
- {{ component.name }} ({{ component.type }}):
  Свойства: {{ component.properties|tojson }}
  {% if component.events %}События: {{ component.events|join(', ') }}{% endif %}
{% endfor %}

{% if application.workflows %}
Workflow логика:
{% for workflow in application.workflows %}
- {{ workflow.name }}: {{ workflow.description }}
{% endfor %}
{% endif %}

Требования к коду:
1. Использовать Python/FastAPI
2. Реализовать все указанные endpoints
3. Добавить валидацию данных
4. Реализовать логику workflow
```

Рекомендации по реализации:
Используйте Pydantic для валидации JSON структур

Jinja2 для шаблонов - гибкий и мощный инструмент
Поддерживайте расширяемость - легко добавлять новые типы шаблонов
Добавьте логирование для отладки генерации
Кэшируйте результаты при работе с большими объемами данных
Напишите тесты для критической логики
Такой подход обеспечит:
Чистую архитектуру с разделением ответственности
Легкость поддержки и расширения
Возможность как CLI, так и API использования
Качественную валидацию входных данных
Гибкую систему шаблонов
