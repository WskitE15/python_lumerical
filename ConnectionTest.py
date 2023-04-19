import sys
sys.path.append("C:\\Program Files\\Lumerical\\v231\\api\\python\\") # Default windows lumapi path
sys.path.append("C:\\PyProj\\MyScripts\\")

import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
import lumapi
import Component, Materials
#####################################################

fdtd = lumapi.FDTD()
Materials.load_material_simple1(fdtd)
Materials.load_material_dispersive_si(fdtd, np, "C:\\PyProj\\MyScripts\\materials\\")
materials = ['Si-Dispersive-Lossy', 'GlassJena-Dispersive', 'aSiH-Jena', 'SiO2 - Non-Dispersive & Lossy']
Component.rectangle(fdtd,materials,[315e-9, 515e-9, 220e-9])
fdtd.save("testFile")

# def huygens_WG_simulation():
#     fdtd = lumapi.FDTD()
#     Materials.load_material_simple1(fdtd)
#     Materials.load_material_dispersive_si(fdtd, np, "C:\\PyProj\\MyScripts\\materials\\")
#     # materials = ['Si-Dispersive-Lossy', 'GlassJena-Dispersive', 'aSiH-Jena', 'SiO2 - Non-Dispersive & Lossy']






