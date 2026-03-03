import json

replacement = """            4: {
                pres: "https://docs.google.com/presentation/d/1KwgtBuYITtBoYcV7tyXsnZg6lbtgI4d2sr07dVSCrHY/embed",
                title: "Unidad 4: Automatización de procesos con IA",
                subtitle: "Optimización de flujos de trabajo, creación de macros con IA y uso de APIs",
                breadcrumb: "Módulo 2 <span>›</span> Herramientas IA",
                plan: {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Comprender los fundamentos y componentes de los flujos de trabajo", "Aprender a grabar y crear macros en Excel utilizando Visual Basic", "Desarrollar macros VBA complejas asistidas por herramientas de IA (ChatGPT)", "Entender el concepto y funcionamiento de las APIs", "Extraer datos estadísticos conectando Power BI a APIs (BCCR, FRED)", "Crear funciones personalizadas en Excel conectadas a la API de OpenAI"] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Optimización y mapeo de procesos rutinarios", "Programación básica de scripts VBA mediante Vibe Coding", "Importación automatizada de datos desde fuentes oficiales", "Interpretación de documentación técnica de APIs", "Integración de IA directamente en hojas de cálculo para análisis de texto"] },
                        { icon: "⏱️", title: "Distribución del Tiempo", items: ["Semana 4 del programa", "Sesiones sincrónicas: 6 horas", "Trabajo asincrónico: 1 hora", "Dedicación semanal total: 7 horas"] },
                        { icon: "📚", title: "Ubicación en el Programa", items: ["Módulo 2: Herramientas IA para Automatización", "Unidad 4 de 5 en este módulo", "Prerequisito: Módulo 1", "Siguiente: Unidad 5"] },
                        { icon: "📝", title: "Contenidos de Esta Unidad", items: ["Teoría de flujos de trabajo y fundamentos de automatización", "Casos prácticos de macros generadas por IA", "Introducción a APIs: La analogía del camarero", "Conexión a la API del BCCR y FRED desde Power BI/Power Query", "Función personalizada con IA en Excel usando JSONConverter.bas"] },
                        { icon: "✅", title: "Sistema de Evaluación", items: ["Ejercicios prácticos por módulo: 40%", "Proyecto final aplicado: 30%", "Participación y asistencia: 20%", "Actividades asincrónicas: 10%"] }
                    ]
                },
                summary: `<h3>🔄 Flujos de Trabajo y Fundamentos de la Automatización</h3>
            <p>Un <strong>flujo de trabajo (workflow)</strong> es una secuencia estructurada de pasos o tareas que se deben completar para lograr un resultado específico. Entender y optimizar estos flujos es crucial para la gestión moderna.</p>
            <div class="example"><h4>Elementos Clave de un Flujo de Trabajo:</h4>
                <ul>
                    <li><strong>Entrada:</strong> El punto de inicio del flujo (información, datos, evento).</li>
                    <li><strong>Actores:</strong> Personas o sistemas que ejecutan las tareas.</li>
                    <li><strong>Procesamiento:</strong> Acciones y transformaciones durante las tareas.</li>
                    <li><strong>Herramientas:</strong> Recursos tecnológicos o manuales utilizados.</li>
                    <li><strong>Salida:</strong> El resultado final o entregable del proceso.</li>
                </ul>
            </div>
            <p>La <strong>automatización</strong> es el uso de tecnologías para ejecutar tareas o procesos con mínima o nula intervención humana. Permite aumentar la velocidad de ejecución, reducir la carga de trabajo manual y escalar operaciones.</p>
            <div class="case"><h4>¿Qué se puede automatizar?</h4>
                <ul>
                    <li><strong>Tareas rutinarias:</strong> Acciones de alta frecuencia, como carga de datos, envío de correos, generación de informes.</li>
                    <li><strong>Reglas claras:</strong> Operaciones basadas en lógica condicional (ej. conciliación contable).</li>
                    <li><strong>Integración de información:</strong> Recopilación de datos de múltiples fuentes (APIs) y sincronización de bases de datos.</li>
                </ul>
            </div>

            <h3>💻 Automatización en Excel: Creación de Macros con IA</h3>
            <p>El primer nivel de automatización abordado es la creación de macros utilizando Visual Basic for Applications (VBA) en Excel, asistido por Inteligencia Artificial (ChatGPT).</p>
            <div class="example"><h4>Caso Práctico: Macros VBA</h4>
                <p>En lugar de programar código VBA desde cero o simplemente usar la "Grabadora de Macros", usamos IA proporcionando <strong>prompts sumamente detallados</strong> que especifican la estructura del archivo, las celdas exactas a leer y la operación a realizar.</p>
                <ul>
                    <li><strong>Vibe Coding:</strong> Es el proceso iterativo donde solicitamos el código, probamos la macro, identificamos errores y pedimos a la IA que los corrija hasta obtener un script funcional.</li>
                    <li><strong>Beneficio:</strong> Ejecutar procesos que tomarían horas de copiado y pegado en apenas unos segundos, sin necesidad de saber programar.</li>
                </ul>
            </div>

            <h3>🌐 APIs e Inteligencia Artificial</h3>
            <p>Una <strong>API</strong> (Interfaz de Programación de Aplicaciones) es un intermediario que permite que dos aplicaciones se comuniquen. Funciona con <em>Peticiones (Requests)</em>, <em>Procesamiento</em> y <em>Respuestas (Responses, usualmente en JSON)</em>.</p>
            <div class="case"><h4>La Analogía del Camarero</h4>
                <p>Imagina un restaurante: Tú (Cliente/App) necesitas datos. La Cocina (Servidor) prepara los datos. El Camarero (API) es quien lleva tu pedido y trae tu comida.</p>
            </div>

            <h3>📊 Automatización de Datos: API del BCCR y FRED</h3>
            <p>Evita actualizar tableros manualmente conectando tus reportes directamente a fuentes de datos oficiales:</p>
            <ul>
                <li><strong>Proceso:</strong> Suscripción a indicadores del BCCR para obtener un token de acceso y generación de un script en Python (vía ChatGPT) para consumir la API de BCCR y de la Reserva Federal de EE.UU (FRED).</li>
                <li><strong>Implementación en Power BI y Power Query:</strong> El script de Python se puede ejecutar directamente dentro de Power BI o Excel (Power Query) para que, al dar clic en "Actualizar", se descarguen los datos más recientes estadísticos en tiempo real de manera automática.</li>
            </ul>

            <h3>🧠 API de Inteligencia Artificial en Excel</h3>
            <p>El nivel más avanzado de la unidad conecta la API de OpenAI directamente dentro de Excel, inyectando inteligencia artificial en las hojas de cálculo mediante una función personalizada (ej. <code>=IAPersonalizada(prompt, celda)</code>).</p>
            <div class="example"><h4>Creación de Función IAPersonalizada</h4>
                <ul>
                    <li><strong>Requisito:</strong> Una API Key de OpenAI y el módulo <em>JsonConverter.bas</em> en Visual Basic.</li>
                    <li><strong>Uso:</strong> Permite resolver problemas complejos que las funciones regulares de Excel (BUSCARV, SI) no pueden resolver.</li>
                    <li><strong>Ejemplos Prácticos:</strong> Extraer el primer apellido de listas irregulares, realizar análisis de sentimiento de comentarios (positivo, negativo, neutro), o catalogar descripciones de texto en códigos de ocupación específicos.</li>
                </ul>
            </div>`,
                videos: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Selección de videos relacionados a la automatización de procesos, flujos de trabajo, macros y APIs.</p>
            <h4 class="tool-category">🎓 Teoría y Macros</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">📈</div>
                    <div class="tool-name">Flujos de Trabajo</div>
                    <div class="tool-desc">Entendiendo los workflows y mapas de procesos</div>
                    <a href="https://www.youtube.com/results?search_query=que+es+un+flujo+de+trabajo+y+para+que+sirve" target="_blank" class="tool-link">Ver en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">🤖</div>
                    <div class="tool-name">Macros con ChatGPT</div>
                    <div class="tool-desc">Crear automatizaciones en Excel VBA usando IA</div>
                    <a href="https://www.youtube.com/results?search_query=macros+excel+vba+chatgpt+tutorial+español" target="_blank" class="tool-link">Ver en YouTube →</a>
                </div>
            </div>

            <h4 class="tool-category" style="margin-top:30px">🔗 Uso de APIs en Análisis de Datos</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">🌐</div>
                    <div class="tool-name">¿Qué es una API?</div>
                    <div class="tool-desc">Explicación intuitiva de las interfaces de programación</div>
                    <a href="https://www.youtube.com/results?search_query=que+es+una+api+explicacion+sencilla" target="_blank" class="tool-link">Ver en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">📊</div>
                    <div class="tool-name">API en Power BI</div>
                    <div class="tool-desc">Cómo importar datos desde una API web en Power BI</div>
                    <a href="https://www.youtube.com/results?search_query=conectar+api+en+power+bi+español" target="_blank" class="tool-link">Ver en YouTube →</a>
                </div>
            </div>

            <h4 class="tool-category" style="margin-top:30px">🧠 API de OpenAI en Excel</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">🔑</div>
                    <div class="tool-name">OpenAI API Key</div>
                    <div class="tool-desc">Cómo obtener y configurar tu API Key de OpenAI</div>
                    <a href="https://www.youtube.com/results?search_query=como+obtener+api+key+openai+chatgpt" target="_blank" class="tool-link">Ver en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">✨</div>
                    <div class="tool-name">Integrar ChatGPT en Excel</div>
                    <div class="tool-desc">Crear funciones personalizadas llamando a ChatGPT vía API</div>
                    <a href="https://www.youtube.com/results?search_query=integrar+chatgpt+api+en+excel+vba" target="_blank" class="tool-link">Ver en YouTube →</a>
                </div>
            </div>`,
                tutorials: `<h4 class="tool-category">🎬 Videos Tutoriales Específicos - Unidad 4</h4>
            <div class="tools-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://youtu.be/OfOg5Gmgito" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/OfOg5Gmgito/hqdefault.jpg" alt="Teoría y Macros" style="width:100%;height:160px;object-fit:cover;">
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">⚙️ Teoría y Macros</div>
                            <div style="font-size:12px;color:var(--gr)">Fundamentos de automatización y desarrollo de macros en Excel con IA</div>
                        </div>
                    </a>
                </div>
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://youtu.be/0LvShmLBIN8" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/0LvShmLBIN8/hqdefault.jpg" alt="Uso de API para automatizar información" style="width:100%;height:160px;object-fit:cover;">
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">🔗 Uso de API para automatizar datos</div>
                            <div style="font-size:12px;color:var(--gr)">Conexión a la API del BCCR y FRED en PowerBI y Excel usando Python</div>
                        </div>
                    </a>
                </div>
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://youtu.be/XMKDJTOxg20" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/XMKDJTOxg20/hqdefault.jpg" alt="API de IA en Excel" style="width:100%;height:160px;object-fit:cover;">
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">🤖 API de IA en Excel</div>
                            <div style="font-size:12px;color:var(--gr)">Integración de la API de OpenAI para crear funciones personalizadas inteligentes</div>
                        </div>
                    </a>
                </div>
            </div>`,
                insumos: `<h4 class="tool-category">📦 Materiales Descargables - Unidad 4</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">📚</div>
                    <div class="tool-name">Insumos Unidad 4.rar</div>
                    <div class="tool-desc">Archivos base, scripts Python y módulos VBA (JsonConverter.bas)</div>
                    <a href="https://drive.google.com/uc?export=download&id=1XiSW0Hqh7mZ0m7MFKYVw1mhKYDzFSrIX" target="_blank" class="tool-link">⬇️ Descargar →</a>
                </div>
            </div>`,
                tools: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Herramientas y plataformas abordadas para la automatización y el uso de APIs.</p>
            <h4 class="tool-category">🛠️ Plataformas y Lenguajes</h4>
            <div class="tools-grid">
                <div class="tool-card"><div class="tool-icon">🐍</div><div class="tool-name">Python</div><div class="tool-desc">Lenguaje para scripts de conexión a APIs</div><a href="https://www.python.org/" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">📊</div><div class="tool-name">Power BI</div><div class="tool-desc">Ejecución de scripts Python para extraer datos</div><a href="https://powerbi.microsoft.com/" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">📝</div><div class="tool-name">Excel (VBA)</div><div class="tool-desc">Entorno para macros y funciones personalizadas</div><a href="https://www.microsoft.com/es-es/microsoft-365/excel" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">🌐</div><div class="tool-name">OpenAI Platform</div><div class="tool-desc">Gestión de API Keys de Inteligencia Artificial</div><a href="https://platform.openai.com/" target="_blank" class="tool-link">Abrir →</a></div>
            </div>`,
                activities: `<h3>📝 Actividades de Práctica - Unidad 4</h3>
            <div class="activity-card" style="background:rgba(99,102,241,.1);border:1px solid rgba(99,102,241,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--p);margin-bottom:12px">⚙️ Actividad 1: Creación de tu primera Macro con IA</h4>
                <p style="margin-bottom:12px">Automatiza una tarea rutinaria en Excel usando Inteligencia Artificial:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Identifica un proceso en Excel que hagas manualmente (ej. limpiar datos, ordenar columnas, aplicar formatos).</li>
                    <li>Escribe un <em>prompt</em> detallado para ChatGPT solicitando el código VBA para esa tarea y realiza "Vibe Coding" hasta que funcione.</li>
                    <li>Pega el código en el módulo de Visual Basic e implementa un botón para ejecutar la macro.</li>
                </ol>
            </div>
            <div class="activity-card" style="background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--g);margin-bottom:12px">🔗 Actividad 2: Conexión y Extracción de Datos vía API</h4>
                <p style="margin-bottom:12px">Automatiza la extracción de indicadores económicos:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Obtén tu token de acceso del Banco Central (BCCR) y de la API de FRED.</li>
                    <li>Abre el código provisto en el archivo de Insumos y agrega tus tokens y variables correspondientes.</li>
                    <li>Carga el script en Power BI o Excel y visualiza los datos cargados dinámicamente.</li>
                </ol>
            </div>
            <div class="activity-card" style="background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--w);margin-bottom:12px">💡 Actividad 3: Análisis de Texto con Función IA en Excel</h4>
                <p style="margin-bottom:12px">Implementa el asistente de IA dentro de Excel:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Configura el módulo VBA predesarrollado con tu propia API Key de OpenAI (requiere JsonConverter.bas).</li>
                    <li>Define una meta para el modelo (ej. categorizar descripciones genéricas según el catálogo oficial - CU).</li>
                    <li>Utiliza la función =IAPersonalizada() para iterar sobre todas tus celdas de forma automatizada.</li>
                </ol>
            </div>`,
                quiz: [
                    { q: "¿Qué es un flujo de trabajo (workflow)?", o: ["Un programa de diseño gráfico", "Una secuencia estructurada de pasos para lograr un resultado", "Un tipo de IA predictiva", "Un lenguaje en la nube"], c: 1 },
                    { q: "¿En qué consiste el 'Vibe Coding' mencionado en la unidad?", o: ["Escuchar música al programar", "Programación iterativa interactuando con la IA para probar y corregir código", "Un lenguaje visual", "Código SQL para bases de datos"], c: 1 },
                    { q: "¿A qué analogía recurrimos para explicar una API?", o: ["Un bibliotecario buscando un libro", "Un intérprete de idiomas", "Un camarero llevando un pedido a la cocina y trayendo la comida al cliente", "Un cartero"], c: 2 },
                    { q: "¿Cuál es una ventaja clave de utilizar la API de Inteligencia Artificial de OpenAI?", o: ["Es gratuita para siempre", "Permite inyectar capacidades de IA en nuestras propias aplicaciones y sistemas sin desarrollar desde cero", "Funciona offline", "Viene instalada en Windows"], c: 1 },
                    { q: "¿Qué componente en Visual Basic se necesita para manejar el JSON de OpenAI en Excel?", o: ["ChatGPT.bas", "ExcelAI.dll", "PowerQuery.exe", "JsonConverter.bas"], c: 3 },
                    { q: "¿Qué información clave requiere el script en Python para conectarse al BCCR?", o: ["El token de acceso personal y el código del indicador", "El número de cédula", "La contraseña del correo", "Un archivo CSV"], c: 0 },
                    { q: "¿Qué ventajas ofrece la función personalizada de IA (IAPersonalizada) frente a las funciones regulares de Excel?", o: ["Es más rápida haciendo sumas", "Permite analizar textos complejos, determinar sentimientos o categorizar datos que no siguen patrones matemáticos", "Convierte Excel a Word automáticamente", "Mejora colores automáticamente"], c: 1 },
                    { q: "¿Qué proceso elimina la necesidad de actualizar reportes descargando archivos web manualmente todas las mañanas?", o: ["Grabar macros manuales copiando y pegando", "El uso de la Grabadora de Macros", "La conexión automatizada vía API en Power BI o Power Query para cargar datos dinámicamente", "Enviar la información por programación de correo electrónico"], c: 2 },
                    { q: "¿Cuál es el propósito del catálogo nivel internacional mencionado en el video (Código CU)?", o: ["Vender productos internacionales", "Es un catálogo que divide y clasifica ocupaciones, que la IA aprendió a buscar y catalogar", "Crear páginas de e-commerce", "Desarrollar componentes PC"], c: 1 },
                    { q: "¿Para qué usaríamos la instrucción 'import pandas as pd' en el Python Script?", o: ["Para programar gráficos VBA", "Para hacer una macro simple", "Es una librería requerida en Python para manejar los datos estructurados y comunicarnos por la API", "Para conectar juegos"], c: 2 }
                ],
                memory: [{ t: "Workflow", d: "Secuencia de pasos para un objetivo" }, { t: "Automatización", d: "Minimizar intervención humana en tareas" }, { t: "API", d: "Intermediario entre aplicaciones" }, { t: "Token", d: "Clave de acceso para la API" }, { t: "Vibe Coding", d: "Programación iterativa con IA" }, { t: "JsonConverter", d: "Librería para API en VBA" }, { t: "API Key", d: "Llave secreta de OpenAI" }, { t: "FRED", d: "Datos económicos mundiales" }],
                trivia: [{ q: "¿A qué analogía nos referimos para explicar una API?", o: ["Cartero y correo", "Camarero y cocina", "Operadora telefónica", "Semáforo y tráfico"], c: 1 }, { q: "¿Qué herramienta utilizamos para ejecutar una consulta Python desde Power BI?", o: ["Script de Python", "Módulo VBA", "DAX", "SQL"], c: 0 }, { q: "¿Qué tipo de costo tiene la API de OpenAI?", o: ["Totalmente gratuita", "Pago por uso de tokens", "Licencia anual fija para Office", "Solo paga si falla el servidor"], c: 1 }, { q: "¿Qué archivo `.bas` era necesario importar en Excel?", o: ["JsonConverter.bas", "OpenAI.bas", "InternetGateway.bas", "PythonToExcel.bas"], c: 0 }, { q: "¿Qué puede averiguar la función de IAPersonalizada que Excel no puede solo?", o: ["Sumar rango", "Análisis de sentimientos de un texto", "Elevar al cuadrado", "Contar letras"], c: 1 }],
                classify: { cat1: "🧩 Visual Basic", cat2: "🌐 APIs", items: [{ t: "Módulo Excel", c: 1 }, { t: "JSONConverter", c: 1 }, { t: "API BCCR", c: 2 }, { t: "Macro Grabada", c: 1 }, { t: "API FRED", c: 2 }, { t: "API OpenAI", c: 2 }, { t: "IAPersonalizada", c: 1 }, { t: "Token de acceso", c: 2 }] },
                hangman: [{ w: "WORKFLOW", h: "Secuencia estructurada de procesos" }, { w: "MACROS", h: "Scripts en Excel" }, { w: "VBA", h: "Lenguaje en Visual Basic" }, { w: "JSON", h: "Formato de respuesta que el servidor envía" }, { w: "TOKEN", h: "Contraseña individual que te otorga un API" }, { w: "ITERACION", h: "Proceso de corrección de código" }, { w: "SENTIMIENTO", h: "Análisis positivo/negativo" }, { w: "PYTHON", h: "Lenguaje de scripts" }],
                simResponses: { "api": "Una <strong>API</strong> es un intermediario que permite a dos aplicaciones comunicarse. En el curso vimos la del BCCR para datos y OpenAI para servicios de IA.", "macros": "Las <strong>Macros en Excel (VBA)</strong> automatizan tareas. Utilizando IA como ChatGPT, las creamos sin programar.", "vba": "<strong>VBA (Visual Basic)</strong> es la consola donde pegamos el código de nuestras Macros generadas por ChatGPT.", "json": "Las APIs entregan datos en formato <strong>JSON</strong>. Para que Excel lo entienda usamos JsonConverter.bas.", "openai": "Al usar la <strong>API de OpenAI</strong> debes obtener tu API Key. Con ella, inyectas IA en Excel.", "token": "Un <strong>token</strong> de acceso es esencial para conectarte a APIs de datos oficiales, como el BCCR.", "default": "Soy el asistente de la Unidad 4. Pregúntame sobre Flujos de trabajo, Automatización, Macros, VBA o APIs." }
            },
"""

import codecs
file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"
with codecs.open(file_path, "r", "utf-8") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if 4330 <= i <= 4558:  # 0-indexed. 4331 to 4559 
        # Skip original lines
        if i == 4330: # insert replacement at line 4331
            new_lines.append(replacement)
        pass
    else:
        new_lines.append(line)

with codecs.open(file_path, "w", "utf-8") as f:
    f.writelines(new_lines)

print("Update completed successfully.")
