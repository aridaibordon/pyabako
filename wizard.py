import numpy as np

from run import run
from constants import ABAKO_PATH, CONFIG_FILE, INP_DIR
from gen_input import gen_cond, gen_config, gen_energymesh


def wizard_run() -> None:
    mode = input("Select abako mod (0 or 1): ")
    print()

    if not mode.isdigit():
        print("Option not valid. Exiting.")

    run(run_grid=int(mode))


def wizard_config() -> None:
    print("Generating configuration file.\n")

    elem = input(f"Set element: ")
    cond = input(f"Set plasma model: ")
    sym = input(f"Set symmetry: ")

    gen_config(CONFIG_FILE, elem, cond, sym)
    print()
    print("Configuration file generated.")


def wizard_cond() -> None:
    print("Generating input conditions file.\n")

    print("Temperature range:")
    min_tev = input(f"\tmin: ")
    max_tev = input(f"\tmax: ")
    n_tev = input(f"\tnumber of divisions: ")

    tev = np.linspace(float(min_tev), float(max_tev), int(n_tev))

    print()
    print("Density range:")
    min_dne = input(f"\tmin: ")
    max_dne = input(f"\tmax: ")
    n_dne = input(f"\tnumber of divisions: ")

    dne = 10 ** np.linspace(
        np.log10(float(min_dne)), np.log10(float(max_dne)), int(n_dne)
    )

    gen_cond(INP_DIR, tev, dne)

    print()
    print("Conditions file generated.")


def wizard_energymesh() -> None:
    print("Generating input energy mesh file.\n")

    print("Energy range:")
    min_e = input(f"\tmin: ")
    max_e = input(f"\tmax: ")
    n_e = input(f"\tnumber of divisions: ")

    energymesh = np.linspace(min_e, max_e, n_e)

    gen_energymesh(INP_DIR, energymesh)

    print()
    print("Energy mesh file generated.")


def main():
    print("pyABAKO wizard\n")
    print("[1] Run ABAKO.")
    print("[2] Create new config file.")
    print("[3] Modify temperature and density conditions.")
    print("[4] Modify energy grid.")
    print()

    option = input("Select an option: ")

    print()
    if not option.isdigit():
        print("Option not valid. Exiting.")
        return

    match int(option):
        case 1:
            wizard_run()
        case 2:
            wizard_config()
        case 3:
            wizard_cond()
        case 4:
            wizard_energymesh()
        case other:
            print("Option not recognised. Exiting")
