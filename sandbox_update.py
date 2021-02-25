#!/bin/python3

import os
import shutil

USERNAME="donkerevader"

HOME = f"/home/{USERNAME}"
SANDBOX_DIR = f"{HOME}/sandbox"

files = os.listdir(HOME)
if "sandbox" in files:
	shutil.rmtree(SANDBOX_DIR)

os.mkdir(SANDBOX_DIR)
