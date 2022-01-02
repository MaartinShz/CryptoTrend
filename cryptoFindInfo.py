import Crypto
import praw
from prawcore import NotFound

def callReddit(cryptoCle):
    docsReddit=[]
    reddit = praw.Reddit(client_id='K-MXXSpylsdQT0bK2QZ-ZA', client_secret='853z2OVS5DKax8hcESS-B8rU1RkJqA', user_agent='test8080')
   
    
    exists = True
    try:
        reddit.subreddits.search_by_name(cryptoCle, exact=True)
        print('subreddit dedié existe')
    except NotFound:
        exists = False
        print('subreddit dedié nexiste pas')
    
    if(exists):
        #---------------------------
        #post du subreddit dédié à la crypto
        #---------------------------
        subreddit = reddit.subreddit(cryptoCle).hot(limit=10)
        for postCrypto in subreddit:
      
            ###(self, id, url, source, titre, texte, auteur, nbCommentaite, upvote)
            txtReddit = Crypto.TexteReddit("id", postCrypto.url, "reddit",postCrypto.title, postCrypto.selftext, postCrypto.author, postCrypto.num_comments, postCrypto.score, postCrypto.created_utc)
            docsReddit.append(txtReddit)
            
    #---------------------------
    # post général qui contient de la crypto
    #---------------------------
    postsearch = reddit.subreddit('all')
    for postCryptoAll in postsearch.search(cryptoCle, limit=10):
        txtRedditAll = Crypto.TexteReddit("id", postCryptoAll.url, "reddit",postCryptoAll.title, postCryptoAll.selftext, postCryptoAll.author, postCryptoAll.num_comments, postCryptoAll.score, postCryptoAll.created_utc)
        docsReddit.append(txtReddit)
       
    return docsReddit

print(callReddit('CEEK'))
