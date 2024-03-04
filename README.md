# TkinterSample
Tkinterのサンプルプロジェクトです。（ラズパイZero WHにて実験）

## 環境準備
1. リポジトリクローン<br>
  ```sh
  $ sudo apt-get install git
  $ git clone https://github.com/taogya/TkinterSample.git
  $ cd TkinterSample
  ```
2. 必要パッケージのインストール<br>
```sh
$ sudo apt-get install python3-venv python3-tk tk-dev libopenblas-dev
```

> [!NOTE]
> OS Liteの場合，以下を実施します。Normal版は実施不要です。<br>
> - `/boot/config.txt` ファイル内の以下を修正する。<br>
> ```
> #hdmi_force_hotplug=1
> ↓
> hdmi_force_hotplug=1
> ```
> - 以下コマンドにて，デスクトップ環境をインストールする。
> ```sh
> $ sudo apt-get install lightdm xserver-xorg raspberrypi-ui-mods
> ```
> - `sudo raspi-config` コマンドにて，VNCを有効化する。
> - `sudo raspi-config` コマンドにて，`Boot Options`を`Desktop`にする。

## ラズパイの温度をグラフ化
vcgencmdコマンドを使用して温度を取得します。
matplotlibを使用したチャートにそれを表示します。

```sh
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ cd src
$ python main.py
```
