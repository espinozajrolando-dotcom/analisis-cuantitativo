import streamlit as st
import matplotlib.pyplot as plt

# ==========================================
# MOTOR ESTADÍSTICO - ANÁLISIS CUANTITATIVO
# ==========================================
def calcular_media(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (datos_ordenados[medio - 1] + datos_ordenados[medio]) / 2
    else:
        return datos_ordenados[medio]

def calcular_moda(datos):
    frecuencias = {}
    for item in datos:
        frecuencias[item] = frecuencias.get(item, 0) + 1
    max_frecuencia = max(frecuencias.values())
    modas = [k for k, v in frecuencias.items() if v == max_frecuencia]
    return modas

def calcular_frecuencias_completas(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    
    abs_freq = {}
    for item in datos_ordenados:
        abs_freq[item] = abs_freq.get(item, 0) + 1
        
    tabla_frecuencias = []
    acumulada_abs = 0
    acumulada_rel = 0
    
    for valor, fi in abs_freq.items():
        acumulada_abs += fi
        hi = fi / n
        acumulada_rel += hi
        
        tabla_frecuencias.append({
            "Valor": valor,
            "fi (Absoluta)": fi,
            "Fi (Acumulada)": acumulada_abs,
            "hi (Relativa)": round(hi, 4),
            "Hi (Rel. Acumulada)": round(acumulada_rel, 4)
        })
        
    return tabla_frecuencias

# ==========================================
# INTERFAZ WEB CON STREAMLIT Y GRÁFICOS
# ==========================================
st.title("📊 App de Análisis Cuantitativo")
st.write("Calcula estadística descriptiva, tablas de frecuencias y polígono de frecuencias estrictamente desde el origen.")

# Cuadro de texto interactivo
entrada_usuario = st.text_input("Ingresa los datos numéricos separados por espacios:", "12 15 12 18 20 15 15 22 25 30 32 35")

if st.button("Calcular y Graficar"):
    try:
        # Convertir texto a lista de números
        datos = [float(x) if '.' in x else int(x) for x in entrada_usuario.split()]
        
        if len(datos) == 0:
            st.warning("⚠️ Por favor ingresa al menos un número.")
        else:
            st.success("¡Gráfico perfeccionado desde el origen con éxito!")
            
            # Métricas principales
            col1, col2, col3 = st.columns(3)
            col1.metric("Cantidad (n)", len(datos))
            col2.metric("Media", round(calcular_media(datos), 2))
            col3.metric("Mediana", calcular_mediana(datos))
            
            st.write(f"**Moda(s):** {calcular_moda(datos)}")
            
            # Tabla de frecuencias
            st.subheader("📈 Tabla de Frecuencias")
            tabla = calcular_frecuencias_completas(datos)
            st.table(tabla)
            
            # ==========================================
            # SECCIÓN DE GRÁFICOS (Polígono anclado en esquinas 0)
            # ==========================================
            st.subheader("📊 Visualización: Histograma con Polígono en el Origen")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            
            # Extraer valores y frecuencias
            valores_orig = [fila["Valor"] for fila in tabla]
            frecuencias_orig = [fila["fi (Absoluta)"] for fila in tabla]
            
            x_pos = list(range(len(valores_orig)))
            labels_barras = [str(v) for v in valores_orig]
            
            # 1. Gráfico de barras de fondo
            ax.bar(x_pos, frecuencias_orig, color='skyblue', edgecolor='black', alpha=0.7, label='Frecuencias (fi)')
            
            # 2. Coordenadas extendidas para que la línea toque estrictamente los bordes laterales externos en cero
            x_poligono = [x_pos[0] - 0.5] + x_pos + [x_pos[-1] + 0.5]
            y_poligono = [0] + frecuencias_orig + [0]
            
            # Trazar polígono
            ax.plot(x_poligono, y_poligono, color='red', marker='o', linewidth=2.5, label='Polígono de Frecuencias')
            
            # Fijar los límites exactos del eje X para que coincidan con los extremos de los puntos adicionales
            ax.set_xlim(x_pos[0] - 0.5, x_pos[-1] + 0.5)
            
            # Configurar etiquetas
            ax.set_xticks(x_pos)
            ax.set_xticklabels(labels_barras)
            
            ax.set_title("Histograma y Polígono de Frecuencias (Anclado en los extremos)")
            ax.set_xlabel("Valores / Marcas de Clase")
            ax.set_ylabel("Frecuencia Absoluta (fi)")
            ax.set_ylim(bottom=0)
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.legend()
            
            plt.tight_layout()
            st.pyplot(fig)
            
    except ValueError:
        st.error("❌ Error: Asegúrate de escribir únicamente números separados por espacios.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Desarrollado con Python y Streamlit por Rolando para Matematicas MLZ © 2026</p>", 
    unsafe_allow_html=True)
