from requests_html import HTMLSession
import re

#Topics = getTopics("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
        
def getTopics():
    session = HTMLSession()
    url = session.get("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
    topics = url.html.find("a.topic-title")
    # récupére la partie titres des topics
    
    #4ème titre liste les topics de la page
    BlocTopicBrut = topics[4].text[0:topics[4].text.find("Page suivante")]
    #topic.text.find("Page suivante") #renvoi la fin de la listes des topics
    listeTopicBrut = re.split('\n',BlocTopicBrut)
    return listeTopicBrut

def getUrlTopics():    
    session = HTMLSession()
    url = session.get("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
    e=[]
    for match in re.finditer("<a class=\"lien-jv topic-title\" href=\"", url.text):
         e.append(match.end())
    if (len(e)==25):# car JVC n'affcihe que les 25 plus récent forum #on s'assure de bien les avoir
        listeUrlTopic=[]
        for i in range(len(e)):
            link = url.text[e[i]:url.text.find(".htm",e[i])+4]
            listeUrlTopic.append('https://www.jeuxvideo.com/ '+link)
        return listeUrlTopic

def getpostsTopic(urlTopic):#retourne toute les posts d'un topic passer en paramètre    
    #urlTopic="https://www.jeuxvideo.com/forums/42-3011927-68489642-1-0-1-0-ca-marche-kda-ou-pas.htm"
    session = HTMLSession()
    url = session.get(urlTopic)
    posts = url.html.find(".bloc-message-forum")
    listeposteBrut = re.split('\n',posts[0].text[:posts[0].text.find("Page suivante")-1])
    # tout les posts sont contenus dans posts[0s]
    return listeposteBrut


#print(getpostsTopic("https://www.jeuxvideo.com/forums/42-3011927-62814144-1-0-1-0-terra-luna.htm"))

print(getTopics())





