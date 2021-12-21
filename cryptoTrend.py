#from jvc import *
from requests_html import HTMLSession
import re

#Topics = getTopics("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
#"http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
#https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
        
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
    return False

