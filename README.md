# Détection d'Émotions en Temps Réel via Webcam

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ce projet a pour objectif de détecter les émotions humaines (joie, tristesse, colère, etc.) en temps réel à partir du flux vidéo d'une webcam, en utilisant des modèles de Machine Learning entraînés sur des points de repère faciaux.

## Table des Matières
1. [Fonctionnalités](#fonctionnalités)
2. [Structure du Projet](#structure-du-projet)
3. [Prérequis](#prérequis)
4. [Installation](#installation)
5. [Utilisation](#utilisation)
6. [Entraîner un nouveau modèle](#entraîner-un-nouveau-modèle)

## Fonctionnalités
- Détection de visage en temps réel.
- Extraction de 68 points de repère faciaux (facial landmarks).
- Classification des émotions à l'aide de deux modèles au choix :
  - **Support Vector Machine (SVM)**
  - **Random Forest**
- Affichage de l'émotion détectée directement sur le flux vidéo.

## Structure du Projet
```
.
├── AMELIORATION_MODELE_WEBCAM.ipynb  # Notebook pour le modèle Random Forest
├── SVM_WEBCAM_FINAL.ipynb            # Notebook pour le modèle SVM
├── webcamwithmodelrandomforest.py    # Script principal pour lancer la détection (Random Forest)
├── webcamwithmodelsvm.py             # Script principal