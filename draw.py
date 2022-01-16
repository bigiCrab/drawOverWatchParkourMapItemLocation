from typing import List
from matplotlib.pyplot import figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.core.multiarray import empty
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


def drawOnPlt2D(_locations: list[Vector], _size=30, _alpha=1, _color=None):
    sizeBase = 10
    data = np.array(list(map(lambda _v: [_v.x, _v.y, _v.z], _locations)))
    x, y, z = data.T
    __s = np.array(list(map(lambda _v: max(10, _size+(_v*sizeBase)), z)))
    plt.scatter(x, y, color=_color, s=__s, alpha=_alpha)
    plt.plot(x, y, color=_color, linewidth=0.5)


def drawOnPlt3D(_locations, _size=30, _alpha=1, _color=None):
    data = np.array(list(map(lambda _v: [_v.x, _v.y, _v.z], _locations)))
    x, y, z = data.T
    ax.plot(x, y, z, '-o', color=_color, alpha=_alpha)


# 2d setting
plt.gca().invert_yaxis()
plt.grid()
# draw data
drawOnPlt2D(Global.ZoneLocations, _color='gray', _size=100)
drawOnPlt2D(Global.HeroLocations, _color='black')
drawOnPlt2D(Global.UnlockLocations, _color='hotpink')
drawOnPlt2D(Global.EasterEggLocations, _color='cyan')
drawOnPlt2D(Global.PortalLocations, _color='green')

# 3d setting
fig = plt.figure()
ax = Axes3D(fig)
ax.invert_yaxis()
ax.set_title("3D plot")
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
# draw data
drawOnPlt3D(Global.ZoneLocations, _color='gray', _size=100)
drawOnPlt3D(Global.HeroLocations, _color='black')
drawOnPlt3D(Global.UnlockLocations, _color='hotpink')
drawOnPlt3D(Global.EasterEggLocations, _color='cyan')
drawOnPlt3D(Global.PortalLocations, _color='green')

plt.show()
