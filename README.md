# 📊 Análisis de Ventas Aurelion

Proyecto de análisis de datos de ventas para la tienda **Aurelion**, enfocado en estadística descriptiva, correlaciones y detección de outliers. Este repositorio contiene notebooks interactivos y código Python estándar para explorar y visualizar patrones en datos de ventas, clientes y productos.

---

## 📋 Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Archivos Principales](#archivos-principales)
- [Análisis Incluidos](#análisis-incluidos)
- [Datos](#datos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## 📌 Descripción General

Este proyecto realiza un análisis completo de datos de ventas usando **Python estándar** (sin dependencias externas en la lógica principal). Incluye:

- **Estadística Descriptiva**: Media, mediana, desviación estándar, cuartiles de variables clave.
- **Análisis de Correlaciones**: Identificación de relaciones entre variables (cantidad, precio, importe).
- **Detección de Outliers**: Métodos IQR y Z-score para identificar valores extremos.
- **Visualizaciones**: Gráficos de distribución, scatter plots, análisis de outliers.
- **Menú Interactivo**: Interfaz educativa en terminal para navegar análisis.

### Objetivo

Proporcionar insights sobre el desempeño de ventas, identificar patrones de comportamiento de clientes y productos, y detectar anomalías en los datos para toma de decisiones.

---

## 🗂️ Estructura del Proyecto

```
Demo/
├── README.md                                 # Este archivo
├── Programa.py                               # Menú interactivo principal
├── Prueba.py                                 # Variante con documentación embebida
│
├── 📁 Documentación/
│   ├── 1.1. Documentación.md                # Descripción del problema y solución
│   ├── 1.2. Pseudocodigo.md                 # Pseudocódigo de funciones
│   ├── 1.3. Diagrama.md                     # Diagramas de flujo ASCII
│   ├── 1.5. Instrucciones.md                # Guía de uso
│   └── 2.0 Documentacion.md                 # Documentación adicional
│
├── 📁 Notebooks Jupyter/
│   ├── 2.1. Estadística_descriptiva.ipynb          # Cálculo de estadísticas básicas
│   ├── 2.2. Correlaciones.ipynb                    # Análisis de correlaciones
│   ├── 2.2. Identificación_Variable.ipynb          # Identificación de variables
│   ├── 2.4. Detección_de_outliers.ipynb            # Métodos IQR y Z-score
│   ├── 2.5. Conclusiones.md                        # Conclusiones del análisis
│   └── Estadisticas_descriptivas_basicas_calculadas.ipynb
│
├── 📁 Datos/
│   ├── Ventas.xlsx                          # Tabla de ventas (fecha, cantidad, importe)
│   ├── Detalle_ventas.xlsx                  # Detalle línea por línea
│   ├── Clientes.xlsx                        # Información de clientes
│   └── Productos.xlsx                       # Catálogo de productos
│
├── 📁 outputs/
│   ├── correlation_pairs.csv                # Pares de correlación calculados
│   └── 📁 correlations_scatter/             # Gráficos de scatter plots
│       ├── correlation_pairs.csv
│       └── [Imágenes PNG de correlaciones]
│
├── 📁 .github/
│   └── copilot-instructions.md              # Instrucciones para agentes AI
│
└── [Archivos PNG de análisis]
    ├── analisis_correlaciones.png
    ├── analisis_distribucion_variables.png
    ├── analisis_outliers.png
    └── estadisticas_descriptivas.png

```

---

## 🔧 Requisitos

### Mínimos (menú interactivo sin análisis real)
- Python 3.8 o superior
- Git (para clonar/sincronizar)

### Para ejecutar notebooks (análisis completo)
- Jupyter Notebook o JupyterLab
- pandas (análisis de datos)
- numpy (operaciones numéricas)
- matplotlib (visualización)
- openpyxl (lectura de Excel)

### Para procesamiento estándar (sin librerías externas)
- Python 3.8+
- Bibliotecas estándar: `csv`, `json`, `datetime`, `collections`

---

## 📥 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/fegones/segundoentregable.git
cd segundoentregable
```

### 2. Crear un entorno virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias (opcional, para notebooks)

```bash
pip install jupyter pandas numpy matplotlib openpyxl seaborn scipy
```

### 4. Iniciar Jupyter (si lo instalaste)

```bash
jupyter notebook
```

---

## 🚀 Uso

### Opción 1: Menú Interactivo (sin dependencias)

```bash
python Programa.py
```

o

```bash
python Prueba.py
```

Esto abrirá un menú interactivo en la terminal con opciones:

```
╔════════════════════════════════════════╗
║  📊 ANÁLISIS DE VENTAS - AURELION 📊  ║
╚════════════════════════════════════════╝

1️⃣  Tema, Problema y Solución
2️⃣  Dataset de Referencia
3️⃣  Pasos / Pseudocódigo
4️⃣  Diagrama del Programa
5️⃣  Salir

Selecciona una opción (1-5):
```

### Opción 2: Ejecutar Notebooks

Abre en Jupyter:
- `2.1. Estadística_descriptiva.ipynb` — Estadísticas básicas
- `2.2. Correlaciones.ipynb` — Análisis de correlaciones
- `2.4. Detección_de_outliers.ipynb` — Detección de valores extremos

### Opción 3: Procesamiento Manual con Python Estándar

```python
# Cargar CSV sin pandas
def leer_csv_simple(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]
    header = lines[0].split(',')
    rows = [dict(zip(header, l.split(','))) for l in lines[1:]]
    return rows

# Uso
detalle = leer_csv_simple('detalle_ventas.csv')
print(f"Filas cargadas: {len(detalle)}")
```

---

## 📊 Archivos Principales

### `Programa.py` / `Prueba.py`

Menú interactivo secuencial que:
- Muestra descripción del problema (ventas, análisis, toma de decisiones)
- Describe la estructura del dataset (columnas, tipos)
- Presenta pseudocódigo de funciones clave
- Dibuja diagramas ASCII del flujo

**No realiza carga real de datos** — es educativo y didáctico.

```python
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == '1':
            opcion_1_tema_problema_solucion()
        elif opcion == '2':
            opcion_2_dataset_referencia()
        # ... resto de opciones
```

### Notebooks Jupyter

#### `2.1. Estadística_descriptiva.ipynb`
Calcula:
- Media, mediana, desviación estándar
- Mínimo, máximo, cuartiles (Q1, Q2, Q3)
- Varianza, rango intercuartílico (IQR)

#### `2.2. Correlaciones.ipynb`
Analiza:
- Correlación de Pearson entre pares de variables
- Scatter plots de relaciones principales
- Matrices de correlación

#### `2.4. Detección_de_outliers.ipynb`
Identifica valores extremos usando:
- **Método IQR**: valores < Q1-1.5×IQR o > Q3+1.5×IQR
- **Método Z-score**: |z| > 3

---

## 📈 Análisis Incluidos

### 1. Estadística Descriptiva

| Métrica | Descripción |
|---------|-------------|
| **Media** | Promedio de valores |
| **Mediana** | Valor central |
| **Desv. Estándar** | Dispersión de datos |
| **Cuartiles** | Q1 (25%), Q2 (50%), Q3 (75%) |
| **Rango** | Máximo - Mínimo |
| **IQR** | Q3 - Q1 (rango intercuartílico) |

### 2. Correlaciones

Identifica relaciones entre:
- `cantidad` vs `importe` → correlación fuerte
- `precio_unitario` vs `importe` → correlación esperada
- Otras variables continuas del dataset

### 3. Detección de Outliers

Métodos aplicados:
- **IQR Method**: Rangos de confianza con 1.5 × IQR
- **Z-score**: Desviaciones estándar > 3
- **Visualización**: Gráficos con puntos marcados

### 4. Conclusiones

Insights principales:
- Productos/clientes con mejor desempeño
- Patrones estacionales (si aplica)
- Anomalías y valores sospechosos
- Recomendaciones de acción

---

## 📂 Datos

### Archivos Esperados

El proyecto espera estos archivos en la carpeta `Datos/`:

| Archivo | Columnas | Descripción |
|---------|----------|-------------|
| `Ventas.xlsx` | id_venta, fecha, cantidad, importe | Resumen de ventas |
| `Detalle_ventas.xlsx` | id_venta, id_producto, cantidad, precio_unitario, importe | Detalle línea a línea |
| `Clientes.xlsx` | id_cliente, nombre, apellido, email, teléfono | Información de clientes |
| `Productos.xlsx` | id_producto, nombre_producto, categoria, precio | Catálogo de productos |

### Formato

- **Excel (.xlsx)**: Lectura con `openpyxl` o `pandas`
- **CSV (.csv)**: Lectura con `csv` stdlib o `pandas`
- **Encoding**: UTF-8 por defecto

---

## 🔍 Ejemplo de Uso Completo

```bash
# 1. Clonar repositorio
git clone https://github.com/fegones/segundoentregable.git
cd segundoentregable

# 2. Ver el menú interactivo
python Programa.py

# 3. Seleccionar opción 1 para ver tema/problema
# 4. Seleccionar opción 2 para ver estructura del dataset
# 5. Seleccionar opción 3 para ver pseudocódigo

# 6. (Opcional) Ejecutar notebooks
jupyter notebook
# Abrir: 2.1. Estadística_descriptiva.ipynb
# Ejecutar celdas (Shift+Enter)
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Directrices

- Usa Python estándar para la lógica principal (sin dependencias externas innecesarias)
- Documenta funciones y variables
- Prueba el código antes de hacer commit
- Usa emojis y Markdown para mejorar legibilidad

---

## 📝 Notas de Desarrollo

### Arquitectura

El proyecto sigue un diseño educativo con separación clara:
- **Lógica de presentación**: `Programa.py`, `Prueba.py` (impresión en terminal)
- **Lógica de procesamiento**: Funciones en archivos separados (si se crean)
- **Análisis interactivo**: Notebooks Jupyter para exploración

### Estándares de Código

```python
# ✅ Preferido: Python estándar
with open('datos.csv', 'r', encoding='utf-8') as f:
    datos = [línea.strip().split(',') for línea in f]

# ⚠️ Alternativa: pandas (si ya está instalado)
import pandas as pd
datos = pd.read_csv('datos.csv')
```

### Configuración de Git

```bash
git config user.name "Felipe"
git config user.email "fegones@hotmail.com"
```

---

## 🐛 Troubleshooting

### Error: Módulo no encontrado

```bash
pip install pandas numpy matplotlib openpyxl
```

### Error: Archivo no encontrado (Datos/)

Asegúrate de que los archivos `.xlsx` estén en la carpeta `Datos/`:
```bash
ls Datos/
# Debe mostrar: Ventas.xlsx, Detalle_ventas.xlsx, Clientes.xlsx, Productos.xlsx
```

### Jupyter no inicia

```bash
pip install jupyter --upgrade
jupyter notebook --version
jupyter notebook
```

---

## 📚 Referencias

- [Python Official Docs](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Jupyter Documentation](https://jupyter.org/documentation)

---

## 📄 Licencia

Este proyecto está bajo licencia **MIT**. Ver archivo `LICENSE` (si existe) para más detalles.

Eres libre de usar, modificar y distribuir este código con atribución.

---

## 👤 Autor

**Felipe Gómez**  
📧 Email: fegones@hotmail.com  
🐙 GitHub: [@fegones](https://github.com/fegones)  

---

## 🙏 Agradecimientos

Gracias a:
- El equipo de Aurelion por los datos de ventas
- GitHub Copilot por asistencia en desarrollo
- La comunidad Python por herramientas y librerías open-source

---

## ⭐ Estado del Proyecto

- ✅ Menú interactivo funcional
- ✅ Notebooks de análisis creados
- ✅ Documentación completa
- 🔄 Integración continua (GitHub Actions - futuro)
- 📦 Distribución en PyPI (futuro)

---

**Última actualización**: Noviembre 2025  
**Versión**: 2.0 (Segundo Entregable)  

---

## 📞 Soporte

Para reportar bugs, preguntas o sugerencias:
- Abre un [Issue](https://github.com/fegones/segundoentregable/issues)
- Envía un email a fegones@hotmail.com
- Crea un [Discussion](https://github.com/fegones/segundoentregable/discussions)

---

*Hecho con ❤️ para Aurelion*
