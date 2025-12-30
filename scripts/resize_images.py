# https://github.com/python-pillow/Pillow
# pip install pillow

import argparse
import sys
import os
from pathlib import Path
from PIL import Image
from typing import List

def resize_images(input_folder, output_folder, rate):
    # 入力フォルダー内のすべてのPNGファイルを処理
    count = 0
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".png"):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name)

            if os.path.exists(output_file): # ファイルの存在確認
                os.remove(output_file) # ファイルを削除

            with Image.open(input_file) as img:
                size = ((int)(img.width * rate), (int)(img.height * rate))
                resized_img = img.resize(size)
                resized_img.save(output_file, format="PNG")
            print("リサイズ完了:", output_file)
            count = count + 1
    print(f"{count} files were resized.")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Resize images in a folder"
    )

    parser.add_argument(
        "input_folder",
        type=Path,
        help="入力フォルダ"
    )
    parser.add_argument(
        "output_folder",
        type=Path,
        help="出力フォルダ"
    )
    parser.add_argument(
        "rate",
        type=float,
        nargs="?",
        default=0.25,
        help="リサイズ倍率（省略時: 0.25）"
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="サブフォルダを再帰的に検索する"
    )

    return parser.parse_args()

def find_directories(input_folder: Path) -> List[Path]:
    directories = []

    for p in input_folder.iterdir():
        if (
            p.is_dir()
            and not p.name.startswith("resized")
        ):
            directories.append(p.resolve())

    return directories


if __name__ == "__main__":

    args = parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    if args.recursive:
        directories = find_directories(args.input_folder)
        # 出力フォルダーが存在しない場合は作成
        os.makedirs(output_folder, exist_ok=True)
        for input_directory in directories:
            resize_images(input_directory, output_folder, args.rate)
    else:
        # 出力フォルダーが存在しない場合は作成
        os.makedirs(output_folder, exist_ok=True)
        resize_images(input_folder, output_folder, args.rate)
