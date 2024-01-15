from pathlib import Path

from copy_item import copy_item
from config_item_paths import config_item_paths


def backup(items):
    for src_path, dst_path in items:
        src_path = Path(src_path).expanduser().resolve()
        dst_path = Path(__file__).parent / dst_path
        
        # removed files will be left in the repository
        copy_item(src_path, dst_path)

    print('Backup done!')


if __name__ == '__main__':
    backup(config_item_paths)