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
       return f"{self.cle}, {self.nom}, {self.marketCap}"  
     # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"{self.nom}" 
    
    def get_cle(self):
        return self.cle
    
    def get_nom(self):
        return self.nom
    
    def get_marketCap(self):
        return self.marketCap
    
    def get_price(self):
        return self.price

    def get_launch(self):
        return self.launch
    
    def get_localisation(self):
        return self.localisation
    
class Texte:
    def __init__(self, id, url, source):
        self.id = id
        self.url = url
        self.source = source
        
    def __str__(self):
        return f'Texte({self.id}, {self.source})'
    
    def get_id(self):
        return self.id

    def get_url(self):
        return self.url
    
    def get_source(self):
        return self.source
    
    
class TexteReddit(Texte):
    def __init__(self, id, url, titre, texte, auteur, nbCommentaire, upvote, dateCreation):
        Texte.__init__(self, id, url, 'reddit')
        self.titre =  titre
        self.texte = texte
        self.auteur = auteur
        self.nbCommentaire = nbCommentaire
        self.upvote = upvote
        self.dateCreation = dateCreation
        
    def __str__(self):
        return f'TexteReddit({self.id}, {self.source}, {self.upvote})'
    
    def __repr__(self):
        return f"{self.titre}"
    
    def get_titre(self):
        return self.titre

    def get_nbCommentaire(self):
        return self.nbCommentaire
    
    def get_upvote(self):
        return self.upvote
    
class TexteJVC(Texte):
    def __init__(self, id, url, titre, auteur, nbMsg, dateDernierMsg):
        Texte.__init__(self, id, url, 'jvc')
        self.titre =  titre
        self.auteur = auteur
        self.nbMsg = nbMsg
        self.dateDernierMsg = dateDernierMsg
        
    def __str__(self):
        return f'TexteJVC({self.id}, {self.source}, {self.dateDernierMsg})'
    
    def __repr__(self):
        return f"{self.source}, {self.titre}"
    
    def get_titre(self):
        return self.titre

    def get_nbCommentaire(self):
        return self.nbMsg
    
    def get_dateDernierMsg(self):
        return self.dateDernierMsg






