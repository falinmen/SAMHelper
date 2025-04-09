import pyautogui
import time
import keyboard

def find_and_click_image(image_path):

    print(f"Поиск изображения: {image_path}")
    try:
        button_location = pyautogui.locateOnScreen(image_path)
        if button_location:
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center)
            print("Кнопка найдена и нажата.")
        else:
            print("Кнопка не найдена.")
    except Exception as e:
        print(f"Ошибка при поиске изображения: {e}")

def process_game():
  
    print("Начинаем обработку текущей игры...")
    
   
    unlock_button_image = r"F:\Users\pc\bott.png"  
    find_and_click_image(unlock_button_image)
    time.sleep(0.3)  

 
    confirm_button_image = r"F:\Users\pc\confirm_button.png"
    find_and_click_image(confirm_button_image)
    time.sleep(0.3)

 
    print("Нажатие клавиши Enter после подтверждения...")
    pyautogui.press('enter')
    time.sleep(0.3) 

   
    print("Закрытие окна игры...")
    close_button_image = r"F:\Users\pc\close_button.png" 
    time.sleep(0.3)

    print("Обработка текущей игры завершена.")

def main():
    print("=== Автоматизация SAM ===")
    print("Внимание: Использование этого скрипта может нарушить правила Steam.")
    print("Нажмите F1, чтобы запустить обработку текущей игры.")
    print("Для выхода из программы нажмите Ctrl+C.")

    try:
        while True:
            if keyboard.is_pressed('f1'):
                print("Горячая клавиша F1 нажата. Начинаем обработку...")
                process_game()
                print("Ожидание следующего нажатия F1...")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Скрипт остановлен пользователем.")

if __name__ == "__main__":
    main()