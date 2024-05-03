#!/usr/bin/env python3

from lilaclib import aur_pre_build
from lilaclib import edit_file


def pre_build():
    aur_pre_build()
    for line in edit_file("PKGBUILD"):
        if line.startswith("_py="):
            line = "_py=cp312"
        print(line)
