# Tic Tac Toe Game

Игра "Крестики-нолики", реализованная на языке Python с использованием библиотеки `pygame`.

---

## Авторы проекта

**Подготовлено:**

- **ФИО:** Бледных Кирилл Дмитриевич и Серов Максим Иванович  
- **ИСУ:** 465230 и 467436

---

## Разделение работы

- **Кирилл Бледных**:  
  - Реализовал метод `check_win` основного класса.  
  - Написал функцию `main`.  
  - Добавил докстринги и комментарии к коду.
  
- **Максим Серов**:  
  - Написал некоторые методы основного класса.  
  - Реализовал функции для рисования объектов в `pygame`.  
  - Создал функцию для сохранения результатов игры.

---

## Описание проекта

В данном проекте реализована игра "Крестики-нолики". Используемая библиотека `pygame` отвечает за отображение игрового интерфейса, рисование линий, крестиков и ноликов.

### Функционал:
1. Полностью интерактивное управление:
   - Возможность делать ходы, кликнув по игровому полю.
   - Автоматическая проверка на победу или ничью.
2. Сохранение результатов игры в файл `results.txt`.
3. Структурированная архитектура кода:
   - Основной класс `Board` для работы с игровым полем.
   - Функции для рисования и управления логикой игры.

---

## Для запуска:

```shell
python main.py
```
Результаты игры будут доступны в results.txt.
