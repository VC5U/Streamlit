import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análisis con NumPy y Pandas", layout="wide")

# ------------------------------
# ENCABEZADO PRINCIPAL
# ------------------------------
st.title("📊 Aplicación Interactiva: NumPy, Pandas y Streamlit")
st.subheader("Realizado por: *Adriana Valentina Cornejo Ulloa*")
st.markdown("---")
st.write("Esta aplicación permite realizar análisis numérico y estadístico con **Python**, "
         "utilizando las librerías **NumPy**, **Pandas** y **Matplotlib** dentro de un entorno **Streamlit** interactivo.")

# ------------------------------
# CREACIÓN DE TABS
# ------------------------------
tabs = st.tabs([
    "📈 Ejercicio 1",
    "🎲 Ejercicio 2",
    "📊 Ejercicio 3",
    "⚙️ Ejercicio 4",
    "📚 DataFrame de Estudiantes"
])

# ------------------------------
# EJERCICIO 1
# ------------------------------
with tabs[0]:
    st.header("📈 Cálculos Estadísticos con NumPy")
    array = np.arange(1, 101)
    media = np.mean(array)
    mediana = np.median(array)
    varianza = np.var(array)
    percentil_90 = np.percentile(array, 90)

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Array generado (1 al 100):**")
        st.code(array, language="python")

    with col2:
        st.metric("Media", f"{media:.2f}")
        st.metric("Mediana", f"{mediana:.2f}")
        st.metric("Varianza", f"{varianza:.2f}")
        st.metric("Percentil 90", f"{percentil_90:.2f}")

# ------------------------------
# EJERCICIO 2
# ------------------------------
with tabs[1]:
    st.header("🎲 Matriz Aleatoria 5x5")
    matriz = np.random.randn(5, 5)
    determinante = np.linalg.det(matriz)
    traza = np.trace(matriz)

    st.write("**Matriz generada aleatoriamente:**")
    st.dataframe(matriz)

    col1, col2 = st.columns(2)
    col1.metric("Determinante", f"{determinante:.4f}")
    col2.metric("Traza", f"{traza:.4f}")

# ------------------------------
# EJERCICIO 3
# ------------------------------
with tabs[2]:
    st.header("📊 Distribución de Frecuencias")
    datos = np.random.randint(0, 11, 1000)
    valores, frecuencias = np.unique(datos, return_counts=True)
    tabla = pd.DataFrame({"Valor": valores, "Frecuencia": frecuencias})
    
    st.write("**Tabla de frecuencias:**")
    st.dataframe(tabla)

    fig, ax = plt.subplots()
    ax.bar(valores, frecuencias)
    ax.set_xlabel("Valor")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Distribución de números aleatorios entre 0 y 10")
    st.pyplot(fig)

# ------------------------------
# EJERCICIO 4
# ------------------------------
with tabs[3]:
    st.header("⚙️ Normalización de un Vector")

    modo = st.radio("Selecciona cómo generar el vector:", ("Manual", "Aleatorio"), horizontal=True)

    if modo == "Manual":
        vector_str = st.text_input("Ingresa los valores separados por comas:", "10, 20, 30, 40")
        try:
            v = np.array([float(x.strip()) for x in vector_str.split(",")])
        except:
            st.error("Por favor ingresa solo números separados por comas.")
            v = np.array([])
    else:
        tamaño = st.slider("Tamaño del vector aleatorio:", 3, 10, 5)
        v = np.random.randint(1, 100, tamaño)

    if v.size > 0:
        media_v = np.mean(v)
        desv_v = np.std(v)
        v_norm = (v - media_v) / desv_v

        col1, col2 = st.columns(2)
        col1.write(f"**Vector original:** {v}")
        col2.write(f"**Vector normalizado:** {np.round(v_norm, 2)}")

# ------------------------------
# 📚 DATAFRAME DE ESTUDIANTES (Datos reales)
# ------------------------------
with tabs[4]:
    st.header("📚 Tabla Interactiva de Estudiantes")
    st.write("Visualiza, filtra y descarga la información real de los estudiantes.")

    estudiantes_data = {
        "Nombre": [
            "Jhony","Ismael","Maura","Stalyn","Erick","Edwin","Adriana","Wendy",
            "Gilson","Kenny","Anthony","David","Carmen","Freddy","Jhon","Andrea"
        ],
        "Apellido": [
            "Mendez", "Loja", "Calle", "Pesantes", "Chacon", "Choez", "Cornejo", "Llivichuzhca",
            "Tenemea", "Valdivieso", "Fajardo", "Lopez", "Neira", "Gomez", "Montenegro", "Calle"
        ],
        "Celular": [
            "0998765432", "0987654321", "0976543210", "0965432109", "0954321098",
            "0943210987", "0932109876", "0921098765", "0910987654", "0955566778",
            "0988776655", "0977665544", "0966554433", "0955443322", "0944332211", "0933221100"
        ],
        "Edad": [
            20, 21, 19, 22, 20, 21, 23, 22,
            24, 20, 21, 23, 22, 21, 20, 22
        ],
        "Curso": [
            "Primer ciclo", "Segundo ciclo", "Tercer ciclo", "Cuarto ciclo", "Quinto ciclo",
            "Sexto ciclo", "Primer ciclo", "Segundo ciclo", "Tercer ciclo", "Cuarto ciclo",
            "Quinto ciclo", "Sexto ciclo", "Primer ciclo", "Segundo ciclo", "Tercer ciclo", "Cuarto ciclo"
        ],
        "Nota": [
            85, 90, 78, 88, 92, 76, 95, 80,
            84, 89, 91, 77, 82, 86, 79, 94
        ],
        "Asignatura": [
            "POO", "Base de datos", "Inteligencia artificial", "Metodología",
            "Formulación de proyectos", "Redes", "Inglés", "Kichwa",
            "App móvil", "Aplicaciones seguras", "Aplicaciones en la nube", "Ética",
            "Diversidad", "Tendencias actuales", "Legislación", "Emprendimiento"
        ]
    }

    df_estudiantes = pd.DataFrame(estudiantes_data)

    # --- FILTROS ---
    st.sidebar.header("🔍 Filtros de búsqueda")
    curso_sel = st.sidebar.multiselect("Selecciona el ciclo:", sorted(df_estudiantes["Curso"].unique()))
    materia_sel = st.sidebar.multiselect("Selecciona la asignatura:", sorted(df_estudiantes["Asignatura"].unique()))

    df_filtrado = df_estudiantes.copy()
    if curso_sel:
        df_filtrado = df_filtrado[df_filtrado["Curso"].isin(curso_sel)]
    if materia_sel:
        df_filtrado = df_filtrado[df_filtrado["Asignatura"].isin(materia_sel)]

    st.write("### 📋 Datos de los estudiantes filtrados:")
    st.dataframe(df_filtrado, use_container_width=True)

    # --- DESCARGA ---
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Descargar CSV filtrado",
        data=csv,
        file_name="estudiantes_filtrados.csv",
        mime="text/csv"
    )

st.markdown("---")
st.caption("💡 Desarrollado con Streamlit | NumPy | Pandas | Matplotlib")
