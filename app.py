import streamlit as st
import cv2
import numpy as np

st.title("📷 Scan Bulletin Quiz & Votes")

# --- CHAMP DE CAPTURE PHOTO ---
img_file = st.camera_input("Prendre le bulletin en photo")

if img_file is not None:
    with st.spinner('Analyse du bulletin en cours...'):
        # 1. Récupération des octets de l'image capturée par Streamlit
        bytes_data = img_file.getvalue()
        
        # 2. Conversion propre en tableau numpy 1D d'octets non signés
        file_bytes = np.frombuffer(bytes_data, np.uint8)
        
        # 3. Décodage de l'image via OpenCV
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        if img is not None:
            # 4. Conversion en نiveaux de gris pour le traitement OMR
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # --- ZONE DE TRAITEMENT OMR ---
            # (Tu peux insérer ici ta logique de détection des cases cochées)
            # score, vote_photo, vote_stand = process_omr_sheet(gray)
            
            # Affichage du résultat temporaire pour valider
            st.success("✅ Image décodée et traitée avec succès !")
            
        else:
            st.error("Erreur : Impossible de décoder l'image de la caméra. Essaie de reprendre une photo.")
