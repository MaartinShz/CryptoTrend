import re

def getCryptoKey(listemots):
    regexCrypto = "^[A-Z]{3,12}$"
    #"(^[[a-z]{3,12}]$|^[[A-Z]{3,12}]$|^[A-Z]{3,12}$)"
    
    clesCrypto=[]
    for cles in listemots:
        #re.search(regexCrypto, cles)
        # on vérfie qu'une chaine est à le format d'une clé de cryptomonnaie
        if(re.search(regexCrypto, cles)):
            clesCrypto.append(cles)
    return clesCrypto


