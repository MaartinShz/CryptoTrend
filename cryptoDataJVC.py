from requests_html import HTMLSession
import re

#Topics = getTopics("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
        
def getTopics():
    session = HTMLSession()
    url = session.get("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
    topics = url.html.find("a.topic-title")
    # récupére la partie titres des topics
    
    #4ème titre liste les topics de la page
    BlocTopicBrut = topics[4].text[0:topics[4].text.find("Page suivante")-1]
    #topic.text.find("Page suivante") #renvoi la fin de la listes des topics
    listeTopicBrut = re.split('\n',BlocTopicBrut)
    
    listeTopic = []
    for topic in listeTopicBrut:
        e=[]
        for match in re.finditer(" ", topic):
            e.append(match.start())
        listeTopic.append(topic[0:e[-3]])#enlève les 3 derniers qui ne sont pas un titre
        #e[-1] date dernier msg  | e[-2] nb msg | e[-3] auteur topic
    return listeTopic

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

def getPostsTopic(urlTopic):#retourne toute les posts d'un topic passer en paramètre    
    #urlTopic="https://www.jeuxvideo.com/forums/42-3011927-68489642-1-0-1-0-ca-marche-kda-ou-pas.htm"
    session = HTMLSession()
    url = session.get(urlTopic)
    posts = url.html.find("div.txt-msg")

    listePostBrut = posts[0].text[:posts[0].text.find("Page suivante")-1]
    listePostBrut = re.split('\n',listePostBrut)
    # tout les posts sont contenus dans posts[0]
    return listePostBrut

