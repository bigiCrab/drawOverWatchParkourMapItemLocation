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

# read Locations
# exec(getAllLocs("map/w.ow"))
exec(getAllLocs("map/WM5SS.ow"))

# draw setting
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])


def drawOnPlt(_locations, _size=30, _alpha=1, _color=None):
    sizeBase = 10
    for idx, loc in enumerate(_locations):
        __s = max(10, _size+(loc.z*sizeBase))
        plt.scatter(loc.x, loc.y, color=_color, s=__s, alpha=_alpha)


drawOnPlt(Global.ZoneLocations, _color='gray', _size=100)

drawOnPlt(Global.HeroLocations, _color='black')

drawOnPlt(Global.UnlockLocations, _color='hotpink')

drawOnPlt(Global.EasterEggLocations, _color='cyan')

drawOnPlt(Global.PortalLocations, _color='green')

plt.gca().invert_yaxis()
plt.grid()
plt.show()
