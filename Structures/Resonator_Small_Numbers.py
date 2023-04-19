# Define Small numbers of component with cladding, box and substrate used in Lumerical simulations
# 2023-April-11
# function lists:
# AddRectangle_two
####################################################


####################################################
####################################################
def AddRectangle_two(fdtd, structure1_x_span=1e-6, structure1_y_span=1e-6, structure1_z_span=1e-6, rotation_angle_z1=0,
                  structure2_x_span=1e-6, structure2_y_span=1e-6, structure2_z_span=1e-6, rotation_angle_z2=0, distance=1e-6,
                  wafer_x_span=10e-6,  wafer_y_span=10e-6, thickness_Cladding=5e-6, thickness_Box=5e-6, thickness_Substrate=5e-6,
                  material_Resonator="Si (Silicon) - Palik", material_Cladding="SiO2 (Glass) - Palik",
                  material_Box="SiO2 (Glass) - Palik", material_Substrate="Si (Silicon) - Palik"):

    # fdtd: the "object" lumapi.FDTD()
    # Materials: [substrate,box,resonator,cladding]
    # structure_size: x_size, y_size, z_size, distance

    # Resonator1 DRAW
    fdtd.addrect()
    fdtd.set("name", "Resonator1")
    fdtd.set("material", material_Resonator)
    fdtd.set("x", -distance/2)
    fdtd.set("x span", structure1_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", structure1_y_span)
    fdtd.set("z min", 0)
    fdtd.set("z max", structure1_z_span)
    fdtd.set("first axis", "z")  # 设置第一转轴
    fdtd.set("rotation 1", rotation_angle_z1)  # 设置第一旋转角

    # Resonator1 DRAW
    fdtd.addrect()
    fdtd.set("name", "Resonator2")
    fdtd.set("material", material_Resonator)
    fdtd.set("x", distance/2)
    fdtd.set("x span", structure2_x_span)
    fdtd.set("y", 0)
    fdtd.set("y span", structure2_y_span)
    fdtd.set("z min", 0)
    fdtd.set("z max", structure2_z_span)
    fdtd.set("first axis", "z")  # 设置第一转轴
    fdtd.set("rotation 1", rotation_angle_z2)  # 设置第一旋转角

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