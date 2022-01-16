import numpy as np
import matplotlib.pyplot as plt

from read import getAllLocs
# defind to match ow class


class Vector:
    def __init__(self, x, z, y):
        self.x = x
        self.y = y
        self.z = z


class GlobalClass:
    ZoneLocations = [Vector(0, 0, 0)]*10
    HeroLocations = [Vector(0, 0, 0)]*10
    UnlockLocations = [Vector(0, 0, 0)]*10
    EasterEggLocations = [Vector(0, 0, 0)]*10
    PortalLocations = [Vector(0, 0, 0)]*20


Global = GlobalClass()

# Locations put here
# Global.EasterEggLocations[0]=Vector(4, 16.200, 59)

# exec(getAllLocs("map/w.ow"))
exec(getAllLocs("map/WM5SS.ow"))

# draw setting
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])


def drawOnPlt(_locations, _cmap='cool', _size=30, _alpha=1, _color=None):
    sizeBase = 10
    for idx, loc in enumerate(_locations):
        __s = max(10, _size+(loc.z*sizeBase))
        if _color == None:
            plt.scatter(loc.x, loc.y, c=colors[idx],
                        cmap=_cmap, s=__s, alpha=_alpha)
        else:
            plt.scatter(loc.x, loc.y, color=_color, s=__s, alpha=_alpha)

drawOnPlt(Global.ZoneLocations, _color='gray', _size=100)

drawOnPlt(Global.HeroLocations, _color='black')

drawOnPlt(Global.UnlockLocations, _color='hotpink')

drawOnPlt(Global.EasterEggLocations, 'cool')

drawOnPlt(Global.PortalLocations, _color='green')

plt.gca().invert_yaxis()
plt.grid()
plt.show()
