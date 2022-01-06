from requests_html import HTMLSession
import re


#------------------------------------------------------------------------------------------------------------
# getTopics() fonction qui recupère tout les titres des topics sur le forum JVC Finance de la page d'accueil
#             et retourne une liste avec tout les mots de ces titres
#------------------------------------------------------------------------------------------------------------
def getTopics():
    
    session = HTMLSession()
    url = session.get("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
    page = url.html.find("a.topic-title")# récupére la partie titre des topics surt JVC
    
    
    #4ème topic contient les topics de la page
    BlocTopicBrut = page[4].text[0:page[4].text.find("Page suivante")-1]
    #page.text.find("Page suivante") #renvoi la fin de la listes des topics
    
    listeTopicBrut = re.split('\n',BlocTopicBrut)#separation de la chaine avec le caratère saut de ligne
    # à partir de là chaque élément correspond à un topic
    
    listeTopic = []
    for topic in listeTopicBrut:
        pos=[]
        for match in re.finditer(" ", topic):
            pos.append(match.start())
        topic = topic[0:pos[-3]] #enlève les 3 derniers mots qui nefont pas partie du titre du topic
        #pos[-1] date dernier msg | pos[-2] nb msg | pos[-3] auteur topic
        
        for word in re.split("\[|\]| ", topic): 
            #sépare les mots des titres en utilisant les espaces
            #et les crochet qui sont souvent là pour entourer une clé crypto
            if len(word)>2: 
                #la clé d'une crypto fait au moins 3 caractères 
                # cela permet de commencer le nettoyage des chaines pouvant etre des cryptos
                listeTopic.append(word)       
    return listeTopic

#------------------------------------------------------------------------------------------------------------
#Exemples d'appel : 
#getTopics()
#------------------------------------------------------------------------------------------------------------

################ FONCTIONS OPERATIONNELLES MAIS PAS UTILISEES DANS CE PROJET ################ 

#------------------------------------------------------------------------------------------------------------
# getUrlTopics() fonction qui retourne les URL des topics sur la page principale du forum JVC Finance
#------------------------------------------------------------------------------------------------------------
def getUrlTopics():    
    session = HTMLSession()
    url = session.get("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
    pos=[]
    for match in re.finditer("<a class=\"lien-jv topic-title\" href=\"", url.text):
         pos.append(match.end())
    if (len(pos)==25):# car JVC n'affiche que les 25 plus récents topics #on s'assure de bien les avoir
        listeUrlTopic=[]
        for i in range(len(pos)):
            link = url.text[pos[i]:url.text.find(".htm",pos[i])+4]
            listeUrlTopic.append('https://www.jeuxvideo.com/ '+link)
        return listeUrlTopic
    
#------------------------------------------------------------------------------------------------------------
# getPostsTopic(urlTopic) fonction retourne toute les posts d'un topic JVC, l'URL du topic JVC est passé en paramètre$*$
#------------------------------------------------------------------------------------------------------------
def getPostsTopic(urlTopic):   
    session = HTMLSession()
    url = session.get(urlTopic)
    posts = url.html.find("div.txt-msg")

    listePostBrut = posts[0].text[:posts[0].text.find("Page suivante")-1]
    listePostBrut = re.split('\n',listePostBrut)
    # tout les posts sont contenus dans posts[0]
    
    listePost = []
    for post in listePostBrut:
        for word in re.split(" ", post):
            if len(word)>2:
                listePost.append(word)           
    return listePost

#------------------------------------------------------------------------------------------------------------
#Exemples d'appel : 
#getUrlTopics()
#getPostsTopic('https://www.jeuxvideo.com/forums/42-3011927-68119667-1-0-1-0-call-20-50-flux-by-saitama.htm')
#------------------------------------------------------------------------------------------------------------