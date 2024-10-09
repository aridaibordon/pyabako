# PyABAKO: a python interface for ABAKO

## Installation and use
This program requires a python version >= 3.11 and to add manually your global path to ABAKO folder to the `ABAKO_PATH` variable located in the constants.py file.

### The `run` command
By default, `run` allow the use of ABAKO in parallel using MPI. `run` admits additional parameters to alter its behaviour.

- run_grid (bool): Indicates if the input conditionally must be computed in a grid (True) or sequentially (False). Default is False.
- n_cores (int): Number of server cores to use in the computation. Default `N_CORES` defined in src/constants.py.

## PyABAKO wizard
PyABAKO includes a wizard that allows direct use of all its functionalities directly from the terminal. It can be open by calling this package folder using a python version >= 3.11. Additional flags can be supplied to change ABAKO configuration directly from the call. The options are,

- `-c ELEM APROX SYM`: create new configuration file by specifying the element (ELEM), plasma dynamics (APROX) and plasma symmetry (SYM).
- `[-d, -t, -e] MIN MAX N`: set electronic density (-d), temperature (-t) or energy mesh (-e) input files between MIN and MAX with N equispaced samples. Density is equispaced in log scale by default. Temperature and energy are expressed in eV.
- `-l LENGTH`: set plasma characteristic LENGTH in $\mu\text{m}$.