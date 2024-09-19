# PyABAKO: a python interface for ABAKO

## Installation and use
This program requires a python version >= 3.11 and to add manually your global path to ABAKO folder to the `ABAKO_PATH` variable located in the src/constants.py file.

### The `run` command
By default, `run` allow the use of ABAKO in parallel using MPI. `run` admits additional parameters to alter its behaviour.

- run_grid (bool): Indicates if the input conditionally must be computed in a grid (True) or sequentially (False). Default is False.
- n_cores (int): Number of server cores to use in the computation. Default `N_CORES` defined in src/constants.py.
