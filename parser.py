import argparse

from gen_input import gen_tev, gen_dne, gen_config, gen_dim, gen_energymesh


PARSER_ARGS = [
    ("-d", 3, float, ("MIN", "MAX", "N"), "set plasma electronic density", gen_dne),
    ("-t", 3, float, ("MIN", "MAX", "N"), "set temperature density (in eV)", gen_tev),
    ("-e", 3, float, ("MIN", "MAX", "N"), "set energy grid (in eV)", gen_energymesh),
    ("-l", 1, int, "LENGTH", "set characteristic plasma length (in um)", gen_dim),
    ("-c", 3, str, ("ELEM", "APROX", "SYM"), "change .config file", gen_config),
]


def get_pyabako_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pyABAKO v(1.0.0)",
        description="A python interface for ABAKO.",
    )

    for args in PARSER_ARGS:
        flag, nargs, type, metavar, help, _ = args
        parser.add_argument(flag, nargs=nargs, type=type, metavar=metavar, help=help)

    return parser
