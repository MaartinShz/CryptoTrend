import Crypto
import praw

def callReddit(cryptoCle):
    docsReddit=[]
    
    reddit = praw.Reddit(client_id='K-MXXSpylsdQT0bK2QZ-ZA', client_secret='853z2OVS5DKax8hcESS-B8rU1RkJqA', user_agent='test8080')
    
    #post du subreddit dédié à la crypto
    subreddit = reddit.subreddit(cryptoCle).hot(limit=10)
    
    for postCrypto in subreddit:
        #print(postCrypto.title+postCrypto.selftext)
        #print(postCrypto.selftext)
        #print(postCrypto.url)
        comment= reddit.comment('rqikqd')#postCrypto.id
        print()

        print('\n')
        
    txtR = Crypto.TexteReddit("id", postCrypto.url, "reddit",postCrypto.title+postCrypto.selftext,"nbComme" )
        #self, id, url, source, upvote, nbCommentaire):
    
    
    #post général qui contient de la crypto
    postsearch = reddit.subreddit('all')
    for post in postsearch.search(cryptoCle, limit=10):
        ##verif find : crypto coin currency pump transaction
        #print(post.title)
        #print( reddit.subreddit(cryptoCle).title)
        #print( reddit.subreddit(cryptoCle).display_name)
        #print( reddit.subreddit(cryptoCle).description)
        #print(post.selftext)
        print('\n')
    return docsReddit

print(callReddit('CEEK'))
