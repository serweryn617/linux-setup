import shutil
from pathlib import Path


def copy_item(src_path, dst_path, clear_dir=True):
    print('Copying', src_path.name)

    if src_path.is_file():
        shutil.copy(src_path, dst_path)
    elif src_path.is_dir():
        if clear_dir and dst_path.is_dir():
            shutil.rmtree(dst_path)
        shutil.copytree(src_path, dst_path, copy_function=shutil.copy, dirs_exist_ok=True)
    else:
        raise FileNotFoundError(src_path)
