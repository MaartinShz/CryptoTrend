import tkinter as tk
from tkinter import *
from tkinter import ttk
import coinmarketcap
#import coinmarketcap
#creer fenetre
window = Tk()

#personnalisation
window.title("Crypto Trend")

window.geometry("1080x720")
window.minsize(610,360)
window.iconbitmap("logo_btc.ico") #revoir le logo
window.config(background='#5C5E73') #choisir couleur


#Frame
frame = Frame(window, bg='#5C5E73', bd=1, relief=SUNKEN)

#titre
label_title=Label(frame, text="Bienvenue sur Crypto Trend", font=("Verdana",30),bg='#5C5E73',fg='white')
label_title.pack()

label_subtitle=Label(frame, text="Trouvez les dernières tendances cryptos ", font=("Verdana",18),bg='#5C5E73',fg='white')
label_subtitle.pack()

frame.pack(padx=20,pady=40)


#Tableau
frame_tab = Frame(window)
frame_tab.pack(padx=20,pady=40)

my_scrollbar=Scrollbar(frame_tab,orient=VERTICAL)
tv=ttk.Treeview(frame_tab, columns=(1,2,3,4,5,6),show="headings",height="10", yscrollcommand=my_scrollbar)

#Config scrollbar
my_scrollbar.config(command=tv.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

##Colonnes
tv['columns']=("Nom","Symbole","Blockchain","MarketCap","Prix","Lancement")

tv.column("Nom",width=120)
tv.column("Symbole",width=120,anchor=CENTER)
tv.column("Blockchain",width=120)
tv.column("MarketCap",width=120)
tv.column("Prix",width=100)
tv.column("Lancement",width=120)

##Heading
tv.heading("Nom",text="Nom")
tv.heading("Symbole",text="Symbole")
tv.heading("Blockchain",text="Blockchain")
tv.heading("MarketCap",text="MarketCap")
tv.heading("Prix",text="Prix")
tv.heading("Lancement",text="Lancement")

##Style
style = ttk.Style()
style.theme_use("clam")
style.configure('Treeview.Heading', font=('Verdana', 10,'bold'), background="#5A5B69")
style.configure('Treeview',highlightthickness=0, font=('Verdana', 8))
#style.map('Treeview',background[('selected',"#5A5B69")])

#Valeurs TEST
tv.insert(parent='',index='end',iid=0,text="Parent",values=(coinmarketcap.tab[0],coinmarketcap.tab[1],coinmarketcap.tab[2],coinmarketcap.tab[3],coinmarketcap.tab[4],coinmarketcap.tab[5]))
tv.insert(parent='',index='end',iid=1,text="Parent",values=("Testtest","TST2","Matic"," $ 80000","$ 17","6 Décembre 2021"))
tv.insert(parent='',index='end',iid=2,text="Parent",values=("Prograpython","PGP","Ethereum"," $ 8970000","$ 323","12 Novembre 2021"))
tv.insert(parent='',index='end',iid=3,text="Parent",values=("Test","TST","Ethereum"," $ 100000","$ 5","12 Décembre 2021"))
tv.insert(parent='',index='end',iid=4,text="Parent",values=("Testtest","TST2","Matic"," $ 80000","$ 17","6 Décembre 2021"))
tv.insert(parent='',index='end',iid=5,text="Parent",values=("Prograpython","PGP","Ethereum"," $ 8970000","$ 323","12 Novembre 2021"))
tv.insert(parent='',index='end',iid=6,text="Parent",values=("Test","TST","Ethereum"," $ 100000","$ 5","12 Décembre 2021"))
tv.insert(parent='',index='end',iid=7,text="Parent",values=("Testtest","TST2","Matic"," $ 80000","$ 17","6 Décembre 2021"))
tv.insert(parent='',index='end',iid=8,text="Parent",values=("Prograpython","PGP","Ethereum"," $ 8970000","$ 323","12 Novembre 2021"))
tv.insert(parent='',index='end',iid=9,text="Parent",values=("Test","TST","Ethereum"," $ 100000","$ 5","12 Décembre 2021"))
tv.insert(parent='',index='end',iid=10,text="Parent",values=("Testtest","TST2","Matic"," $ 80000","$ 17","6 Décembre 2021"))
tv.insert(parent='',index='end',iid=11,text="Parent",values=("Prograpython","PGP","Ethereum"," $ 8970000","$ 323","12 Novembre 2021"))
tv.insert(parent='',index='end',iid=12,text="Parent",values=("Test","TST","Ethereum"," $ 100000","$ 5","12 Décembre 2021"))



tv.pack()

#afficher
window.mainloop()



























