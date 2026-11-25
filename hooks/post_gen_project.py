import subprocess

MESSAGE_COLOR = "\x1b[34m"  # Azul
RESET_COLOR = "\x1b[0m"     # Restablecer color

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_COLOR}")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])

print(f"{MESSAGE_COLOR}The begining of your destiny is defined now! Create and have fun!{RESET_COLOR}")
