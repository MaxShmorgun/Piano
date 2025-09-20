from pygame import *
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE
from keys import create_key_rects, draw_keys
from sounds import load_sounds
init()
mixer.init()

pressed = set()
key_rects = create_key_rects(7)
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano")
running = True


KEYS = {}
keys_list = ['a6', 'c6', 'd6', 'f6', 'g6', 'e6', 'b6']  
sounds = {}
sounds = load_sounds(keys_list)

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
            if k in keys_list:
                pressed.add(keys_list.index(k))
        if e.type == KEYUP:
            k = key.name(e.key)
            if k in keys_list:
                pressed.remove(keys_list.index(k))

        if e.type == MOUSEBUTTONDOWN:
            for i, r in enumerate(key_rects):
                if r.collidepoint(e.pos):
                    sounds[keys_list[i]].play()
                    pressed.add(i)
        if e.type == MOUSEBUTTONUP:
            for i, r in enumerate(key_rects):
                if i in pressed and r.collidepoint(e.pos):
                    pressed.remove(i)

    screen.fill(WHITE)
    draw_keys(screen, key_rects, pressed)
    display.update()
