import subprocess
import os
import platform

# I'll extend this to more distros in the future.
software = {
    "Linux": ["neovim-bin", "bpython", "tmux", "github-cli", "pix", "lua-language-server"]
}

window_managers = ["hyprland", "i3"]

# Exclude non-config files and special cases
special = ["home", "systemd"]
excluded = ["README.md", ".git", ".gitmodules"]
excluded.extend(special)

operating_system = platform.system()
software = " ".join(software[operating_system])

print(software)

# subprocess.run(["pacman", "-Syu", "yay"])
# subprocess.run(["yay", "-S", software])

print("Supported window managers: ")
print("\n".join(window_managers))

window_manager = input("\nChoose via full name (e.g i3): ")

os.chdir("..")

cwd = os.getcwd()
home = "/".join(cwd.split("/")[1:3])

for file in os.listdir():
    paths = []
    if file not in excluded:
        paths.append(f"{os.getcwd()}/{file}/")

    # Creating the symlinks for files whose configuration
    # lives in ~/.config/
    for path in paths:
        print(f"ln -s {path} {home}/.config/{file}")
