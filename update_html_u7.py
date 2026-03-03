import codecs

replacement = """            7: {
                pres: "https://docs.google.com/presentation/d/12vL8DCfr60RSXlZvefE9hU6kNCcIua9UymDV4Xz6QAI/embed",
                title: "Unidad 7: Uso de la plataforma de Google AI Studio y Entornos Agent-First",
                subtitle: "Vibe Coding, Ingeniería de Especificación y desarrollo asistido avanzado con Antigravity",
                breadcrumb: "Módulo 2 <span>›</span> Herramientas IA",
                plan: {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Comprender y aplicar la Ingenería de Especificación como evolución profesional del Vibe Coding", "Dominar la plataforma Google AI Studio para estructurar, refinar y probar prompts", "Aprender el ciclo de desarrollo asistido utilizando IDEs orientados a agentes (Agent-First)", "Configurar y operar Google Antigravity aplicando el Review-Driven Development", "Desarrollar proyectos funcionales (ej. diseño web con chatbot) controlando los Artifacts de la IA"] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Construcción de prompts estructurados (Contexto, Objetivo, Pasos y Salidas Esperadas)", "Configuración de parámetros avanzados en Gemini (Live API, Code Execution, Prompts Gallery)", "Operación de entornos de codificación automatizados mediante el uso seguro de agentes", "Revisión sistemática de Diffs, Task Lists e Implementation Plans", "Despliegue estructural guiando a la IA con carpetas como /info e /imagenes"] },
                        { icon: "⏱️", title: "Distribución del Tiempo", items: ["Semana 7 del programa", "Sesiones sincrónicas: 6 horas", "Trabajo asincrónico: 1 hora", "Dedicación semanal total: 7 horas"] },
                        { icon: "📚", title: "Ubicación en el Programa", items: ["Módulo 2: Herramientas IA para Automatización", "Unidad 7 de 5 en este módulo", "Prerequisito: Unidad 6 (Agentes de IA)", "Siguiente: Unidad 8 (Integrador Módulo 2)"] },
                        { icon: "📝", title: "Contenidos de Esta Unidad", items: ["Vibe Coding vs Ingeniería de Especificación paso a paso para la IA", "Google AI Studio: Laboratorio en tiempo real, Live API y generación Multimodal", "Entornos IDE Agent-First: Sistema de Orquestación y Control de Trazabilidad en Antigravity", "Reglas de Seguridad y Configuración Crítica: Modo Review y Allowlist", "Resolución de proyectos prácticos (Sitios Web con Chatbots) iterando desde un Prompt Maestro"] },
                        { icon: "✅", title: "Sistema de Evaluación", items: ["Ejercicios prácticos de prompts: 40%", "Proyecto de codificación asisitida: 30%", "Participación y revisión de código: 20%", "Actividades asincrónicas: 10%"] }
                    ]
                },
                summary: `<h3>⚡ Vibe Coding y la Ingeniería de Especificación</h3>
            <p>El <strong>Vibe Coding</strong> (término acuñado por Andrej Karpathy) es una metodología intuitiva donde describes qué crear utilizando lenguaje natural (la "vibra") en lugar de programar la sintaxis tradicional. Sin embargo, para escalar hacia proyectos profesionales, seguros y sin alucinaciones, este enfoque evoluciona a la <strong>Ingeniería de Especificación</strong>.</p>
            
            <div class="example"><h4>💡 ¿Cómo estructurar un problema complejo para la IA?</h4>
            <p>La regla fundamental es dar siempre <strong>"Pasos, no objetivos vagos"</strong>. Un buen prompt de ingeniería se estructura en 6 componentes vitales:</p>
            <ol>
                <li><strong>Contexto:</strong> Tipo de problema y la procedencia de los datos.</li>
                <li><strong>Objetivo:</strong> El resultado macro esperado (el "qué").</li>
                <li><strong>Entradas:</strong> Variables/insumos explícitos disponibles.</li>
                <li><strong>Pasos Explícitos:</strong> Secuencia cronológica estricta de acciones o tareas analíticas a ejercer.</li>
                <li><strong>Restricciones:</strong> Límites metodológicos y reglas de formato indispensables.</li>
                <li><strong>Salida Esperada:</strong> Tipo del entregable final (Documentos HTML, Reportes, Gráficos).</li>
            </ol></div>
            
            <h3>🔬 Google AI Studio: Tu Laboratorio Central</h3>
            <p><strong>Google AI Studio</strong> no es solo un chat, funciona como una plataforma estructurada y "playground" interactivo enfocada a probar modelos (como Gemini 1.5 Pro o Flash). Aporta herramientas profundas para crear instrucciones como <em>Freeform Prompt</em> y <em>Structured Prompt</em> antes de automatizar proyectos grandes.</p>
            <ul>
                <li><strong>Capacidades Multimodales:</strong> Capaz de procesar masivamente texto, imágenes, audios y video simultáneo.</li>
                <li><strong>Experimentación Avanzada:</strong> Facilita el ajuste dinámico paramétrico para desarrolladores midiendo variables como Temperatura, Tokens y el uso directo de Python para Code Execution.</li>
                <li><strong>Live API:</strong> Ideal para construir sistemas en tiempo real aplicando interacciones asíncronas bidireccionales de audio y video fluido sin demoras de capa.</li>
            </ul>

            <h3>🚀 Google Antigravity y los IDEs Agent-First</h3>
            <p>A diferencia de conversar pasivamente, los entornos como <strong>Antigravity</strong> (IDE Agent-First) permiten a los agentes tener un "cuerpo" que trabaja activamente sobre tu proyecto utilizando tres capacidades: el <strong>Editor</strong> (manejo de archivos reales en VS Code), la <strong>Terminal</strong> (ejecución de comandos y servidores locales) y el <strong>Browser</strong> (ingreso y verificación autónoma en la Web).</p>
            
            <div class="case"><h4>⚙️ El Ciclo de Operación Segura (Review-Driven Development)</h4>
            <p>Un ingeniero utiliza Antigravity como orquestador humano mediante las siguientes reglas:</p>
            <ul>
                <li><strong>Orquestación Incial:</strong> El humano provee el <em>"Prompt Maestro"</em> y define el Workspace (ej. creando carpetas de insumos <code>/info</code> y <code>/imagenes</code>).</li>
                <li><strong>Documentación y Artifacts:</strong> Para garantizar trazabilidad, el agente produce obligatoriamente elementos verificables como el <em>Task List</em> (lista de actividades) y el <em>Implementation Plan</em> antes de codificar.</li>
                <li><strong>Revisión de Diffs:</strong> El desarrollador acepta o rechaza las re-escrituras directas al código por sub-bloques sin que la IA cambie todo de golpe por su cuenta.</li>
                <li><strong>Comandos Seguros:</strong> Mantener una ejecución aprobada manualmente de la terminal y dominios filtrados (Allowlist) son piezas irrenunciables de seguridad en clase para evitar riesgos.</li>
            </ul></div>`,
                videos: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Selección oficial de demostraciones, conceptos de Vibe Coding y tutoriales de IDEs de agentes autónomos. Haz clic para ver en YouTube.</p>
            <h4 class="tool-category">🧠 Ingeniería y Vibe Coding</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">⚡</div><div class="tool-name">Karpathy & Vibe Coding</div>
                    <div class="tool-desc">Entendiendo cómo dejar el código tradicional atrás</div>
                    <a href="https://www.youtube.com/results?search_query=Andrej+Karpathy+Vibe+Coding+explicacion" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">✍️</div><div class="tool-name">Prompt Structuring</div>
                    <div class="tool-desc">Ingeniería de pasos a la IA (Desglose de problemas)</div>
                    <a href="https://www.youtube.com/results?search_query=Ingenieria+de+prompts+avanzada+paso+a+paso" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
            </div>
            
            <h4 class="tool-category" style="margin-top:30px">🔬 Studio y Agent IDEs</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">🌟</div><div class="tool-name">Google AI Studio Masterclass</div>
                    <div class="tool-desc">Experimenta modelos Gemini y Code Execution</div>
                    <a href="https://www.youtube.com/results?search_query=Google+AI+Studio+Gemini+tutorial+español" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">🤖</div><div class="tool-name">Antigravity & Agent IDEs</div>
                    <div class="tool-desc">Trazabilidad en proyectos de Antigravity / Cursor</div>
                    <a href="https://www.youtube.com/results?search_query=IDE+Agent+First+AI+Coding+software" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
            </div>`,
                tutorials: `<h4 class="tool-category">🎬 Videos Tutoriales Específicos - Unidad 7</h4>
            <div class="tools-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://www.youtube.com/watch?v=LTm8FgcNHJc" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/LTm8FgcNHJc/hqdefault.jpg" alt="Vibe Coding e Ingeniería de Especificación" style="width:100%;height:160px;object-fit:cover;" />
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">⚡ Vibe Coding e Ingeniería</div>
                            <div style="font-size:12px;color:var(--gr)">El paso a paso de cómo estructurar requerimientos para no recibir resultados erróneos de la IA.</div>
                        </div>
                    </a>
                </div>
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://www.youtube.com/watch?v=txTSUu4mcfM" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/txTSUu4mcfM/hqdefault.jpg" alt="Uso de Google AI Studio" style="width:100%;height:160px;object-fit:cover;" />
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">🌟 Laboratorio AI Studio</div>
                            <div style="font-size:12px;color:var(--gr)">Aprende a ejecutar pruebas complejas con modelos, conectando código e interactuando con los Prompts Estructurados.</div>
                        </div>
                    </a>
                </div>
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://www.youtube.com/watch?v=ZwAExZYwDJ4" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/ZwAExZYwDJ4/hqdefault.jpg" alt="Uso de IDE Agent-First" style="width:100%;height:160px;object-fit:cover;" />
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">🚀 IDE de Agente: Antigravity</div>
                            <div style="font-size:12px;color:var(--gr)">Programando un sitio web completo dictándole la infraestructura y supervisando el desarrollo vía Diffs.</div>
                        </div>
                    </a>
                </div>
            </div>`,
                insumos: `<h4 class="tool-category">📦 Materiales Descargables - Unidad 7</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">📚</div>
                    <div class="tool-name">Insumos Unidad 7.zip</div>
                    <div class="tool-desc">Contiene el Prompt Maestro, catálogo demostrativo y archivos base de /info e /imagenes.</div>
                    <a href="https://drive.google.com/uc?export=download&id=1CRSPsBfmek8SW0KZzsGWUlzsK-Tpl1M1" target="_blank" class="tool-link">⬇️ Descargar →</a>
                </div>
            </div>`,
                tools: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Plataformas de desarrollo agent-first para probar y refinar código real.</p>
            <h4 class="tool-category">🛠️ Plataformas Core</h4>
            <div class="tools-grid">
                <div class="tool-card"><div class="tool-icon">🌟</div><div class="tool-name">Google AI Studio</div><div class="tool-desc">Entorno de experimentación nativa Gemini</div><a href="https://aistudio.google.com/" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">⚡</div><div class="tool-name">Antigravity</div><div class="tool-desc">IDE Agent-First para ingenieros</div><a href="https://github.com/google-deepmind/antigravity" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">👨‍💻</div><div class="tool-name">Cursor AI</div><div class="tool-desc">Editor de código asistido con chat in-line</div><a href="https://www.cursor.com/" target="_blank" class="tool-link">Abrir →</a></div>
            </div>`,
                activities: `<h3>📝 Actividades Prácticas y Evaluativas - Unidad 7</h3>
            <div class="activity-card" style="background:rgba(99,102,241,.1);border:1px solid rgba(99,102,241,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--p);margin-bottom:12px">🔬 Actividad 1: Ingeniería de Especificación en Google AI Studio (45 min)</h4>
                <p style="margin-bottom:12px">Diseña un wireframe textual y estructuración paso a paso usando la experimentación:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Abre Google AI Studio e inicia un <em>Structured Prompt</em>. Coloca un "System instruction" que defina al modelo como un arquitecto web senior experiente.</li>
                    <li>Suministra en las instrucciones el contexto y objetivo de la landing page. Envíale tus restricciones exactas (Ej. Móvil primero y no emplear JavaScript complejo).</li>
                    <li>Itera tu prompt pidiéndole la respuesta en niveles de entrega: Sitemap primero, wireframe luego y, finalmente, código HTML simplificado.</li>
                </ol>
            </div>
            <div class="activity-card" style="background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--g);margin-bottom:12px">🚀 Actividad 2: Flujo Completo con IDE Agent-First (Web Comercial) (60 min)</h4>
                <p style="margin-bottom:12px">Trabaja roles de Product Owner para orquestar la generación funcional de un sitio web asisito por agente:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Abre Antigravity o tu entorno Agent-First y carga una carpeta de <code>Workspace</code> recién vacía. Transfiere los adjuntos de Insúmos en las carpetas de negocio (<code>/info</code> e <code>/imagenes</code>).</li>
                    <li>Dile a tu Agente el "Prompt Maestro" requiriendo obligatoriamente primero planificar generando <em>Artifacts de Task List y Código Planificado</em>.</li>
                    <li>Supervisa cada decisión: Acepta los bloqueos de "Diff" correctos y pide mejoras por chat al ver las integraciones y renderización del portafolio. Obtén como meta final la estructura generada sobre <code>/public</code>.</li>
                </ol>
            </div>
            <div class="activity-card" style="background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--w);margin-bottom:12px">💻 Actividad 3: Revisión de Artefactos (Trazabilidad y Seguridad) (30 min)</h4>
                <p style="margin-bottom:12px">Aplica las reglas de control y seguridad operativa en agentes:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Una vez programado el sitio anterior, pide a la IA añadirle un botón flotante de Chatbot funcional conectado a una ruta de API simulada.</li>
                    <li>Cuando la IA pida generar una instalación en Terminal o iniciar un empaquetado de proyecto, <strong>pausa y revisa el comando sugerido</strong>, entendiendo el proceso Review-Driven.</li>
                    <li>Estudia los <em>Artifacts</em> guardados por el sistema y documenta el documento final de recorrido conocido como Walkthrough evidenciando tu labor de Product Owner.</li>
                </ol>
            </div>`,
                quiz: [
                    { q: "¿En qué radica fundamentalmente el concepto de Vibe Coding?", o: ["En aprender a programar algoritmos en C++", "En describir en lenguaje natural la idea general para que la IA desarrolle automáticamente el código sin preocuparte de la implementación técnica formal", "En enviar emoticonos o vibes positivos y que la IA los lea", "En codificar exclusivamente aplicaciones para edición musical"], c: 1 },
                    { q: "¿Por qué el Vibe Coding tradicional suele fallar en entornos profesionales grandes?", o: ["Porque solo funciona en Linux.", "Porque da órdenes muy vagas de alto nivel, lo que causa suposiciones implícitas erróneas y un código desordenado complicado de escalar.", "Porque genera códigos muy costosos financieramente.", "Porque la IA ignora las órdenes naturales largas."], c: 1 },
                    { q: "¿Cuál es el principio central recomendado en la Ingeniería de Especificación?", o: ["Dar siempre 'pasos verificables' en vez de objetivos vagos a la IA", "Delegar el 100% de la toma de decisiones al agente", "Escribir siempre en inglés formal técnico", "Enviar todo el código roto en un solo prompt masivo"], c: 0 },
                    { q: "¿Para qué caso de uso en especial el curso resalta utilizar Google AI Studio?", o: ["Creación completa final y almacenamiento hosteado de bases de datos masivas automatizadas", "Como un 'Playground' o laboratorio avanzado para experimentar tempranamente los prompts con parámetros como Temperatura y verificar Code Execution seguro a manera de prototipo", "Para grabar la pantalla e impartir videollamadas con humanos", "Para crear cuentas corporativas de Google Workspace únicamente."], c: 1 },
                    { q: "¿Qué diferencia drástica de capacidades poseen entornos Agent-First (ej. Antigravity) respecto al típico ChatGPT?", o: ["Antigravity procesa palabras más bonitas", "Los IDE tipo Antigravity actúan realmente poseyendo alcance al Editor de Texto físico, la Terminal para correr comandos y un Browser para verificar en la web los resultados en tiempo real", "Solo trabajan mediante conexión inalámbrica Bluetooth profunda.", "Antigravity es puramente un creador genérico de imágenes planas 2D"], c: 1 },
                    { q: "¿Qué mecanismo vital en el entorno asegura que el desarrollador lleve la trazabilidad y la IA no programe a su propio arbitrio?", o: ["El sistema de Artifacts que elaboran documentos como el Task List, el Plano de Implementación y los Diffs revisables del código editado", "El firewall interno en los modelos de lenguaje", "El botón de apagado manual del PC", "Las suscripciones Premium limitadas a tiempo"], c: 0 },
                    { q: "¿En qué consiste la regla del Review-Driven Development implementada en la clase de Agentes?", o: ["Exigir que compañeros humanos revisen tu trabajo en remoto y puntúen luego en redes", "Balance de desarrollo donde la IA propone paso a paso y pide autorización (approval) obligatoria previo a codificar sobre los archivos o comandos sensibles", "Solo poder escribir reseñas automatizadas hacia la IA tras su ejecución final en caso de fallo", "Delegar de inicio todo el trabajo complejo bajo un modo automático ('turbo') a fin de acortar tiempos y que decida libremente"], c: 1 },
                    { q: "¿Cuál es una técnica primordial que usamos dentro del Prompt Maestro en nuestro ejercicio de diseño Web en clase?", o: ["Utilizar un tono estrictamente intimidante sobre el asistente virtual", "Comenzar requiriendo que lea la carpeta interna de /info y sus lineamientos empresariales verídicos antes de fabricar cualquier dato, evitando que mienta o alucine (asignando en cambio placeholders)", "Pedir que elija autónomamente colores y descargue al azar fotografías de internet sin base para agilizar la entrega", "Generar 15 iteraciones visuales diferentes por minuto sobre toda la página publicitaria y desechar las que posean fallos."], c: 1 },
                    { q: "¿Qué beneficio tiene obligar al Agente a presentar un 'Artifact' documentado como el Task List (Listado de Tareas) desde el inicio de proyecto?", o: ["Ayuda principalmente a cobrar más en la factura a nuestro cliente", "Vuelve un paso lenta la automatización, generando código por líneas para cobrar suscripción y ancho de banda al emplearlo", "Garantiza un orden secuencial, evaluable lógicamente y acorta el tiempo detectando si el Agente tomó malos enfoques de diseño a futuro, en lugar de improvisar al momento de generar todo del tirón", "Se elabora simplemente como decorativo obligatorio."], c: 2 },
                    { q: "¿Si tengo múltiples tareas iterativas, cuál es la regla de oro enseñada para solicitarles cambios al Agente a lo largo de la práctica?", o: ["Amasar un gran prompt de quejas abarcando modificaciones desde frontend, backend, menús e imágenes fallidas unificando 15 peticiones juntas.", "Realizar iteraciones pequeñas y precisas a modo '1 corrección = 1 Ticket o Instrucción', guiando controladamente al modelo en sus próximos diffs", "Borrar totalmente el ambiente de código local si el agente comete una equivocación o genera fallas menores en un diff", "Esperar a que cambie versiones el LLM localmente antes de reanudar operaciones operativas."], c: 1 }
                ],
                memory: [{ t: "Vibe Coding", d: "Construir indicando un propósito (vibra) general" }, { t: "Especificación", d: "Descomponer exigencias en pasos estrictos para la IA" }, { t: "Google AI Studio", d: "Playground interactivo de desarrollo de Prompts" }, { t: "Artifacts", d: "Evidencias documentadas del estado de trabajo (ej. planes)" }, { t: "Agent-First (Antigravity)", d: "Entornos automatizados de terminal, código y supervisión Web" }, { t: "Review-Driven", d: "El desarrollador humano aprueba rigurosamente cada tarea sugerida" }, { t: "Diffs", d: "Los fragmentos detallados de código modificado por el Agente para revisar" }, { t: "Prompt Maestro", d: "Macro-instrucción que delimita carpetas base y reglas inamovibles" }],
                trivia: [{ q: "¿Quién acuñó el término técnico de 'Vibe Coding' en un entorno de software?", o: ["Elon Musk", "Sam Altman", "Andrej Karpathy", "Geoffrey Hinton"], c: 2 }, { q: "¿Qué nombre recibe en Antigravity el listado o documento de evidencias que valida qué hará y codificará paso a paso la IA?", o: ["Dossier Técnico", "Artifact: Implementation Plan / Task List", "Blueprint general", "Libro Blanco del Agente"], c: 1 }, { q: "¿Dentro del ejercicio guiado web de Antigravity, de dónde se indicó que proviene la evidencia/material comercial real indispensable para impedir que el Agente alucine sobre la empresa?", o: ["De un listado PDF ajeno buscado en línea de forma autónoma", "Desde subcarpetas estrictas estipuladas localmente (Ej. /info)", "De plantillas autogeneradas por ChatGPT incrustadas internamente", "De llamadas a base de datos de enciclopedia virtual local"], c: 1 }, { q: "¿Qué peligro abarca conceder 'Autonomía Total' y obviar el modo Review en un IDE al ejecutar comandos Shell (terminal)?", o: ["La IA podría saturar la tarjeta gráfica al punto de fundirla", "Riesgos drásticos de permitir instalar dependencias dudosas o que borre el sistema completo al interpretar muy libremente los flujos", "Cero riesgos documentados; están fuertemente protegidas contra todo daño lógico", "Consume muchísimos más tokens y el servicio deja de contestar de inmediato"], c: 1 }, { q: "¿En qué área es fuertemente potente y destaca inicialmente la funcionalidad de Live API de Gemini en desarrollos empresariales?", o: ["Para analizar códigos binarios ultra-densos sin errores lógicos", "Para habilitar aplicaciones o tutores enfocados principalmente a streams bidireccionales en baja latencia (Audio/Video)", "Para procesar hojas de cálculos Excel estáticas en background", "Para desarrollar únicamente juegos interactivos móviles localizados."], c: 1 }],
                classify: { cat1: "📦 Entornos & Elementos", cat2: "💡 Metodologías Prácticas", items: [{ t: "Google AI Studio", c: 1 }, { t: "Ingeniería de Especificación", c: 2 }, { t: "Antigravity IDE", c: 1 }, { t: "Review-Driven Development", c: 2 }, { t: "Artifacts y Diffs", c: 1 }, { t: "Redacción de Prompt Maestro", c: 2 }, { t: "Carpetas Locales (/info)", c: 1 }, { t: "Suministrar 'Pasos vs Objetivos'", c: 2 }] },
                hangman: [{ w: "VIBE", h: "Término que denota construir sobre la idea o esencia de algo sin técnica" }, { w: "ESPECIFICACION", h: "Ingeniería orientada a detallar instrucciones por pasos lógicos irrestrictos" }, { w: "STUDIO", h: "Laboratorio principal de ensayo para los LLM de Google" }, { w: "ANTIGRAVITY", h: "El entorno de Agentes utilizado en la clase para desarrollo avanzado programático" }, { w: "ARTIFACT", h: "Trazabilidad técnica generada por un Agente tipo 'lista y planes'" }, { w: "DIFFS", h: "Vistas técnicas rápidas de código removido y añadido por el Agente para aprobación" }, { w: "TERMINAL", h: "Ventana que requiere revisión crítica antes de permitir comandos al ambiente local" }, { w: "ALLOWLIST", h: "Restricción crucial implementada en navegador para que el Agente limite sus visitas web locales." }],
                simResponses: { "vibe": "El <strong>Vibe Coding</strong> es una técnica de alto nivel donde la forma y propósito guía la orden. Es rápida pero inestable sin supervisión. Evoluciona a <em>Ingeniería de Especificación</em> para ser sólida.", "antigravity": "<strong>Antigravity</strong> (como ejemplo de IDE Agent-First) empodera agentes con Terminal y un Explorer, posibilitando planes que tú en el rol de Product Owner validas bajo <em>Review-Driven Development</em>.", "studio": "En <strong>Google AI Studio</strong> probamos parámetros precisos tempranos combinando flujos como la generación de esquemas textuales directos mediante instrucciones.", "artifact": "Los <strong>Artifacts</strong> (Task List, Implementation Plan, Walkthrough) funcionan en Antigravity como evidencias escritas del plan agente, permitiendo tu iteración humana informada y disminuyendo 'trust gap'.", "maestro": "El <strong>Prompt Maestro</strong> concentra el rol, el contexto inicial explícito del marco real usando insumos (en /info e /imagenes) impidiéndole a la IA salirse con desvaríos y centrando el formato paso a paso de tareas.", "especificacion": "La <strong>Ingeniería de Especificación</strong> requiere en cada prompt: detallar el contexto, definir métricas claras de salida, enumerar restricciones y <em>siempre sugerir Pasos, No Objetivos vagos</em> a la IA empresarial.", "default": "¡Soy el asistente de la Unidad 7! Pregúntame sobre el entorno de Google AI Studio, las reglas vitales de Antigravity o el marco analítico de Vibe Coding vs Ingeniería de Especificación." }
            },
"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"
with codecs.open(file_path, "r", "utf-8") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if 4948 <= i <= 5140:  # 0-indexed. 4949 to 5141
        if i == 4948:
            new_lines.append(replacement)
        pass # replace them
    else:
        new_lines.append(line)

with codecs.open(file_path, "w", "utf-8") as f:
    f.writelines(new_lines)

print("Update completed successfully for Unit 7.")
