from tkinter import *
from tkinter import ttk

from Crypto import Crypto
import coinmarketcap
import cryptoFindInfo
import cryptoDataJVC
import cryptoFindKey


#On récupère la liste des cryptos de JVC
#url = "https://www.jeuxvideo.com/forums/42-3011927-68193322-1-0-1-0-ceek-vr-meta-space-x-nasa-votre-excuse-pour-ne-pas-monter-dans-le-train.htm"
x = cryptoDataJVC.getTopics()
#x = cryptoDataJVC.getPostsTopic(url) #j'ai remis ca pour l'instant ca utilise moins de crédits
listeCrypto=cryptoFindKey.getCryptoKey(x)

#On vérifie que ces crytpos existent + récupération de leurs infos
cryptoValid=coinmarketcap.create_liste(x,listeCrypto)


#créer fenêtre
window = Tk()
    
#Fonction pour recupérer la valeur de la crypto sélectionné et afficher ses caractéristiques (textes/topics où elle est évoquée)
def selectItem(a):
    curItem = tree.selection()[0] #curItem prend la valeur de l'item sélectionné
    #print("Dans notre liste : crypto numéro ",curItem)
    
    idCrypto=cryptoValid[int(curItem)].get_cle() #Retrouver la clé de la bonne crypto à partir de son numéro
    infoTexteReddit=cryptoFindInfo.callReddit(idCrypto) #On stock dans infoTexteReddit les texte liés à la crypto sélectionnée
    infoTexteJVC=cryptoFindInfo.callJVC(idCrypto) #On stock dans infoTexteJVC les texte liés à la crypto sélectionnée
    
    win = Toplevel(window)
    win.title("Informations sur les textes en lien avec cette crypto") 
    win.geometry("1080x720")
    win.minsize(610,360)
    win.iconbitmap("logo_btc.ico") 
    win.config(background='#5C5E73')
    #fenêtre pour le titre et sous-titre
    framebis = Frame(win, bg='#5C5E73', bd=1, relief=SUNKEN)
    #Affiche le nom de la crypto en titre
    label_titlebis=Label(framebis, text=cryptoValid[int(curItem)].get_nom(), font=("Verdana",30),bg='#5C5E73',fg='white')
    label_titlebis.pack()
    label_subtitle=Label(framebis, text="Informations sur les textes tirés Reddit et JVC ", font=("Verdana",18),bg='#5C5E73',fg='white')
    label_subtitle.pack()
    framebis.pack(padx=20,pady=40)    
    
    #fenêtre pour le tree reddit
    frame_tabbis = Frame(win)
    frame_tabbis.pack(padx=20,pady=20)
    
    #Tree pour les textes Reddit
    treebis=ttk.Treeview(frame_tabbis, columns=(1,2,3,4),show="headings",height="10")
    treebis['columns']=("Titre","Url","Nbcom","Votes")
    treebis.column("Titre",width=350)
    treebis.column("Url",width=270)
    treebis.column("Nbcom",width=240,anchor=CENTER)
    treebis.column("Votes",width=170,anchor=CENTER)
    ##Heading
    treebis.heading("Titre",text="Titre")
    treebis.heading("Url",text="Url")
    treebis.heading("Nbcom",text="Nombre de Commentaires")
    treebis.heading("Votes",text="Votes positifs")
    #insertion des valeurs 
    print("Url Reddit")
    for i in range(len(infoTexteReddit)):
        treebis.insert(parent='',index='end',iid=i,text="Parent",
          values=(infoTexteReddit[i].get_titre(),infoTexteReddit[i].get_url(),infoTexteReddit[i].get_nbCommentaire(),infoTexteReddit[i].get_upvote()))
        print("url ",i," : ",infoTexteReddit[i].get_url())
    #Nous voulions que les url soient cliquables directement dans l'interface, nous n'avons cependant pas réussi
    #Nous avons alors décidé des les afficher dans la console afin que l'utilisateur puisse, s'il le souhaite, les copier coller
    
    
    #affichage du tree
    treebis.pack() 
    
    #Tree pour les textes JVC
    frame_tabter = Frame(win)
    frame_tabter.pack(padx=20,pady=20)
    
    treeter=ttk.Treeview(frame_tabbis, columns=(1,2,3,4),show="headings",height="10")
    treeter['columns']=("Titre","Url","Nbmsg","Derniermsg")
    treeter.column("Titre",width=350)
    treeter.column("Url",width=270)
    treeter.column("Nbmsg",width=240,anchor=CENTER)
    treeter.column("Derniermsg",width=170,anchor=CENTER)
    ##Heading
    treeter.heading("Titre",text="Titre")
    treeter.heading("Url",text="Url")
    treeter.heading("Nbmsg",text="Nombre de messages")
    treeter.heading("Derniermsg",text="Dernier message")
    #insertion des valeurs
    print("Url JVC")
    for i in range(len(infoTexteJVC)):
        treeter.insert(parent='',index='end',iid=i,text="Parent",
          values=(infoTexteJVC[i].get_titre(),infoTexteJVC[i].get_url(),infoTexteJVC[i].get_nbCommentaire(),infoTexteJVC[i].get_dateDernierMsg()))
        print("url ",i," : ",infoTexteJVC[i].get_url())
    #affichage du tree
    treeter.pack() 
    
    
#Page principale contenant la liste des cryptos récupérées
window.title("Crypto Trend")

window.geometry("1080x720")
window.minsize(610,360)
window.iconbitmap("logo_btc.ico") 
window.config(background='#5C5E73') 


#Frame pour titre + sous-titre
frame = Frame(window, bg='#5C5E73', bd=1, relief=SUNKEN)

#titre
label_title=Label(frame, text="Bienvenue sur Crypto Trend", font=("Verdana",30),bg='#5C5E73',fg='white')
label_title.pack()
#sous-titre
label_subtitle=Label(frame, text="Trouvez les dernières tendances cryptos ", font=("Verdana",18),bg='#5C5E73',fg='white')
label_subtitle.pack()

frame.pack(padx=20,pady=40)


#frame pour afficher le tableau contenant la liste des cryptos
frame_tab = Frame(window)
frame_tab.pack(padx=20,pady=40)
#barre de défilement
my_scrollbar=Scrollbar(frame_tab,orient=VERTICAL)
tree=ttk.Treeview(frame_tab, columns=(1,2,3,4,5,6),show="headings",height="10", yscrollcommand=my_scrollbar)

#Config scrollbar
my_scrollbar.config(command=tree.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

##Colonnes
tree['columns']=("Nom","Symbole","Blockchain","MarketCap","Prix","Lancement")

tree.column("Nom",width=170)
tree.column("Symbole",width=150,anchor=CENTER)
tree.column("Blockchain",width=150,anchor=CENTER)
tree.column("MarketCap",width=170)
tree.column("Prix",width=150)
tree.column("Lancement",width=150)

##Heading
tree.heading("Nom",text="Nom")
tree.heading("Symbole",text="Symbole")
tree.heading("Blockchain",text="Blockchain")
tree.heading("MarketCap",text="MarketCap ($)")
tree.heading("Prix",text="Prix ($)")
tree.heading("Lancement",text="Lancement")
#bind : lorsque l'on sélectionne une crypto, appelle la fonction "selectItem"
tree.bind('<ButtonRelease-1>',selectItem)
##Style
style = ttk.Style()
style.theme_use("clam")
style.configure('Treeview.Heading', font=('Verdana', 10,'bold'), background="#5A5B69")
style.configure('Treeview',highlightthickness=0, font=('Verdana', 8))
#style.map('Treeview',background[('selected',"#5A5B69")])

#Insertion des cryptos
for i in range(len(cryptoValid)):
    tree.insert(parent='',index='end',iid=i,text="Parent",
          values=(cryptoValid[i].get_nom(),cryptoValid[i].get_cle(),cryptoValid[i].get_localisation(),
                  cryptoValid[i].get_marketCap(),cryptoValid[i].get_price(),cryptoValid[i].get_launch()[0:10]))
tree.pack()


#afficher
window.mainloop()



























