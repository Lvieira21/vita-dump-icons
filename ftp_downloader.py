import tkinter as tk
import os
from tkinter import filedialog, Text
import eel
from ftplib import FTP #FTP Access
from PIL import Image #resizing

APPMETA_VITA = 'ur0:/appmeta'

def start_ftp(psv_ip, port):
    ftp = FTP()
    try: 
        ftp.connect(psv_ip, port)
        ftp.login()
        print ("Login successfull")
        return ftp
    except:
        close_conn(ftp)
        return False

def scan_dirs(ftp):
    ftp.cwd(APPMETA_VITA)

    pastas = []
    nomes = []
    ftp.dir("", pastas.append) #Get entire path to gameID folders
    
    #Get GameID folder names
    for pasta in pastas:
        pasta = pasta.split()
        nomes.append(pasta[8])

    return nomes

def download_icons(ftp, nomes, download_dir):
    for nome in nomes:
        
        ftp.cwd(nome)
        try:
            ftp.retrbinary("RETR " + 'icon0.png', open(os.path.join(download_dir, nome + '.png'), 'wb').write) #download icon
            print("Game ID{} image downloaded successfully".format(nome))
            imagem = Image.open(os.path.join(download_dir, nome + '.png')) #find downloaded image
            imagem = imagem.resize((512,512))
            imagem.save(os.path.join(download_dir, nome + '.png')) #overwriting resized image onto original
            print("{} resized".format(nome))
            ftp.cwd('..')
        except:
            print("Game ID {} icon was not found".format(nome))
            ftp.cwd('..')


def close_conn(ftp):
    ftp.close()   