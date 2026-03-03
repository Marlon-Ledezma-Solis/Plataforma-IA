# -*- coding: utf-8 -*-
import codecs
import re

html_u7_summary_high_quality = """<h3>⚡ La Dicotomía en el Desarrollo con Inteligencia Artificial: Vibe Coding vs. Ingeniería de Especificación</h3>
            <p>La llegada de los Grandes Modelos de Lenguaje (LLMs) ha democratizado la programación, introduciendo nuevas metodologías en el ecosistema de desarrollo de software. Entre ellas destaca el concepto de <strong>Vibe Coding</strong>, un término acuñado en 2025 por Andrej Karpathy (ex-director de IA en Tesla). El Vibe Coding se define como una forma de programar donde el usuario no escribe código, sino que interactúa con la IA en lenguaje natural puro, transmitiéndole la "vibra" o la esencia general (el <em>vibe</em>) de lo que desea construir.</p>
            
            <div class="case"><h4>Características y Limitaciones del Vibe Coding</h4>
            <ul>
                <li><strong>Ventajas:</strong> Reduce drásticamente la barrera de entrada técnica. Resulta brillante para prototipar rápidamente, iterar de manera instantánea y permitir que personas sin conocimientos profundos de sintaxis puedan generar bloques de código o aplicaciones básicas (como una lista de tareas simple o una landing page estática).</li>
                <li><strong>Limitaciones Críticas (El Código Espagueti):</strong> El Vibe Coding fracasa rotundamente ante sistemas empresariales complejos. Al pedirle a la IA "hazme un sistema contable moderno", la IA, carente de métricas y contexto profundo, produce código fracturado, dependencias desactualizadas e interfaces no escalables. La falta de rigor genera código no estructurado ("espagueti") que resulta imposible de auditar y mantener humanamente a mediano y largo plazo.</li>
            </ul></div>
            
            <p>Para solventar el precipicio técnico del Vibe Coding, la evolución profesional impone la práctica de la <strong>Ingeniería de Especificación</strong>. Esto no significa volver a escribir código a mano, sino asumir el rol de Arquitecto o "Product Owner". Consiste en descomponer exhaustiva y metódicamente un problema en etapas incrementales y específicas, dotando a la Inteligencia Artificial de un marco inquebrantable de trabajo. Un prompt de Ingeniería de Especificación jamás es ambiguo; contiene rigurosamente:</p>
            <ul>
                <li><strong>Roles y Contexto:</strong> "Actúa como un Desarrollador Frontend Senior usando React y Tailwind CSS."</li>
                <li><strong>Objetivos Finitos y Metas Acotadas:</strong> "Construye únicamente el componente de la barra superior de navegación interactiva central."</li>
                <li><strong>Insumos Inalterables (Inputs):</strong> "Utiliza exclusivamente los códigos de colores corporativos #FF5733 y la tipografía Roboto alojada en la ruta local correspondiente de assets."</li>
                <li><strong>Restricciones Dogmáticas y Pasos Secuenciados:</strong> "No inventes ni asumas variables, no utilices librerías externas que no hayan sido aprobadas, y valida el diseño Mobile-First antes de pasar a la versión de escritorio."</li>
            </ul>

            <h3>🔬 Laboratorio de Experimentación: El Potencial de Google AI Studio</h3>
            <p>Alejándonos de las interfaces de chat convencionales y enfocadas en usuarios finales (como ChatGPT o la interfaz estándar de Gemini), entramos al entorno avanzado de <strong>Google AI Studio</strong>. Ésta es la plataforma oficial gratuita de Google DeepMind para desarrolladores, diseñada para testear y parametrizar los modelos fundacionales masivos como Gemini 1.5 Pro y Gemini Flash sin filtros comerciales.</p>
            
            <div class="example"><h4>Parámetros y Capacidades de Orquestación en AI Studio</h4>
            <ul>
                <li><strong>Configuración del Sistema (System Instructions):</strong> A diferencia de un chat normal, aquí predefines el comportamiento matriz de la IA de manera imperativa en la cabecera. Este "comportamiento" acompaña a la IA a través de todas las iteraciones futuras dentro de la misma sesión, garantizando consistencia absoluta (por ejemplo, "Responde siempre en formato JSON estructurado").</li>
                <li><strong>Control de Temperatura (Temperature):</strong> Es el parámetro matemático que rige el grado de aleatoriedad en las predicciones del modelo.
                    <ul>
                        <li><em>Temperatura Baja (0.1 - 0.3):</em> Obliga al modelo a ser conservador, robótico y preciso. Es el ajuste obligatorio y crítico para programación de código puro, matemáticas, y análisis de datos estadísticos exactos.</li>
                        <li><em>Temperatura Alta (0.8 - 1.0+):</em> Fomenta variabilidad y creatividad. Es útil para brainstorming, escritura creativa o redacción de correos de marketing.</li>
                    </ul>
                </li>
                <li><strong>Top-K y Top-P (Filtrado de Núcleo):</strong> Al igual que la temperatura, modulan probabilísticamente el vocabulario que el modelo considera para su siguiente palabra (Token). Permiten afinar el equilibrio ideal entre diversidad léxica y consistencia estructural sin llegar a alucinar.</li>
                <li><strong>Prompts Estructurados (Structured Prompts):</strong> En lugar de chatear libremente, usas un formato de tabla o grilla (similar a Microsoft Excel) para entrenar al modelo con docenas de ejemplos de Input y Output simultáneos (One-Shot o Few-Shot Prompting). Esto disciplina al modelo para que, al darle un nuevo Input, emita un Output con el formato exacto sin necesidad de escribir código complejo de validación.</li>
            </ul></div>

            <h3>🚀 Entornos Agent-First IDE: El Paradigma del Review-Driven Development</h3>
            <p>La máxima expresión contemporánea de desarrollo asistido reside en los <strong>IDE Agent-First</strong>, tales como <em>Cursor, Cline o arquitecturas modulares como Antigravity</em>. A diferencia de tener una página web abierta con ChatGPT en el navegador y copiar y pegar código a un editor, estos entornos híbridos embeben y fusionan a la Inteligencia Artificial directamente en las entrañas de los archivos locales de tu proyecto en el disco duro del ordenador.</p>
            
            <div class="bib"><h4>Pilares Operativos de la Autonomía Asistida en tu Máquina Local:</h4>
            <ol>
                <li><strong>Inspección y Ejecución Embebida:</strong> El Agente IA no está ciego; tiene visión periférica. Puede leer todos tus directorios, buscar a través de miles de líneas de código en milisegundos y, lo más revolucionario, puede invocar la consola o Terminal (Bash/PowerShell) para ejecutar scripts locales, crear archivos por sí mismo y desplegar emuladores del navegador para visualizar el resultado autogenerado en tiempo real.</li>
                <li><strong>El Artefacto Maestro (Artifacts y Task Lists):</strong> Para gobernar a un ente con tanto poder y evitar que destruya el proyecto localmente, el programador lo obliga primero a generar artefactos documentales. El Agente redacta un <em>Plan de Arquitectura</em> o <em>Task_List.md</em> en Markdown donde enumera sus intenciones. El humano evalúa la lógica, y solo si es sólida, autoriza al agente a comenzar a codificar paso a paso de forma metódica.</li>
                <li><strong>Evaluación mediante Diffs (Visualización Comparativa):</strong> Bajo la estricta doctrina de <em>Review-Driven Development</em>, el agente jamás inserta el código de fondo sin avisar. Genera visualizaciones o "Diffs" comparativos (generalmente usando texto <span style="color:red">Rojo</span> para lo que la IA planea eliminar, y <span style="color:green">Verde</span> para lo que planea añadir). Tú, como Product Owner, revisas esta propuesta visual y la apruebas o rechazas con un simple clic definitivo.</li>
                <li><strong>Comandos Terminales y 'Allowlists':</strong> Cuando el Agente necesita invocar componentes externos (como instalar librerías vía <code>npm</code> o borrar rutas), el sistema Agent-First lo frena en seco y solicita confirmación humana. Nunca se conceden permisos "auto-run" o de ejecución a ciegas, conformando así una barrera de seguridad infranqueable contra manipulaciones catastróficas del sistema operativo matriz.</li>
            </ol></div>
            
            <p>La simbiosis perfecta en 2025 no consiste en apartarse y dejar que la IA cree todo de la nada (Vibe Coding extremo), sino en ejercer una rectoría metódica, dogmática y estructurada (Ingeniería de Especificación) empleando las consolas más potentes para parametrizarla (AI Studio) y los editores inmersivos nativos más eficientes (IDEs Agent-First) para auditar cada iteración visualmente como un director de orquesta soberano y en completo control de la tecnología.</p>"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    content = f.read()

# Replace U7 summary directly
# Match the U7 block up to its 'summary' property and inject the high quality one.
content = re.sub(
    r'(7:\s*\{.*?,\s*summary:\s*)`[\s\S]*?`', 
    lambda m: f"{m.group(1)}`{html_u7_summary_high_quality}`", 
    content, 
    flags=re.DOTALL
)

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(content)

print("U7 summary replaced with high-quality, professional, meaningful extensive text.")
