from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import decimal

from Crypto import Crypto

#---------------------------
#fonction validCrypto : si la crypto existe, on récupère ses données avec l'API de Coinmarketcap
#---------------------------

def validCrypto(symbole): #On rentre le symbole de la crypto en entrée
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol':symbole,    
        'convert':'USD',                    
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '79674268-4592-43f3-8fb2-1ddb6939b324', #Clé que l'on utilise sur Coinmarketcap
    }
    session = Session()
    session.headers.update(headers)
    try:
      response = session.get(url, params=parameters)
      donnees = json.loads(response.text)
      return(donnees)
    except (ConnectionError, Timeout, TooManyRedirects) as erreur:
      print(erreur)

#---------------------------
#On créé les cryptos existantes que l'on ajoute à la liste des cryptos
#On utilise l'API de Coinmarketcap (site qui ressence l'ensemble des cryptos)
#Afin de vérifier que les cryptos récupérées du forum JVC selon nos critères existent
#Et que toutes les informations que nous désirons sont disponibles sur Coinmarketcap
#--------------------------- 

#variables en entrée : liste des topics récupérés (voir CryptoDataJVC) et la liste des cryptos récupérées de JVC (voir cryptoFindKey)
def create_liste(postsTopic,listeCrypto): 
    liste_crypto=[] #contient les instances de classe
    crypto_in_liste=[] #contient les symboles des crypto dans liste_crypto afin d'éviter les doublons
    for symbol in listeCrypto:
        nomSymbol=symbol
        recup=validCrypto(nomSymbol)
        try: #marketcap < 1 milliard et crypto pas déjà dans la liste (on vérifie aussi marketcap > 0 car certains cas marketcap pas indiqué sur JVC donc on évite de récupérer 0)
            if(0<recup['data'][nomSymbol]['quote']['USD']['market_cap']<1000000000 and (nomSymbol not in crypto_in_liste)): 
                cle=recup['data'][nomSymbol]['symbol']
                nom=recup['data'][nomSymbol]['name']
                marketcap=round(recup['data'][nomSymbol]['quote']['USD']['market_cap'],2)
                prix=round(recup['data'][nomSymbol]['quote']['USD']['price'],10)
                launch=recup['data'][nomSymbol]['date_added'] #date de lancement
                localisation=recup['data'][nomSymbol]['platform']['symbol'] #blockchain où est codée la crypto
                new_crypto = Crypto(cle, nom, marketcap, prix, launch, localisation) #On créé une nouvelle instance qu'on va ajouter dans la liste
                liste_crypto.append(new_crypto)
                crypto_in_liste.append(nomSymbol)
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





