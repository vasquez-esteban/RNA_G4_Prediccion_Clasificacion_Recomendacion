---
title: Rna G4 Trabajo3
emoji: 🐨
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.34.0
app_file: gradio_app/app.py
pinned: false
license: mit
short_description: Este proyecto implementa un sistema inteligente basado en RN
---

# Sistema Inteligente para Predicción, Clasificación y Recomendación en Transporte

Este proyecto implementa un sistema inteligente basado en aprendizaje profundo que resuelve tres problemáticas clave en una empresa de transporte:

1. **Predicción de demanda de rutas** (series de tiempo)
2. **Clasificación de conducción distractiva** (imágenes)
3. **Recomendación de destinos personalizados** (sistemas de recomendación)

Cada módulo está documentado, entrenado y expuesto mediante una interfaz web desarrollada en Streamlit y un backend hosteado en **Hugging Face**.

**Se recomienda trabajar en cuadernos de Kaggle para cada módulo. Allí se debe hacer el preprocesamiento, entrenamiento y evaluación de los modelos. Una vez entrenados, los modelos deben ser guardados localmente (formato .h5 o .pkl) para luego integrarlos en la aplicación web usando Hugging Face.**

---

## Estructura del Proyecto

```
RNA_G4_Sistema_Inteligente_Transporte/
├── files/             # Datos de entrada y salida
├── src/               # Código fuente modular
│   ├── demanda/
│   ├── clasificacion/
│   └── recomendacion/
├── streamlit_app/     # Aplicación web integrada
├── reporte/           # Reporte técnico (RMarkdown)
├── video/             # Recursos del video
├── requirements.txt
├── setup.sh / setup.bat
└── README.md
```

---

## Guía Rápida de Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/vasquez-esteban/RNA_G4_Sistema_Inteligente_Transporte
cd RNA_G4_Sistema_Inteligente_Transporte
```

### 2. Configurar entorno Python (Linux/macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

#### En Windows:

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup.bat
```

---

## Ejecutar la aplicación web

```bash
streamlit run streamlit_app/app.py
```

Se podrán subir imágenes de conducción, consultar la demanda esperada por ruta y obtener recomendaciones personalizadas para usuarios.

---

## Generar el reporte técnico

Requiere tener instalado **R** y **RStudio**.

1. Abrir `reporte/reporte_blog.Rmd`.
2. Instalar paquetes necesarios:

```r
install.packages(c("ggplot2", "dplyr", "readxl", "kableExtra", "gganimate"))
```

3. Ejecutar o compilar como `HTML`.

---

## Publicaciones

- Reporte en RPubs: [Reporte](https://rpubs.com/evasp/rna-g4-aplicaciones-prediccion-clasificacion-recomendacion)
- App Web
- Video

---

## Requisitos

- Python ≥ 3.10
- Streamlit ≥ 1.20
- TensorFlow ≥ 2.12 (para modelo de clasificación)
- R ≥ 4.0
- R packages: `rmarkdown`, `ggplot2`, `readxl`, `kableExtra`, `gganimate`

Todas las dependencias de Python están listadas en `requirements.txt`.

---

## Estado Final

Entrega final con modelos funcionales, app integrada y documentación profesional.
