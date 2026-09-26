Для использования утилиты в консоли необходимо:
1. Зайти в корень репрозитория (Папка lab1 через команду cd)
2. Создать виртуальное окружение (python -m venv .venv)
3. Активировать его (.\.venv\Scripts\Activate.ps1) если отказано,
то разрешить для текущего окна консоли и повторить попытку (Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)
5. Установить проект из pyproject.toml (python -m pip install -e .)
Основные команды:
Запускает тесты: python -m pytest
Проверка ruff: ruff check
Справка: python -m toolkit --help
Калькулятор: python -m toolkit calc "EXPRESSION"
Конвертер: python -m toolkit convert VALUE --from UNIT --to UNIT
