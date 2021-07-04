import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # 1. text Widgetの作成
        # frame Widget(Frame)を親要素として、text Widgetを作成する。
        # height : 高さを設定
        # Textについて : https://kuroro.blog/python/bK6fWsP9LMqmER1CBz9E/
        text = tk.Text(frame, height=4)

        # 2. scrollbar Widgetの作成
        # frame Widget(Frame)を親要素として、scrollbar Widgetを作成する。
        # orient option : 垂直scrollbarを作成するため、tk.VERTICALを設定。水平scrollbarの場合は、tk.HORIZONTALを設定する。
        # command option : scrollbar Widgetを動かした場合に、連動して表示する内容を設定。今回は、text Widgetをy軸方向に動かした内容を表示する。
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)

        # 3. scrollbar Widgetをtext Widgetに反映する
        # scrollbar Widgetの設定内容をtext Widgetと紐付ける。
        # yscrollcommand : text Widget内で上下移動した場合に、scrollbarが追従するように設定する。
        text["yscrollcommand"] = scrollbar.set

        # 4. text Widget, scrollbar Widgetを配置
        # frame Widget(Frame)を親要素とした場合に、text Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        text.grid(row=0, column=0)
        # frame Widget(Frame)を親要素とした場合に、scrollbar Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
