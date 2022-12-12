## Auth2

> Categorie : Reverse
>
> Bon en vrai au début j'étais naze, je retente !
> `Le flag n'est pas au format cybn{}`
>
> Difficulté : Easy
>
> Auteur : m00n


Un fichier .py cette fois-ci

```python
import base64

a = b'Vly{4Gjd-vbvI~VZ8UjeGX'
wlcm = b'PitX$AaidZbZBKDW@&PBbRc1MbZBL6bRc(Ob8aVeAZKrHWG*00VR>R@AY*7@Zf9w3XCQQFWgu)}ZfA92XJsIFX>4pDXk~10E&'
prmt = b'MQ(Iuav*eQWgu{2b8~lZa%4In'
print(base64.b85decode(wlcm.decode()).decode())
b = input(base64.b85decode(prmt.decode()).decode())
b = base64.b85encode(str.encode(b))
if a == b:
    print("Can you stop breaking my authentification FOR 5 MINUTES ?! Im trying to learn !\n(tu peux soumettre ce password comme flag)")
else:
    print("Well seems stronger this time, try again !")
```

Beaucoup de texte encodé 🤧

Mais en regardant de plus près, on voit que l'on doit rentrer un input, sauvegardé dans `b`, mais surtout encodé avant d'etre sauvegardé<br/>
Puis on compare cet input encodé avec `a`. Et la valeur de `a` ne change pas tout du long. Et si on affichait la valeur décodée de `a` ?

En s'inspirant des lignes du code, on peut alors avoir : 
```python
print(base64.b85decode(wlcm.decode()).decode())
print(base64.b85decode(a.decode()).decode())
```

et si on exécute : 
```
Okay so the first authent wasn't good. Maybe changing the language will help.
b3773r_4u7h_m4yb3
```

🚩 `cybn{b3773r_4u7h_m4yb3}`
