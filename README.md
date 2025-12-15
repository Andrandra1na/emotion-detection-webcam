---

title: Emotion Detection Webcam
emoji: 🎥
colorFrom: purple
colorTo: pink
sdk: gradio
app_file: app.py
pinned: false
-------------

# 🚀 Détection d’Émotions en Temps Réel via Webcam

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Ce projet permet de détecter les émotions humaines en temps réel à partir du flux vidéo d’une webcam. Il combine des techniques de vision par ordinateur (détection de visage et points de repère faciaux) et des modèles de Machine Learning pour classifier l’émotion observée.

---

## 📋 Table des matières

1. Fonctionnalités
2. Technologies utilisées
3. Prérequis
4. Installation
5. Entraînement des modèles
6. Utilisation
7. Fonctionnement interne
8. Structure du projet
9. Contribution
10. Licence

---

## ✨ Fonctionnalités

* Détection de visage en temps réel via la webcam
* Extraction de 68 points de repère faciaux (facial landmarks)
* Classification automatique des émotions
* Choix du modèle de prédiction :

  * Support Vector Machine (SVM)
  * Random Forest
* Affichage en direct de l’émotion détectée sur le flux vidéo

---

## 🛠️ Technologies utilisées

* Python 3.8+
* OpenCV (capture et traitement vidéo)
* Dlib (détection de visage et landmarks)
* Scikit-learn (SVM et Random Forest)
* Joblib (sauvegarde et chargement des modèles)
* NumPy (calculs numériques)
* Jupyter Notebook (entraînement et expérimentation)

---

## 🛑 Prérequis

Avant de lancer le projet, téléchargez le modèle Dlib des points de repère faciaux :

* shape_predictor_68_face_landmarks.dat
  [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

Décompressez le fichier et placez `shape_predictor_68_face_landmarks.dat` à la racine du projet.

---

## 🔧 Installation

1. Cloner le dépôt

```bash
git clone https://github.com/<VOTRE-USERNAME>/emotion-detection-webcam.git
cd emotion-detection-webcam
```

2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
```

3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Contenu du fichier `requirements.txt` :

```txt
opencv-python
dlib
scikit-learn==1.3.0
numpy
```

---

## 🧪 Entraînement des modèles

Les fichiers `.joblib` ne sont pas versionnés dans le dépôt. Les modèles doivent être entraînés localement.

1. Lancer Jupyter Notebook

```bash
jupyter notebook
```

2. Exécuter les notebooks suivants :

* `SVM_WEBCAM_FINAL.ipynb` (modèle SVM)
* `AMELIORATION_MODELE_WEBCAM.ipynb` (modèle Random Forest)

Les modèles entraînés seront sauvegardés dans les dossiers correspondants.

---

## ▶️ Utilisation

Assurez-vous que votre webcam est connectée et fonctionnelle.

* Lancer la détection avec le modèle SVM

```bash
python webcamwithmodelsvm.py
```

* Lancer la détection avec le modèle Random Forest

```bash
python webcamwithmodelrandomforest.py
```

Appuyez sur la touche **q** pour quitter l’application.

---

## 🧠 Fonctionnement interne

1. Capture du flux vidéo depuis la webcam
2. Détection du visage avec Dlib
3. Extraction des 68 points de repère faciaux
4. Normalisation des coordonnées et réduction de dimension (ACP)
5. Prédiction de l’émotion via le modèle sélectionné
6. Affichage de l’émotion et du cadre du visage en temps réel

---

## 📂 Structure du projet

```
.
├── AMELIORATION_MODELE_WEBCAM.ipynb
├── SVM_WEBCAM_FINAL.ipynb
├── webcamwithmodelsvm.py
├── webcamwithmodelrandomforest.py
├── requirements.txt
├── README.md
└── shape_predictor_68_face_landmarks.dat
```

---

## 🤝 Contribution

Les contributions sont bienvenues.

1. Forker le projet
2. Créer une branche (`feature/nom-fonctionnalite`)
3. Commiter les changements
4. Pusher la branche
5. Ouvrir une Pull Request

---

## 📄 Licence

Ce projet est distribué sous licence MIT.
