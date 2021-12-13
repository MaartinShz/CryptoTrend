#from jvc import *
from requests_html import HTMLSession

#Topics = getTopics("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
#"http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
#https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")


s = HTMLSession()
g = s.get("https://www.jeuxvideo.com/forums/0-3011927-0-1-0-1-0-finance.htm")
#topics = g.html.find("a class=('lien-jv', 'topic-title')")

topics = g.html.find("a.topic-title")
#".topic-list li")



r_topics=[]
for topic in topics:
        print(topic)
        print('\n \n')

#print(r_topics)
#print(len(topics))
#<a class="lien-jv topic-title" 
#href="/forums/42-3011927-54330133-1-0-1-0-ico-chsb-swissborg-pour-les-investisseurs-qui-croient-au-projet.htm"

