
import streamlit as st
import joblib
import json
from PIL import Image
import pytesseract
import io

# Cargar modelo de clasificación
model = joblib.load("modelo_clasificacion.pkl")

# Cargar base de conocimiento
with open("base_conocimiento.json", "r", encoding="utf-8") as f:
    base_conocimiento = json.load(f)

def buscar_solucion(categoria):
    for item in base_conocimiento:
        if item["categoria"] == categoria:
            return item["solucion"], item["especialista"]
    return "No se encontró solución registrada.", "N/A"

def procesar_ocr(imagen):
    texto = pytesseract.image_to_string(imagen, lang='spa')
    return texto.strip()

# Interfaz
st.set_page_config(page_title="Demo IA - Clasificación de Tickets", layout="centered")
st.title("🎯 Clasificador Inteligente de Tickets de Soporte")
st.markdown("Este demo utiliza un modelo de IA para clasificar automáticamente tickets según su descripción o imagen.")

texto_ticket = st.text_area("📝 Describa el problema del ticket (obligatorio)", height=150)

imagen_ticket = st.file_uploader("🖼️ O cargue una imagen del error (opcional)", type=["png", "jpg", "jpeg"])

if st.button("🔍 Analizar Ticket"):
    if not texto_ticket and not imagen_ticket:
        st.warning("Debe ingresar una descripción o subir una imagen.")
    else:
        texto_final = texto_ticket
        if imagen_ticket:
            st.info("Procesando imagen con OCR...")
            imagen = Image.open(imagen_ticket)
            texto_img = procesar_ocr(imagen)
            if texto_img:
                st.markdown("**Texto detectado en imagen:**")
                st.code(texto_img)
                texto_final += " " + texto_img

        st.success("Clasificando ticket...")
        categoria = model.predict([texto_final])[0]
        solucion, especialista = buscar_solucion(categoria)

        st.markdown(f"### 📌 Categoría asignada: `{categoria}`")
        st.markdown(f"**👩‍💻 Especialista sugerido:** {especialista}")
        st.markdown("**✅ Solución recomendada:**")
        st.info(solucion)
