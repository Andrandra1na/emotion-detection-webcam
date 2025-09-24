import joblib
import cv2


model = joblib.load("joblib RandomForest/final_emotion_detection_RF_model.joblib")
label_encoder = joblib.load("joblib RandomForest/label_encoder_RF.joblib")
pca = joblib.load("joblib RandomForest/pca_RF.joblib")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Redimensionner l'image à la taille attendue par le modèle
    resized_img = cv2.resize(gray, (48, 48))
    
    # Normaliser l'image
    normalized_img = resized_img / 255.0
    
    # Transformer l'image en un vecteur 1D
    flattened_img = normalized_img.flatten().reshape(1, -1)
    
    # Appliquer le PCA à l'image normalisée
    pca_transformed_img = pca.transform(flattened_img)
    
    # Faire une prédiction avec le modèle chargé
    emotion_prediction = model.predict(pca_transformed_img)
    
    # Décoder l'émotion prédite en utilisant le LabelEncoder
    emotion_label = label_encoder.inverse_transform(emotion_prediction)[0]
    
    # Afficher l'émotion sur la vidéo en direct
    cv2.putText(frame, f'Emotion: {emotion_label}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Afficher le flux vidéo
    cv2.imshow('Emotion Detection', frame)
    
    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
