import gradio as gr
import joblib
import cv2
import numpy as np
import os

# --- CONFIGURATION CHEMINS ---
# On vérifie si le dossier existe pour éviter le crash brutal
BASE_DIR = "joblib SVM"
PATH_MODEL = os.path.join(BASE_DIR, "final_emotion_detection_svm_model.joblib")
PATH_PCA = os.path.join(BASE_DIR, "pca.joblib")
PATH_LABEL = os.path.join(BASE_DIR, "label_encoder.joblib")

print(f"Dossier de travail actuel : {os.getcwd()}")
print(f"Contenu du dossier : {os.listdir('.')}")

# --- CHARGEMENT ---
print("Chargement du modèle SVM...")
MODELS_LOADED = False
ERROR_MSG = ""

if os.path.exists(BASE_DIR):
    try:
        model = joblib.load(PATH_MODEL)
        pca = joblib.load(PATH_PCA)
        label_encoder = joblib.load(PATH_LABEL)
        print("✅ Modèle SVM chargé avec succès !")
        MODELS_LOADED = True
    except Exception as e:
        print(f"❌ Erreur chargement joblib : {e}")
        ERROR_MSG = str(e)
else:
    print(f"❌ ERREUR GRAVE : Le dossier '{BASE_DIR}' est introuvable sur le serveur.")
    ERROR_MSG = f"Dossier '{BASE_DIR}' introuvable. Vérifiez l'upload."

def predict_emotion(image):
    if not MODELS_LOADED:
        return f"Erreur serveur : {ERROR_MSG}"
    
    if image is None:
        return "En attente..."

    try:
        # Conversion
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image

        # Traitement identique à l'entraînement
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
    description="Si vous voyez ce message, le déploiement a réussi."
)

if __name__ == "__main__":
    interface.launch()