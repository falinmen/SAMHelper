# 🎮 ASMHelper.py — Автоматизация работы с SAM

## Описание проекта

**ASMHelper.py** — это Python-скрипт, созданный для автоматизации процесса разблокировки достижений в игре через **SAM (Steam Achievement Manager)**. Программа позволяет быстро обработать игры, выполняя все необходимые действия по нажатию одной горячей клавиши (`F1`). Она идеально подходит для пользователей, которые хотят сэкономить время при работе с SAM.

<div align="center">

![](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHRxZ3dndjA2c240OHk1YXQ3d2x2Y3BvMTFnNm84MWhsOXM2aXpvbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/I2BBVL9r1pDkqV23ta/giphy.gif)

</div>

---

## Функционал

### Основные возможности:
- 🔓 Нажатие кнопки "Unlock All" (разблокировка всех достижений).
- ✅ Подтверждение действия.
- ⌨️ Нажатие клавиши `Enter`.
- ❌ Закрытие окна игры.

---

## Требования

### Для запуска скрипта:
1. **Python 3.6+**: Установите Python с [официального сайта](https://www.python.org/).
2. **Установленные библиотеки**:
   ```bash
   pip install pyautogui keyboard
  ## Как использовать

### Шаг 1: Настройка программы

1. Убедитесь, что у вас установлен Python.
2. Скопируйте файл `ASMHelper.py` и изображения (`bott.png`, `confirm_button.png`, `close_button.png`) в одну папку.

---

### Шаг 2: Выбор изображений

Программа запросит пути к изображениям кнопок:
- `bott.png` — кнопка "Unlock All".
- `confirm_button.png` — кнопка подтверждения.
- `close_button.png` — кнопка закрытия окна.

Убедитесь, что изображения находятся в той же папке, что и `ASMHelper.py`, или укажите полные пути. (Вручную или перетащить файлы в окно терминала)

---

### Шаг 3: Работа с SAM

1. Откройте SAM и выберите игру, которую хотите обработать.
2. Запустите скрипт через терминал:
   ```bash
   python ASMHelper.py
3. Нажмите клавишу `F1`.
4. Программа автоматически выполнит все действия для разблокировки достижений.
## Важные замечания

⚠️ **Использование автоматизации для получения достижений нарушает правила Steam и может привести к блокировке аккаунта.**

- **Совместимость изображений**:  
  Убедитесь, что скриншоты кнопок совпадают с интерфейсом SAM. Если разрешение экрана или масштабирование отличаются, программа может не найти кнопки.
- **Права администратора**:  
  Если программа использует библиотеку `keyboard`, запустите терминал от имени администратора.

---

## Лицензия

MIT License. Используйте на свой страх и риск.

---

## Контакты

Если у вас есть вопросы или предложения:

- **Telegram**: @falinmen
- **GitHub**: [[КЛИК]](https://github.com/falinmen)

---

✨ **Спасибо за использование проекта!** ✨
