class Crypto:
  def __init__(self, cle, nom, marketCap, price, launch, localisation):
    self.cle = cle
    self.nom = nom
    self.marketCap = marketCap
    
    self.price = price
    self.launch = launch
    self.localisation = localisation
    
    self.corpus = []
    
    def __str__(self):
        return f'Crypto({self.cle},{self.nom},{self.marketCap})'

class Texte:
    def __init__(self, id, url, source):
        self.id = id
        self.url = url
        self.source = source
        
    def __str__(self):
        return f'Texte({self.id}, {self.source})'
    
class TexteReddit(Texte):
    def __init__(self, id, url, source, upvote, nbCommentaire):
        Texte.__init__(self, id, url, source)
        self.upvote = upvote
    def __str__(self):
        return f'TexteReddit({self.id}, {self.source}, {self.upvote})'

# test = Crypto('cle', 'nom', 'marketCap', 'price', 'launch', 'localisation')
# test = Texte('id', 'url', 'source')
# test = TexteReddit('id', 'url', 'source', 'upvote', 'nbCommentaire')
# print(test)