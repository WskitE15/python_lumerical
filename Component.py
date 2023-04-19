# Define structures used in Lumerical simulations
# 2023-March-31
# function lists:
#    rectangle, disk, rectangle_dimer, rectangle_n_odd, rectangle_n_even
####################################################
def rectangle(fdtd, materials, structure_size):
    # fdtd: the 'object' lumapi.FDTD()
    # Materials: [substrate,box,resonator,cladding]
    # structure_size: x_size, y_size, z_size

    # DEFINE WAFER
    thickness_layer1 = 5e-6  # Cladding
    thickness_layer2 = 5e-6  # Box
    thickness_layer3 = 3e-6  # Substrate
    wafer_x = 10.0e-6
    wafer_y = 10.0e-6

    # DRAW SILICON SLAB
    fdtd.addrect()
    fdtd.set('name', 'Substrate')
    fdtd.set('material', materials[0])
    fdtd.set('x', 0)
    fdtd.set('x span', wafer_x)
    fdtd.set('y', 0)
    fdtd.set('y span', wafer_y)
    fdtd.set('z max', -thickness_layer2)
    fdtd.set('z min', -thickness_layer3 - thickness_layer2)
    fdtd.set('alpha', 0.2)

    # DRAW BURRIED OXIDE
    fdtd.addrect()
    fdtd.set("name", "Box")
    fdtd.set("material", materials[1])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", -thickness_layer2)
    fdtd.set("z max", 0)
    fdtd.set("alpha", 0.5)

    # Resonator DRAW
    fdtd.addrect()
    fdtd.set('name', 'Resonator')
    fdtd.set("material", materials[2])
    fdtd.set("x", 0)
    fdtd.set("x span", structure_size[0])
    fdtd.set("y", 0)
    fdtd.set("y span", structure_size[1])
    fdtd.set("z min", 0)
    fdtd.set("z max", structure_size[2])

    # DRAW CLADDING
    fdtd.addrect()
    fdtd.set("name", "Cladding")
    fdtd.set("material", materials[3])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", 0)
    fdtd.set("z max", thickness_layer1)
    fdtd.set("override mesh order from material database", 3)
    fdtd.set("mesh order", 3)
    fdtd.set("alpha", 0.6)


####################################################
####################################################
def disk(fdtd, materials, structure_size):
    # fdtd: the 'object' lumapi.FDTD()
    # Materials: [substrate,box,resonator,cladding]
    # structure_size: radius, height

    # DEFINE WAFER
    thickness_layer1 = 5e-6  # Cladding
    thickness_layer2 = 5e-6  # Box
    thickness_layer3 = 3e-6  # Substrate
    wafer_x = 10.0e-6
    wafer_y = 10.0e-6

    # DRAW SILICON SLAB
    fdtd.addrect()
    fdtd.set('name', 'Substrate')
    fdtd.set('material', materials[0])
    fdtd.set('x', 0)
    fdtd.set('x span', wafer_x)
    fdtd.set('y', 0)
    fdtd.set('y span', wafer_y)
    fdtd.set('z max', -thickness_layer2)
    fdtd.set('z min', -thickness_layer3 - thickness_layer2)
    fdtd.set('alpha', 0.2)

    # DRAW BURRIED OXIDE
    fdtd.addrect()
    fdtd.set("name", "Box")
    fdtd.set("material", materials[1])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", -thickness_layer2)
    fdtd.set("z max", 0)
    fdtd.set("alpha", 0.5)

    # PARTICLE DRAW
    fdtd.addcircle()
    fdtd.set('name', 'Resonator')
    fdtd.set('material', materials[2])
    fdtd.set('x', 0)
    fdtd.set('y', 0)
    fdtd.set("z", structure_size[1] / 2)
    fdtd.set('z span', structure_size[1])
    fdtd.set('radius', structure_size[0])

    # DRAW CLADDING
    fdtd.addrect()
    fdtd.set("name", "Cladding")
    fdtd.set("material", materials[3])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", 0)
    fdtd.set("z max", thickness_layer1)
    fdtd.set("override mesh order from material database", 3)
    fdtd.set("mesh order", 3)
    fdtd.set("alpha", 0.6)


####################################################
####################################################
def rectangle_dimer(fdtd, materials, structure_size):
    # fdtd: the 'object' lumapi.FDTD()
    # Materials: [substrate,box,resonator,cladding]
    # structure_size: x_size, y_size, z_size, distance

    # DEFINE WAFER
    thickness_layer1 = 5e-6  # Cladding
    thickness_layer2 = 5e-6  # Box
    thickness_layer3 = 3e-6  # Substrate
    wafer_x = 25.0e-6
    wafer_y = 25.0e-6

    # DRAW SILICON SLAB
    fdtd.addrect()
    fdtd.set("name", "Substrate")
    fdtd.set("material", materials[0])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z max", -thickness_layer2)
    fdtd.set("z min", -thickness_layer3 - thickness_layer2)
    fdtd.set("alpha", 0.2)

    # DRAW BURRIED OXIDE
    fdtd.addrect()
    fdtd.set("name", "Box")
    fdtd.set("material", materials[1])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", -thickness_layer2)
    fdtd.set("z max", 0)
    fdtd.set("alpha", 0.5)

    # PARTICLE DRAW
    fdtd.addrect()
    fdtd.set('name', 'Resonator_1')
    fdtd.set("material", materials[2])
    fdtd.set("x min", -structure_size[3]/2 - structure_size[0])
    fdtd.set("x max", -structure_size[3]/2)
    fdtd.set("y", 0)
    fdtd.set("y span", structure_size[1])
    fdtd.set("z min", 0)
    fdtd.set("z max", structure_size[2])

    # PARTICLE DRAW
    fdtd.addrect()
    fdtd.set('name', 'Resonator_2')
    fdtd.set("material", materials[2])
    fdtd.set("x min", structure_size[3]/2)
    fdtd.set("x max", structure_size[3]/2 + structure_size[0])
    fdtd.set("y", 0)
    fdtd.set("y span", structure_size[1])
    fdtd.set("z min", 0)
    fdtd.set("z max", structure_size[2])

    # DRAW CLADDING
    fdtd.addrect()
    fdtd.set("name", "Cladding")
    fdtd.set("material", materials[3])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", 0)
    fdtd.set("z max", thickness_layer1)
    fdtd.set("override mesh order from material database", 3)
    fdtd.set("mesh order", 3)
    fdtd.set("alpha", 0.2)


####################################################
####################################################
def rectangle_n_odd(fdtd, materials, structure_size, n_particle):
    # fdtd: the 'object' lumapi.FDTD()
    # Materials: [substrate,box,resonator,cladding]
    # structure_size: x_size, y_size, z_size, distance
    # n_particle: number of resonators, must be an Odd number

    thickness_layer1 = 5e-6  # Cladding
    thickness_layer2 = 5e-6  # Box
    thickness_layer3 = 3e-6  # Substrate
    wafer_x = 25.0e-6
    wafer_y = 25.0e-6

    # DRAW SILICON SLAB
    fdtd.addrect()
    fdtd.set("name", "Substrate")
    fdtd.set("material", materials[0])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z max", -thickness_layer2)
    fdtd.set("z min", -thickness_layer3 - thickness_layer2)
    fdtd.set("alpha", 0.2)

    # DRAW BURRIED OXIDE
    fdtd.addrect()
    fdtd.set("name", "Box")
    fdtd.set("material", materials[1])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", -thickness_layer2)
    fdtd.set("z max", 0)
    fdtd.set("alpha", 0.5)

    # PARTICLE DRAW
    number_list = range(int(-n_particle / 2), int(n_particle / 2) + 1)
    for ii in number_list:
        fdtd.addrect()
        fdtd.set("name", "Resonator_"+str(ii))
        fdtd.set("material", materials[2])
        fdtd.set("x min", ii * (structure_size[3] + structure_size[0]) - structure_size[0]/2)
        fdtd.set("x max", ii * (structure_size[3] + structure_size[0]) + structure_size[0]/2)
        fdtd.set("y", 0)
        fdtd.set("y span", structure_size[1])
        fdtd.set("z min", 0)
        fdtd.set("z max", structure_size[2])
        fdtd.addtogroup("Segmented WG")

    # DRAW CLADDING
    fdtd.addrect()
    fdtd.set("name", "Cladding")
    fdtd.set("material", materials[3])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", 0)
    fdtd.set("z max", thickness_layer1)
    fdtd.set("override mesh order from material database", 3)
    fdtd.set("mesh order", 3)
    fdtd.set("alpha", 0.2)


####################################################
####################################################
def rectangle_n_even(fdtd, materials, structure_size, n_particle):
    # fdtd: the 'object' lumapi.FDTD()
    # materials: [substrate,box,resonator,cladding]
    # structure_size: x_size, y_size, z_size, distance
    # n_particle: number of resonators, must be an Even number

    thickness_layer1 = 5e-6  # Cladding
    thickness_layer2 = 5e-6  # Box
    thickness_layer3 = 3e-6  # Substrate
    wafer_x = 25.0e-6
    wafer_y = 25.0e-6

    # DRAW SILICON SLAB
    fdtd.addrect()
    fdtd.set("name", "Substrate")
    fdtd.set("material", materials[0])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z max", -thickness_layer2)
    fdtd.set("z min", -thickness_layer3 - thickness_layer2)
    fdtd.set("alpha", 0.2)

    # DRAW BURRIED OXIDE
    fdtd.addrect()
    fdtd.set("name", "Box")
    fdtd.set("material", materials[1])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", -thickness_layer2)
    fdtd.set("z max", 0)
    fdtd.set("alpha", 0.5)

    # PARTICLE DRAW
    number_list1 = range(-int(n_particle / 2), 0)
    number_list2 = range(1, int(n_particle / 2) + 1)
    for ii in number_list1:
        fdtd.addrect()
        fdtd.set("name", "Resonator_" + str(ii))
        fdtd.set("material", materials[2])
        fdtd.set("x min", ii * (structure_size[3] + structure_size[0]) + structure_size[3]/2)
        fdtd.set("x max", ii * (structure_size[3] + structure_size[0]) + structure_size[0] + structure_size[3]/2)
        fdtd.set("y", 0)
        fdtd.set("y span", structure_size[1])
        fdtd.set("z min", 0)
        fdtd.set("z max", structure_size[2])
        fdtd.addtogroup("Segmented WG")

    for ii in number_list2:
        fdtd.addrect()
        fdtd.set("name", "Resonator_" + str(ii))
        fdtd.set("material", materials[2])
        fdtd.set("x min", ii * (structure_size[3] + structure_size[0]) - structure_size[0] - structure_size[3]/2)
        fdtd.set("x max", ii * (structure_size[3] + structure_size[0]) - structure_size[3]/2)
        fdtd.set("y", 0)
        fdtd.set("y span", structure_size[1])
        fdtd.set("z min", 0)
        fdtd.set("z max", structure_size[2])
        fdtd.addtogroup("Segmented WG")

    # DRAW CLADDING
    fdtd.addrect()
    fdtd.set("name", "Cladding")
    fdtd.set("material", materials[3])
    fdtd.set("x", 0)
    fdtd.set("x span", wafer_x)
    fdtd.set("y", 0)
    fdtd.set("y span", wafer_y)
    fdtd.set("z min", 0)
    fdtd.set("z max", thickness_layer1)
    fdtd.set("override mesh order from material database", 3)
    fdtd.set("mesh order", 3)
    fdtd.set("alpha", 0.2)


####################################################
####################################################
