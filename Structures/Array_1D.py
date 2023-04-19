# Define 1D and 2D Grating  used in Lumerical simulations
# 2023-April-12
# function lists:
# AddRectangle_n_odd, AddRectangle_n_even


####################################################
####################################################
def AddRectangle_n_odd(fdtd, array_number=4, structure_x_span=1e-6, structure_y_span=1e-6, structure_z_span=1e-6, rotation_angle_z=0, distance=1e-6,
                  wafer_x_span=10e-6,  wafer_y_span=10e-6, thickness_Cladding=5e-6, thickness_Box=5e-6, thickness_Substrate=5e-6,
                  material_Resonator="Si (Silicon) - Palik", material_Cladding="SiO2 (Glass) - Palik",
                  material_Box="SiO2 (Glass) - Palik", material_Substrate="Si (Silicon) - Palik"):
    # fdtd: the "object" lumapi.FDTD()
    # array_number: number of resonators, must be an Odd number


    # PARTICLE DRAW
    number_list = range(int(-array_number / 2), int(array_number / 2) + 1)
    for i in number_list:
        fdtd.addrect()
        fdtd.set("name", "Resonator_"+str(i))
        fdtd.set("material", material_Resonator)
        fdtd.set("x min", i * (distance + structure_x_span) - structure_x_span/2)
        fdtd.set("x max", i * (distance + structure_x_span) + structure_x_span/2)
        fdtd.set("y", 0)
        fdtd.set("y span", structure_y_span)
        fdtd.set("z min", 0)
        fdtd.set("z max", structure_z_span)
        fdtd.set("first axis", "z")  # 设置第一转轴
        fdtd.set("rotation 1", rotation_angle_z)  # 设置第一旋转角
        fdtd.addtogroup("Segmented WG")


    # DRAW BURRIED OXIDE
    fdtd.addrect()
    fdtd.set("name", "Box")
    fdtd.set("material", material_Box)
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y_span)
    fdtd.set("z min", -thickness_Box)
    fdtd.set("z max", 0)
    fdtd.set("alpha", 0.2)


    # DRAW CLADDING
    fdtd.addrect()
    fdtd.set("name", "Cladding")
    fdtd.set("material", material_Cladding)
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y_span)
    fdtd.set("z min", 0)
    fdtd.set("z max", thickness_Cladding)
    fdtd.set("override mesh order from material database", 1)
    fdtd.set("mesh order", 3)
    fdtd.set("alpha", 0.3)


    # DRAW SILICON SLAB
    fdtd.addrect()
    fdtd.set("name", "Substrate")
    fdtd.set("material", material_Substrate)
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y_span)
    fdtd.set("z max", -thickness_Box)
    fdtd.set("z min", -thickness_Substrate - thickness_Box)
    fdtd.set("alpha", 0.4)



####################################################
####################################################
def AddRectangle_n_even(fdtd, array_number=4, structure_x_span=1e-6, structure_y_span=1e-6, structure_z_span=1e-6, rotation_angle_z=0, distance=1e-6,
                  wafer_x_span=10e-6,  wafer_y_span=10e-6, thickness_Cladding=5e-6, thickness_Box=5e-6, thickness_Substrate=5e-6,
                  material_Resonator="Si (Silicon) - Palik", material_Cladding="SiO2 (Glass) - Palik",
                  material_Box="SiO2 (Glass) - Palik", material_Substrate="Si (Silicon) - Palik"):
    # fdtd: the "object" lumapi.FDTD()
    # array_number: number of resonators, must be an Even number


    # PARTICLE DRAW
    number_list1 = range(-int(array_number / 2), 0)
    number_list2 = range(1, int(array_number / 2) + 1)
    for i in number_list1:
        fdtd.addrect()
        fdtd.set("name", "Resonator_" + str(i))
        fdtd.set("material", material_Resonator)
        fdtd.set("x min", i * (distance + structure_x_span) + distance/2)
        fdtd.set("x max", i * (distance + structure_x_span) + structure_x_span + distance/2)
        fdtd.set("y", 0)
        fdtd.set("y span", structure_y_span)
        fdtd.set("z min", 0)
        fdtd.set("z max", structure_z_span)
        fdtd.set("first axis", "z")  # 设置第一转轴
        fdtd.set("rotation 1", rotation_angle_z)  # 设置第一旋转角
        fdtd.addtogroup("Segmented WG")

    for i in number_list2:
        fdtd.addrect()
        fdtd.set("name", "Resonator_" + str(i))
        fdtd.set("material", material_Resonator)
        fdtd.set("x min", i * (distance + structure_x_span) - structure_x_span - distance/2)
        fdtd.set("x max", i * (distance + structure_x_span) - distance/2)
        fdtd.set("y", 0)
        fdtd.set("y span", structure_y_span)
        fdtd.set("z min", 0)
        fdtd.set("z max", structure_z_span)
        fdtd.set("first axis", "z")  # 设置第一转轴
        fdtd.set("rotation 1", rotation_angle_z)  # 设置第一旋转角
        fdtd.addtogroup("Segmented WG")


    # DRAW BURRIED OXIDE
    fdtd.addrect()
    fdtd.set("name", "Box")
    fdtd.set("material", material_Box)
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y_span)
    fdtd.set("z min", -thickness_Box)
    fdtd.set("z max", 0)
    fdtd.set("alpha", 0.2)


    # DRAW CLADDING
    fdtd.addrect()
    fdtd.set("name", "Cladding")
    fdtd.set("material", material_Cladding)
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y_span)
    fdtd.set("z min", 0)
    fdtd.set("z max", thickness_Cladding)
    fdtd.set("override mesh order from material database", 1)
    fdtd.set("mesh order", 3)
    fdtd.set("alpha", 0.3)


    # DRAW SILICON SLAB
    fdtd.addrect()
    fdtd.set("name", "Substrate")
    fdtd.set("material", material_Substrate)
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y_span)
    fdtd.set("z max", -thickness_Box)
    fdtd.set("z min", -thickness_Substrate - thickness_Box)
    fdtd.set("alpha", 0.5)


####################################################
####################################################
