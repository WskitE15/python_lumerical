# Material library
# 2023-April-01
# functions:
#   load_material_simple1, including: Air, Si-Dispersive-Lossy, SiO2 - Dispersive & Lossy, SiO2 - Non-Dispersive & Lossy
#   load_material_dispersive_si, including: Si-Tafelmeier, aSiH-Jena, GlassJena-Dispersive
####################################################
def load_material_simple1(fdtd):
    # material: AIR
    new_material = fdtd.addmaterial("Dielectric")
    fdtd.setmaterial(new_material, "name", "AIR")
    fdtd.setmaterial("AIR", "Refractive Index", 1)
    # fdtd.setmaterial("AIR", "color", [0.1, 0.1, 0, 1])

    # material: SILICON (Dispersive & Lossy) from Silicon Photonics by Lucas
    material_name = "Si-Dispersive-Lossy"
    new_material = fdtd.addmaterial("Lorentz")
    fdtd.setmaterial(new_material, "name", material_name)
    fdtd.setmaterial(material_name, "Permittivity", 7.98737492)
    fdtd.setmaterial(material_name, "Lorentz Linewidth", 1e8)
    fdtd.setmaterial(material_name, "Lorentz Resonance", 3.93282466e+15)
    fdtd.setmaterial(material_name, "Lorentz Permittivity", 3.68799143)
    # fdtd.setmaterial(material_name, "color", [0.8, 0, 0, 1])

    # material_name = "SiO2 - Dispersive & Lossy"
    new_material = fdtd.addmaterial("Lorentz")
    material_name = "SiO2 - Dispersive & Lossy"
    fdtd.setmaterial(new_material, "name", material_name)
    fdtd.setmaterial(material_name, "Permittivity", 2.119881)
    fdtd.setmaterial(material_name, "Lorentz Linewidth", 1e10)
    fdtd.setmaterial(material_name, "Lorentz Resonance", 3.309238e+13)
    fdtd.setmaterial(material_name, "Lorentz Permittivity", 49.43721)
    # fdtd.setmaterial(material_name, "color", [0.5, 0.5, 0.5, 1])

    # material_name = "SiO2 - Non-dispersive & Lossless"
    new_material = fdtd.addmaterial("Dielectric")
    material_name = "SiO2 - Non-Dispersive & Lossy"
    fdtd.setmaterial(new_material, "name", material_name)
    fdtd.setmaterial(material_name, "Permittivity", 1.455**2)
    # fdtd.setmaterial(material_name, "color", [0.5, 0.5, 0.5, 1])


def load_material_dispersive_si(fdtd, np, path):
    # material: SILICON (Tafelmeier)
    material_data = np.loadtxt(path+'aSi_Tafelmaier.txt')
    freq = material_data[:, 0]  # frequency in Hz
    material_nk = material_data[:, 1] + 1j*material_data[:, 2]
    sampled_data = np.stack((freq, material_nk), axis=1 )
    material_name = 'Si-Tafelmeier'
    new_material = fdtd.addmaterial('Sampled data')
    fdtd.setmaterial(new_material, 'name', material_name)
    fdtd.setmaterial(material_name, 'max coefficients', 10)
    fdtd.setmaterial(material_name, 'tolerance', 0.001)
    fdtd.setmaterial(material_name, 'sampled data', sampled_data)
    # fdtd.setmaterial(material_name, 'color', (0.9,0,0,1) )

    # material: Amorphous silicon hydronated ANU-Jena
    material_data = np.loadtxt(path + 'aSiH_Jena.txt')
    freq = material_data[:, 0]  # frequency in Hz
    material_nk = material_data[:, 1] + 1j * material_data[:, 2]
    sampled_data = np.stack((freq, material_nk), axis=1)
    material_name = 'aSiH-Jena'
    new_material = fdtd.addmaterial('Sampled data')
    fdtd.setmaterial(new_material, 'name', material_name)
    fdtd.setmaterial(material_name, 'max coefficients', 10)
    fdtd.setmaterial(material_name, 'tolerance', 0.001)
    fdtd.setmaterial(material_name, 'sampled data', sampled_data)
    # fdtd.setmaterial(material_name, 'color', [0.9, 0.2, 0, 1])

    # material: SiO2 Jena (Dispersive & Lossy)
    material_data = np.loadtxt(path + 'Glass_Jena_Dispersive.txt')
    freq = material_data[:, 0]  # frequency in Hz
    material_nk = material_data[:, 1] + 1j * material_data[:, 2]
    sampled_data = np.stack((freq, material_nk), axis=1)
    material_name = 'GlassJena-Dispersive'
    new_material = fdtd.addmaterial('Sampled data')
    fdtd.setmaterial(new_material, 'name', material_name)
    fdtd.setmaterial(material_name, 'max coefficients', 10)
    fdtd.setmaterial(material_name, 'tolerance', 0.001)
    fdtd.setmaterial(material_name, 'sampled data', sampled_data)
    # fdtd.setmaterial(material_name, 'color', [0.5, 0.5, 1, 0.6])

