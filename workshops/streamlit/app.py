import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import time

# Configuración de la página
st.set_page_config(
    page_title="Titanic Dataset",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

texto_introduccion = """
    ### Introducción 
    
    ...
    
"""

texto_conclusiones = """
    ### Conclusiones

    ...

"""

# Función para mostrar el mensaje letra por letra
def show_typing_effect(message, delay=0.1):
    # Usa un contenedor vacío para actualizar el texto
    text_placeholder = st.empty()
    text = ""

    # Mostrar el mensaje letra por letra
    for char in message:
        text += char
        text_placeholder.markdown(text)
        time.sleep(delay)

# Mensaje de agradecimiento
agradecimiento = "😊 ¡Gracias por acompañarnos en este recorrido histórico y por explorar los datos con nosotros!"


# Función para graficar variables numéricas
def plot_numeric_variables(df):
    st.markdown("### Análisis de Variables Numéricas")
    col1, col2 = st.columns(2)
    variable = col1.selectbox("Seleccione una variable numérica:", ['Age', 'Fare'], key="numeric_var_select")

    # Histograma
    plot_type = col2.selectbox("Tipo de gráfico:", ["Univariado", "Bivariado"], key="numeric_plot_type")


# Función para graficar variables categóricas
def plot_categorical_variables(df):
    st.markdown("### Análisis de Variables Categóricas")
    col1, col2 = st.columns(2)
    variable = col1.selectbox("Seleccione una variable categórica:", ['Pclass', 'Sex', 'SibSp', 'Embarked'], key="categorical_var_select")

    # Gráfico de barras
    plot_type = col2.selectbox("Tipo de gráfico:", ["Univariado", "Bivariado"], key="categorical_plot_type")

def main():
    """
    Main function to set up the Streamlit app layout.
    """
    cs_sidebar()  # Configura el contenido de la barra lateral
    cs_body()     # Configura el contenido del cuerpo principal
    return None

def cs_sidebar():
    """
    Sidebar con un resumen del análisis del Titanic.
    """
    st.sidebar.title("Análisis del Titanic")

    # Mostrar logo del Titanic
    logo_url = "images/empty.png"
    st.sidebar.image(logo_url, width=300)

    # Objetivos del análisis
    with st.sidebar:
        with st.expander("🎯 Objetivos del Análisis"):
            st.markdown(
                """
                1. ...
                2. ...
                3. ...
                """
            )

        # Información relevante del dataset
        with st.expander("📊 Información del Dataset"):
            st.markdown(
                """
                1. ...
                2. ...
                3. ...
                4. ...
                """
            )

    # Footnote en el sidebar
    st.sidebar.markdown("""
    ---
    📄 **Material elaborado por [Seth&Nut](https://seth-nut.github.io/website/)**.
    """)

# Función principal
def cs_body():
    st.title("Análisis Exploratorio de Datos - Titanic")

    # Introducción al conjunto de datos del Titanic
    st.markdown(texto_introduccion)
    

    st.subheader("Datos del Titanic")
    st.write(pd.DataFrame())

    # Análisis de variables numéricas y categóricas
    plot_numeric_variables(pd.DataFrame())
    plot_categorical_variables(pd.DataFrame())

    # Conclusiones
    st.markdown(texto_conclusiones)

    # Llamar a la función en el momento adecuado
    show_typing_effect(agradecimiento)

# Ejecutar la aplicación
if __name__ == "__main__":
    main()