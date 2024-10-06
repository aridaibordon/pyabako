import os
import wizard

import numpy as np

from constants import INP_DIR, CONFIG_FILE
from parser import PARSER_ARGS, get_pyabako_parser


def manage_parse_key_args(key: str, kargs: list[float | str], flag_cmd_dict: dict[function]) -> None:
    flag_cmd = flag_cmd_dict[key]
    if key in ["d", "t", "e"]:
        min, max, n = kargs

        if key == "d":
            data_range = 10 ** np.linspace(np.log10(min), np.log10(max), int(n))
        else:
            data_range = np.linspace(min, max, int(n))

        flag_cmd(INP_DIR, data_range)

    if key in ["l"]:
        flag_cmd(INP_DIR, *kargs)

    if key in ["c"]:
        elem, aprox, sym = kargs
        flag_cmd(CONFIG_FILE, elem, aprox, sym)


def main() -> None:
    parser = get_pyabako_parser()
    args = vars(parser.parse_args())

    # run default wizard if not args are provided
    if not any(args.values()):
        wizard.main()

    # otherwise run flag specific command
    flag_cmd_dict = {key: arg[-1] for key, arg in zip(args, PARSER_ARGS)}
    for key in args:
        kargs = args.get(key, None)
        if kargs:
            manage_parse_key_args(key, kargs, flag_cmd_dict)


if __name__ == "__main__":
    main()
