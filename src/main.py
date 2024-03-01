import time
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from threading import Thread
import subprocess


class ChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chart App")

        # チャートの初期データ
        self.data = []

        # チャートの作成
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Time (HH:mm:ss)")
        self.ax.set_ylabel("Temperature")
        self.ax.set_xlim(0, 30)
        self.ax.set_ylim(0, 100)
        self.line, = self.ax.plot([], [], 'b-')

        # チャートを表示するキャンバス
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # チャートをクリアするボタン
        self.clear_button = tk.Button(self.root, text="Clear Chart", command=self.clear_chart)
        self.clear_button.pack(side=tk.BOTTOM)

        # データを非同期で追加する処理を開始
        self.thread = Thread(target=self.add_data)
        self.thread.start()

    def add_data(self):
        while True:
            # ラズパイのCPU温度を取得するコマンドを実行
            result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)

            # 出力から温度値を抽出
            output = result.stdout.strip()
            temperature = float(output.split('=')[1].split('\'')[0])

            # データを追加
            self.data.append(temperature)

            # チャートを更新
            self.line.set_data(range(len(self.data)), self.data)
            self.ax.set_xlim(max(0, len(self.data) - 30), len(self.data))
            self.canvas.draw()

            # 1秒待機
            time.sleep(1)

    def clear_chart(self):
        # チャートのデータをクリア
        self.data = []

        # チャートを更新
        self.line.set_data([], [])
        self.ax.set_xlim(0, 30)
        self.ax.set_ylim(0, 100)
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = ChartApp(root)
    root.mainloop()
