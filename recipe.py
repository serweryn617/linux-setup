# Cooking recipe, checkout Cook at https://github.com/serweryn617/cook

from pathlib import Path

base_path = Path(__file__).parent.resolve()

default_build_server = 'local'

projects = {}

projects['alacritty'] = (
    'mkdir -p ~/.config/alacritty',
    f'ln -s {base_path}/config/alacritty/alacritty.toml ~/.config/alacritty/alacritty.toml',
)

projects['bash'] = (
    f'ln -s {base_path}/config/bash/bash_aliases ~/.bash_aliases',
    f'ln -s {base_path}/config/bash/inputrc ~/.inputrc',
    'cat config/bash/bashrc_additional >> ~/.bashrc',
)

projects['git'] = (
    f'git config --global --add include.path {base_path}/config/git/gitconfig',
)

projects['i3'] = (
    'mkdir -p ~/.config/i3',
    f'ln -s {base_path}/config/i3/config ~/.config/i3/config',
)

projects['libinput'] = (
    f'ln -s {base_path}/config/libinput-gestures/libinput-gestures.conf ~/.config/libinput-gestures.conf',
)

projects['picom'] = (
    'mkdir -p ~/.config/picom',
    f'ln -s {base_path}/config/picom/picom.conf ~/.config/picom/picom.conf',
)

projects['scripts'] = (
    f'ln -s {base_path}/config/scripts ~/.config/scripts',
)

projects['starship'] = (
    f'ln -s {base_path}/config/starship/starship.toml ~/.config/starship.toml',
)

projects['systemd'] = (
    f'sudo ln -s {base_path}/config/systemd/battery-charge-threshold.service /etc/systemd/system/battery-charge-threshold.service',
)

projects['xorg'] = (
    f'sudo ln -s {base_path}/config/xorg/20-natural-scrolling.conf /etc/X11/xorg.conf.d/',
)
