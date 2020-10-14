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
    if (directory == 'Select folder...'):
        eel.show_confirmation("Select folder first!")
        return
    eel.show_confirmation("Make sure the PSV has FTP turned on")
    port = int(port)
    print(ps_vita_ip)
    print(port)
    print(directory)
    ftp = ftp_downloader.start_ftp(ps_vita_ip, port)
    if (ftp):
        print(ftp)
        nomes = ftp_downloader.scan_dirs(ftp)
        ftp_downloader.download_icons(ftp, nomes, directory)
        ftp_downloader.close_conn(ftp)
        print("All files downloaded successfully")
        eel.show_confirmation("All files downloaded successfully")
    else:
        print("There's something wrong FTPWise")
        eel.show_confirmation("Sorry, couldn't complete your request")
       

eel.init("_view")
eel.start("index.html", size=(800,423))