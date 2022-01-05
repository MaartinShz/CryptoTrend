import re
#------------------------------------------------------------------------------------------------------------
# getCryptoKey(listemots) # methode qui applique une regex permettant de nettoyer une liste de mots
#                        pour n'avoir que des chaines pouvant possiblement être des clés de crypto
#------------------------------------------------------------------------------------------------------------
def getCryptoKey(listemots):
    regexCrypto = "^[A-Z]{3,12}$"
    clesCrypto=[]
    for cles in listemots:
        # on vérfie qu'une chaine est à le format d'une clé de cryptomonnaie
        if(re.search(regexCrypto, cles)):
            clesCrypto.append(cles)
    return clesCrypto


