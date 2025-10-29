"""
Archivo de pruebas para la librería CorePy
Ejecutar: python test_core.py
"""

from core import (
    AnalizadorCuantitativo, 
    AnalizadorCualitativo, 
    AnalizadorBivariado,
    analizar
)


def test_analizador_cuantitativo():
    """Prueba todas las funciones del analizador cuantitativo"""
    print("\n" + "="*70)
    print("TEST 1: ANALIZADOR CUANTITATIVO")
    print("="*70)
    
    # Datos de prueba: Calificaciones de estudiantes
    calificaciones = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91, 87, 83, 94, 86, 90]
    
    print(f"\n📊 Datos: {calificaciones}")
    print(f"📊 Total de observaciones: {len(calificaciones)}")
    
    try:
        analizador = AnalizadorCuantitativo(calificaciones)
        
        # Prueba 1: Medidas de tendencia central
        print("\n--- Medidas de Tendencia Central ---")
        print(f"Media: {analizador.media():.2f}")
        print(f"Mediana: {analizador.mediana():.2f}")
        print(f"Moda: {analizador.moda()}")
        
        # Prueba 2: Medidas de dispersión
        print("\n--- Medidas de Dispersión ---")
        print(f"Varianza: {analizador.varianza():.2f}")
        print(f"Desviación Estándar: {analizador.desviacion_estandar():.2f}")
        print(f"Coeficiente de Variación: {analizador.coeficiente_variacion():.2f}%")
        print(f"Rango: {analizador.rango():.2f}")
        print(f"Rango Intercuartílico (IQR): {analizador.rango_intercuartilico():.2f}")
        
        # Prueba 3: Percentiles y cuartiles
        print("\n--- Percentiles y Cuartiles ---")
        q1, q2, q3 = analizador.cuartiles()
        print(f"Q1 (25%): {q1:.2f}")
        print(f"Q2 (50%): {q2:.2f}")
        print(f"Q3 (75%): {q3:.2f}")
        print(f"Percentil 90: {analizador.percentil(90):.2f}")
        
        # Prueba 4: Medidas de forma
        print("\n--- Medidas de Forma ---")
        print(f"Asimetría: {analizador.asimetria():.4f}")
        if analizador.asimetria() > 0:
            print("  → Distribución asimétrica a la derecha")
        elif analizador.asimetria() < 0:
            print("  → Distribución asimétrica a la izquierda")
        else:
            print("  → Distribución simétrica")
            
        print(f"Curtosis: {analizador.curtosis():.4f}")
        if analizador.curtosis() > 0:
            print("  → Distribución leptocúrtica (colas pesadas)")
        elif analizador.curtosis() < 0:
            print("  → Distribución platicúrtica (colas ligeras)")
        else:
            print("  → Distribución mesocúrtica (similar a normal)")
        
        # Prueba 5: Resumen completo
        print("\n--- Resumen Estadístico Completo ---")
        resumen = analizador.resumen()
        for clave, valor in resumen.items():
            print(f"{clave}: {valor}")
        
        print("\n✅ TEST 1 COMPLETADO CON ÉXITO")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR EN TEST 1: {str(e)}")
        return False


def test_analizador_cualitativo():
    """Prueba todas las funciones del analizador cualitativo"""
    print("\n" + "="*70)
    print("TEST 2: ANALIZADOR CUALITATIVO")
    print("="*70)
    
    # Datos de prueba: Preferencias de transporte
    transportes = ['auto', 'bus', 'bicicleta', 'bus', 'auto', 'metro', 
                   'bus', 'bicicleta', 'auto', 'bus', 'metro', 'bus',
                   'auto', 'bicicleta', 'bus', 'metro', 'bus']
    
    print(f"\n📊 Datos: {transportes}")
    print(f"📊 Total de observaciones: {len(transportes)}")
    
    try:
        analizador = AnalizadorCualitativo(transportes)
        
        # Prueba 1: Información básica
        print("\n--- Información Básica ---")
        print(f"Categorías únicas: {analizador.categorias_unicas()}")
        print(f"Moda: {analizador.moda()}")
        
        # Prueba 2: Frecuencias
        print("\n--- Frecuencias Absolutas ---")
        frec_abs = analizador.frecuencias_absolutas()
        for categoria, freq in sorted(frec_abs.items(), key=lambda x: x[1], reverse=True):
            print(f"{categoria}: {freq}")
        
        print("\n--- Frecuencias Porcentuales ---")
        frec_porc = analizador.frecuencias_porcentuales()
        for categoria, freq in sorted(frec_porc.items(), key=lambda x: x[1], reverse=True):
            print(f"{categoria}: {freq}%")
        
        # Prueba 3: Tabla de frecuencias completa
        print("\n--- Tabla de Frecuencias Completa ---")
        print(f"{'Categoría':<15} {'Frec.Abs':<10} {'Frec.Rel':<12} {'Frec.%':<10} {'Frec.Acum':<12}")
        print("-" * 70)
        
        tabla = analizador.tabla_frecuencias()
        for cat, valores in tabla.items():
            print(f"{cat:<15} {valores['frecuencia_absoluta']:<10} "
                  f"{valores['frecuencia_relativa']:<12.4f} "
                  f"{valores['frecuencia_porcentual']:<10.2f} "
                  f"{valores['frecuencia_acumulada']:<12}")
        
        # Prueba 4: Medidas de diversidad
        print("\n--- Medidas de Diversidad ---")
        print(f"Entropía de Shannon: {analizador.entropia():.4f}")
        print(f"Índice de Simpson: {analizador.indice_diversidad_simpson():.4f}")
        
        # Prueba 5: Resumen completo
        print("\n--- Resumen Completo ---")
        resumen = analizador.resumen()
        for clave, valor in resumen.items():
            print(f"{clave}: {valor}")
        
        print("\n✅ TEST 2 COMPLETADO CON ÉXITO")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR EN TEST 2: {str(e)}")
        return False


def test_analizador_bivariado():
    """Prueba el análisis de correlación y regresión"""
    print("\n" + "="*70)
    print("TEST 3: ANALIZADOR BIVARIADO")
    print("="*70)
    
    # Datos de prueba: Horas de estudio vs Calificación
    horas_estudio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    calificaciones = [50, 55, 62, 68, 75, 79, 85, 90, 93, 98]
    
    print(f"\n📊 Variable X (Horas de estudio): {horas_estudio}")
    print(f"📊 Variable Y (Calificaciones): {calificaciones}")
    
    try:
        analizador = AnalizadorBivariado(horas_estudio, calificaciones)
        
        # Prueba 1: Covarianza
        print("\n--- Medidas de Asociación ---")
        print(f"Covarianza: {analizador.covarianza():.4f}")
        
        # Prueba 2: Correlación
        correlacion = analizador.correlacion_pearson()
        print(f"Correlación de Pearson: {correlacion:.4f}")
        
        if correlacion > 0.7:
            print("  → Correlación positiva fuerte")
        elif correlacion > 0.3:
            print("  → Correlación positiva moderada")
        elif correlacion > -0.3:
            print("  → Correlación débil o nula")
        elif correlacion > -0.7:
            print("  → Correlación negativa moderada")
        else:
            print("  → Correlación negativa fuerte")
        
        # Prueba 3: R²
        r2 = analizador.coeficiente_determinacion()
        print(f"Coeficiente de Determinación (R²): {r2:.4f}")
        print(f"  → {r2*100:.2f}% de la varianza de Y es explicada por X")
        
        # Prueba 4: Regresión lineal
        print("\n--- Regresión Lineal Simple ---")
        regresion = analizador.regresion_lineal_simple()
        print(f"Intercepto (β₀): {regresion['intercepto']}")
        print(f"Pendiente (β₁): {regresion['pendiente']}")
        print(f"Ecuación: {regresion['ecuacion']}")
        
        # Hacer una predicción
        horas_nueva = 12
        prediccion = regresion['intercepto'] + regresion['pendiente'] * horas_nueva
        print(f"\n💡 Predicción: Si estudias {horas_nueva} horas, "
              f"tu calificación estimada sería: {prediccion:.2f}")
        
        # Prueba 5: Resumen completo
        print("\n--- Resumen Completo ---")
        resumen = analizador.resumen()
        for clave, valor in resumen.items():
            if isinstance(valor, dict):
                print(f"\n{clave}:")
                for k, v in valor.items():
                    print(f"  {k}: {v}")
            else:
                print(f"{clave}: {valor}")
        
        print("\n✅ TEST 3 COMPLETADO CON ÉXITO")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR EN TEST 3: {str(e)}")
        return False


def test_funcion_analizar():
    """Prueba la función helper 'analizar' con detección automática"""
    print("\n" + "="*70)
    print("TEST 4: FUNCIÓN HELPER 'analizar()' CON DETECCIÓN AUTOMÁTICA")
    print("="*70)
    
    try:
        # Datos numéricos
        print("\n--- Prueba con datos numéricos (auto-detección) ---")
        datos_num = [10, 20, 30, 40, 50]
        analizador1 = analizar(datos_num, tipo='auto')
        print(f"Tipo detectado: {type(analizador1).__name__}")
        print(f"Media: {analizador1.media()}")
        
        # Datos categóricos
        print("\n--- Prueba con datos categóricos (auto-detección) ---")
        datos_cat = ['A', 'B', 'A', 'C', 'B', 'A']
        analizador2 = analizar(datos_cat, tipo='auto')
        print(f"Tipo detectado: {type(analizador2).__name__}")
        print(f"Moda: {analizador2.moda()}")
        
        print("\n✅ TEST 4 COMPLETADO CON ÉXITO")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR EN TEST 4: {str(e)}")
        return False


def test_casos_borde():
    """Prueba casos especiales y validaciones"""
    print("\n" + "="*70)
    print("TEST 5: CASOS BORDE Y VALIDACIONES")
    print("="*70)
    
    resultados = []
    
    # Test 5.1: Lista vacía
    print("\n--- Test 5.1: Lista vacía ---")
    try:
        AnalizadorCuantitativo([])
        print("❌ FALLÓ: Debería lanzar error con lista vacía")
        resultados.append(False)
    except ValueError as e:
        print(f"✅ CORRECTO: Error capturado - {e}")
        resultados.append(True)
    
    # Test 5.2: Datos no numéricos en cuantitativo
    print("\n--- Test 5.2: Datos no numéricos en analizador cuantitativo ---")
    try:
        AnalizadorCuantitativo([1, 2, 'tres', 4])
        print("❌ FALLÓ: Debería lanzar error con datos no numéricos")
        resultados.append(False)
    except TypeError as e:
        print(f"✅ CORRECTO: Error capturado - {e}")
        resultados.append(True)
    
    # Test 5.3: Datos con valores iguales (sin varianza)
    print("\n--- Test 5.3: Datos sin varianza ---")
    try:
        analizador = AnalizadorCuantitativo([5, 5, 5, 5, 5])
        print(f"Media: {analizador.media()}")
        print(f"Desviación estándar: {analizador.desviacion_estandar()}")
        print("✅ CORRECTO: Maneja correctamente datos sin varianza")
        resultados.append(True)
    except Exception as e:
        print(f"❌ FALLÓ: {e}")
        resultados.append(False)
    
    # Test 5.4: Diferentes tamaños en bivariado
    print("\n--- Test 5.4: Variables de diferente tamaño ---")
    try:
        AnalizadorBivariado([1, 2, 3], [4, 5])
        print("❌ FALLÓ: Debería lanzar error con tamaños diferentes")
        resultados.append(False)
    except ValueError as e:
        print(f"✅ CORRECTO: Error capturado - {e}")
        resultados.append(True)
    
    # Test 5.5: Datos con un solo elemento único (cualitativo)
    print("\n--- Test 5.5: Datos cualitativos con una sola categoría ---")
    try:
        analizador = AnalizadorCualitativo(['A', 'A', 'A', 'A'])
        print(f"Moda: {analizador.moda()}")
        print(f"Entropía: {analizador.entropia()}")
        print("✅ CORRECTO: Maneja correctamente una sola categoría")
        resultados.append(True)
    except Exception as e:
        print(f"❌ FALLÓ: {e}")
        resultados.append(False)
    
    if all(resultados):
        print("\n✅ TEST 5 COMPLETADO CON ÉXITO")
        return True
    else:
        print(f"\n⚠️ TEST 5 COMPLETADO CON {resultados.count(False)} FALLOS")
        return False


def ejecutar_todos_los_tests():
    """Ejecuta todos los tests y muestra un resumen"""
    print("\n" + "="*70)
    print("🧪 INICIANDO SUITE DE PRUEBAS COMPLETA")
    print("="*70)
    
    resultados = {
        'Test 1 - Cuantitativo': test_analizador_cuantitativo(),
        'Test 2 - Cualitativo': test_analizador_cualitativo(),
        'Test 3 - Bivariado': test_analizador_bivariado(),
        'Test 4 - Función Helper': test_funcion_analizar(),
        'Test 5 - Casos Borde': test_casos_borde()
    }
    
    # Resumen final
    print("\n" + "="*70)
    print("📊 RESUMEN DE RESULTADOS")
    print("="*70)
    
    for nombre_test, resultado in resultados.items():
        simbolo = "✅" if resultado else "❌"
        print(f"{simbolo} {nombre_test}: {'PASÓ' if resultado else 'FALLÓ'}")
    
    total_exitosos = sum(resultados.values())
    total_tests = len(resultados)
    
    print("\n" + "="*70)
    print(f"TOTAL: {total_exitosos}/{total_tests} tests exitosos "
          f"({(total_exitosos/total_tests)*100:.1f}%)")
    print("="*70)
    
    if total_exitosos == total_tests:
        print("\n🎉 ¡TODOS LOS TESTS PASARON! La librería funciona correctamente.")
    else:
        print(f"\n⚠️ {total_tests - total_exitosos} test(s) fallaron. "
              "Revisa los mensajes de error arriba.")


if __name__ == "__main__":
    ejecutar_todos_los_tests()
