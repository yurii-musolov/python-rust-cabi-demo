import ctypes
import platform
from pathlib import Path


def get_library_name() -> str:
    system: str = platform.system()

    if system == "Linux":
        return "librustlib.so"

    if system == "Darwin":
        return "librustlib.dylib"

    if system == "Windows":
        return "rustlib.dll"

    raise RuntimeError(f"Unsupported OS: {system}")


ROOT: Path = Path(__file__).resolve().parent.parent

LIB_PATH: Path = (
    ROOT
    / "rustlib"
    / "target"
    / "release"
    / get_library_name()
)

rustlib = ctypes.CDLL(str(LIB_PATH))

rustlib.sum_of_squares.argtypes = [ctypes.c_uint64]
rustlib.sum_of_squares.restype = ctypes.c_uint64


def sum_of_squares_rust(limit: int) -> int:
    return int(rustlib.sum_of_squares(limit))