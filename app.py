import tkinter as tk
from tkinter import filedialog, messagebox # importando somente dois conteudos do modulo
import webbrowser

# fun para abrir arquivos
def open_arq():
    rout = filedialog.askopenfilename(defaultextension='.txt',filetypes=[('Arquivos de texto','*.txt'),('Todos os arquivos','*.*')])
    
    if rout:
        with open(rout,'r') as arq:
            texto.delete(1.0,tk.END)
            texto.insert(tk.END,arq.read())

# fun save
def sava_arq():
    rout = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[('Arquivos de texto','*.txt'),('Todos os arquivos','*.*')])
    
    if rout:
        with open(rout,'w') as arq:
            arq.write(texto.get(1.0,tk.END))

# fun exit
def exit():
    if messagebox.askokcancel('Sair','Você quer mesmo sair?'):
        root.quit()

# abrir insta fun

def social():
    webbrowser.open('https://www.instagram.com/edukl.art?igsh=MWtyc2VwYjlyM21qYg==')

# abrir github

def github():
    webbrowser.open('https://github.com/EduklArtDev')

# about

def about():
    # sobre 
    about_win =tk.Toplevel(root)
    about_win.title('About for app')
    about_win.geometry('300x300')

    # rotulo 
    label = tk.Label(about_win,text='Simples editor de texto em python-tk. Criado por Eduardo O.S.',justify='center')
    label.pack(pady=20)

    # sociais
    btn = tk.Button(about_win,text='Instagram',command=social)
    btn.pack()
    btn = tk.Button(about_win,text='GitHub',command=github)
    btn.pack()

    # exit
    btn = tk.Button(about_win,text='Sair',command=about_win.destroy)
    btn.pack()

# janela principal
root = tk.Tk()
root.title('edText - By Eduardo O.S')
root.geometry('550x400')




# textarea
texto = tk.Text(root, wrap='word', undo=True, bg='white', fg='black')
texto.pack(expand=True,fill=tk.BOTH)


# menu 
menu = tk.Menu(root)
root.config(menu=menu)

# menu itens 
arq_menu = tk.Menu(menu,tearoff=0)
menu.add_cascade(label='Arquivo',menu=arq_menu)
arq_menu.add_command(label='Open',command=open_arq)
arq_menu.add_command(label='Save',command=sava_arq)
arq_menu.add_separator()
arq_menu.add_command(label='About',command=about)
arq_menu.add_separator()
arq_menu.add_command(label='Sair',command=exit)

# start
root.mainloop()