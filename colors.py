from flask import Flask
from flask import render_template
import random
import numpy as np
from PIL import Image

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/img")
def image():

    # HSVの場合
    # line_data = np.arange(256)
    value = random.randint(0, 255)

    line_data = np.full(256, value)

    hue = np.tile(
        line_data, (256, 1)
    )  # 255x255の2次元配列を生成 [0,1..,254,255],[0,1..,254,255]
    sat = np.transpose(hue)  # hueの配列の行と列を入れ替え [0 0],[1,1],[254,254],[255,255]
    val = np.full_like(
        hue, 255
    )  # hueと同じ構造とデータ型を生成 [255,255],[255,255]..,[255,255],[255,255]

    mat = np.stack([hue, sat, val], 2)  # 3つの2次元配列を結合して3次元配列にする axisで結合の階層を指定
    im = Image.fromarray(np.uint8(mat), "HSV")

    im_rgb = im.convert("RGB")  # HSVからRGBに変換
    im_rgb.save("static/images/color.png")
    return render_template("img.html")


if __name__ == "__main__":
    app.run(debug=True)
