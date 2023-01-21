from selenium import webdriver

# Créer une instance de navigateur
browser = webdriver.Firefox()

# Ouvrir la page d'accueil de Wikipedia
browser.get("https://fr.wikipedia.org/")

# Trouver tous les éléments de titre d'article
titles = browser.find_elements_by_css_selector(".mainpage-box h3 a")

# Imprimer les titres
for title in titles:
    print(title.text)

# Fermer le navigateur
browser.quit()
