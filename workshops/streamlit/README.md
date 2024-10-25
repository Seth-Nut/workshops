# Proyecto de Análisis de Datos del Titanic 🚢

Este proyecto es una aplicación interactiva en Streamlit para explorar el conjunto de datos del Titanic. La app permite visualizar y analizar factores que influyeron en la supervivencia de los pasajeros.

## Estructura de Archivos

- `app.py`: Archivo principal para la aplicación de Streamlit. 

## Requisitos

- Python 3.8 o superior
- Paquetes: `streamlit`, `pandas`, `plotly`, `altair`

Instala los paquetes necesarios con:

```bash
pip install -r requirements.txt
```

## Instrucciones para completar `app.py`

### 1. **Agregar textos**

```python
texto_introduccion = """
    ### Introducción 

    El **RMS Titanic**, uno de los transatlánticos más grandes y lujosos de su época, se hundió     trágicamente el 15 de abril de 1912,
    después de chocar contra un iceberg durante su viaje inaugural desde Southampton a Nueva York.  Este desastre es uno de los 
    incidentes marítimos más emblemáticos de la historia, con una pérdida significativa de vidas.   A bordo del Titanic, se encontraban 
    pasajeros de distintas clases sociales, edades y nacionalidades, todos enfrentándose a las  mismas adversidades pero con diferentes 
    tasas de supervivencia.

    ¡Comencemos la exploración de los datos y descubramos qué factores influyeron en la     supervivencia a bordo del Titanic!
"""

texto_conclusiones = """
    ### Conclusiones

    En este análisis, exploramos cómo factores clave como la **edad**, el **género**, la **clase**  y el hecho de viajar con 
    **familiares** influyeron en las probabilidades de supervivencia de los pasajeros del Titanic:

    - **Género**: Las mujeres sobrevivieron más que los hombres, reflejando la política de  "mujeres y niños primero".
    - **Clase**: Los pasajeros de primera clase tuvieron una mayor probabilidad de supervivencia    en comparación con los de 
      segunda y tercera clase.
    - **Edad**: Los niños pequeños sobrevivieron más que los adultos, especialmente si viajaban     con familiares.
    - **Familiares**: Viajar en familia aumentó las probabilidades de supervivencia, posiblemente   debido al apoyo mutuo.

    Este análisis nos muestra cómo las circunstancias personales y sociales influyeron en el    destino de los pasajeros del Titanic. 
"""
```

### 2. **Agregar Datos y Funciones Faltantes**

   **Carga de Datos:**
   Agrega la siguiente función `cargar_datos()` en `app.py` para cargar el conjunto de datos del Titanic:

   ```python
   @st.cache_data
   def cargar_datos():
       """
       Cargar los datos del Titanic desde una URL pública.
       """
       return pd.read_csv("data/titanic.csv")
   ```

   **Preprocesamiento de Datos:**
   Copia esta función `preprocesar_datos()` en `app.py` para limpiar y transformar el DataFrame antes de la visualización:

   ```python
   def preprocesar_datos(df):
       # Eliminar columnas no necesarias
       cols_eliminar = ['Name', 'Ticket']
       df = df.drop(cols_eliminar, axis=1)

       # Rellenar valores faltantes
       df['Age'] = df['Age'].fillna(df['Age'].mean())
       df['Cabin'] = df['Cabin'].fillna('N').str[0]  # Solo tomar la primera letra de 'Cabin'
       df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

       # Convertir columnas a tipos adecuados
       cols_convertir = ['Pclass', 'SibSp', 'Parch']
       df[cols_convertir] = df[cols_convertir].astype(str)
       
       return df
   ```

### 3. **Completar Visualización de Variables**

   **Gráficos para Variables Numéricas:**
   Copia el contenido de la función `plot_numeric_variables()` de `app-solution.py` en `app.py` para habilitar el análisis de variables numéricas con histogramas:

   ```python
   def plot_numeric_variables(df):
       st.markdown("### Análisis de Variables Numéricas")
       col1, col2 = st.columns(2)
       variable = col1.selectbox("Seleccione una variable numérica:", ['Age', 'Fare'], key="numeric_var_select")

       # Histograma
       plot_type = col2.selectbox("Tipo de gráfico:", ["Univariado", "Bivariado"], key="numeric_plot_type")
       
       if plot_type == "Univariado":
           fig = px.histogram(df, x=variable, title=f"Histograma de {variable}")
       else:
           fig = px.histogram(df, x=variable, color='Survived', title=f"Histograma de {variable} por Supervivencia")

       st.plotly_chart(fig)
   ```

   **Gráficos para Variables Categóricas:**
   Completa la función `plot_categorical_variables()` en `app.py` para crear gráficos de barras para variables categóricas:

   ```python
   def plot_categorical_variables(df):
       st.markdown("### Análisis de Variables Categóricas")
       col1, col2 = st.columns(2)
       variable = col1.selectbox("Seleccione una variable categórica:", ['Pclass', 'Sex', 'SibSp', 'Embarked'], key="categorical_var_select")

       # Gráfico de barras
       plot_type = col2.selectbox("Tipo de gráfico:", ["Univariado", "Bivariado"], key="categorical_plot_type")

       if plot_type == "Univariado":
           chart = alt.Chart(df).mark_bar().encode(
               alt.X(variable, title=variable),
               y='count()',
               tooltip=[variable, 'count()']
           ).properties(
               title=f"Barplot de {variable}"
           )
       else:
           chart = alt.Chart(df).mark_bar().encode(
               alt.X(variable, title=variable),
               y='count()',
               color='Survived:N',
               tooltip=[variable, 'count()', 'Survived']
           ).properties(
               title=f"Barplot de {variable} por Supervivencia"
           )

       st.altair_chart(chart, use_container_width=True)
   ```

### 4. **Estructura Principal (`cs_sidebar` y `cs_body`)**

   **Sidebar (`cs_sidebar()`):**
   Añade la función `cs_sidebar()` en `app.py` para configurar el sidebar con los objetivos y la información del dataset:

   ```python
   def cs_sidebar():
       """
       Sidebar con un resumen del análisis del Titanic.
       """
       st.sidebar.title("Análisis del Titanic")

       # Mostrar logo del Titanic
       logo_url = "images/titanic.png"
       st.sidebar.image(logo_url, width=300)

       # Objetivos del análisis
       with st.sidebar:
           with st.expander("🎯 Objetivos del Análisis"):
               st.markdown(
                   """
                   1. **Supervivencia**: Explorar los factores que influyeron en la supervivencia de los pasajeros.
                   2. **Características Clave**: Analizar cómo la clase, el género y la edad afectan las probabilidades de supervivencia.
                   3. **Visualización de Datos**: Mostrar gráficos que faciliten la comprensión de los resultados.
                   """
               )

           # Información relevante del dataset
           with st.expander("📊 Información del Dataset"):
               st.markdown(
                   """
                   1. **Pasajeros**: El conjunto de datos contiene información sobre 891 pasajeros del Titanic.
                   2. **Supervivencia**: La columna `Survived` indica si un pasajero sobrevivió o no (1: sobrevivió, 0: no sobrevivió).
                   3. **Variables Principales**:
                      - `Pclass`: Clase del pasajero (1ª, 2ª o 3ª).
                      - `Sex`: Género del pasajero.
                      - `Age`: Edad del pasajero.
                      - `SibSp`: Número de hermanos/esposos a bordo.
                      - `Parch`: Número de padres/hijos a bordo.
                      - `Fare`: Tarifa pagada por el pasajero.
                      - `Embarked`: Puerto de embarque (C = Cherburgo, Q = Queenstown, S = Southampton).
                   4. **Fuente**: [Dataset del Titanic](https://www.kaggle.com/c/titanic/data)
                   """
               )

       # Footnote en el sidebar
       st.sidebar.markdown("""
       ---
       📄 **Material elaborado por [Seth&Nut](https://seth-nut.github.io/website/)**.
       """)
   ```

   **Contenido Principal (`cs_body()`):**
   Completa `cs_body()` en `app.py` para añadir la introducción, visualizaciones y conclusiones:

   ```python
   def cs_body():
       st.title("Análisis Exploratorio de Datos - Titanic")

       # Introducción al conjunto de datos del Titanic
       st.markdown(texto_introduccion)
       
       # Cargar y preprocesar datos
       df = cargar_datos()
       df_preprocesado = preprocesar_datos(df)
       
       st.subheader("Datos del Titanic")
       st.write(df.head())

       # Análisis de variables numéricas y categóricas
       plot_numeric_variables(df_preprocesado)
       plot_categorical_variables(df_preprocesado)

       # Conclusiones
       st.markdown(texto_conclusiones)

       # Llamar a la función en el momento adecuado
       show_typing_effect(agradecimiento)
   ```

### 5. **Ejecutar la Aplicación**
   Una vez completado `app.py`, ejecuta la aplicación en Streamlit con el siguiente comando:

   ```bash
   streamlit run app.py
   ```

Con estas instrucciones, deberías tener una versión funcional de `app.py` completa y lista para ejecutar como se muestra en `app-solution.py`.

## Recursos

- Dataset de Titanic: [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)
- [Documentación de Streamlit](https://docs.streamlit.io/)

## Créditos

Material elaborado por el equipo de [Seth&Nut](https://seth-nut.github.io/website/).
