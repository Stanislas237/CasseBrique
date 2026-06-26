# 🧱 Casse-Brique

Un jeu de casse-brique développé en **Python** avec **Pygame**.

Le but est simple : détruire toutes les briques sans perdre toutes vos vies. Au fil des niveaux, la difficulté augmente et plusieurs bonus viennent pimenter la partie.

---

## 🎮 Fonctionnalités

- Plusieurs niveaux
- Difficulté progressive
- Système de vies
- Musique d'ambiance
- Effets sonores
- Fond d'écran choisi aléatoirement parmi 5 à chaque lancement

### Bonus

| Bonus | Effet |
|-------|-------|
| **Extend** | Élargit temporairement la plateforme |
| **Blast** | Rend la balle invincible (traverse les briques) |
| **Triple** | Ajoute deux balles supplémentaires |
| **Fast** | Augmente la vitesse de la balle |

---

## ❤️ Système de vies

- Le joueur commence avec **4 vies**.
- Une vie est perdue chaque fois que la balle tombe.
- À chaque niveau terminé, le joueur gagne **1 vie** (maximum **5**).
- La partie se termine lorsque toutes les vies sont perdues.

---

## 📈 Progression

À chaque niveau :

- la vitesse de la balle augmente ;
- une vie est gagnée (jusqu'à 5) ;
- le niveau suivant est chargé.

---

## 🚀 Installation

### Windows

Téléchargez la dernière version depuis les **Releases** puis lancez l'installateur.

Aucune installation de Python n'est nécessaire.

---

### Depuis les sources

Prérequis :

- Python 3.12+
- Pygame

Installation :

```bash
pip install pygame
python main.py
```

---

## 🛠️ Compilation

L'exécutable Windows est généré avec :

- PyInstaller (`--onefile --windowed`)
- Inno Setup pour l'installateur

---

## 📄 Licence

Ce projet est distribué sous la licence MIT.

---

## 👨‍💻 Crédits
Développé par **Stanislas (By Stan.co)**  
https://t.me/unity_engine_stan_co  

---

> *Merci de soutenir le projet en laissant une étoile ⭐ sur le dépôt et suivre le canal Telegram !*
