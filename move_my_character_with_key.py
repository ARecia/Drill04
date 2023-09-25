from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 720
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('megaman.png')

def handle_events():
    global running
    global x,y
    global dx,dy   # dir x,y 속도 개선이 필요

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx += 5
            elif event.key == SDLK_LEFT:
                dx -= 5
            elif event.key == SDLK_UP:
                dy += 5
            elif event.key == SDLK_DOWN:
                dy -= 5
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx -= 5
            elif event.key == SDLK_LEFT:
                dx += 5
            elif event.key == SDLK_UP:
                dy -= 5
            elif event.key == SDLK_DOWN:
                dy += 5

running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dx, dy = 0, 0
hide_cursor()

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 10, 100, 130, x, y)

    update_canvas()
    handle_events()

    if x < 0:
        x = 0
    elif x > TUK_WIDTH:
        x = TUK_WIDTH
    if y < 0:
        y = 0
    elif y > TUK_HEIGHT:
        y = TUK_HEIGHT

    x += dx
    y += dy

    frame = (frame + 1) % 8
    delay(0.085)

close_canvas()