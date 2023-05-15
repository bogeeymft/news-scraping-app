import feedparser
from tkinter import *
import webview


def default_color_button():
    btn_gundem.configure(bg="blue")
    btn_saglik.configure(bg="blue")
    btn_dunya.configure(bg="blue")
    btn_ekonomi.configure(bg="blue")


def clear_frame():
    for widget in fr_haberler.winfo_children():
        widget.destroy()

def open_url(event):
    webview.create_window(event.widget.cget("text"), event.widget.cget("text"))
    webview.start()


def add_haberler(haberler):
    haber_count = 0
    for haber in haberler.entries:
        haber_count = haber_count + 1
        if haber_count > 2:
            break
        Label(
            fr_haberler, text=haber.title, anchor="w", font=("Helveticabold", 14)
        ).pack(side=TOP, fill="x")
        lbl_link = Label(
            fr_haberler,
            text=haber.link,
            anchor="w",
            font=("Helveticabold", 14),
            fg="blue",
            cursor="hand2",
        )
        lbl_link.pack(side=TOP, fill="x")
        lbl_link.bind("<Button-1>", open_url)
        Label(fr_haberler, text="-", anchor="c", bg="pink").pack(side=TOP, fill="x")


def gundem_command():
    for url in gundem_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)


def dunya_command():
    for url in dunya_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)


def ekonomi_command():
    for url in ekonomi_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)


def saglik_command():
    for url in saglik_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)


gundem_url = [
    "https://www.ntv.com.tr/gundem.rss",
    "https://www.takvim.com.tr/rss/guncel.xml",
    "https://www.yeniakit.com.tr/rss/haber/gundem",
    "https://www.ahaber.com.tr/rss/gundem.xml",
             ]

ekonomi_url = [
    "https://www.ntv.com.tr/ekonomi.rss",
    "https://www.ahaber.com.tr/rss/ekonomi.xml",
    "https://www.cnnturk.com/feed/rss/ekonomi/news",
    "https://www.yeniakit.com.tr/rss/haber/ekonomi",
              ]

saglik_url = [
    "https://www.ntv.com.tr/saglik.rss",
    "https://www.yeniakit.com.tr/rss/haber/saglik",
    "https://www.ahaber.com.tr/rss/saglik.xml",
    "https://www.cnnturk.com/feed/rss/saglik/news",
             ]

dunya_url = [
    "https://www.cnnturk.com/feed/rss/dunya/news",
    "https://www.ntv.com.tr/dunya.rss",
    "http://www.mynet.com/haber/rss/kategori/dunya/",
    "https://www.sabah.com.tr/rss/dunya.xml",
            ]


window = Tk()
window.title("News Bot Programs")
window.geometry("1000x600")

fr_haberler = Frame(window, height=600)
fr_buttons = Frame(window, relief=RAISED, bg="pink", bd=2)

btn_gundem = Button(
    fr_buttons,
    text="Gündem",
    font=("Helveticabold", 14),
    bg="lightblue",
    command=gundem_command,
)
btn_dunya = Button(
    fr_buttons,
    text="Dünya",
    font=("Helveticabold", 14),
    bg="lightblue",
    command=dunya_command,
)
btn_ekonomi = Button(
    fr_buttons,
    text="Ekonomi",
    font=("Helveticabold", 14),
    bg="lightblue",
    command=ekonomi_command,
)
btn_saglik = Button(
    fr_buttons,
    text="Sağlık",
    font=("Helveticabold", 14),
    bg="lightblue",
    command=saglik_command,
)

btn_gundem.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_dunya.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_ekonomi.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_saglik.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
fr_haberler.grid(row=0, column=1, sticky="nsew")

window.mainloop()
