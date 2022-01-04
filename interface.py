#import tkinter as tk
from tkinter import *
from tkinter import ttk
import coinmarketcap
import cryptoFindInfo

#creer fenetre
window = Tk()



#Recupérer la valeur de l'item sélectionné et l'afficher
def selectItem(a):
    curItem = tree.selection()[0] #curItem prend la valeur de l'item sélectionné
    print(curItem)
    
    idCrypto=coinmarketcap.cryptoValid[int(curItem)].get_cle() #Retrouver la clé de la bonne crypto à partir de son numéro
    infoTexteReddit=cryptoFindInfo.callReddit(idCrypto) #On stock dans infoTexteReddit les texte liés à la crypto sélectionnée
    infoTexteJVC=cryptoFindInfo.callJVC(idCrypto) #On stock dans infoTexteJVC les texte liés à la crypto sélectionnée
    
    win = Toplevel(window)
    win.title("Informations sur les textes en lien avec cette crypto") 
    win.geometry("1080x720")
    win.minsize(610,360)
    win.iconbitmap("logo_btc.ico") #revoir le logo
    win.config(background='#5C5E73')
    #titre
    framebis = Frame(win, bg='#5C5E73', bd=1, relief=SUNKEN)
    #Affiche le nom de la crypto en titre
    label_titlebis=Label(framebis, text=coinmarketcap.cryptoValid[int(curItem)].get_nom(), font=("Verdana",30),bg='#5C5E73',fg='white')
    label_titlebis.pack()
    label_subtitle=Label(framebis, text="Informations sur les textes tirés Reddit et JVC ", font=("Verdana",18),bg='#5C5E73',fg='white')
    label_subtitle.pack()
    framebis.pack(padx=20,pady=40)    
    
    #Tableau
    frame_tabbis = Frame(win)
    frame_tabbis.pack(padx=20,pady=20)
    
    #Tree pour les textes Reddit
    treebis=ttk.Treeview(frame_tabbis, columns=(1,2,3,4),show="headings",height="10")
    treebis['columns']=("Titre","Url","Nbcom","Votes")
    treebis.column("Titre",width=300)
    treebis.column("Url",width=200)
    treebis.column("Nbcom",width=200,anchor=CENTER)
    treebis.column("Votes",width=150,anchor=CENTER)
    ##Heading
    treebis.heading("Titre",text="Titre")
    treebis.heading("Url",text="Url")
    treebis.heading("Nbcom",text="Nombre de Commentaires")
    treebis.heading("Votes",text="Votes positifs")
    #insertion des valeurs
    for i in range(len(infoTexteReddit)):
        treebis.insert(parent='',index='end',iid=i,text="Parent",
          values=(infoTexteReddit[i].get_titre(),infoTexteReddit[i].get_url(),infoTexteReddit[i].get_nbCommentaire(),infoTexteReddit[i].get_upvote() ))
    #affichage du tree
    treebis.pack() 
    
    #Tree pour les textes JVC
    frame_tabter = Frame(win)
    frame_tabter.pack(padx=20,pady=20)
    
    treeter=ttk.Treeview(frame_tabbis, columns=(1,2,3,4),show="headings",height="10")
    treeter['columns']=("Titre","Url","Nbmsg","Derniermsg")
    treeter.column("Titre",width=300)
    treeter.column("Url",width=200)
    treeter.column("Nbmsg",width=200,anchor=CENTER)
    treeter.column("Derniermsg",width=150,anchor=CENTER)
    ##Heading
    treeter.heading("Titre",text="Titre")
    treeter.heading("Url",text="Url")
    treeter.heading("Nbmsg",text="Nombre de messages")
    treeter.heading("Derniermsg",text="Dernier message")
    #insertion des valeurs
    for i in range(len(infoTexteJVC)):
        treeter.insert(parent='',index='end',iid=i,text="Parent",
          values=(infoTexteJVC[i].get_titre(),infoTexteJVC[i].get_url(),infoTexteJVC[i].get_nbCommentaire(),infoTexteJVC[i].get_dateDernierMsg()))
    #affichage du tree
    treeter.pack() 
    
    
    
    
#personnalisation
window.title("Crypto Trend")

window.geometry("1080x720")
window.minsize(610,360)
window.iconbitmap("logo_btc.ico") 
window.config(background='#5C5E73') 


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
tree.heading("MarketCap",text="MarketCap ($)")
tree.heading("Prix",text="Prix ($)")
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

tree.pack()


#afficher
window.mainloop()



























