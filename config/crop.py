#!/usr/bin/env python3


# Wallpapers from:
# https://www.reddit.com/r/wallpapers/comments/c6s990/firewatch/
# https://www.reddit.com/r/wallpapers/comments/v1saxx/constraint_5120x2880_animated_version_in_the/
# https://www.reddit.com/r/wallpapers/comments/1q17i1i/favorites_from_my_wallpaper_collection/
# https://www.reddit.com/r/wallpapers/comments/1qjq6i1/sverre_malling_norwegian_muskox_2018/
# https://programmerhumor.io/vim-memes/i-dont-remember-this-scene-r4cc


import os
from PIL import Image

input_dir = "wallpapers_raw"
output_dir = "wallpapers"
target_width, target_height = (3840, 2160)  # 4K

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)

    if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")):
        print("Skipping", filename)
        continue

    try:
        with Image.open(filepath) as img:
            width, height = img.size

            left = max((width - target_width) // 2, 0)
            top = max((height - target_height) // 2, 0)
            right = min(left + target_width, width)
            bottom = min(top + target_height, height)

            cropped = img.crop((left, top, right, bottom))

            is_4k = cropped.size == (target_width, target_height)

            if cropped.mode != "RGB":
                cropped = cropped.convert("RGB")

            out_name = os.path.splitext(filename)[0] + (' 4K' if is_4k else '') + ".jpg"
            out_path = os.path.join(output_dir, out_name)
            cropped.save(out_path, "JPEG", quality=95)

            print(f"Processed {filename} -> {out_name}")

    except Exception as e:
        print(f"Failed to process {filename}: {e}")
