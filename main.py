import ftp_downloader
import tkinter as tk
from tkinter import filedialog
import eel

@eel.expose
def select_folder():
    root = tk.Tk()
    root.withdraw()
    download_dir = filedialog.askdirectory(parent=root)
    print(download_dir)
    eel.show_path(download_dir)

@eel.expose
def run_app(ps_vita_ip, port, directory):
    port = int(port)
    print(ps_vita_ip)
    print(port)
    print(directory)
    ftp = ftp_downloader.start_ftp(ps_vita_ip, port)
    if (ftp):
        ftp_downloader.create_down_dir(directory)
        nomes = ftp_downloader.scan_dirs(ftp)
        ftp_downloader.download_icons(ftp, nomes, directory)
        print("All files downloaded successfully")
        ftp_downloader.close_conn(ftp)

eel.init("_view")
eel.start("index.html", size=(800,420))