# Define monitor for single component used in Lumerical simulations
# 2023-April-6
# function lists:
# FrequencyPower_SingleComponent, Frequency_SingleComponent


##  Frequency-Domain Field and Power
def AddFrequencyPower_SingleComponent(fdtd, name="power1", monitor_type="X_Normal",
                                      x=0, x_span=1e-6, y=0, y_span=1e-6, z=0, z_span=1e-6,
                                      f_points=50):
    # fdtd: the "object" lumapi.FDTD()
    # structure_size: x_span, y_span, z_span

    fdtd.addpower()
    fdtd.set("name", name)
    fdtd.setglobalmonitor("frequency points", f_points)
    if monitor_type=="X_Normal":
        fdtd.set("x", x)
        # fdtd.set("x span", x_span)
        fdtd.set("y", y)
        fdtd.set("y span", y_span)
        fdtd.set("z", z)
        fdtd.set("z span", z_span)
    elif monitor_type=="y_Normal":
        fdtd.set("x", x)
        fdtd.set("x span", x_span)
        fdtd.set("y", y)
        # fdtd.set("y span", y_span)
        fdtd.set("z", z)
        fdtd.set("z span", z_span)
    elif monitor_type == "z_Normal":
        fdtd.set("x", x)
        fdtd.set("x span", x_span)
        fdtd.set("y", y)
        fdtd.set("y span", y_span)
        fdtd.set("z", z)
        # fdtd.set("z span", z_span)
    elif monitor_type == "3D":
        fdtd.set("x", x)
        fdtd.set("x span", x_span)
        fdtd.set("y", y)
        fdtd.set("y span", y_span)
        fdtd.set("z", z)
        fdtd.set("z span", z_span)
    elif monitor_type == "Linear_X":
        fdtd.set("x", x)
        fdtd.set("x span", x_span)
        fdtd.set("y", y)
        # fdtd.set("y span", y_span)
        fdtd.set("z", z)
        # fdtd.set("z span", z_span)
    elif monitor_type == "Linear_Y":
        fdtd.set("x", x)
        # fdtd.set("x span", x_span)
        fdtd.set("y", y)
        fdtd.set("y span", y_span)
        fdtd.set("z", z)
        # fdtd.set("z span", z_span)
    elif monitor_type == "Linear_Y":
        fdtd.set("x", x)
        # fdtd.set("x span", x_span)
        fdtd.set("y", y)
        # fdtd.set("y span", y_span)
        fdtd.set("z", z)
        fdtd.set("z span", z_span)
    else:
        fdtd.set("x", x)
        # fdtd.set("x span", x_span)
        fdtd.set("y", y)
        # fdtd.set("y span", y_span)
        fdtd.set("z", z)
        # fdtd.set("z span", z_span)


##  Frequency-Domain Field Profile
def AddFrequency_SingleComponent(fdtd, ):
    # fdtd: the "object" lumapi.FDTD()
    # structure_size: x_span, y_span, z_span

    fdtd.add


















