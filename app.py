import gradio as gr
import joblib
import cv2
import numpy as np

# 1. Chargement des modèles
# On utilise les mêmes chemins que dans ton dossier
print("Chargement du modèle RandomForest...")
try:
    model = joblib.load("joblib RandomForest/final_emotion_detection_RF_model.joblib")
    label_encoder = joblib.load("joblib RandomForest/label_encoder_RF.joblib")
    pca = joblib.load("joblib RandomForest/pca_RF.joblib")
    print("Modèles chargés avec succès !")
except Exception as e:
    print(f"Erreur lors du chargement des modèles : {e}")

def predict_emotion(image):
    """
    Fonction qui prend une image (depuis la webcam du navigateur),
    applique le même traitement que ton script local,
    et renvoie l'émotion.
    """
    if image is None:
        return "En attente de la caméra..."

    # L'image vient de Gradio en format RGB
    # Etape 1 : Conversion en niveaux de gris
    # Note: Gradio envoie du RGB, donc on fait RGB2GRAY (pas BGR2GRAY)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Etape 2 : Redimensionnement (48x48) - Comme dans ton script
    resized_img = cv2.resize(gray, (48, 48))
    
    # Etape 3 : Normalisation (CRUCIAL : / 255.0) - Comme dans ton script
    normalized_img = resized_img / 255.0
    
    # Etape 4 : Aplatissement (Flatten)
    flattened_img = normalized_img.flatten().reshape(1, -1)
    
    # Etape 5 : Transformation PCA
    pca_transformed_img = pca.transform(flattened_img)
    
    # Etape 6 : Prédiction
    emotion_prediction = model.predict(pca_transformed_img)
    
    # Etape 7 : Décodage du label
    emotion_label = label_encoder.inverse_transform(emotion_prediction)[0]
    
    return emotion_label

# 2. Création de l'interface Web
interface = gr.Interface(
    fn=predict_emotion,
    inputs=gr.Image(sources=["webcam"], streaming=True, type="numpy"), 
    outputs="text",
    live=True, # Permet le temps réel
    title="Détection d'Émotion (Random Forest)",
    description="Ce modèle analyse votre visage en temps réel (48x48 pixels + PCA + Random Forest)."
)

# Lancement de l'application
if __name__ == "__main__":
    interface.launch()