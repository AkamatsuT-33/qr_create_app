#### インポート ####
import tkinter as tk
import tkinter.ttk as ttk
import qrcode
from PIL import ImageTk, Image
from tkinter import filedialog
from os.path import expanduser

#### rootの設定 ####
root = tk.Tk()
root.title(u'QR Create App')
root.geometry('415x500')
root.resizable(False, False)

#### 関数 ####
def update_canvas(img):
    global qr, qr_img
    qr_img = ImageTk.PhotoImage(img, width=110, height=110)
    qr.create_image(0, 0, image=qr_img, anchor=tk.NW, tag='q')
    qr.update()

def img_save(img):
    folder = expanduser("~")
    _file = filedialog.asksaveasfilename(initialdir = str(folder) + '\Downloads', initialfile = 'qrcode_image.png', filetypes=[('QRコード画像', '.png')])
    print(_file)
    if _file:
        img.save(_file)
    else:
        pass

def qr_qreate_show():
    url = entry.get()

    code = qrcode.QRCode(version=10,
                        error_correction=qrcode.constants.ERROR_CORRECT_Q,
                        box_size=6,
                        border=5)
    
    code.add_data(url)
    img = code.make_image(fill_color='black', back_color='white')
    update_canvas(img)

def qr_qreate_save():
    url = entry.get()
    print(url)

    code = qrcode.QRCode(version=10,
                        error_correction=qrcode.constants.ERROR_CORRECT_Q,
                        box_size=6,
                        border=5)
    
    code.add_data(url)
    img = code.make_image(fill_color='black', back_color='white')
    update_canvas(img)
    img_save(img)

def str_clear():
    global entry
    qr.delete('q')
    sv.set('')

#### ウィジェット・変数 ####
qr_img = None
qr = tk.Canvas(root, width=400, height=400, bg="lightgray")
sv = tk.StringVar()
entry = ttk.Entry(root, text="URL", textvariable=sv, width=34)
btn_0 = ttk.Button(root, text='Clear', command=str_clear, width=10)
btn_1 = ttk.Button(root, text='Create', command=qr_qreate_show, width=20)
btn_2 = ttk.Button(root, text='Save', command=qr_qreate_save, width=10)


#### 設置 ####
qr.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W + tk.E)
btn_0.grid(row=1, column=3, columnspan=1, padx=5, pady=5, sticky=tk.W + tk.E)
btn_1.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W + tk.E)
btn_2.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky=tk.W + tk.E)


root.mainloop()
