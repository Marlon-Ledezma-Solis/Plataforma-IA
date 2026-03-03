# -*- coding: utf-8 -*-
import codecs
import re

html_u8_plan = """ {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Implementar la IA Generativa como herramienta de apoyo operativo en entornos reales.", "Identificar y mapear procesos administrativos manuales susceptibles de estandarización.", "Generar, auditar y depurar código VBA (Macros) utilizando asistentes virtuales asistidos.", "Documentar técnicamente el impacto y la mejora continua del proceso."] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Diseño de Prompts estructurados para extracción de código de automatización.", "Integración de IA con Microsoft Office (Excel/Word).", "Evaluación de fallos humanos rutinarios y su mitigación técnica.", "Elaboración de manuales descriptivos de antes/después del impacto tecnológico."] },
                        { icon: "⏱️", title: "Tiempo Estimado", items: ["Identificación de Caso de Estudio: 2 horas", "Desarrollo de Gem/GPT y formulación de Prompts: 3 horas", "Integración y depuración de VBA en Office: 4 horas", "Pruebas y Documentación Final: 3 horas."] },
                        { icon: "📚", title: "Ubicación Curricular", items: ["Ejercicio Integrador del Módulo 2.", "Cierre y Evaluación de las Unidades 4, 5, 6 y 7.", "Prerequisito: Dominio básico de Google AI Studio y agentes conversacionales.", "Siguiente fase: Módulo 3 (Python para automatización)."] },
                        { icon: "📝", title: "Resumen de Tareas", items: ["Diagnóstico de rutinas manuales.", "Higiene de Datos (limpieza de archivos base).", "Creación de asistente IA especializado (Gem/GPT).", "Inyección del Script VBA generado en el Editor Office.", "Despliegue de botón de ejecución."] },
                        { icon: "✅", title: "Sistema de Evaluación", items: ["Funcionalidad y estabilidad de la Macro: 40%", "Evidencia de Prompts e interacción con IA: 30%", "Calidad y claridad de la Documentación: 15%", "Impacto validado (ahorro de tiempo/errores): 15%"] }
                    ]
                }"""

html_u8_summary = """<h3>🛠️ El Eslabón Final: De la Teoría a la Operatividad Integrada con IA</h3>
            <p>La culminación teórica del Módulo 2 no reside en la mera adquisición de conceptos abstractos, sino en el despliegue empírico de la denominada <strong>IA Operativa</strong>. Hasta este punto, hemos recorrido el uso de la IA en Microsoft Office (Unidad 4), la automatización mediante herramientas generativas (Unidad 5), los agentes especializados (Unidad 6) y la orquestación avanzada en ecosistemas como Google AI Studio (Unidad 7). La Unidad 8 se concibe como el <em>Ejercicio Integrador transversal</em>, cuyo propósito es fusionar todo este conocimiento para resolver problemas palpables del día a día administrativo sin requerir conocimientos de programación informática previos.</p>
            
            <div class="case"><h4>El Paradigma del Arquitecto No-Programador</h4>
            <p>Muchas entidades asumen erróneamente que "automatizar" exige poseer un título en Ciencias de la Computación o haber pasado años dominando lenguajes estructurados. El enfoque revolucionario de esta unidad demuestra lo contrario: el estudiante adopta el papel de "Arquitecto de Soluciones". Su responsabilidad no es memorizar la complicada sintaxis de <strong>Visual Basic for Applications (VBA)</strong> de Excel o Word, sino dominar la interacción precisa, analítica e imperativa con la IA (Ingeniería de Especificación y Prompts) para que ésta escriba, corrija y comente el código algorítmico detrás de escena de manera perfecta.</p>
            </div>

            <h3>⚙️ Metodología del Proyecto Estructural (Fases de Implementación)</h3>
            <p>El desafío práctico de esta unidad radica en tomar un proceso burocrático, manual y propenso al error humano, y someterlo a una transformación digital sistemática utilizando un Asistente Personalizado, Gem o GPT, y coronándolo con la integración de una script autoejecutable (Macro) en el entorno de escritorio.</p>
            
            <ol>
                <li><strong>Fase Analítica (Identificación y Diagnóstico):</strong> Antes de invocar a la IA, el profesional debe auditar su entorno. Consiste en detectar tareas de alto volumen de desgaste: cruzado manual de facturas en Excel, limpieza de bases de correos, o consolidación semanal de reportes. Analizar dónde ocurren estadísticamente los márgenes de error por fatiga humana es el paso fundacional ineludible.</li>
                <li><strong>Higiene de Datos y Preparación del Lienzo Base (Data Sanitization):</strong> Una automatización aplicada sobre un archivo desordenado únicamente producirá desastres de forma acelerada. Esta etapa requiere preparar la estructura de Excel o Word: nombrar cabeceras de columnas, estructurar hojas lógicas fijas, definir rangos dinámicos de entrada e implementar esquemas sólidos antes de requerir la inyección del código automatizado.</li>
                <li><strong>Desarrollo del Asistente y Parametrización (Prompting):</strong> Aquí reside el punto de inflexión. El estudiante debe pre-configurar un Asistente (Gem/GPT) con órdenes detalladas y no vagas. En lugar de ordenar "Hazme una macro", la especificación correcta exige: <em>"Actúa como Ingeniero de Datos Excel; elabora una Macro VBA robusta, debidamente comentada línea por línea para pedagogía, que extraiga la data de la columna A de la hoja 'Raw', elimine espacios en blanco y duplique formatado a la hoja 'Master'."</em></li>
                <li><strong>Inmersión del Código (Deployment):</strong> Se extrae el código funcional generado por la Inteligencia Artificial y se inyecta nativamente en el Editor de Código del ecosistema Office. Es obligatorio requerir a la IA que integre la funcionalidad a través de Botones de Interfaz (GUI) o disparadores automáticos (Event Handlers) para que la herramienta pueda ser empleada a futuro por colegas que desconozcan por completo su origen.</li>
                <li><strong>Sandbox y Depuración (In-the-loop Testing):</strong> La primera ejecución rara vez es milagrosa. Se implementan prácticas de ejecución con bases de prueba irrelevantes. Si la macro arroja un error <em>'Run-time Error 1004'</em>, el estudiante simplemente copia y pega el error reportado devuelta a su GPT logrando que la IA audite su propia matriz, identifique la fisura de lógica y provea la porción corregida de la sintaxis.</li>
            </ol>

            <div class="bib"><h4>Entregables Finales y Beneficios de Alta Oferta Laboral</h4>
            <p>Al concluir esta certificación empírica, no se entrega simplemente un script; se entrega un <strong>Paquete de Solución Profesional Auditado</strong>. Esto incluye el archivo ejecutable de la Macro, las evidencias de las sesiones y chats de depuración iterativos con la IA, y fundamentalmente, una documentación gerencial del ROI (Retorno de Inversión Tecnológica) demostrando qué cuello de botella se solventó y cuántas horas hombre se ahorraron a la organización de cara al futuro.</p>
            <p>La adopción de estas capacidades catapulta la empleabilidad en áreas de soporte administrativo, pymes, recursos humanos y centros de servicio (Call Centers). A ojos de la corporación moderna, el operador ya no es alguien que gasta horas mecánicamente arrastrando celdas en Excel; se ha convertido en un analista logístico capaz de sintetizar soluciones escalables orquestando motores de IA de vanguardia.</p>
            </div>"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    content = f.read()

# Replace U8 plan (preserving meta attributes)
content = re.sub(
    r'(8:\s*\{[\s\S]*?breadcrumb[\s\S]*?plan:\s*)\{[\s\S]*?\}(\s*,\s*summary:\s*`)',
    lambda m: f"{m.group(1)}{html_u8_plan}{m.group(2)}",
    content,
    flags=re.DOTALL
)

# Replace U8 summary
content = re.sub(
    r'(8:\s*\{.*?,\s*summary:\s*)`[\s\S]*?`', 
    lambda m: f"{m.group(1)}`{html_u8_summary}`", 
    content, 
    flags=re.DOTALL
)

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(content)

print("U8 plan and summary replaced with high-quality content.")
