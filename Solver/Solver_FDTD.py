# Define simulation parameters used in Lumerical simulations
# 2023-April-11
# function lists:
# Solver_FDTD_3D


def AddSolver_FDTD_3D(fdtd, sim_time=1000, x=0, x_span=1e-6, y=0, y_span=1e-6, z=0, z_span=1e-6,
                      mesh_type="auto non-uniform", mesh_order=2, mesh_refinement="conformal variant 0",
                      x_min_bc="PML", x_max_bc="PML", y_min_bc="PML", y_max_bc="PML",  z_min_bc="PML", z_max_bc="PML",
                      symmetry_on_boundaries=0, boundaries_layers=8):
    # fdtd: the "object" lumapi.FDTD()

    fdtd.addfdtd()
    fdtd.set("dimension", "3D")
    fdtd.set("simulation time", sim_time)
    fdtd.set("x", x)
    fdtd.set("x span", x_span)
    fdtd.set("y", y)
    fdtd.set("y span", y_span)
    fdtd.set("z", z)
    fdtd.set("z span", z_span)
    fdtd.set("mesh type", mesh_type)
    fdtd.set("mesh accuracy", mesh_order)
    fdtd.set("mesh refinement", mesh_refinement)
    fdtd.set("x min bc", x_min_bc)
    fdtd.set("x max bc", x_max_bc)
    fdtd.set("y min bc", y_min_bc)
    fdtd.set("y max bc", y_max_bc)
    fdtd.set("z min bc", z_min_bc)
    fdtd.set("z max bc", z_max_bc)
    fdtd.set("allow symmetry on all boundaries", symmetry_on_boundaries)
    fdtd.set("pml layers", boundaries_layers)


