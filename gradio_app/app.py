"""App principal con nuestros modelos"""

import gradio as gr  # type: ignore


def greet(name):
    """Función de prueba"""
    return "Hello " + name + "!!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
