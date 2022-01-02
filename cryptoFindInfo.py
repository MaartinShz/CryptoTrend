import Crypto
import praw

def callReddit(cryptoCle):
    docsReddit=[]
    
    reddit = praw.Reddit(client_id='K-MXXSpylsdQT0bK2QZ-ZA', client_secret='853z2OVS5DKax8hcESS-B8rU1RkJqA', user_agent='test8080')
    
    #post du subreddit dédié à la crypto

    subreddit = reddit.subreddit(cryptoCle).hot(limit=10)
    for postCrypto in subreddit:
        #id
        #print(postCrypto.url)
        #source
        
        #print(postCrypto.title)
        #print(postCrypto.selftext)
        #print(postCrypto.author)
        
        #print(postCrypto.num_comments) #nb commentaire
        #print(postCrypto.score) #nb upvote
        #print(postCrypto.
        
        
        #print(postCrypto.id)
        #print(postCrypto.subreddit)
        #url= 'https://www.reddit.com/r/'+ str(postCrypto.subreddit) +'/comments/'+ str(postCrypto.id)
        txtReddit = Crypto.TexteReddit("id", postCrypto.url, "reddit",postCrypto.title, postCrypto.selftext, postCrypto.author, postCrypto.num_comments, postCrypto.score)
        #(self, id, url, source, titre, texte, auteur, nbCommentaite, upvote)
        docsReddit.append(txtReddit)
    
    # #post général qui contient de la crypto
    
    # postsearch = reddit.subreddit('all')
    # for post in postsearch.search(cryptoCle, limit=10):
    #     ##verif find : crypto coin currency pump transaction
    #     #print(post.title)
    #     #print( reddit.subreddit(cryptoCle).title)
    #     #print( reddit.subreddit(cryptoCle).display_name)
    #     #print( reddit.subreddit(cryptoCle).description)
    #     #print(post.selftext)
    #     print('\n')
        
    return docsReddit

print(callReddit('CEEK'))
