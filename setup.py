import sys
from cx_Freeze import setup, Executable

# List all the packages and modules you want to include
build_exe_options = {
    "packages": ["os"],
    "includes": ["pandas", "selenium"],
}

setup(
    name="Meu App",
    version="0.1",
    description="Minha 1° Aplicação!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)
