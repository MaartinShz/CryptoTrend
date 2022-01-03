#import tkinter as tk
from tkinter import *
from tkinter import ttk
import coinmarketcap


#creer fenetre
window = Tk()

#Recupérer la valeur de l'item sélectionné
def selectItem(a):
    curItem = tree.selection()[0]
    print(curItem)
    
    win = Toplevel(window)
    win.title(coinmarketcap.cryptoValid[int(curItem)].get_nom())
    win.geometry("1080x720")
    win.minsize(610,360)
    win.iconbitmap("logo_btc.ico") #revoir le logo
    win.config(background='#5C5E73')
    #titre
    framebis = Frame(win, bg='#5C5E73', bd=1, relief=SUNKEN)
    label_titlebis=Label(framebis, text=coinmarketcap.cryptoValid[int(curItem)].get_nom(), font=("Verdana",30),bg='#5C5E73',fg='white')
    label_titlebis.pack()
    framebis.pack(padx=20,pady=40)    
    
    #Tableau
    frame_tabbis = Frame(win)
    frame_tabbis.pack(padx=20,pady=40)
    
    treebis=ttk.Treeview(frame_tabbis, columns=(1,2,3,4),show="headings",height="10")
    treebis['columns']=("Titre","Url","Nbcom","Votes")
    treebis.column("Titre",width=150)
    treebis.column("Url",width=150)
    treebis.column("Nbcom",width=200)
    treebis.column("Votes",width=150)
    ##Heading
    treebis.heading("Titre",text="Nom")
    treebis.heading("Url",text="Url")
    treebis.heading("Nbcom",text="Nombre de Commentaires")
    treebis.heading("Votes",text="Votes positifs")
    treebis.pack()
    
    
    
#personnalisation
window.title("Crypto Trend")

window.geometry("1080x720")
window.minsize(610,360)
window.iconbitmap("logo_btc.ico") 
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
tree=ttk.Treeview(frame_tab, columns=(1,2,3,4,5,6),show="headings",height="10", yscrollcommand=my_scrollbar)

#Config scrollbar
my_scrollbar.config(command=tree.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

##Colonnes
tree['columns']=("Nom","Symbole","Blockchain","MarketCap","Prix","Lancement")

tree.column("Nom",width=150)
tree.column("Symbole",width=120,anchor=CENTER)
tree.column("Blockchain",width=120,anchor=CENTER)
tree.column("MarketCap",width=150)
tree.column("Prix",width=120)
tree.column("Lancement",width=120)

##Heading
tree.heading("Nom",text="Nom")
tree.heading("Symbole",text="Symbole")
tree.heading("Blockchain",text="Blockchain")
tree.heading("MarketCap",text="MarketCap")
tree.heading("Prix",text="Prix")
tree.heading("Lancement",text="Lancement")

tree.bind('<ButtonRelease-1>',selectItem)
##Style
style = ttk.Style()
style.theme_use("clam")
style.configure('Treeview.Heading', font=('Verdana', 10,'bold'), background="#5A5B69")
style.configure('Treeview',highlightthickness=0, font=('Verdana', 8))
#style.map('Treeview',background[('selected',"#5A5B69")])

#Insertion des cryptos

for i in range(len(coinmarketcap.cryptoValid)):
    tree.insert(parent='',index='end',iid=i,text="Parent",
          values=(coinmarketcap.cryptoValid[i].get_nom(),coinmarketcap.cryptoValid[i].get_cle(),coinmarketcap.cryptoValid[i].get_localisation(),
                  coinmarketcap.cryptoValid[i].get_marketCap(),coinmarketcap.cryptoValid[i].get_price(),coinmarketcap.cryptoValid[i].get_launch()[0:10]))


"""
tree.insert(parent='',index='end',iid=0,text="Parent",values=(coinmarketcap.tab[0],coinmarketcap.tab[1],coinmarketcap.tab[2],coinmarketcap.tab[3],
                                                            coinmarketcap.tab[4],coinmarketcap.tab[5]))
tree.insert(parent='',index='end',iid=1,text="Parent",values=(coinmarketcap.tab2[0],coinmarketcap.tab2[1],coinmarketcap.tab2[2],coinmarketcap.tab2[3],
                                                            coinmarketcap.tab2[4],coinmarketcap.tab2[5]))

"""
tree.pack()


#afficher
window.mainloop()



























