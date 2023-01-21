import requests
from bs4 import BeautifulSoup

proxy = {"http": "http://198.199.120.102:8080", "https": "http://198.199.120.102:8080"}
# URL de connexion
login_url = "https://le-beguin.fr/login/"

# Données de connexion
data = {"username": "steeve.co@orange.fr", "password": "Tmax500_t"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

try:
    # Envoi de la requête de connexion
    response = requests.post(login_url, data=data, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print("login success")
        url = "https://le-beguin.fr/member/790591/profil/show/854916"

        try:
            # Envoi de la requête pour accéder à la page de profil en incluant les cookies retournés lors de la connexion
            response = requests.get(login_url, headers=headers, cookies=response.cookies)

            # Vérification de la réponse HTTP
            if response.status_code == 200:
                # Récupération du contenu HTML de la page
                html = response.content
                # Initialisation de BeautifulSoup avec le contenu HTML
                soup = BeautifulSoup(html, 'html.parser')

                city_element = soup.find('span', id='city')
                if city_element:
                    city = city_element.get_text()
                else:
                    city = ""

                age_element = soup.find('span', id='age')
                if age_element:
                    age = age_element.get_text()
                else:
                    age = ""

                min_age_element = soup.find('span', id='min_age')

                if min_age_element:
                    min_age = min_age_element.get_text()
                else:
                    min_age = ""
            else:
                print("Error: Could not scrape profile.")
        except Exception as e:
            print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
