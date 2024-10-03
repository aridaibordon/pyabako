from os.path import join


# Default ABAKO folder path
ABAKO_PATH = "/Banco/aridai/abako/"

# Default config parameters
DEFAULT_ELEM = "Ar"
DEFAULT_COND = "N"  # N -> NLTE, L -> LTE, C -> Corona, S -> Spectral
DEFAULT_SYM = "C"

# Machine params
MAX_CORES = 20

# Default file names
TEV_FNAME = "tab_tev.txt"
DNE_FNAME = "tab_dne.txt"
PHO_FNAME = "photonenergymesh.txt"
CON_FNAME = "condiciones.txt"

# Default global pathes
INP_DIR = join(ABAKO_PATH, "input_files")
OUT_DIR = join(ABAKO_PATH, "output_files")
ABAKO_EXE = join(ABAKO_PATH, "abako")
CONFIG_FILE = join(INP_DIR, ".config")
INP_TEV_FILE = join(INP_DIR, TEV_FNAME)
INP_DNE_FILE = join(INP_DIR, DNE_FNAME)
INP_PHO_FILE = join(INP_DIR, PHO_FNAME)
