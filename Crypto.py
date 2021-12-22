class Crypto:
  def __init__(self, cle, nom, marketCap, price, launch, localisation, corpus):
    self.cle = cle
    self.nom = nom
    self.marketCap = marketCap
    
    self.price = price
    self.launch = launch
    self.localisation =localisation
    
    self.corpus = corpus
    
    def __str__(self):
        return f'Person({self.cle},{self.nom},{self.marketCap})'
    
test = Crypto('cle', 'nom', 'marketCap', 'price', 'launch', 'localisation', 'corpus')
print(test)