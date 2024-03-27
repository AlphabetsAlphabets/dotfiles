import platform

software = {
    "Linux": ["neovim-bin", "bpython", "tmux", "github-cli", "pix", "lua-language-server"]
}

operating_system = platform.system()
software = " ".join(software[operating_system])
print(software)
