---
title: Emotion Detection Webcam
emoji: 🎥
colorFrom: purple
colorTo: pink
sdk: gradio
app_file: app.py
pinned: false
---

# 🚀 Détection d'Émotions en Temps Réel via Webcam

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Ce projet a pour objectif de détecter les émotions humaines en temps réel à partir du flux vidéo d'une webcam. Il utilise des techniques de vision par ordinateur pour extraire les points de repère du visage (facial landmarks) et des modèles de Machine Learning pour classifier l'émotion correspondante.

<<<<<<< HEAD
## 📋 Table des Matières
1. [Fonctionnalités Clés](#-fonctionnalités-clés)
2. [Technologies Utilisées](#-technologies-utilisées)
3. [Prérequis](#-prérequis)
4. [Installation](#-installation)
5. [Utilisation](#-utilisation)
6. [Comment ça fonctionne ?](#-comment-ça-fonctionne-)
7. [Structure du Projet](#-structure-du-projet)
8. [Contribuer](#-contribuer)
9. [Licence](#-licence)

## ✨ Fonctionnalités Clés
- Détection de visage en temps réel : Localise le visage principal dans le flux vidéo.
- Extraction de 68 points de repère faciaux : Cartographie les traits du visage (yeux, bouche, nez...).
- Classification d'émotions : Utilise des modèles pré-entraînés pour prédire l'émotion.
- Deux modèles au choix :
  - Support Vector Machine (SVM) : Un classifieur robuste et efficace.
  - Random Forest : Un modèle d'ensemble performant.
- Affichage en direct : L'émotion détectée est affichée directement sur le flux vidéo.

## 🛠️ Technologies Utilisées
- Python 3.8+
- OpenCV : Pour la capture et le traitement vidéo en temps réel.
- Dlib : Pour la détection de visages et l'extraction des points de repère faciaux.
- Scikit-learn : Pour l'implémentation des modèles SVM et Random Forest.
- Joblib : Pour la sauvegarde et le chargement des modèles entraînés.
- Numpy : Pour les manipulations numériques.
- Jupyter Notebook : Pour l'expérimentation et l'entraînement des modèles.

## 🛑 Prérequis
Avant de commencer, vous aurez besoin de télécharger le modèle pré-entraîné de Dlib pour la détection des points de repère faciaux :
- [shape_predictor_68_face_landmarks.dat](http.dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
=======

## 📋 Table des Matières
1. [Fonctionnalités Clés](#-fonctionnalités-clés)
2. [Technologies Utilisées](#-technologies-utilisées)
3. [Prérequis](#-prérequis)
4. [Installation](#-installation)
5. [Utilisation](#-utilisation)
6. [Comment ça fonctionne ?](#-comment-ça-fonctionne-)
7. [Structure du Projet](#-structure-du-projet)
8. [Contribuer](#-contribuer)
9. [Licence](#-licence)

## ✨ Fonctionnalités Clés
- **Détection de visage en temps réel** : Localise le visage principal dans le flux vidéo.
- **Extraction de 68 points de repère faciaux** : Cartographie les traits du visage (yeux, bouche, nez...).
- **Classification d'émotions** : Utilise des modèles pré-entraînés pour prédire l'émotion.
- **Deux modèles au choix** :
  - **Support Vector Machine (SVM)** : Un classifieur robuste et efficace.
  - **Random Forest** : Un modèle d'ensemble performant.
- **Affichage en direct** : L'émotion détectée est affichée directement sur le flux vidéo.

## 🛠️ Technologies Utilisées
- **Python 3.8+**
- **OpenCV** : Pour la capture et le traitement vidéo en temps réel.
- **Dlib** : Pour la détection de visages et l'extraction des points de repère faciaux.
- **Scikit-learn** : Pour l'implémentation des modèles SVM et Random Forest.
- **Joblib** : Pour la sauvegarde et le chargement des modèles entraînés.
- **Numpy** : Pour les manipulations numériques.
- **Jupyter Notebook** : Pour l'expérimentation et l'entraînement des modèles.

## 🛑 Prérequis
Avant de commencer, vous aurez besoin de télécharger le modèle pré-entraîné de Dlib pour la détection des points de repère faciaux :
- **[shape_predictor_68_face_landmarks.dat](http.dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)**
>>>>>>> develop

Téléchargez-le, décompressez-le et placez le fichier `shape_predictor_68_face_landmarks.dat` à la racine de votre projet.

## 🔧 Installation

Suivez ces étapes pour mettre en place l'environnement de développement.

<<<<<<< HEAD
1. Clonez le dépôt :
=======
**1. Clonez le dépôt :**
>>>>>>> develop
```bash
git clone https://github.com/<VOTRE-USERNAME>/emotion-detection-webcam.git
cd emotion-detection-webcam
```

<<<<<<< HEAD
2. Créez un environnement virtuel (recommandé) :
=======
**2. Créez un environnement virtuel (recommandé) :**
>>>>>>> develop
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

<<<<<<< HEAD
3. Installez les dépendances :
=======
**3. Installez les dépendances :**
>>>>>>> develop
Créez un fichier `requirements.txt` avec le contenu suivant :
```txt
opencv-python
dlib
scikit-learn==1.3.0  # Spécifier une version peut éviter des conflits
numpy
```
Puis installez-le :
```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
4. Préparez le jeu de données :
Ce projet utilise un jeu de données qui n'est pas inclus dans le dépôt. Veuillez ajouter ici les instructions pour que l'utilisateur télécharge et décompresse `archive_4.zip` au bon endroit.

5. Entraînez les modèles :
=======
**4. Préparez le jeu de données :**
Ce projet utilise un jeu de données qui n'est pas inclus dans le dépôt. **Veuillez ajouter ici les instructions pour que l'utilisateur télécharge et décompresse `archive_4.zip` au bon endroit.**

**5. Entraînez les modèles :**
>>>>>>> develop
Les modèles `.joblib` sont ignorés par Git. Vous devez les générer en exécutant les notebooks Jupyter. Lancez Jupyter :
```bash
jupyter notebook
```
Ouvrez et exécutez les cellules des deux notebooks suivants pour entraîner les modèles et sauvegarder les fichiers `.joblib` dans les dossiers `joblib SVM/` et `joblib RandomForest/` :
- `SVM_WEBCAM_FINAL.ipynb`
- `AMELIORATION_MODELE_WEBCAM.ipynb`

## ▶️ Utilisation

Une fois l'installation terminée, vous pouvez lancer la détection d'émotions. Assurez-vous que votre webcam est connectée et fonctionnelle.

<<<<<<< HEAD
Pour utiliser le modèle SVM :
=======
**Pour utiliser le modèle SVM :**
>>>>>>> develop
```bash
python webcamwithmodelsvm.py
```

<<<<<<< HEAD
Pour utiliser le modèle Random Forest :
```bash
python webcamwithmodelrandomforest.py
```
Appuyez sur la touche 'q' pour quitter l'application.

## 🧠 Comment ça fonctionne ?
Le pipeline de traitement est le suivant :
1.  Capture Vidéo : Une image est capturée depuis la webcam.
2.  Détection de Visage : La bibliothèque Dlib détecte la position du visage dans l'image.
3.  Extraction des Points de Repère : Le modèle `shape_predictor_68_face_landmarks.dat` est utilisé pour extraire les 68 points clés du visage.
4.  Prétraitement : Les coordonnées des points sont normalisées et une Analyse en Composantes Principales (ACP) est appliquée pour réduire la dimensionnalité et extraire les caractéristiques les plus pertinentes.
5.  Prédiction : Le vecteur de caractéristiques est passé au modèle de Machine Learning chargé (SVM ou Random Forest) qui prédit l'émotion.
6.  Affichage : Un rectangle est dessiné autour du visage et l'émotion prédite est affichée en haut de celui-ci.
=======
**Pour utiliser le modèle Random Forest :**
```bash
python webcamwithmodelrandomforest.py
```
Appuyez sur la touche **'q'** pour quitter l'application.

## 🧠 Comment ça fonctionne ?
Le pipeline de traitement est le suivant :
1.  **Capture Vidéo** : Une image est capturée depuis la webcam.
2.  **Détection de Visage** : La bibliothèque Dlib détecte la position du visage dans l'image.
3.  **Extraction des Points de Repère** : Le modèle `shape_predictor_68_face_landmarks.dat` est utilisé pour extraire les 68 points clés du visage.
4.  **Prétraitement** : Les coordonnées des points sont normalisées et une Analyse en Composantes Principales (ACP) est appliquée pour réduire la dimensionnalité et extraire les caractéristiques les plus pertinentes.
5.  **Prédiction** : Le vecteur de caractéristiques est passé au modèle de Machine Learning chargé (SVM ou Random Forest) qui prédit l'émotion.
6.  **Affichage** : Un rectangle est dessiné autour du visage et l'émotion prédite est affichée en haut de celui-ci.
>>>>>>> develop

## 📂 Structure du Projet
```
.
├── .gitignore                    # Fichiers à ignorer par Git
├── AMELIORATION_MODELE_WEBCAM.ipynb # Notebook pour l'entraînement du modèle Random Forest
├── SVM_WEBCAM_FINAL.ipynb        # Notebook pour l'entraînement du modèle SVM
├── webcamwithmodelrandomforest.py # Script principal (utilise le modèle Random Forest)
├── webcamwithmodelsvm.py         # Script principal (utilise le modèle SVM)
├── requirements.txt              # Liste des dépendances Python
├── README.md                     # Ce fichier
└── shape_predictor_68_face_landmarks.dat # (Prérequis) Modèle Dlib
```

## 🤝 Contribuer
Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce projet, n'hésitez pas à forker le dépôt et à créer une Pull Request.
1. Forkez le projet.
2. Créez votre branche de fonctionnalité (`git checkout -b feature/NouvelleFonctionnalite`).
3. Commitez vos changements (`git commit -m 'feat: Ajout d'une nouvelle fonctionnalité'`).
4. Pushez vers la branche (`git push origin feature/NouvelleFonctionnalite`).
5. Ouvrez une Pull Request.
