from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

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
        'X-CMC_PRO_API_KEY': '994352b1-f247-4a59-82e4-0f117bf65dbf',
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

url = "https://www.jeuxvideo.com/forums/42-3011927-68193322-1-0-1-0-ceek-vr-meta-space-x-nasa-votre-excuse-pour-ne-pas-monter-dans-le-train.htm"
x = cryptoDataJVC.getPostsTopic(url)
listeCrypto=cryptoFindKey.getCryptoKey(x)
listeCrypto

#---------------------------
#On créé les cryptos existantes que l'on ajoute à la liste des cryptos
#--------------------------- 

def create_liste(postsTopic,listeCrypto):
    liste_crypto=[] #contient les instances de classe
    crypto_in_liste=[] #contient les symbole dans crypto dans liste_crypto
    for symbol in listeCrypto:
        nomSymbol=symbol
        test=validCrypto(nomSymbol)
        test
        try: #marketcap < 1 milliard et crypto pas déjà dans la liste
            if(test['data'][nomSymbol]['quote']['USD']['market_cap']<1000000000 and nomSymbol not in crypto_in_liste): 
                cle=test['data'][nomSymbol]['id']
                nom=test['data'][nomSymbol]['name']
                marketcap=test['data'][nomSymbol]['quote']['USD']['market_cap']
                prix=test['data'][nomSymbol]['quote']['USD']['price']
                launch=test['data'][nomSymbol]['date_added'] #recoder la date ?
                localisation=test['data'][nomSymbol]['platform']['symbol']
                new_crypto = Crypto(cle, nom, marketcap, prix, launch, localisation)
                liste_crypto.append(new_crypto)
                crypto_in_liste.append(nomSymbol)
                #print(new_crypto) # JE COMPRENDS PAS POURQUOI CA MARCHE PAS
                #print(new_crypto.get_cle()) #CA NON PLUS
                
                print("---------------------------------------------")
                print("Crypto ajoutée ("+nomSymbol+")")
            else:
                print("---------------------------------------------")
                print("MarketCap déjà élevé / Crypto déjà dans la liste ("+nomSymbol+")")
        except KeyError:
            print("---------------------------------------------")
            print("Cette crypto n'existe pas ("+nomSymbol+")")
        except TypeError:
            print("---------------------------------------------")
            print("Information manquante ("+nomSymbol+")")
    return(liste_crypto)


#test=create_liste(x,listeCrypto)
#test

tab=["yoyoyo","yo","Ethereum"," $ 42","$ 1000","12 Novembre 1999"]
tab[0]






