import Crypto
import praw
from prawcore import NotFound
from requests_html import HTMLSession
import re
import uuid

#------------------------------------------------------------------------------------------------------------
# callReddit(cryptoCle) # méthode qui prend en paramètre une clé crypto et qui renvoie une liste de post Reddit en lien avec cette crypto
#------------------------------------------------------------------------------------------------------------
def callReddit(cryptoCle):
    docsReddit=[]
    reddit = praw.Reddit(client_id='K-MXXSpylsdQT0bK2QZ-ZA', client_secret='853z2OVS5DKax8hcESS-B8rU1RkJqA', user_agent='test8080')
    
    exists = False
    if(cryptoCle !='CALL' and cryptoCle !='TOP'): # CALL et TOP sont des chaines de caractère réservé par reddit
        try:
            reddit.subreddits.search_by_name(cryptoCle, exact=True)
            exists = True
            #on teste si il y a un subreddit dedié existe
        except NotFound:
            exists = False
    
    if(exists):
        #---------------------------
        #post du subreddit dédié à la crypto
        #---------------------------
        subreddit = reddit.subreddit(cryptoCle).hot(limit=10)# on sélectionne les 10 post les plus populaires
        for postCrypto in subreddit:
            
            # on créer un objet Texte REddit ayant toutes les informations nécessaire sur le post sur la crypto en paramètre
            txtReddit = Crypto.TexteReddit(uuid.uuid1(), postCrypto.url, postCrypto.title, postCrypto.selftext, postCrypto.author, postCrypto.num_comments, postCrypto.score, postCrypto.created_utc)
            docsReddit.append(txtReddit)
            
    #---------------------------
    # post général sur Reddit qui contient crypto
    #---------------------------
    postsearch = reddit.subreddit('all')
    for postCryptoAll in postsearch.search(cryptoCle, limit=10):# on sélectionne les 10 post les plus populaires
        txtRedditAll = Crypto.TexteReddit(uuid.uuid1(), postCryptoAll.url, postCryptoAll.title, postCryptoAll.selftext, postCryptoAll.author, postCryptoAll.num_comments, postCryptoAll.score, postCryptoAll.created_utc)
        docsReddit.append(txtRedditAll)
       
    return docsReddit

#------------------------------------------------------------------------------------------------------------
# callJVC(cryptoCle) # méthode qui prend en paramètre une clé crypto et qui renvoie une liste de topic JVC en lien avec cette crypto
#------------------------------------------------------------------------------------------------------------
def callJVC(cryptoCle):
    docsJVC=[]
    #lien pour effectuer une recherche avec la cle crypto sur JVC Finance 
    link ="https://www.jeuxvideo.com/recherche/forums/0-3011927-0-1-0-1-0-finance.htm?search_in_forum="+cryptoCle+"&type_search_in_forum=titre_topic"
    
    session = HTMLSession()
    url = session.get(link)
    page = url.html.find("a.topic-title")# on récupère le html qui nous intéresse
    
    #Préparation des données pour pouvoir les exploiter
    BlocInfos = page[0].text[0:page[0].text.find("Résultats pour la recherche de")-1]
    listeInfos = re.split('\n',BlocInfos)
    i = 0 #compteur qui permet de selectionner la ligne pour avoir plus tard l'url correpondante au bon topic
    for ligne in listeInfos:
        pos=[]
        for match in re.finditer(" ", ligne):
            pos.append(match.start())
        
        titreJVC = ligne[0:pos[-3]]
        
        chaine = re.split(" ", ligne)
        
        auteurJVC = chaine[-3]#auteur
        nbMsgJVC = chaine[-2]#nb msg
        dateDernierMsgJVC = chaine[-1]#date
        urlJVC = "https://www.jeuxvideo.com/" + page[i].attrs["href"] #url du topic traitant de la crypto
        i=i+1

        txtJVC= Crypto.TexteJVC(uuid.uuid1(), urlJVC, titreJVC, auteurJVC, nbMsgJVC, dateDernierMsgJVC)
        docsJVC.append(txtJVC) 

    return docsJVC
