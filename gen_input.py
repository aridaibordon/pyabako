from os.path import join
from constants import DEFAULT_ELEM, DEFAULT_COND, DEFAULT_SYM, DNE_FNAME, TEV_FNAME, PHO_FNAME, CON_FNAME


def gen_cond(
        path: str,
        data_tev: list,
        data_dne: list,
        ) -> None:
    """Generate plasma conditions input files"""
    ndata_tev, ndata_dne = len(data_tev), len(data_dne)
    with open(join(path, DNE_FNAME), "w") as f_dne:
        f_dne.write(f"  {ndata_dne}\n")
        for dne in data_dne:
            f_dne.write(f"   {dne:.5e}\n")

    with open(join(path, TEV_FNAME), "w") as f_tev:
        f_tev.write(f"  {ndata_tev}\n")
        for tev in data_tev:
            f_tev.write(f"   {tev:.2f}\n")


def gen_config(
    path: str,
    elem: str = DEFAULT_ELEM,
    cond: str = DEFAULT_COND,
    sym: str = DEFAULT_SYM,
) -> None:
    """Generate configuration file"""
    with open(path, "w") as f:
        f.write(f"N {cond} Y {sym} E\n\n")
        f.write(f"{elem:<2} {6:>2} {0:>2}\n\n")
        f.write("IP")


def gen_dim(path: str, dim: int):
    """Generate characteristic plasma length file"""
    with open(join(path, CON_FNAME), "w") as f_con:
        f_con.write(1)
        f_con.write(f"0d0 0d0 {dim}d0")


def gen_energymesh(path: str, data_pho: list) -> None:
    """Generate energy mesh file"""
    ndata_pho = len(data_pho)
    with open(join(path, PHO_FNAME), "w") as f:
        f.write(f"{ndata_pho}\n")
        for pho in data_pho:
            f.write(f"   {pho:.7e}\n")
