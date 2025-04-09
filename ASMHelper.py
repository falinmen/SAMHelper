import pyautogui
import time
import keyboard  # Для обработки горячих клавиш

# Словарь для хранения путей к изображениям
image_paths = {
    "unlock_button": None,
    "confirm_button": None,
    "close_button": None
}

def find_and_click_image(image_path):
    """
    Находит и кликает по указанному изображению на экране.
    :param image_path: Путь к изображению кнопки.
    """
    print(f"Поиск изображения: {image_path}")
    try:
        button_location = pyautogui.locateOnScreen(image_path)  # Без confidence
        if button_location:
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center)
            print("Кнопка найдена и нажата.")
        else:
            print("Кнопка не найдена.")
    except Exception as e:
        print(f"Ошибка при поиске изображения: {e}")

def process_game():
    """
    Обрабатывает текущую игру: разблокирует достижения и закрывает окно.
    """
    print("Начинаем обработку текущей игры...")
    
    # Проверяем, что все изображения выбраны
    if not all(image_paths.values()):
        print("Ошибка: Не все изображения выбраны!")
        return

    # Ищем и нажимаем кнопку "Unlock All"
    find_and_click_image(image_paths["unlock_button"])
    time.sleep(0.3)  # Задержка после нажатия кнопки "Unlock All"

    # Подтверждение действия (если требуется)
    find_and_click_image(image_paths["confirm_button"])
    time.sleep(0.3)  # Задержка после нажатия кнопки подтверждения

    # Дополнительное нажатие Enter после подтверждения
    print("Нажатие клавиши Enter после подтверждения...")
    pyautogui.press('enter')
    time.sleep(0.3)  # Увеличенная задержка после нажатия Enter

    # Закрытие окна игры
    print("Закрытие окна игры...")
    find_and_click_image(image_paths["close_button"])
    time.sleep(0.3)  # Задержка после закрытия окна игры

    print("Обработка текущей игры завершена.")

def select_images():
    """
    Запрашивает у пользователя пути к изображениям через консоль.
    """
    print("Введите полные пути к изображениям или перетащите файлы в консоль.")
    print("Если изображение не требуется, оставьте поле пустым.")
    
    # Выбор bott.png (Unlock All)
    image_paths["unlock_button"] = input("1. Путь к bott.png (Unlock All): ").strip().strip('"')
    if not image_paths["unlock_button"]:
        print("bott.png не выбран.")

    # Выбор confirm_button.png (Подтверждение)
    image_paths["confirm_button"] = input("2. Путь к confirm_button.png (Подтверждение): ").strip().strip('"')
    if not image_paths["confirm_button"]:
        print("confirm_button.png не выбран.")

    # Выбор close_button.png (Закрытие окна)
    image_paths["close_button"] = input("3. Путь к close_button.png (Закрытие окна): ").strip().strip('"')
    if not image_paths["close_button"]:
        print("close_button.png не выбран.")

    print("\nВыбранные изображения:")
    for key, path in image_paths.items():
        print(f"{key}: {path}")

def start_processing():
    """
    Запускает обработку игр.
    """
    print("Ожидание нажатия F1 для запуска обработки...")
    while True:
        if keyboard.is_pressed('f1'):
            print("Горячая клавиша F1 нажата. Начинаем обработку...")
            process_game()
            print("Ожидание следующего нажатия F1...")
        time.sleep(0.1)

def main():
    print("=== Автоматизация SAM ===")
    print("Внимание: Использование этого скрипта может нарушить правила Steam.")
    
    # Выбор изображений
    select_images()

    # Запуск обработки
    start_processing()

if __name__ == "__main__":
    main()