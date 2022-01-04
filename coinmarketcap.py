from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import decimal

#---------------------------
#fonction validCrypto : si la crypto existe, on récupère ses données
#---------------------------

def validCrypto(symbole):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol':symbole,    
        'convert':'USD',                    
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '79674268-4592-43f3-8fb2-1ddb6939b324',
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
      response = session.get(url, params=parameters)
      donnees = json.loads(response.text)
      #print(donnees)
      return(donnees)
    except (ConnectionError, Timeout, TooManyRedirects) as erreur:
      print(erreur)

#---------------------------
#On récupère la liste des cryptos de JVC
#---------------------------

from Crypto import Crypto
import cryptoDataJVC
import cryptoFindKey
import cryptoFindInfo

url = "https://www.jeuxvideo.com/forums/42-3011927-68193322-1-0-1-0-ceek-vr-meta-space-x-nasa-votre-excuse-pour-ne-pas-monter-dans-le-train.htm"
#x = cryptoDataJVC.getTopics()
x = cryptoDataJVC.getPostsTopic(url) #j'ai remis ca pour l'instant ca utilise moins de crédits
listeCrypto=cryptoFindKey.getCryptoKey(x)


#---------------------------
#On créé les cryptos existantes que l'on ajoute à la liste des cryptos
#--------------------------- 

def create_liste(postsTopic,listeCrypto):
    liste_crypto=[] #contient les instances de classe
    crypto_in_liste=[] #contient les symbole dans crypto dans liste_crypto
    for symbol in listeCrypto:
        nomSymbol=symbol
        recup=validCrypto(nomSymbol)
        try: #marketcap < 1 milliard et crypto pas déjà dans la liste
            if(0<recup['data'][nomSymbol]['quote']['USD']['market_cap']<1000000000 and (nomSymbol not in crypto_in_liste)): 
                cle=recup['data'][nomSymbol]['symbol']
                nom=recup['data'][nomSymbol]['name']
                marketcap=round(recup['data'][nomSymbol]['quote']['USD']['market_cap'],2)
                prix=round(recup['data'][nomSymbol]['quote']['USD']['price'],10)
                launch=recup['data'][nomSymbol]['date_added'] #recoder la date ?
                localisation=recup['data'][nomSymbol]['platform']['symbol']
                new_crypto = Crypto(cle, nom, marketcap, prix, launch, localisation)
                liste_crypto.append(new_crypto)
                crypto_in_liste.append(nomSymbol)
                #print(new_crypto.get_cle()) 
                print("---------------------------------------------")
                print("Crypto ajoutée ("+nomSymbol+")")
            else:
                print("---------------------------------------------")
                print("MarketCap déjà élevé ou non indiqué / Crypto déjà dans la liste ("+nomSymbol+")")
        except KeyError:
            print("---------------------------------------------")
            print("Cette crypto n'existe pas ("+nomSymbol+")")
        except TypeError:
            print("---------------------------------------------")
            print("Information manquante ("+nomSymbol+")")
    return(liste_crypto)


cryptoValid=create_liste(x,listeCrypto)




