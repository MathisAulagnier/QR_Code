# Générateur de QR Code

Ce script Python génère un QR Code à partir d'une URL en utilisant la bibliothèque `qrcode`.

## Utilisation

Pour utiliser ce script, suivez les étapes suivantes :

1. Assurez-vous d'avoir [Python](https://www.python.org) installé sur votre système.

2. Installez la bibliothèque `qrcode` si elle n'est pas déjà installée en utilisant la commande suivante :

   ```bash
   pip install qrcode
   ```

3. Exécutez le script en spécifiant les paramètres d'entrée suivants :

`--url : L'URL à encoder dans le QR Code.`

`--bcol : La couleur de fond du QR Code.` 

`--size : La taille du QR Code (entier).`

Voici un exemple d'utilisation :

```bash
python3 generateQR.py --url "votre_url" 
python3 generateQR.py --url "votre_url" --bcol "yellow"
python3 generateQR.py --url "votre_url" --bcol "yellow" --size 30
```

Le QR Code généré sera enregistré sous le nom ``qr.png`` dans le répertoire actuel.

Configuration par défaut

Si vous ne spécifiez pas d'arguments, le script utilisera les valeurs par défaut suivantes :

URL : "https://github.com/MathisAulagnier/QR_Code"
Couleur de fond : "white"
Taille : 10


## Auteur

Ce script a été créé par Aulagnier Mathis.

## Licence

Ce script est sous licence MIT. Consultez le fichier [LICENSE](LICENSE.md) pour plus de détails.
