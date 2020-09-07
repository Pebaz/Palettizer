import toml, pprint, math, sys
from raylib.dynamic import raylib as rl, ffi
from raylib.colors import *
from haishoku.haishoku import Haishoku

TILE_SIZE = 64

colors = toml.load(open((sys.argv[1:] or ['palettes/painting.toml'])[0]))
pprint.pprint(colors)

WIDTH = 640
HEIGHT = 512

rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE)
rl.InitWindow(WIDTH, HEIGHT, b'Palettizer - Press E To Export Palette')
rl.SetTargetFPS(30)

def get_dropped_files():
    files = []
    if rl.IsFileDropped():
        file_count = ffi.new('int *')
        files = rl.GetDroppedFiles(file_count)
        files = [ffi.string(files[i]).decode() for i in range(file_count[0])]
        rl.ClearDroppedFiles()
    return files

while not rl.WindowShouldClose():
    for file in get_dropped_files():
        h = Haishoku.loadHaishoku(file)
        colors = {str(blob) : blob[1] for blob in h.palette}

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

