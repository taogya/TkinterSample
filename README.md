# TkinterSample
Tkinterのサンプルプロジェクトです。（ラズパイZero WHにて実験）

## 環境準備
OS Liteの場合，以下を実施します。Normal版は実施不要です。<br>
1. `sudo raspi-config` コマンドにて，VNCを有効化する
1. `/boot/config.txt` ファイル内の以下を修正する。
```
#hdmi_force_hotplug=1
↓
hdmi_force_hotplug=1
```

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