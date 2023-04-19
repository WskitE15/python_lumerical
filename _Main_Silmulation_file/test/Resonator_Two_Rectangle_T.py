import sys
sys.path.append("C:\\Program Files\\Lumerical\\v231\\api\\python\\") # Default windows lumapi path

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
import lumapi
import Structures, Analysis, materials.Materials_Load, Monitor, Plots, Solver, Source
##########################################################################################################
file_path = "D:\\work\\Simulation\\python_lumerical\\_Main_Silmulation_file\\test\\simulation_file\\"
file_name = "Resonator_Two_Rect_single_T"




fdtd = lumapi.FDTD()
WavStart = 1e-6                                    # Set source wavelength
WavStop = 1.6e-6                                     # Set source wavelength
gap = 0.36e-6
size_x1 = 0.245e-6
size_y1 = 0.421e-6
size_z1 = 0.273e-6
size_x2 = 0.248e-6
size_y2 = 0.384e-6
size_z2 = size_z1
periodic = 0.77e-6


# add structures and set parameter
Structures.AddRectangle_two(fdtd, structure1_x_span=size_x1, structure1_y_span=size_y1, structure1_z_span=size_z1, rotation_angle_z1=0,
                  structure2_x_span=size_x2, structure2_y_span=size_y2, structure2_z_span=size_z2, rotation_angle_z2=0, distance=gap,
                  material_Resonator="Si (Silicon) - Palik", material_Cladding="SiO2 (Glass) - Palik",
                  material_Box="SiO2 (Glass) - Palik", material_Substrate="Si (Silicon) - Palik")

# add solver and set parameter
Solver.AddSolver_FDTD_3D(fdtd, mesh_order= 3, sim_time=3000e-15, x_span=periodic, y_span=periodic, z=size_z1/2, z_span=size_z1+WavStop*2,
                         x_min_bc="Periodic", x_max_bc="Periodic", y_min_bc="Periodic", y_max_bc="Periodic", z_min_bc="PML", z_max_bc="PML",
                         boundaries_layers=16)

Source.AddPlaneWave(fdtd, name="PlaneWave1", wavelengnth=[WavStart, WavStop], injection_axis="z", direction="Backward",
                    x_span=periodic+0.5e-6, y_span=periodic+0.5e-6, z=WavStop-0.1e-6)

# add monitor and set parameter
Monitor.AddFrequencyPower_SingleComponent(fdtd, name="T", monitor_type="Z_Normal",
                                          x_span=periodic+0.5e-6, y_span=periodic+0.5e-6, z=size_z1/2-WavStop+0.1e-6,
                                          f_points=51)



fdtd.save(str(file_path)+str(file_name))
fdtd.run()
T = fdtd.getresult("T", "T")

##########################################################################################################
# data processing and plot
plt.plot(T["lambda"], abs(T["T"]))
plt.xlabel('wavelength')
plt.ylabel('Intensity')
plt.show()
print(T)











