import toml, pprint, math, sys
from raylib.dynamic import raylib as rl, ffi
from raylib.colors import *

TILE_SIZE = 64

colors = toml.load(open((sys.argv[1:] or ['palettes/painting.toml'])[0]))
pprint.pprint(colors)

WIDTH = 640
HEIGHT = 512

rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE)
rl.InitWindow(WIDTH, HEIGHT, b'Palettizer')
rl.SetTargetFPS(30)

while not rl.WindowShouldClose():
    rl.BeginDrawing()
    rl.ClearBackground(WHITE)

    x, y = 0, 0
    for name, color in colors.items():
        r, g, b = color
        rl.DrawRectangle(x, y, TILE_SIZE, TILE_SIZE, (r, g, b, 255))
        x += TILE_SIZE
        if x > WIDTH:
            x = 0
            y += TILE_SIZE
    
    rl.EndDrawing()

    if rl.IsKeyPressed(rl.KEY_E):
        rl.TakeScreenshot(b'pallet.png')

rl.CloseWindow()

