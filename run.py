import os

from constants import (
    OUT_DIR,
    INP_TEV_FILE,
    INP_DNE_FILE,
    ABAKO_EXE,
    MAX_CORES
)


def run(*args, **kwargs) -> None:
    if not os.path.exists(OUT_DIR):
        os.system(f"mkdir {OUT_DIR} | echo 'Creating output folder...'")

    cmd = configure_cmd(*args, **kwargs)
    os.system(cmd)


def configure_cmd(run_grid: bool = False, n_cores: int = MAX_CORES) -> str:
    run_grid = int(run_grid)
    return f"nohup mpirun -n {n_cores} {ABAKO_EXE} -p {run_grid} -tf {INP_TEV_FILE} -df {INP_DNE_FILE} &"
