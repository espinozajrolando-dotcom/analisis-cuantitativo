# ==========================================
# APP DE ANÁLISIS CUANTITATIVO INTERACTIVO
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
            "valor": valor,
            "fi": fi,
            "Fi": acumulada_abs,
            "hi": round(hi, 4),
            "Hi": round(acumulada_rel, 4)
        })
        
    return tabla_frecuencias

def calcular_marca_de_clase(limite_inferior, limite_superior):
    return (limite_inferior + limite_superior) / 2


# --- MENÚ INTERACTIVO DE LA APLICACIÓN ---
def ejecutar_app():
    print("========================================")
    print("📊 BIENVENIDO A TU APP DE ANÁLISIS CUANTITATIVO")
    print("========================================")
    
    entrada = input("Ingresa los datos numéricos separados por espacios (ej: 12 15 12 18 20): ")
    
    # Convertimos el texto ingresado en una lista de números decimales/enteros
    try:
        # Si el usuario ingresa números con punto o enteros
        datos_usuario = [float(x) if '.' in x else int(x) for x in entrada.split()]
        
        if len(datos_usuario) == 0:
            print("⚠️ No ingresaste ningún dato.")
            return

        print("\n========================================")
        print("📈 REPORTE DE RESULTADOS")
        print("========================================")
        print("Datos analizados:", datos_usuario)
        print("Cantidad total (n):", len(datos_usuario))
        print("Media aritmética:", round(calcular_media(datos_usuario), 2))
        print("Mediana:", calcular_mediana(datos_usuario))
        print("Moda:", calcular_moda(datos_usuario))
        
        print("\n--- TABLA DE FRECUENCIAS ---")
        print(f"{'Valor':<8} | {'fi':<4} | {'Fi':<4} | {'hi':<6} | {'Hi':<6}")
        print("-" * 42)
        for fila in calcular_frecuencias_completas(datos_usuario):
            print(f"{fila['valor']:<8} | {fila['fi']:<4} | {fila['Fi']:<4} | {fila['hi']:<6} | {fila['Hi']:<6}")
        print("========================================")
        
    except ValueError:
        print("❌ Error: Asegúrate de ingresar solo números separados por espacios.")

if __name__ == "__main__":
    ejecutar_app()
