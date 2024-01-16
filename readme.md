
# Web Crawler per la ricerca di email

Questo script Python utilizza le librerie `requests`, `BeautifulSoup` e `re` per cercare indirizzi email in pagine web. Il crawler segue tutti i link fino a una profondità massima impostabile.

## Installazione

Per eseguire questo script, è necessario avere installato Python e le seguenti librerie Python:

- requests
- BeautifulSoup
- re
- argparse

Puoi installare queste librerie con pip:

```pip install requests beautifulsoup4```



## Utilizzo

Per utilizzare questo script, esegui il seguente comando da terminale:

```python crawler.py -d <depth> -q <query```


Dove:

*depth* è la profondità massima di crawling (obbligatorio)
*query* è la query di ricerca (obbligatorio)

### Note
Questo script è molto semplice e non gestisce errori di rete, pagine non trovate, ecc. Potrebbe essere necessario aggiungere ulteriori controlli per gestire questi casi. Inoltre, l'uso di web crawler può essere regolato da termini di servizio o leggi sulla privacy, quindi assicurati di utilizzarlo in modo responsabile.


Ricorda di sostituire <depth> e <query> con i valori desiderati quando esegui lo script.
