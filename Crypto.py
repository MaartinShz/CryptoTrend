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
    
class TexteReddit(Texte):
    def __init__(self, id, url, source, titre, texte, auteur, nbCommentaite, upvote, dateCreation):
        Texte.__init__(self, id, url, source)
        self.titre =  titre
        self.texte = texte
        self.auteur = auteur
        self.nbCommentaite = nbCommentaite
        self.upvote = upvote
        self.dateCreation = dateCreation
    def __str__(self):
        return f'TexteReddit({self.id}, {self.source}, {self.upvote})'
    def __repr__(self):
        return f"{self.titre}" 

#test = Crypto('cle', 'nom', 'marketCap', 'price', 'launch', 'localisation')
#test = Texte('id', 'url', 'source')
#tester = TexteReddit('id', 'url', 'source','titre','texte','auteur','nbCommentaire','upvote','dateCrea')
#print(tester)






