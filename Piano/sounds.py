import pygame
pygame.mixer.init()


def load_sounds(keys_list):
    sounds = {} 
    for key_name in keys_list:
        try:
            sounds[key_name] = pygame.mixer.Sound(f'sounds/{key_name}.mp3')
        except pygame.error:
            print(f"Помилка: Не вдалося завантажити звук для {key_name}. Перевірте наявність файлу.")
    if len(sounds) != len(keys_list):
        print("Увага: Не всі звуки було завантажено. Програма може працювати некоректно.")
    return sounds 