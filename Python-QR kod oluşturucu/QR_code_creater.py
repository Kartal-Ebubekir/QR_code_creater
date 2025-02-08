from tkinter import *
from tkinter import filedialog,messagebox,ttk # Dosya işlemleri için --> filedialog , kullanıcıya mesaj vermek için --> messagebox , daha modern entry için (Bu uygulamada sadece entry için kullanıldı) --> ttk
from PIL import  Image,ImageTk # Qr kodu tkinter ekranında görüntülemek için Image ve ImageTk
from pyqrcode import QRCode # Qr kod oluşturmak için QRCode
import png # pyqrcode kütüphanesinin PNG formatında QR kodu kaydetmesi için gereklidir.
import os # Gereksiz dosyaları silmek ve dosya ikonu yolunu kontrol etmek için os modülünü import ediyoruz

def qr_code_creater():
  url = url_input.get()
  if url :
    qr_url = pyqrcode.create(url)
    qr_url.png("temp_qr.png",scale=8)
    qr_image = Image.open("temp_qr.png")
    qr_image = qr_image.resize((250,250),Image.Resampling.LANCZOS)
    qr_tk_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_tk_image) #Pointer mantığı gibi çalışır.Resmi label'a ekler ama kaydetmez (ptr) .
    qr_label.image = qr_tk_image # Resmi kaydeder *(ptr)
    create_file(qr_url)
  else:
    messagebox.showwarning("Warning","Please enter a link")

def create_file(qr_url):
  file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("SVG Files", ".svg"), ("PNG File", ".png")],title="File Save Path")
  if file_path:
    if file_path.endswith(".svg"):
      qr_url.svg(file_path, scale=8)
    elif file_path.endswith(".png"):
      qr_url.png(file_path, scale=8)
    status_label.config(text="QR code has been created and saved.", fg="green")
    messagebox.showinfo("Success", "QR Code saved successfully!")
    os.remove("temp_qr.png")

window = Tk()
window.title("QR Code Creator")
if os.path.exists("icon.png"):
  window.iconphoto(True,PhotoImage(file="icon.png")) # True --> Ana pencerenin ikonunu değiştirmeye yarar , False --> Ana pencerenin ikonu değişmez sonraki pencereler için uygulanır.
# PhotoImage(file="") --> Dosyayı tkinter'e uyumlu hale getirir.
else:
  print("Application icon file not found")
window.resizable(0,0)
window.geometry("800x600")
window.configure(bg="#2c2c2c")

frame = Frame(window, bg="#2c2c2c")
frame.place(relx=0.5, rely=0.4, anchor=CENTER)  # Ortalamak için

input_label = Label(frame, text="Enter the Link :", font="Helvetica 12 bold", fg="white",bg="#2c2c2c")
url_input = ttk.Entry(frame, width=40)
create_qr_code = Button(frame, text="Create QR Code" ,bg="#808080", font="Helvetica 12 bold",command=qr_code_creater)
status_label = Label(frame, text="", fg="white",bg="#2c2c2c")
message = Label(frame, text="(Even if you do not enter a link, it will still generate a QR code)", font="arial 10", fg="red", bg="#2c2c2c")
qr_label = Label(frame, bg="#2c2c2c")

input_label.pack(pady=5)
url_input.pack(pady=5)
message.pack(pady=5)
create_qr_code.pack(pady=10)
status_label.pack(pady=5)
qr_label.pack(pady=10)

window.mainloop()
