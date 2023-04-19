import sys, os
sys.path.append("D:\Program Files\Lumerical\v231\api\python") #Default windows lumapi path
import lumapi
import collections
import numpy as np



# loads and runs script.lsf while hiding the application window
# inc = lumapi.FDTD(filename="script.lsf", hide=True)

fdtd = lumapi.FDTD()
fdtd.addfdtd(dimension="3D", x = 0.0e-9, y = 0.0e-9, z = 0.0e-9, x_span = 3.0e-6, y_span = 3.0e-6, z_span = 3.0e-6)
props = collections.OrderedDict([("name", "power"),("override global monitor settings", True),("x", 0.),("y", 0.4e-6),
                     ("monitor type", "linear x"),("frequency points", 10.0)])
fdtd.addpower(properties=props)
rectangle = fdtd.addrect(x = 2e-6, y = 0.0, z = 0.0)
rectangle.x_span = 10.0e-6
rectangle.y_span = 0.4e-6
rectangle.z_span = 0.2e-6