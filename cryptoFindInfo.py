import Crypto
import praw
from prawcore import NotFound
from requests_html import HTMLSession
import re

def callReddit(cryptoCle):
    docsReddit=[]
    reddit = praw.Reddit(client_id='K-MXXSpylsdQT0bK2QZ-ZA', client_secret='853z2OVS5DKax8hcESS-B8rU1RkJqA', user_agent='test8080')
    
    exists = True
    try:
        reddit.subreddits.search_by_name(cryptoCle, exact=True)
        #print('subreddit dedié existe')
    except NotFound:
        exists = False
        #print('subreddit dedié nexiste pas')
    
    if(exists):
        #---------------------------
        #post du subreddit dédié à la crypto
        #---------------------------
        subreddit = reddit.subreddit(cryptoCle).hot(limit=10)
        for postCrypto in subreddit:
            
            ###(self, id, url, source, titre, texte, auteur, nbCommentaite, upvote)
            txtReddit = Crypto.TexteReddit("id", postCrypto.url, postCrypto.title, postCrypto.selftext, postCrypto.author, postCrypto.num_comments, postCrypto.score, postCrypto.created_utc)
            docsReddit.append(txtReddit)
            
    #---------------------------
    # post général qui contient de la crypto
    #---------------------------
    postsearch = reddit.subreddit('all')
    for postCryptoAll in postsearch.search(cryptoCle, limit=10):
        txtRedditAll = Crypto.TexteReddit("id", postCryptoAll.url, postCryptoAll.title, postCryptoAll.selftext, postCryptoAll.author, postCryptoAll.num_comments, postCryptoAll.score, postCryptoAll.created_utc)
        docsReddit.append(txtRedditAll)
       
    return docsReddit


def callJVC(cryptoCle):
    docsJVC=[]
    link ="https://www.jeuxvideo.com/recherche/forums/0-3011927-0-1-0-1-0-finance.htm?search_in_forum="+cryptoCle+"&type_search_in_forum=titre_topic"
    
    session = HTMLSession()
    url = session.get(link)
    page = url.html.find("a.topic-title")
    
    
    
    BlocInfos = page[0].text[0:page[0].text.find("Résultats pour la recherche de")-1]
    #print(BlocInfos)
    listeInfos = re.split('\n',BlocInfos)
    #print(listeInfos)
    for ligne in listeInfos:
        pos=[]
        for match in re.finditer(" ", ligne):
            pos.append(match.start())
        
        titreJVC = ligne[0:pos[-3]]
        
        chaine = re.split(" ", ligne)
        
        auteurJVC = chaine[-3]#auteur
        nbMsgJVC = chaine[-2]#nb msg
        dateDernierMsgJVC = chaine[-1]#date
        
        txtJVC= Crypto.TexteJVC('id', 'url', titreJVC, auteurJVC, nbMsgJVC, dateDernierMsgJVC)
        docsJVC.append(txtJVC)
        
    ####
    #data = url.html.links
    # for x in data:
    #     print(x)

    return docsJVC

#print(callJVC('ceek'))
#print(callReddit('ceek'))
#test=callJVC('ceek')
#test[0].get_dateDernierMsg() #Out[7]: '08:39:17' Jsp si c'est utilisable ça



