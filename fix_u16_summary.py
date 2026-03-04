# -*- coding: utf-8 -*-
import codecs
import re

html_u16_summary = """<h3>📊 Power BI y Power Query: El Motor Empresarial del Análisis de Datos</h3>
            <p>La <strong>Unidad 16</strong> marca la entrada al Módulo 5 ("Análisis de Datos"), donde el foco se desplaza desde la automatización de procesos hacia la <em>inteligencia analítica</em> de la información corporativa. Microsoft Power BI emerge como la plataforma de referencia global para la creación de dashboards interactivos y la depuración profesional de conjuntos de datos masivos, superando con creces las capacidades estáticas del Excel tradicional gracias a su motor de visualización dinámica y su profundo integrador de fuentes heterogéneas.</p>

            <div class="case"><h4>Las Tres Secciones Fundamentales de Power BI</h4>
            <p>A diferencia de un gráfico estático en Hoja de Cálculo, Power BI organiza la inteligencia de negocio en tres capas interconectadas que conforman el <em>ciclo analítico completo</em>:</p>
            <ul>
                <li><strong>Vista de Visualización (Report View):</strong> El lienzo creativo donde el analista arrastra y combina más de 30 tipos de objetos visuales nativos (Gráficos de Barras, Matrices, KPIs, Mapas Geográficos, Slicers interactivos). Cualquier segmentación aplicada en un visual se propaga en cascada a todos los demás, creando una experiencia de exploración analítica verdaderamente reactiva.</li>
                <li><strong>Vista de Tabla y Modelo de Datos:</strong> El repositorio donde residen las tablas cargadas desde distintas fuentes (Excel, CSV, SQL Server, APIs REST). Aquí el analista examina la granularidad de los datos, verifica tipos, y escribe fórmulas DAX (Data Analysis Expressions) para calcular métricas calculadas dinámicas imposibles de lograr en Excel con fórmulas clásicas.</li>
                <li><strong>Vista de Relaciones (Model View):</strong> El diagrama Entidad-Relación visual del modelo analítico. Define qué columna de una tabla se conecta o une con otra tabla (joins de clave primaria y foránea), habilitando la propagación de filtros cruzados entre distintas tablas del modelo dimensional.</li>
            </ul></div>

            <h3>🔧 Power Query: La Fábrica de Limpieza de Datos Ejecutiva</h3>
            <p>Antes de visualizar, los datos deben ser <strong>depurados, transformados y estandarizados</strong>. Power Query es el motor ETL (Extract, Transform, Load) embebido que graba y replica automáticamente cada paso de transformación como pasos auditables, replicables y editables. Al actualizar la fuente de origen, la secuencia entera se repite sola en segundos.</p>

            <div class="example"><ul>
                <li><strong>Limpieza Elemental (Higiene de la Tabla):</strong> Quitar filas en blanco, duplicados o con errores; promover la primera fila como encabezado; cambiar tipos de dato (texto a número, fecha local, booleano); reemplazar valores nulos o incorrectos por estándar convenido; dividir columnas por delimitador (ej. separar "Apellido Nombre" en dos campos distintos).</li>
                <li><strong>Reestructuración Dimensional (Reshaping Profundo):</strong> Transponer tablas (intercambiar filas por columnas); aplicar "Anular Dinamización" (Unpivot) para convertir columnas de meses en una sola columna "Periodo" y otra "Valor" —formato necesario para visualizarse correctamente en Power BI—; o "Dinamizar" categorías de texto en columnas numéricas específicas.</li>
                <li><strong>Consolidación Multi-Fuente (Append & Merge):</strong> Anexar (Append) varias tablas con la misma estructura en un único dataset acumulado historicamente (ej. ventas Enero + Febrero + Marzo); o cargar automáticamente todos los archivos Excel de una carpeta de red entera de una sola vez, creando un proceso de actualización de datos mensual de un solo clic.</li>
            </ul></div>

            <div class="bib"><h3>🤖 IA Aplicada a Power Query: El GPT Limpiador de Datos</h3>
            <p>El cierre formativo de esta Unidad conecta el ciclo analítico con la Inteligencia Artificial generativa. Se desarrolla un GPT especializado, entrenado con un Prompt detallado de limpieza de datos estructurados. El flujo práctico consiste en enviar un extracto del dataset crudo al GPT, quien analiza las columnas, diagnostica los problemas (nulos, inconsistencias de formato, outliers estadísticos), y devuelve una lista priorizada de pasos de limpieza sugeridos en lenguaje natural. El analista selecciona cuáles aceptar y el GPT genera automáticamente el código M de Power Query (o los pasos equivalentes) para ejecutarlos en segundos, reduciendo dramáticamente el tiempo de preparación de datos en proyectos de Business Intelligence de gran escala.</p>
            </div>"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    txt = f.read()

txt = txt.replace("\r\n", "\n")

# Replace U16 summary
txt = re.sub(
    r'(16:\s*\{[\s\S]*?summary:\s*)`[\s\S]*?`(\s*,\s*videos:\s*`)',
    lambda m: f"{m.group(1)}`{html_u16_summary}`{m.group(2)}",
    txt,
    flags=re.DOTALL
)

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(txt)

print("Summary correcto para la Unidad 16 inyectado exitosamente.")
