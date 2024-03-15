from tkinter import *

fenetre = Tk()
fenetre.geometry('600x600')
fenetre.title('Identification')
fenetre['bg'] = 'blue'
label = Label(fenetre, text='Cest pas ouf mais bon...', bg='blue', font='green')
label.pack(padx=20)
entree = Entry(fenetre, textvariable='mot de passe correct')
entree.pack()
def message():
    print('Mot de passe valide')

bouton = Button(fenetre, text='Click!', command=message)
bouton.pack()

options = Menu()

fichier = Menu()

mon_menu = Menu(fenetre)
fichier = Menu(mon_menu)
mon_menu.add_cascade(label="fichier")
mon_menu.add_cascade(label="options")
options = Menu(mon_menu)
mon_menu.add
mon_menu.mainloop

fenetre.mainloop()