# Guía para Agentes AI en este Proyecto
# Guía para Agentes AI en este Proyecto (nivel: básico, Python estándar)
# Instrucciones para GitHub Copilot
Proyecto: Tienda Aurelion  
Fecha: 2025-10-17

Propósito: Registrar las peticiones (prompts) en lenguaje natural utilizadas con Copilot durante el desarrollo del Sprint 1 para generar código, documentación y tests relacionados con el análisis de ventas.

Este repositorio contiene un pequeño menú interactivo diseñado como guía/descripción de un análisis de ventas. El código actual es didáctico: muestra flujos, pseudocódigo y estructuras esperadas, pero no carga librerías externas ni realiza procesamiento con pandas ni numpy.

## Objetivo del agente
- Trabajar en nivel básico de Python (sintaxis, control de flujo, estructuras de datos básicas).
- NO usar librerías externas: usar solo la biblioteca estándar (ej.: `open`, `csv`, `datetime`, `collections`).

## Archivos clave
- `Programa.py` y `Prueba.py` — menú interactivo y documentación embebida (las dos tienen la misma lógica).
- Referencias a datasets: `ventas.csv`, `detalle_ventas.csv`, `productos.csv` (estos archivos no están incluidos por defecto).

## Arquitectura y patrones descubiertos
- Programa secuencial con un bucle principal en `main()` que muestra el menú y llama a funciones: `opcion_1_tema_problema_solucion`, `opcion_2_dataset_referencia`, `opcion_3_pasos_pseudocodigo`, `opcion_4_diagrama_programa`.
- Cada función solo imprime texto y pseudocódigo; no hay funciones de carga/transformación reales todavía.
- Usa emojis y diagramas ASCII para mejorar la salida en terminal — es aceptable mantener ese estilo en extensiones.

## Restricciones de implementación para agentes
- Implementaciones nuevas deben ser "puramente Python" (sin instalar paquetes). Preferir `csv` del stdlib o `open()`+`split()` para leer archivos.
- Evitar características avanzadas no necesarias (por ejemplo, multithreading, async) — mantener el enfoque educativo.

## Ejemplo práctico (cómo cargar y agregar ventas con Python estándar)
El siguiente fragmento muestra un método mínimo y autocontenido para leer `detalle_ventas.csv` y sumar `importe` por `id_venta` y por `nombre_producto` usando solo la biblioteca estándar:

```python
# Ejemplo mínimo: sumar importe por producto usando solo stdlib
def leer_csv_simple(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]
    header = lines[0].split(',')
    rows = [dict(zip(header, l.split(','))) for l in lines[1:]]
    return rows

def sumar_por_producto(detalle_rows):
    totals = {}
    for r in detalle_rows:
        prod = r.get('nombre_producto')
        importe = int(r.get('importe', '0'))
        totals[prod] = totals.get(prod, 0) + importe
    return totals

# Uso:
# detalle = leer_csv_simple('detalle_ventas.csv')
# totales = sumar_por_producto(detalle)
# print(totales)
```

## Qué buscar y documentar cuando se modifica el proyecto
- Si añades carga real de datos, documenta dónde está el CSV esperado y el encoding (utf-8 por defecto).
- Añade una pequeña función utilitaria para validación de esquema (columnas esperadas) usando solo código simple.
- Mantén las funciones de impresión separadas de las de procesamiento — esto facilita pruebas manuales.

## Flujo de trabajo recomendado (manual)
1. Ejecutar localmente con `python Programa.py` o `python Prueba.py`.
2. Para añadir procesamiento de datos: crear funciones en un nuevo archivo (ej.: `procesamiento.py`) que usen solo stdlib.
3. Probar manualmente en terminal y documentar cambios en este archivo.

## Ejemplo de check simple de esquema (sin librerías)
```python
def validar_columnas(rows, expected):
    if not rows:
        return False
    return set(expected).issubset(set(rows[0].keys()))
```

---
Si quieres, puedo:
- Añadir un archivo `procesamiento.py` con funciones reales que implementen el pseudocódigo usando solo Python estándar.
- Añadir ejemplos adicionales, como cálculo del Top 10 de clientes y generación de un CSV de salida con `open()`.

Por favor dime si quieres que implemente esas funciones (haré los cambios y ejecutaré pruebas básicas localmente).