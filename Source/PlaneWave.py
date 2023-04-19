# Define Plane Wave used in Lumerical simulations
# 2023-April-6
# function lists:
# PlaneWave

def AddPlaneWave(fdtd, name="Plane1", wavelengnth=[1.5e-6, 1.6e-6], injection_axis="z", direction="Forward",
                x=0, x_span=1e-6, y=0, y_span=1e-6, z=0, z_span=1e-6, angle_theta=0, angle_phi=0, polarization_angle=0):
    # fdtd: the "object" lumapi.FDTD()

    fdtd.addplane()
    fdtd.set("name", name)

    fdtd.set("injection axis", injection_axis)
    fdtd.set("direction", direction)
    fdtd.set("angle theta", angle_theta)
    fdtd.set("angle phi", angle_phi)
    fdtd.set("polarization angle", polarization_angle)


    if injection_axis=="x":
        fdtd.set("x", x)
        # fdtd.set("x span", x_span)
        fdtd.set("y", y)
        fdtd.set("y span", y_span)
        fdtd.set("z", z)
        fdtd.set("z span", z_span)
    if injection_axis=="y":
        fdtd.set("x", x)
        fdtd.set("x span", x_span)
        fdtd.set("y", y)
        # fdtd.set("y span", y_span)
        fdtd.set("z", z)
        fdtd.set("z span", z_span)
    if injection_axis=="z":
        fdtd.set("x", x)
        fdtd.set("x span", x_span)
        fdtd.set("y", y)
        fdtd.set("y span", y_span)
        fdtd.set("z", z)
        # fdtd.set("z span", z_span)

    fdtd.set("wavelength start", wavelengnth[0])
    fdtd.set("wavelength stop", wavelengnth[1])







