# Документация проекта: Калькулятор на PyQt6

## Описание проекта
Калькулятор с графическим интерфейсом, разработанный с использованием библиотеки PyQt6. Приложение поддерживает базовые арифметические операции: сложение, вычитание, умножение, деление, возведение в степень, а также очистку данных.

## Функциональность
- **Графический интерфейс:** Удобное расположение кнопок и полей вывода.
- **Базовые операции:** Сложение, вычитание, умножение, деление, возведение в степень.
- **Очистка данных:** Кнопка «С» сбрасывает все введённые значения.
- **Отображение результата:** Результат выводится в строке ввода и на LCD-дисплее.

## Требования
- Python 3.7 или выше
- PyQt6

## Установка зависимостей
```
pip install PyQt6
```

## Настройка проекта
1. Сохраните код в файл с расширением `.py` (например, `calculator_app.py`).
2. Убедитесь, что файл `calculator1.py` содержит корректное определение интерфейса.

## Структура проекта
### Основные компоненты
- **Класс Window:** Управляет логикой приложения.
- **Методы:**
  - `special_func()` — обработка операций.
  - `common_func()` — ввод чисел.

### Используемые библиотеки
- **PyQt6:** Создание графического интерфейса.

## Запуск приложения
1. Откройте терминал в директории с файлом.
2. Запустите приложение командой:
```
python calculator_app.py
```

## Использование приложения
1. Запустите приложение.
2. Нажимайте кнопки для ввода чисел и операций.
3. Нажмите «=» для получения результата.
4. Нажмите «С» для очистки данных.

## Возможные проблемы и их решение
- **Ошибка при запуске:**
  - Убедитесь, что PyQt6 установлен.
  - Проверьте структуру проекта и наличие всех файлов.

- **Некорректный вывод:**
  - Проверьте корректность логики методов `special_func` и `common_func`.

## Безопасность
- Регулярно обновляйте библиотеки.
- Следите за корректностью ввода данных.

---

# Project Documentation: PyQt6 Calculator

## Project Description
A calculator with a graphical interface developed using the PyQt6 library. The application supports basic arithmetic operations, including addition, subtraction, multiplication, division, exponentiation, and data clearing.

## Features
- **Graphical Interface:** Convenient button and output field layout.
- **Basic Operations:** Addition, subtraction, multiplication, division, exponentiation.
- **Data Clearing:** The "C" button resets all input values.
- **Result Display:** The result is displayed in the input field and on the LCD display.

## Requirements
- Python 3.7 or higher
- PyQt6

## Dependency Installation
```
pip install PyQt6
```

## Project Setup
1. Save the code in a `.py` file (e.g., `calculator_app.py`).
2. Ensure the `calculator1.py` file contains the correct interface definition.

## Project Structure
### Main Components
- **Window Class:** Manages application logic.
- **Methods:**
  - `special_func()` — handles operations.
  - `common_func()` — handles number input.

### Libraries Used
- **PyQt6:** For creating the graphical interface.

## Running the Application
1. Open a terminal in the project directory.
2. Run the application with the command:
```
python calculator_app.py
```

## Using the Application
1. Launch the application.
2. Press buttons to enter numbers and operations.
3. Press "=" to get the result.
4. Press "C" to clear the data.

## Possible Issues and Solutions
- **Error on Launch:**
  - Ensure PyQt6 is installed.
  - Check the project structure and the presence of all files.

- **Incorrect Output:**
  - Verify the logic of `special_func` and `common_func` methods.

## Security
- Regularly update libraries.
- Ensure correct data input.

