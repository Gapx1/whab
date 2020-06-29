from bs4 import BeautifulSoup
import urllib.request
from sendmail import sendmail


seite = 'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz?keyword=test&attribute_tree_level_0=&attribute_tree_level_1=&typedKeyword=test'
response = urllib.request.urlopen(seite)
html = response.read()


soup = BeautifulSoup(html, "lxml")
anzeigen = soup.find_all('a', itemprop='url')


webliste = []
for link in anzeigen:
    webliste.append(link.get('href'))


f = open('links.txt', 'r+')
i = 0
neu = 0
alteliste = f.readlines()
neuelinks = []

if len(webliste) > 0:
    while i < 5:
        if alteliste:
            erstezeile = alteliste[0].strip()
            print(erstezeile)
        else:
            erstezeile = None

        if erstezeile in webliste[:5]:
            if erstezeile != webliste[i]:
                print(webliste[i])
                print('nicht gleich')
                neu += 1
                neuelinks.append(webliste[i])

            else:
                print('sind gleich')
                break
            i += 1
        else:
            print('ausnahme weil anzeige verschwunden etc')
            f.seek(0)
            for p in webliste[:5]:
                f.write(p + '\n')
            neuelinks.append('etwas komisches ist passiert ;) hier die 5 aktuellsten Anzeigen:')
            neuelinks.append(webliste)
            break
    if neu > 0:
        f.seek(0)
        for p in webliste[:5]:
            f.write(p + '\n')
    print(neu)
    f.close()

    if neuelinks:
        sendmail(neuelinks)
else:
    print('keine Inserate!')
