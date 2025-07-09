# AITickets
## 🎯 Sistema Inteligente de Clasificación de Tickets de Soporte

Este proyecto es un **demo funcional** que simula un sistema inteligente de gestión de tickets para la mesa de ayuda de Cualquier empresa, utilizando técnicas de inteligencia artificial basadas en agentes especializados.

---

## 🚀 Descripción

El sistema permite:
- Ingresar un ticket mediante texto y/o imagen.
- Aplicar **procesamiento de lenguaje natural** para clasificar el incidente automáticamente.
- Usar **visión por computadora (OCR)** para extraer texto de imágenes adjuntas.
- Consultar una **base de conocimiento simulada** para sugerir soluciones y asignar especialistas.

Todo esto está encapsulado en una interfaz web sencilla, construida con [**Streamlit**](https://streamlit.io/).

---

## 🧠 Arquitectura de la Solución

- **Frontend**: Streamlit
- **Backend (IA)**:
  - `scikit-learn` para clasificación automática
  - `OpenCV` + `pytesseract` para OCR de imágenes
- **Persistencia**: Base de conocimiento en formato `.json`
- **Lenguaje**: Python 3

---

## 📂 Estructura del Proyecto

```

📁 AIticket\
│
├── app.py                     # Aplicación Streamlit
├── modelo\_clasificacion.pkl   # Modelo de clasificación entrenado
├── base\_conocimiento.json     # Base de conocimiento simulada
├── ejemplos/                  # Carpeta para imágenes de prueba
│   └── error\_factura.png
└── README.md                  # Este archivo

````

---

## ⚙️ Instalación y Ejecución

1. Clona este repositorio o descarga los archivos.

2. Instala las dependencias:
```bash
pip install -r requirements.txt
````

3. Asegúrate de tener instalado **Tesseract OCR**:

* En Ubuntu:

```bash
sudo apt install tesseract-ocr
```

* En Windows:
  [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

4. Ejecuta la app:

```bash
streamlit run app.py
```

---

## 💡 Ejemplo de uso

1. Abre la interfaz local en tu navegador.
2. Escribe una descripción del problema o sube una imagen del error.
3. Haz clic en "🔍 Analizar Ticket".
4. El sistema mostrará:

   * Categoría del incidente
   * Especialista recomendado
   * Solución sugerida desde la base de conocimiento

---

## 🎓 Enfoque académico

Este proyecto fue desarrollado como parte del **Trabajo de Investigación en Ingeniería** de la **Corporación Unificada Nacional de Educación Superior - CUN**, aplicando principios de Ingeniería de Sistemas, Inteligencia Artificial y metodologías de innovación como **Design Thinking**.

---

## 📈 Resultados esperados

* ✅ Reducción simulada del tiempo de clasificación en 50%
* ✅ Precisión simulada de clasificación: 87%
* ✅ Uso eficiente de la base de conocimiento: 75%
* ✅ Alta aceptación del sistema por parte de los usuarios (4.3 / 5)

---

## 📜 Licencia

Este proyecto fue desarrollado con fines académicos. Puedes reutilizar el código respetando los créditos y propósitos de investigación y aprendizaje.

---

## 👨‍💻 Autor

**Andrés Mauricio Ardila Marín**
Estudiante de Ingeniería de Sistemas
CUN – Colombia 🇨🇴
2025
