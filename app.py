import gradio as gr
import joblib
import cv2
import numpy as np
import os

# --- CONFIGURATION CHEMINS ---
# On pointe vers le nouveau nom de dossier "models"
BASE_DIR = "models"
PATH_MODEL = os.path.join(BASE_DIR, "final_emotion_detection_svm_model.joblib")
PATH_PCA = os.path.join(BASE_DIR, "pca.joblib")
PATH_LABEL = os.path.join(BASE_DIR, "label_encoder.joblib")

# Debugging : On affiche ce qu'il y a sur le serveur pour être sûr
print(f"📂 Dossier actuel : {os.getcwd()}")
if os.path.exists(BASE_DIR):
    print(f"✅ Le dossier '{BASE_DIR}' existe. Contenu : {os.listdir(BASE_DIR)}")
else:
    print(f"❌ ERREUR : Le dossier '{BASE_DIR}' est introuvable !")
    print(f"   Contenu de la racine : {os.listdir('.')}")

# --- CHARGEMENT ---
print("Chargement du modèle SVM...")
MODELS_LOADED = False
ERROR_MSG = ""

try:
    if os.path.exists(PATH_MODEL):
        model = joblib.load(PATH_MODEL)
        pca = joblib.load(PATH_PCA)
        label_encoder = joblib.load(PATH_LABEL)
        print("✅ Modèle SVM chargé avec succès !")
        MODELS_LOADED = True
    else:
        ERROR_MSG = "Fichiers modèles introuvables."
except Exception as e:
    print(f"❌ Erreur chargement : {e}")
    ERROR_MSG = str(e)

def predict_emotion(image):
    if not MODELS_LOADED:
        return f"Erreur serveur : {ERROR_MSG}. (Vérifiez les logs)"
    
    if image is None:
        return "En attente..."

    try:
        # Conversion
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image

        # Traitement
        resized_img = cv2.resize(gray, (48, 48))
        normalized_img = resized_img / 255.0
        flattened_img = normalized_img.flatten().reshape(1, -1)
        pca_transformed_img = pca.transform(flattened_img)

        # Prédiction
        emotion_prediction = model.predict(pca_transformed_img)
        emotion_label = label_encoder.inverse_transform(emotion_prediction)[0]
        
        return str(emotion_label)

    except Exception as e:
        return f"Erreur calcul : {e}"

# Interface
interface = gr.Interface(
    fn=predict_emotion,
    inputs=gr.Image(sources=["webcam"], streaming=True, type="numpy"),
    outputs="text",
    live=True,
    title="Détection Émotion (SVM)",
    description="Projet Détection temps réel"
)

if __name__ == "__main__":
    interface.launch()