# Sistema Inteligente para Predicción, Clasificación y Recomendación en Transporte

Este repositorio contiene el **código fuente** para un sistema inteligente basado en aprendizaje profundo que resuelve tres problemáticas clave en una empresa de transporte:

1. **Predicción de demanda de rutas** (series de tiempo)
2. **Clasificación de conducción distractiva** (imágenes)
3. **Recomendación de destinos personalizados** (sistemas de recomendación)

**Este repositorio solo incluye el código. La aplicación web que integra los modelos se encuentra en un repositorio separado y se despliega en Hugging Face.**

---

## Estructura del Proyecto

```
RNA_G4_Sistema_Inteligente_Transporte/
├── LICENSE                        # Licencia del proyecto
├── README.md                      # Descripción del proyecto
├── reporte                        # Reporte técnico (RMarkdown y HTML)
├── src                            # Código fuente modular (demanda, clasificación, recomendación)
│   ├── clasificacion/             # Análisis y modelo de clasificación de conducción distractiva
│   ├── demanda/                   # Análisis y modelo de predicción de demanda
│   └── recomendacion/             # Análisis y modelo de recomendación de destinos
└── video                          # Archivos relacionados con el video del proyecto
```

---

## Guía Rápida de Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/vasquez-esteban/RNA_G4_Prediccion_Clasificacion_Recomendacion
cd RNA_G4_Prediccion_Clasificacion_Recomendacion
```

#### En Windows:

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup.bat
```

### 2. Entrenar y guardar los modelos

Dentro del directorio correspondiente (por ejemplo, `src/demanda`, `src/clasificacion` o `src/recomendacion`), están los cuadernos de Kaggle usados para cada modelo.

---

## Referencias

La **aplicación web** que integra estos modelos se encuentra en un repositorio separado y está desplegada en **Hugging Face**. En este repositorio, la aplicación web utiliza los modelos entrenados desde este repositorio para realizar las predicciones, clasificación y recomendaciones.

---

## Generar el reporte técnico

Requiere tener instalado **R** y **RStudio**.

1. Abrir `reporte/reporte_blog.Rmd`.
2. Instalar los paquetes necesarios:

```r
install.packages(c("ggplot2", "dplyr", "readxl", "kableExtra", "gganimate"))
```

3. Ejecutar o compilar como `HTML`.

---

## Publicaciones

- Reporte en RPubs: [Reporte](https://rpubs.com/evasp/rna-g4-trabajo3)
- **App Web**: Desplegada en Hugging Face [Aquí](https://evasp-rna-g4-trabajo3.hf.space/).
- Video explicativo [Aquí](https://www.youtube.com/watch?v=c_Ndzs11zYI).

---

## Estado Final

Este repositorio contiene reportes de los modelos entrenados. La app web está integrada en un repositorio separado y se despliega en **Hugging Face**. Ambos están documentados para su fácil uso e integración.
