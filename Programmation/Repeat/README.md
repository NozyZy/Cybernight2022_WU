## Repeat

> Categorie : Prog
>
> Timon : Il te faut peut-être une autre méthode, répète après moi : Hakuna Matata. 
> Simba : Quoi ?!
> Pumba: Ha-ku-na Ma-ta-ta ! ça veut dire: pas de soucis !!
>
> Difficulté : Easy
>
> Auteur : Maestran
>
> Command : nc 10.242.0.1 10002

On se connecte donc via un shell, et ça nous demande répéter ma chaine '123456789'<br/>
On répète donc, et ça nous demande d'aller plus vite, et de répéter une autre chaine

En essayant plusieurs fois à la main, on voit que la première chaine est toujours la même, mais que les suivantes changent.<br/>
Il faut donc programmer la répétition : 

En utilisant le pacakeg python `pwntools` (`pip install pwntools`)

```py
from pwn import *
conn = remote('10.242.0.1', 10002) # connexion
# répéter à l'infini
while True:
    # on récupère l'output en format bytes, donc il faut le décoder
	data = conn.recvline().decode('utf-8').strip()
	# on affiche les données reçues
	print("> " + data)
	# On ne va envoyer que ce dont on a besoin de répéter, donc on eclue les messages du bot
	if data and 'Répète après moi :' not in data and 'Bravo ! Plus vite maintenant' not in data:
        # on répète donc la chaine de caractère, mais encodée en bytes
		conn.send(f'{data}\n'.encode())
conn.close()
```

Vous remarquerez que l'on boucle à l'infini, et que l'on ne s'arrête pas quand l'on trouve un string 'CYBN', et bien parce que l'on doit répéter au moins une fois un faux flag<br/>
Donc on attend que l'on ne reçoive plus rien, c'est-à-dire quand la console arrête de print

Allez, voilà le flag

🚩 `CYBN{S0m3t1m3s_1t's_34s13r_t0_4ut0m4t3_n0?}`
