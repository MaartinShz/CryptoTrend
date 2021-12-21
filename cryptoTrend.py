from requests_html import HTMLSession
import re


#Topics = getTopics("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
        
def getTopic():
    session = HTMLSession()
    url = session.get("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
    topics = url.html.find("a.topic-title")
    topics=topics[4:5] # récupére la partie titres des topics
    
    for topic in topics:
        BlocTopicBrut = topic.text[0:topic.text.find("Page suivante")]
        #topic.text.find("Page suivante") #renvoi la fin de la listes des topics
    
    listeTopicBrut = re.split('\n',BlocTopicBrut)
    ### TO IMPROVE
    #for top in listeTopicBrut:
        #on essaye d'enlever au max le nb msg l'auteur et l'heure des chiane
        #pseudo 15 + date 8 + 2 espacce + 5 ~ nb msg = 30
        #top = top[0:top.find(" ",-30)]
        
        #print(top)
        #print("\n")
    return listeTopicBrut


def getUrlTopic():    
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


    