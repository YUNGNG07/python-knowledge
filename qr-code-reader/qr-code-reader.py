# Requirements: qrcode, opencv-python, pillow, pyzbar

import cv2
import qrcode
import tkinter as tk
from PIL import Image
from pyzbar import pyzbar
# Widgets styling
from tkinter import ttk
# Browse and specify file paths
from tkinter import filedialog as fd
# Displays additional messages for debugging
from tkinter.messagebox import showinfo, showerror, askyesno


def close_window():
    """
    Confirm with users before closing the window
    """
    if askyesno(title='Close QR Code Generator and Scanner', message='Are you sure you want to close the application?'):
        window.destroy()

def generate_qrcode():
    """
    Function for generating the QR Code
    """
    qrcode_data = str(data_entry.get())
    qrcode_name = str(filename_entry.get())
    if qrcode_name == '':
        showerror(title='Error', message='An error occured.\n' \
                  '\nThe following is the cause:\n   -> Empty filename entry field\n\n' \
                  'Make sure the filename entry field is filled when generating the QRCode.')
    else:
        if askyesno(title='Confirmation', message=f'Do you want to create a QRCode with the provided information?'):
            try:
                qr = qrcode.QRCode(version=1, box_size=6, border=4)
                qr.add_data(qrcode_data)
                qr.make(fit=True)
                name = qrcode_name + '.png'
                qrcode_image = qr.make_image(fill_color='black', back_color='white')
                qrcode_image.save(name)
                global Image
                Image = tk.PhotoImage(file=f'{name}')
                image_label1.config(image=Image)
                reset_button.config(state='normal', command=reset)
            except:
                showerror(title='Error', message='Please provide a valid filename')

def reset():
    """
    Function for resetting or clearing the image label
    """
    if askyesno(title='Reset', message='Are you sure you want to reset?'):
        image_label1.config(image='')
        image_label2.config(image='')
        reset_button.config(state='disabled')
        reset_button2.config(state='disabled')
        data_label.config(text='')
        data_entry.delete(0, 'end')
        filename_entry.delete(0, 'end')
        file_entry.delete(0, 'end')

def open_dialog():
    filetypes = (('PNG extension', '*.png'), ('JPG extension', '*.jpg'), ('JPEG extension', '*.jpeg'), ('All Files', '*.*'))
    name = fd.askopenfilename(title='Select file', filetypes=filetypes)
    file_entry.delete(0, 'end')
    file_entry.insert(0, name)

def detect_qrcode():
    """
    Function to detect QRCode from image
    """
    image_file = file_entry.get()
    if image_file == '':
        showerror(title='Error', message='Please provide a QR Code image file to detect')
    else:
        try:
            global qrcode_image
            qrcode_image = tk.PhotoImage(file=f'{image_file}')
            image_label2.config(image=qrcode_image)

            qr_img = cv2.imread(f'{image_file}')
            data = pyzbar.decode(qr_img)
            for name in data:
                info = name.data.decode('utf-8')
            data_label.config(text=info)
            reset_button2.config(state='normal', command=reset)
        except:
            showerror(title='Error', message='An error occured while detecting data from the provided file.\n' \
                  '\nThe following is the cause:\n   -> Wrong image file\n\n' \
                  'Make sure the image file is a valid QRCode.')

def read_barcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x+6, y-6), font, 1, (255, 255, 255), 1)

        data_label.config(text=barcode_info)

    return frame

def open_camera():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcode(frame)
        cv2.imshow('Real Time QRCode / Barcode Scanner', frame)
        # Close if ESC key is pressed
        if cv2.waitKey(1) & 0xFF == 27 or data_label.cget('text'):
            break

    camera.release()
    cv2.destroyAllWindows()

def copy():
    window.clipboard_clear()
    window.clipboard_append(data_label.cget('text'))
    window.update()


# Initialize Tkinter window
window = tk.Tk()
window.title('QR Code Generator and Scanner')
# Alternate way to display window icon
# icon = tk.PhotoImage(file=r'C:/Users/yungng07/Documents/python-knowledge/qr-code-reader/icons/qr-code.png')
# window.iconphoto(False, icon)
window.iconbitmap(r'C:\Users\yungng07\Documents\python-knowledge\qr-code-reader\icons\icon.ico')
# Dimensions and position of window
window.geometry('500x480+440+180')
window.resizable(height=False, width=False)
window.protocol('WM_DELETE_WINDOW', close_window)

# Styles for the widgets, labels, entries and buttons
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 11))
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font=('DotumChe', 10))

# Create the Notebook widget
tab_control = ttk.Notebook(window)
first_tab = ttk.Frame(tab_control)
second_tab = ttk.Frame(tab_control)
tab_control.add(first_tab, text='QR Code Generator')
tab_control.add(second_tab, text='QR Code Scanner')
tab_control.pack(expand=1, fill='both')

first_canvas = tk.Canvas(first_tab, width=500, height=480)
first_canvas.pack()
second_canvas = tk.Canvas(second_tab, width=500, height=480)
second_canvas.pack()

# Widgets for first tab
image_label1 = ttk.Label(window)
first_canvas.create_window(250, 150, window=image_label1)

qrdata_label = ttk.Label(window, text='QRcode Data', style='TLabel')
data_entry = ttk.Entry(window, width=55, style='TEntry')
first_canvas.create_window(70, 330, window=qrdata_label)
first_canvas.create_window(300, 330, window=data_entry)

filename_label = ttk.Label(window, text='Filename', style='TLabel')
filename_entry = ttk.Entry(window, width=55, style='TEntry')
first_canvas.create_window(84, 360, window=filename_label)
first_canvas.create_window(300, 360, window=filename_entry)

reset_button = ttk.Button(window, text='Reset', style='TButton', state='disabled')
generate_button = ttk.Button(window, text='Generate QRCode', style='TButton', command=generate_qrcode)
first_canvas.create_window(300, 390, window=reset_button)
first_canvas.create_window(410, 390, window=generate_button)

# Widgets for second tab
image_label2 = ttk.Label(window)
data_label = ttk.Label(window)
second_canvas.create_window(250, 150, window=image_label2)
second_canvas.create_window(250, 300, window=data_label)

file_entry = ttk.Entry(window, width=60, style='TEntry')
browse_button = ttk.Button(window, text='Browse', style='TButton', command=open_dialog)
second_canvas.create_window(200, 350, window=file_entry)
second_canvas.create_window(430, 350, window=browse_button)

detect_button = ttk.Button(window, text='Scan QRCode', style='TButton', command=detect_qrcode)
second_canvas.create_window(65, 385, window=detect_button)
camera_button = ttk.Button(window, text='Turn On Camera', style='TButton', command=open_camera)
second_canvas.create_window(175, 385, window=camera_button)
copy_button = ttk.Button(window, text='Copy', style='TButton', command=copy)
second_canvas.create_window(277, 385, window=copy_button)
reset_button2 = ttk.Button(window, text='Reset', style='TButton', state='disabled')
second_canvas.create_window(370, 385, window=reset_button2)

window.mainloop()
