# https://github.com/python-pillow/Pillow
# pip install pillow

import sys
import os
from PIL import Image


def resize_images(input_folder, output_folder, rate):
    # 入力フォルダー内のすべてのPNGファイルを処理
    count = 0
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".png"):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name)

            with Image.open(input_file) as img:
                size = ((int)(img.width * rate), (int)(img.height * rate))
                resized_img = img.resize(size)
                resized_img.save(output_file, format="PNG")
            print("リサイズ完了:", output_file)
            count = count + 1
    print(f"{count} files were resized.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "使い方: python scripts\\resize_images.py <input_folder> <output_folder> [<rate>]"
        )
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        rate = 0.25
        if 3 < len(sys.argv):
            rate = float(sys.argv[3])

        # 出力フォルダーが存在しない場合は作成
        os.makedirs(output_folder, exist_ok=True)

        resize_images(input_folder, output_folder, rate)
