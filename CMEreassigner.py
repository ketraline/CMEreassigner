from PIL import Image
import sys

def colorImage(x,y,z):
    Color = Image.open(x)
    Map = Image.open(y)
    Edit = Image.open(z)

    colors = Color.load()
    maps = Map.load()
    edits = Edit.getdata()

    Maps = []
    for x in range(Map.size[0]):
        row = []
        for y in range(Map.size[1]):
            row.append(maps[x,y])
        Maps.append(row)

    maps = Map.getdata()
    exits = []

    for x in range(len(edits)):
        if edits[x][3] != 0:
            for y in range(len(Maps)):
                if edits[x] in Maps[y]:
                    pos = Maps[y].index(edits[x])
                    exits.append(colors[y,pos])
                    break
        else:
            exits.append(((255, 255, 255, 0)))
    
    Edit.putdata(exits)
    Edit.save("Exit.png", "PNG")

if __name__ == "__main__":
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]
    colorImage(x,y,z)