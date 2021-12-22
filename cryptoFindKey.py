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


# ## EXEMPLE ##
# import cryptoDataJVC
# url = "https://www.jeuxvideo.com/forums/42-3011927-68193322-1-0-1-0-ceek-vr-meta-space-x-nasa-votre-excuse-pour-ne-pas-monter-dans-le-train.htm"
# x = cryptoDataJVC.getPostsTopic(url)
# y=getCryptoKey(x)
# print(y)

