import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análisis con NumPy y Pandas", layout="wide")

st.title("📊 Aplicación Interactiva: NumPy, Pandas y Streamlit")
st.write("Aplicación para análisis numérico y estadístico con Python, desarrollada en Streamlit.")

# ---------------------------------
# EJERCICIO 1
# ---------------------------------
st.header("Ejercicio 1: Cálculos Estadísticos")
array = np.arange(1, 101)
media = np.mean(array)
mediana = np.median(array)
varianza = np.var(array)
percentil_90 = np.percentile(array, 90)

st.write(f"**Array:** {array}")
st.write(f"**Media:** {media}")
st.write(f"**Mediana:** {mediana}")
st.write(f"**Varianza:** {varianza}")
st.write(f"**Percentil 90:** {percentil_90}")

# ---------------------------------
# EJERCICIO 2
# ---------------------------------
st.header("Ejercicio 2: Matriz Aleatoria 5x5")
matriz = np.random.randn(5, 5)
determinante = np.linalg.det(matriz)
traza = np.trace(matriz)

st.write("**Matriz generada:**")
st.write(matriz)
st.write(f"**Determinante:** {determinante:.4f}")
st.write(f"**Traza:** {traza:.4f}")

# ---------------------------------
# EJERCICIO 3
# ---------------------------------
st.header("Ejercicio 3: Distribución de Frecuencias")
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

# ---------------------------------
# EJERCICIO 4
# ---------------------------------
st.header("Ejercicio 4: Normalización de un Vector")
modo = st.radio("Selecciona cómo generar el vector:", ("Manual", "Aleatorio"))

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
    st.write(f"**Vector original:** {v}")
    media_v = np.mean(v)
    desv_v = np.std(v)
    v_norm = (v - media_v) / desv_v
    st.write(f"**Vector normalizado:** {v_norm}")

# ---------------------------------
# SECCIÓN EXTRA: DataFrame de Estudiantes
# ---------------------------------
st.header("📚 DataFrame de Estudiantes")
st.write("Crea y administra una tabla editable con información de los estudiantes.")

n = 18  # número de estudiantes
data = {
    "Nombres": [f"Estudiante{i}" for i in range(1, n + 1)],
    "Apellidos": [f"Apellido{i}" for i in range(1, n + 1)],
    "Edad": np.random.randint(18, 25, n),
    "Notas": np.random.uniform(6, 10, n).round(2),
    "Materias": np.random.choice(["Matemáticas", "Física", "Programación", "Redes"], n)
}

df = pd.DataFrame(data)
df_editable = st.data_editor(df, num_rows="dynamic")
st.write("### Vista previa del DataFrame:")
st.dataframe(df_editable)

# Botón para descargar CSV
csv = df_editable.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Descargar CSV",
    data=csv,
    file_name="estudiantes.csv",
    mime="text/csv"
)
