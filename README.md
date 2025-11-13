# Análisis de Ventas - Pipeline ETL

Sistema ETL para análisis de datos de ventas implementado con **Pipeline Pattern**, siguiendo estándares de ingeniería de datos.
Este proyecto implementa un Pipeline Pattern inspirado en Orquestador2 (Bancolombia), garantizando modularidad, escalabilidad y mantenibilidad.

---

## ¿Por qué esta arquitectura?

Durante mi experiencia de **1 año como Ingeniero de Datos en Bancolombia**, trabajé en la construcción de ETL usando **Orquestador2** como estándar. Este proyecto aplica los mismos principios:

- **Pipeline Pattern**: Flujo secuencial de transformaciones (Extract → Transform → Load)
- **Modularidad**: Cada paso es independiente y reutilizable
- **Escalabilidad**: Agregar nuevos transformadores sin modificar código existente
- **SOLID Principles**: Código mantenible y testeable

Esta arquitectura permite que el código se adapte fácilmente a procesos internos corporativos, similar a herramientas como Orquestador2.

---

## Patrón de Diseño: Pipeline Pattern

**Pipeline Pattern** es el patrón ideal para procesos ETL donde los datos fluyen secuencialmente a través de múltiples transformaciones:

```
Input → [Extract] → [Transform 1] → [Transform 2] → [Transform N] → [Load] → Output
```

**Ventajas:**

- Cada paso tiene una responsabilidad única
- Fácil agregar/quitar pasos
- Testing independiente de cada componente
- Flujo de datos explícito y claro

---

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)

---

## Guía de Instalación

### 1. Clonar el repositorio

`````bash
# Windows
git clone <URL_DEL_REPOSITORIO>
cd ventas-analysis

```bash

### 2. Crear entorno virtual

````bash
# Windows
python -m venv venv
venv\Scripts\activate


### 3. Instalar dependencias

```bash
pip install -r requirements.txt
`````

**Dependencias:**

- `pandas` - Manipulación de datos
- `numpy` - Operaciones numéricas
- `openpyxl` - Lectura/escritura de Excel

### 4. Crear carpeta data

crea una carpeta data al mismo nivel que la carpeta src y en esta pon el archivo datos_ventas.xlsx

### 5. Ejecutar el pipeline

```bash
python main.py
```

**Entrada:** `datos_ventas.xlsx` (debe estar en el directorio raíz)  
**Salida:** `resumen_ventas.xlsx` (con 2 hojas: Resumen_Ventas y Ventas_Mensuales)

## Autor

Anthony Arango Resterpo
Ingeniero de Datos  
Experiencia: 1 año en Bancolombia - Construcción de pipelines ETL con Orquestador2

---
