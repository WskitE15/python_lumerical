import sys
sys.path.append("C:\\Program Files\\Lumerical\\v231\\api\\python\\") # Default windows lumapi path

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
import lumapi
import Structures, Analysis, materials.Materials_Load, Monitor, Plots, Solver, Source
##########################################################################################################

file_path = "D:\\work\\Simulation\\python_lumerical\\_Main_Silmulation_file\\test\\simulation_file\\"





fdtd = lumapi.FDTD()

WavStart = 1e-6                                        # Set source wavelength
WavStop = 1.6e-6                                       # Set source wavelength

sweep_number = 3                                       # Set sweep number
wavelength_points = 51                                 # Set number wavelength points

wavelength = np.ones((1, wavelength_points))          # set array for wavelength data
T = np.ones((sweep_number, wavelength_points))        # set array for Transmission data

#set structures parameters
size_x_start = 0.24e-6                                # set parameter which will sweep
dx = 0.2e-8                                           # set delta x used in sweep
size_x = size_x_start
size_y = 0.421e-6
size_z = 0.273e-6
periodic = 0.4e-6

# add structures and set parameter
Structures.AddRectangle(fdtd, structure_x_span=size_x, structure_y_span=size_y, structure_z_span=size_z,
                   material_Resonator="Si (Silicon) - Palik", material_Cladding="SiO2 (Glass) - Palik",
                   material_Box="SiO2 (Glass) - Palik", material_Substrate="Si (Silicon) - Palik")

# add solver and set parameter
Solver.AddSolver_FDTD_3D(fdtd, mesh_order= 2, sim_time=3000e-15, x_span=periodic, y_span=periodic, z_span=size_z+WavStop*2,
                         x_min_bc="Periodic", x_max_bc="Periodic", y_min_bc="Periodic", y_max_bc="Periodic", z_min_bc="PML", z_max_bc="PML")

Source.AddPlaneWave(fdtd, name="PlaneWave1", wavelengnth=[WavStart, WavStop], injection_axis="z", direction="Backward",
                    x_span=periodic+0.5e-6, y_span=periodic+0.5e-6, z=WavStop-0.1e-6)

# add monitor and set parameter
Monitor.AddFrequencyPower_SingleComponent(fdtd, name="T", monitor_type="Z_Normal",
                                          x_span=periodic+0.5e-6, y_span=periodic+0.5e-6, z=-WavStop+0.1e-6,
                                          f_points=wavelength_points)



for i in range(sweep_number):

    size_x = size_x_start+i*dx
    file_name = "Resonator_Rect_single_T_x"+str(size_x)
    fdtd.setnamed("Resonator", "x span", size_x)


    fdtd.save(str(file_path)+str(file_name))
    fdtd.run()


    T_result = fdtd.getresult("T", "T")
    T[i,:]=abs(T_result["T"])
    wavelength = T_result["lambda"]
    plt.plot(wavelength, T[i,:])
    fdtd.switchtolayout()

##########################################################################################################
# data processing and plot
plt.xlabel('wavelength')
plt.ylabel('Intensity')
plt.show()
print(T)











