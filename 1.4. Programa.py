def mostrar_menu():
    """Muestra el menú principal y solicita una opción al usuario."""
    print("\n" + "="*50)
    print("      📊 MENÚ DE ANÁLISIS DE VENTAS Y DATOS 📊")
    print("="*50)
    print("1. 💡 Tema, Problema y Solución del Análisis")
    print("2. 💾 Dataset de Referencia (Fuente, Estructura y Tipos)")
    print("3. 📝 Información, Pasos y Pseudocódigo (Python)")
    print("4. 🖼️ Diagrama Conceptual del Programa (ASCII)")
    print("0. 🚪 Salir")
    print("="*50)
    return input("👉 Ingrese el número de su opción: ")

def opcion_1_tema_problema_solucion():
    """Despliega el desarrollo de Tema, Problema y Solución."""
    print("\n" + "#"*60)
    print("## 1. 💡 Tema, Problema y Solución del Análisis ##")
    print("#"*60)
    print("### Tema:")
    print("Análisis del rendimiento de ventas por producto y a lo largo del tiempo, con un enfoque en la preferencia e impacto de los medios de pago y la identificación de clientes más valiosos (MVC).")
    print("\n### Problema:")
    print("La empresa necesita entender sus patrones de venta, evaluar la contribución de cada medio de pago al volumen total, y determinar las preferencias de pago de sus clientes de mayor valor para optimizar estrategias.")
    print("\n### Solución:")
    print("Generar informes clave que desglosen las ventas, cuantifiquen la participación porcentual de cada medio de pago en el total de ventas, y aíslen la preferencia de pago del Top 10 de clientes más valiosos.")
    print("\n" + "#"*60)

def opcion_2_dataset_referencia():
    """Despliega el desarrollo del Dataset de Referencia."""
    print("\n" + "#"*60)
    print("## 2. 💾 Dataset de Referencia ##")
    print("#"*60)
    print("### Dataset: Ventas (ventas.csv)")
    print("- **Fuente:** Registro de transacciones.")
    print("- **Definición:** Encabezado de la venta (fecha, cliente, medio de pago).")
    print("- **Estructura, Tipos y Escala:** Relacional. Columnas clave: `id_venta` (int), `fecha` (datetime), `medio_pago` (string). Escala: 120 transacciones.")
    
    print("\n### Dataset: Detalle_ventas (detalle_ventas.csv)")
    print("- **Fuente:** Registro de ítems vendidos.")
    print("- **Definición:** Detalles de productos en una venta (producto, cantidad, importe).")
    print("- **Estructura, Tipos y Escala:** Relacional. Columnas clave: `id_venta` (int), `nombre_producto` (string), `importe` (int, unidad monetaria). Escala: 343 registros de detalle.")
    
    print("\n### Dataset: Productos (productos.csv)")
    print("- **Fuente:** Catálogo de productos.")
    print("- **Definición:** Información estática (categoría, precio unitario).")
    print("- **Estructura, Tipos y Escala:** Relacional. Columnas clave: `id_producto` (int), `categoria` (string). Escala: 100 productos.")
    print("\n" + "#"*60)
    print("### Estructura y Tipos de Datos:")
    print("\nTabla Clientes")
    print("id_cliente      int     ordinal")
    print("nombre_cliente  str     nominal")
    print("email           str     nominal")
    print("ciudad          str     nominal")
    print("fecha_alta      str     intervalo")

    print("\nTabla Productos")
    print("id_producto     int     ordinal")
    print("nombre_producto str     nominal")
    print("categoria       str     nominal")
    print("precio_unitario int     Razón")

    print("\nTabla Ventas")
    print("id_venta        int     ordinal")
    print("fecha           str     intervalo")
    print("id_cliente      int     ordinal")
    print("nombre_cliente  str     nominal")
    print("email           str     nominal")
    print("medio_pago      str     nominal")

    print("\nTabla Detalle_ventas")
    print("id_venta        int     ordinal")
    print("id_producto     int     ordinal")
    print("nombre_producto str     nominal")
    print("cantidad        int     razón")
    print("precio_unitario int     razón")
    print("importe         int     razón")

def opcion_3_pasos_pseudocodigo():
    """Despliega el desarrollo de Información, Pasos y Pseudocódigo (Python)."""
    print("\n" + "#"*60)
    print("## 3. 📝 Información, Pasos y Pseudocódigo (Python) ##")
    print("#"*60)
    print("### Pasos del Programa:")
    print("1. **Carga y Preparación:** Unir `Ventas` y `Detalle_ventas` por `id_venta`, limpiar datos y extraer `año` y `mes` de la fecha.")
    print("2. **Carlos Q1:** Agrupar y sumar ventas por `año`, `mes` y `nombre_producto`.")
    print("3. **Carlos Q2 / Luis Q1:** Agrupar y sumar ventas por `medio_pago` y calcular su porcentaje global.")
    print("4. **Karla Q1:** Calcular gasto por cliente, identificar el **Top 10** de clientes más valiosos (MVC) y analizar la preferencia de `medio_pago` solo para ellos.")
    
    print("\n### Pseudocódigo (Python):")
    print("```python")
    print("# Preparación de Datos")
    print("df_sales = pd.merge(df_ventas, df_detalle, on='id_venta')")
    print("df_sales['fecha'] = pd.to_datetime(df_sales['fecha'])")
    print("df_sales['anio'] = df_sales['fecha'].dt.year")
    print("\n# Carlos Q1: Ventas por Producto y Tiempo")
    print("ventas_prod_tiempo = df_sales.groupby(['anio', 'mes', 'producto'])['importe'].sum()")
    print("\n# Carlos Q2 & Luis Q1: Impacto de Medios de Pago")
    print("ventas_medio_pago = df_sales.groupby('medio_pago')['importe'].sum()")
    print("total_global = ventas_medio_pago.sum()")
    print("ventas_medio_pago['porcentaje'] = (ventas_medio_pago / total_global) * 100")
    print("\n# Karla Q1: Preferencia de Clientes Valiosos")
    print("top_10_clientes = df_sales.groupby('id_cliente')['importe'].sum().nlargest(10).index")
    print("df_sales_mvc = df_sales[df_sales['id_cliente'].isin(top_10_clientes)]")
    print("preferencia_mvc = df_sales_mvc.groupby('medio_pago')['importe'].sum()")
    print("```")
    print("\n" + "#"*60)

def opcion_4_diagrama_programa():
    """Despliega la descripción del Diagrama Conceptual del Programa (ASCII)."""
    print("\n" + "#"*60)
    print("## 4. 🖼️ Diagrama Conceptual del Programa (ASCII) ##")
    print("#"*60)
    print("El flujo del programa se representa conceptualmente de la siguiente manera:")
    print("\n")
    print("      [INICIO]")
    print("         |")
    print("         V")
    print("  [Cargar & Unir CSVs]")
    print("  (Ventas + Detalle) -> (DF_SALES)")
    print("         |")
    print("  +------+------+-------+")
    print("  |             |             |")
    print("  V             V             V")
    print("[Análisis 1]  [Análisis 2]  [Análisis 3]")
    print("(Carlos Q1)   (C2/Luis Q1)  (Karla Q1 - MVC)")
    print("(Prod/Tiempo) (Medio Pago)  (Top Clientes)")
    print("  |             |             |")
    print("  +------+------+-------+")
    print("         |")
    print("         V")
    print("   [Generar Reportes CSV]")
    print("         |")
    print("         V")
    print("       [FIN]")
    print("\n" + "#"*60)

def main():
    """Función principal que ejecuta el menú interactivo."""
    opcion = ''
    while opcion != '0':
        opcion = mostrar_menu()

        if opcion == '1':
            opcion_1_tema_problema_solucion()
        elif opcion == '2':
            opcion_2_dataset_referencia()
        elif opcion == '3':
            opcion_3_pasos_pseudocodigo()
        elif opcion == '4':
            opcion_4_diagrama_programa()
        elif opcion == '0':
            print("\n" + "="*50)
            print("🥳 ¡Gracias por utilizar el Analizador de Ventas! ¡Hasta pronto! 🫡")
            print("="*50)
        else:
            print("\n⚠️ Opción no válida. Por favor, ingrese un número del 0 al 4.")

# Iniciar el programa
if __name__ == "__main__":
    main()