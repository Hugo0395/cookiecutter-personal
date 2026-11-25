
import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"    # Rojo
MESSAGE_COLOR = "\x1b[34m"  # Azul
RESET_COLOR = "\x1b[0m"     # Restablecer color

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: The project slug cannot start with 'x'.{RESET_COLOR}")
    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You are going to create something amazing!")
print(f"Creating project at {os.getcwd()}{RESET_COLOR}")
