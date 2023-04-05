import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from ftplib import FTP
import requests
from PIL import ImageTk, Image
import os 

##############################################################################

def connect():
    ip = ip_entry.get()
    port = port_entry.get()
    ftp = FTP()
#    ftp.login(user="root", passwd="root")
    try:
        ftp.connect(ip, int(port)) 
        # Ajouter ici le code pour se connecter à la PS3 avec ftplib
        messagebox.showinfo(f"Info", "Successful connection")
        requests.get(f"http://{ip_entry.get()}/notify.ps3mapi?msg=Ps3 Console Api Connected!&icon=22&snd=1")

    except:
        messagebox.showerror("Error", "Connection failed\nCheck console IP | Ex. 192.168.0.24")

def select_file():
    filename = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

def file_send_connect():
    ip2 = ip_entry.get()
    port2 = port_entry.get()
    ps3 = FTP()
    ps3.connect(ip2, int(port2))
    ps3.login()

    filename = file_entry.get()
    remote_dir = remote_dir_entry.get()

    try:
        ps3.cwd(remote_dir)
        with open(filename, 'rb') as f:
            remote_filename = filename.split('/')[-1]
            ps3.storbinary(f'STOR {remote_filename}', f)
        messagebox.showinfo(f"Info", "successful transfer")
    except:
        messagebox.showerror(f"Error", "transfer failed\n- Check destination url \nEx. dev_hdd0/folder, dev_usb000/dossier")


##############################################################################

root = tk.Tk()

root.title("Ps3 Control API [By Sandax]")
root.geometry("354x428")
root.iconbitmap('Resources/logo_PS3_Control_API.ico')
root.resizable(0, 0)

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

tab_control.add(tab1, text=' Connect ')
tab_control.add(tab2, text=' Leds ')
tab_control.add(tab3, text=' Buzzer ')
tab_control.add(tab4, text=' Notify ')
tab_control.add(tab5, text=' File PC->PS3 ')
tab_control.add(tab6, text=' Crédit ')

#####################################################

image1 = Image.open("Resources/2.png")
photo1 = ImageTk.PhotoImage(image1)
label1 = tk.Label(tab1, image=photo1)
label1.image = photo1
label1.place(x=0, y=0)

image2 = Image.open("Resources/4.png")
photo2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(tab2, image=photo2)
label2.image = photo2
label2.place(x=0, y=0)

image3 = Image.open("Resources/5.png")
photo3 = ImageTk.PhotoImage(image3)
label3 = tk.Label(tab3, image=photo3)
label3.image = photo3
label3.place(x=0, y=0)

image4 = Image.open("Resources/6.png")
photo4 = ImageTk.PhotoImage(image4)
label4 = tk.Label(tab4, image=photo4)
label4.image = photo4
label4.place(x=0, y=0)

image5 = Image.open("Resources/7.png")
photo5 = ImageTk.PhotoImage(image5)
label5 = tk.Label(tab5, image=photo5)
label5.image = photo5
label5.place(x=0, y=0)

image6 = Image.open("Resources/8.png")
photo6 = ImageTk.PhotoImage(image6)
label6 = tk.Label(tab6, image=photo6)
label6.image = photo6
label6.place(x=0, y=0)

##############################################################################
# Onglet 1

ip_entry = tk.Entry(tab1)
ip_entry.place(x=110, y=65)

port_entry = tk.Entry(tab1)
port_entry.place(x=110, y=130)

connect_button = tk.Button(tab1, text="Connect", command=connect)
connect_button.place(x=140, y=170)

##############################################################################

def open_color_link():
    color = color_var.get()
    if color == "Green":
        requests.get(f"http://{ip_entry.get()}/led.ps3mapi?color=0&mode=0")
        

    elif color == "Red":
        requests.get(f"http://{ip_entry.get()}/led.ps3mapi?color=1&mode=0")


    elif color == "Yellow":
        requests.get(f"http://{ip_entry.get()}/led.ps3mapi?color=2&mode=1")


    elif color == "Off":
        requests.get(f"http://{ip_entry.get()}/led.ps3mapi?color=1&mode=0")

# Onglet 2
color_var = tk.StringVar()
color_menu = ttk.Combobox(tab2, textvariable=color_var, state='readonly')
color_menu['values'] = ("Green", "Red", "Yellow", "Off")
color_menu.current(0)
color_menu.place(x=100, y=90)

color_button = tk.Button(tab2, text="Set LED", command=open_color_link)
color_button.place(x=150, y=120)

##############################################################################

def open_bip_link():
    bip = bip_var.get()
    if bip == "Bip":
        requests.get(f"http://{ip_entry.get()}/buzzer.ps3mapi?snd=1")
    elif bip == "Double Bip":     
        requests.get(f"http://{ip_entry.get()}/buzzer.ps3mapi?snd=2")
    elif bip == "Triple Bip":
        requests.get(f"http://{ip_entry.get()}/buzzer.ps3mapi?snd=3")

# Onglet 3
bip_var = tk.StringVar()
bip_menu = ttk.Combobox(tab3, textvariable=bip_var, state='readonly')
bip_menu['values'] = ("Bip", "Double Bip", "Triple Bip")
bip_menu.current(0)
bip_menu.place(x=105, y=90)

bip_button = tk.Button(tab3, text="Set BIP", command=open_bip_link)
bip_button.place(x=150, y=120)
##############################################################################
# Onglet 4

def send_Notify():
    text_notify = text_entry.get("1.0", tk.END)
    requests.get(f"http://{ip_entry.get()}/notify.ps3mapi?msg={text_notify}&icon={icon_entry.get()}&snd=1")

text_entry = tk.Text(tab4, height=3, width=20)
text_entry.place(x=92, y=65)

icon_entry = tk.Entry(tab4)
icon_entry.place(x=114, y=170)

text_button = tk.Button(tab4, text="Send Notify", command=send_Notify)
text_button.place(x=147, y=200)

##############################################################################
# ongelt 5
file_entry = ttk.Entry(tab5)
file_entry.place(x=110, y=85)

select_button = ttk.Button(tab5, text='Select File', command=select_file)
select_button.place(x=135, y=113)

remote_dir_entry = ttk.Entry(tab5)
remote_dir_entry.place(x=110, y=205)

transfer_button = ttk.Button(tab5, text='Send File', command=file_send_connect)
transfer_button.place(x=135, y=230)

##############################################################################

tab_control.pack(expand=1, fill='both')
root.mainloop()

# le code n'est vraiment pas optimisé / the code is really not optimized
# but plz stars :')