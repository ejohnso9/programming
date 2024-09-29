#!/usr/bin/env python
# file: PE_format.py

"""
DESCRIPTION
    This is my own Python programming for exploring issues about C
    programs and C executables. For example, trying to unwind the
    PE/COFF format and understand what is in an .exe at the binary
    level.

"""


# GLOBAL DATA
NORMAL_EXIT = 0  # main() int return code
# msvc_dir = r'/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.39.33519/bin/Hostx64/x64'



# Standard Python Libraries
from glob import glob
from pathlib import Path
import sys


def getExeBytes(path: Path):
    with open(path, 'rb') as fd:
        bytes = fd.read()

    return bytes


def main(exe_path: Path) -> int:
    print('main():')
    print(f"    exe_path is: '{exe_path}'")

    # files = glob(str(exe_path.parent) + '/*.exe')
    # print(files)

    bytes = getExeBytes(exe_path)
    P = ord('P')

    print("PE offset: " + str(bytes[60: 64]))
    print(bytes.index(P))

    print("EXE bytes[0xd0:0xdf]: " + str(bytes[0xd0:0xdf+1]))
    print("EXE bytes[0xf0:0xff]: " + str(bytes[0xf0:0xff+1]))

    return NORMAL_EXIT


if __name__ == '__main__':
    # path = Path('C:\\') / msvc_dir
    dir_path = Path('/home/ej/bin')
    print(dir_path)
    try:
        assert dir_path.is_dir()
    except AssertionError as ae_x:
        print(f'AssertionError: {ae_x}')

    exe_path = dir_path / 'dumpbin.exe'
    rc = main(exe_path)
    sys.exit(rc)

# EOF

