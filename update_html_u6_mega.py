import codecs

replacement = """            6: {
                pres: "https://docs.google.com/presentation/d/1hP9bFL8LhqGn_9i_QGXyEo0DiM1QNCaH8BuGQoppA7c/embed",
                title: "Unidad 6: Plataformas de Agentes de IA Especializados",
                subtitle: "De chatbots a ejecutores autónomos usando el estándar MCP",
                breadcrumb: "Módulo 2 <span>›</span> Herramientas IA",
                plan: {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Comprender la evolución desde chatbots estáticos hacia agentes autónomos ejecutores", "Dominar el concepto de MCP (Model Context Protocol) y su arquitectura técnica básica", "Implementar integraciones MCP reales en plataformas globales como Gemini, ChatGPT y Claude", "Operar plataformas agénticas especializadas (Kimi, Genspark, Manus, Minimax)", "Diseñar aplicaciones interactivas y automatizaciones de correo delegando en Agentes IAM"] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Implementación segura de conexiones Workspace y Cloud usando MCP nativo", "Orquestación de tareas complejas en la Web: desde leer adjuntos hasta generar reportes y aplicaciones interactivas en vivo", "Evaluación crítica del 'Vendor Lock-in' y adopción de estándares iterativos", "Gestión de riesgos empresariales y alucinaciones en agentes productivos"] },
                        { icon: "⏱️", title: "Distribución del Tiempo", items: ["Semana 6 del programa", "Sesiones sincrónicas: 6 horas", "Trabajo asincrónico: 1 hora", "Diligencia práctica en Labs MCP: 2 horas extras recomendadas", "Dedicación semanal total: 9 horas"] },
                        { icon: "📚", title: "Ubicación en el Programa", items: ["Módulo 2: Herramientas IA para Automatización", "Unidad 6 de 5 (Extensión técnica avanzada) en este módulo", "Prerequisito: Unidad 5 (Automatización Generativa)", "Siguiente: Unidad 7 (Google AI Studio)"] },
                        { icon: "📝", title: "Contenidos de Esta Unidad", items: ["Historia Automática: De LLMs al ecosistema MCP Q2 2025", "Arquitectura MCP: JSON-RPC, Manifiestos y la conjunción Cliente-Servidor", "Agentes Especializados I: Kimi 2.5 para documentacion académica y analítica", "Agentes Especializados II: Genspark para lectura de mails, adjuntos y envíos dinámicos", "Agentes de Front-End: Manus AI para la generación de Apps interactivas financieras", "Agentes de Research: Minimax para análisis exhaustivo y generación de gráficos Python"] },
                        { icon: "✅", title: "Sistema de Evaluación", items: ["Configuración de entorno MCP propio (Capturas): 30%", "Pruebas de Apps generadas con Manus AI: 30%", "Trabajo evaluativo con Kimi 2.5: 20%", "Respuestas al Simulador e integraciones: 20%"] }
                    ]
                },
                summary: `<h3>🔌 MCP: El Protocolo que Revolucionó a la IA</h3>
            <p>Antes de 2024, la inteligencia artificial se encontraba aislada dentro de las interfaces de chat; los modelos podían dar respuestas, pero no podían observar tus archivos, manejar tu calendario o alterar bases de datos sin construir APIs complejas que requerían meses de desarrollo experto.</p>
            <p>Creado y lanzado por Anthropic a finales de 2024, el <strong>MCP (Model Context Protocol)</strong> se posiciona como el "USB-C de la Inteligencia Artificial". Consiste en un estándar universal de código abierto capaz de conectar LLMs con sistemas corporativos reales, posibilitando a los agentes inspeccionar y ejecutar comandos sobre servicios de terceros en tiempo real sin rediseñar infraestructura. Su estructura de JSON Manifest y comunicación <em>Cliente-Servidor</em> liquida la dependencia con proveedores únicos (Vendor Lock-in) y ha sido rápidamente adoptada de manera nativa por la rama de automatizadores globales (n8n, Make) e IDEs modernos.</p>
            
            <div class="case"><h4>🔄 Integraciones MCP en la Práctica</h4>
            <ul>
                <li><strong>En Gemini:</strong> Mediante integraciones de Workspace, es factible indicarle a Gemini que cree eventos masivos en el Google Calendar o indague en tu bandeja de entrada unificando flujos. Sin embargo, su conexión actual en fase inicial con Gmail posee todavía inestabilidades de filtrado de datos respecto a otras herramientas.</li>
                <li><strong>En ChatGPT:</strong> El protocolo MCP nativo autoriza puentes instantáneos conectando Dropbox o Microsoft Teams para que el asistente indexe directorios densos, extraiga PDFs de "Econometría Empresarial" y extraiga métricas sin bajarlos primero.</li>
                <li><strong>En Claude:</strong> Por haber fundado el protocolo, ofrece un enorme repertorio, incluso conectores desktop de escritorio locales para manipular archivos de Windows directamente, editar código y leer carpetas privadas del disco duro al instante.</li>
            </ul></div>
            
            <h3>🤖 La Evolución: Agentes Especializados al Rescate</h3>
            <p>Con MCP funcionando como la vía neurológica de la IA, a mediados del 2025 explotaron comercialmente los "Agentes de IA". Diferenciándose brutalmente del clásico "Chatbot de propósito general", estos agentes tienen misiones analíticas, control de red, y capacidades de interacción sin detenerse. Representan el salto real a un sistema autónomo.</p>
            
            <div class="example"><h4>⚡ Plataformas Agénticas del Mercado Atual (Q2 2025)</h4>
            <ul>
                <li><strong>Kimi 2.5:</strong> Altamente focalizado en creación documental y presentaciones. Puede ingerir un PDF empresarial, transmutarse a su rol 'Adaptativo o Visual Académico', y escupir un Slide Deck profesional de 30 páginas altamente pulido sin necesitar los cortos límites de tokens habituales de plataformas como Gamma.</li>
                <li><strong>Genspark:</strong> Destaca fenomenalmente en la trazabilidad de tareas con sus MCPs. Si le inyectas tus correos, no solo narra el resumen; explora inteligentemente hilos anidados, abre archivos adjuntos en el fondo (como proformas de reparación), prepara el borrador y realiza el envío (disparador SMTP) completamente por ti si se lo pides.</li>
                <li><strong>Manus AI:</strong> Un ecosistema brutal si buscas transformar prompts en interfaces. Se le puede solicitar, por ejemplo, desarrollar un evaluador de riesgos en la bolsa de valores; no solo contestará texto intertivo, sino que codificará y renderizará en vivo una <em>Web App Simuladora Gráfica</em> manejable, dotada de menús, filtros de perfil de usuario (Conservador/Agresivo) y proyección de retornos.</li>
                <li><strong>Minimax:</strong> Un agente de Research avanzado. Excepcional explorador y programador analítico: se sumerge en internet y puede escribir él solo rutinas de Python (visibles en su pestaña de /Files y /Code) necesarias para autogenerarte gráficas demográficas con base en datasets estáticos o financieros subidos.</li>
            </ul></div>
            
            <div class="bib"><h3>📚 Retos de la Adopción</h3>
            <p>La adopción actual de agentes acarrea tres macrodesafíos ineludibles para los arquitectos:</p>
            <ol>
                <li><strong>Seguridad de Datos PII:</strong> Limitar hasta dónde posee permiso el agente sobre bases CRM.</li>
                <li><strong>Trazabilidad y Supervisión:</strong> ¿Quién es el responsable si un Agente de Genspark envía un presupuesto fatal y erróneo al cliente? Es obligatorio incorporar pasos de Review in-the-loop que corten los ciclos automáticos en tareas de alta responsabilidad comercial.</li>
                <li><strong>Control de API y Costos M/N:</strong> Limitar el bucle infinito en caso de que la IA sufra una alucinación multi-tarea.</li>
            </ol>
            </div>`,
                videos: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Selección de contenidos visuales recomendados por la cátedra para entender MCP y el estado del arte de Agentes en 2025.</p>
            <h4 class="tool-category">🔌 Arquitectura MCP y Fundamentos</h4>
            <div class="tools-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
                <div class="tool-card">
                    <div class="tool-icon">🧠</div><div class="tool-name">Explicando MCP Definitivo</div>
                    <div class="tool-desc">Entendiendo cómo Anthropic estandarizó las comunicaciones</div>
                    <a href="https://www.youtube.com/results?search_query=Model+Context+Protocol+explanation+Anthropic" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">💼</div><div class="tool-name">MCP + Codelabs Custom</div>
                    <div class="tool-desc">Cómo un desarrollador implementa un MCP local rápido</div>
                    <a href="https://www.youtube.com/results?search_query=Build+Custom+MCP+Server+Tutorial" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
            </div>
            
            <h4 class="tool-category" style="margin-top:30px">🤖 Agentes Especializados (2025)</h4>
            <div class="tools-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
                <div class="tool-card">
                    <div class="tool-icon">🖥️</div><div class="tool-name">Manus AI: Desarrollo Web</div>
                    <div class="tool-desc">Despliegue interactivo de Aplicaciones usando Manus</div>
                    <a href="https://www.youtube.com/results?search_query=Manus+AI+app+builder+showcase" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">📩</div><div class="tool-name">Genspark & Mails MCP</div>
                    <div class="tool-desc">Super Agentes de Genspark administrando Google CRM</div>
                    <a href="https://www.youtube.com/results?search_query=Genspark+super+agent+automation" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">📊</div><div class="tool-name">Minimax Pro Research</div>
                    <div class="tool-desc">Descubriendo los límites de Minimax y su generación de análisis en Python</div>
                    <a href="https://www.youtube.com/results?search_query=Minimax+AI+data+analysis" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
                <div class="tool-card">
                    <div class="tool-icon">🎫</div><div class="tool-name">Kimi 2.5 Documentación</div>
                    <div class="tool-desc">Explorando creación de slides de cero</div>
                    <a href="https://www.youtube.com/results?search_query=Kimi+2.5+features+presentation+generation" target="_blank" class="tool-link">Buscar en YouTube →</a>
                </div>
            </div>`,
                tutorials: `<h4 class="tool-category">🎬 Videos Tutoriales Específicos - Unidad 6</h4>
            <div class="tools-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://www.youtube.com/watch?v=mX3enpPh8ac" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/mX3enpPh8ac/hqdefault.jpg" alt="Uso de MCPs en la Industria" style="width:100%;height:160px;object-fit:cover;" />
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">🔌 Protocolo MCP en Práctica</div>
                            <div style="font-size:12px;color:var(--gr)">Aprende a acoplar Gemini, ChatGPT y Claude a tus calendarios web, bandejas de correo y nubes (Dropbox).</div>
                        </div>
                    </a>
                </div>
                <div class="tool-card" style="padding:0;overflow:hidden;border-radius:12px;">
                    <a href="https://www.youtube.com/watch?v=3vmSRyDk8sY" target="_blank" style="text-decoration:none;color:inherit;">
                        <img src="https://img.youtube.com/vi/3vmSRyDk8sY/hqdefault.jpg" alt="Uso de Agentes de IA" style="width:100%;height:160px;object-fit:cover;" />
                        <div style="padding:12px;">
                            <div style="font-weight:600;margin-bottom:4px;color:var(--wh)">🤖 Agentes Autónomos en Acción</div>
                            <div style="font-size:12px;color:var(--gr)">Demostración técnica de Kimi, Genspark (con sus MCP nativos potentes), Manus (creación de Apps) y el Minimax analítico.</div>
                        </div>
                    </a>
                </div>
            </div>`,
                insumos: `<h4 class="tool-category">📦 Materiales Descargables - Unidad 6</h4>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-icon">📚</div>
                    <div class="tool-name">Insumos Unidad 6.zip</div>
                    <div class="tool-desc">Material de agenda ficticia para el Calendar, Prompts para Manus y Minimax, y reportes simulados para Kimi.</div>
                    <a href="https://drive.google.com/uc?export=download&id=1t3jN638z5q8bWj48H4_8M197A598_d_x" target="_blank" class="tool-link">⬇️ Descargar →</a>
                </div>
            </div>`,
                tools: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Directorio de plataformas de propósito agéntico con MCPs integrados activamente.</p>
            <div class="tools-grid">
                <div class="tool-card"><div class="tool-icon">🎫</div><div class="tool-name">Kimi</div><div class="tool-desc">Agente líder en generación de slides y análisis bibliográfico adaptativo</div><a href="https://kimi.moonshot.cn/" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">📩</div><div class="tool-name">Genspark</div><div class="tool-desc">Super Agente asíncrono con potente manipulación de adjuntos e hilos</div><a href="https://www.genspark.ai/" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">🖥️</div><div class="tool-name">Manus AI</div><div class="tool-desc">Creador veloz de web apps interactivas modulares</div><a href="https://manus.im/" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">📊</div><div class="tool-name">Minimax</div><div class="tool-desc">Agente para investigación de mercado y automatización con Python interno</div><a href="https://hailuoai.video/" target="_blank" class="tool-link">Abrir →</a></div>
                <div class="tool-card"><div class="tool-icon">🔌</div><div class="tool-name">Claude.ai</div><div class="tool-desc">Chat con soporte MCP local Desktop para control de OS</div><a href="https://claude.ai/" target="_blank" class="tool-link">Abrir →</a></div>
            </div>`,
                activities: `<h3>📝 Actividades Prácticas y Evaluativas - Unidad 6</h3>
            <div class="activity-card" style="background:rgba(99,102,241,.1);border:1px solid rgba(99,102,241,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--p);margin-bottom:12px">🔬 Actividad 1: Laboratorio de MCPs Nativos con Google y Microsoft (45 min)</h4>
                <p style="margin-bottom:12px">Opera directamente las extensiones de integración en tu Workspace personal:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Abre Gemini. En configuración activa tu Google Workspace. Extrae el archivo 'Eventos' de insumos, cambia las fechas a 2026 y adjúntalo pidiéndole organizar las fechas en tu calendario. Verifica su efectividad.</li>
                    <li>Abre ChatGPT (cuenta libre o plus). Ve a la sesión de Apps y vincula tu cuenta de Dropbox. Solicítale al asistente encontrar un libro o archivo PDF que poseas ahí usando palabras claves inexactas, para validar que el modelo de pensamiento logra buscar.</li>
                </ol>
            </div>
            <div class="activity-card" style="background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--g);margin-bottom:12px">🚀 Actividad 2: Flujo Documental Completo en Kimi (45 min)</h4>
                <p style="margin-bottom:12px">Conviértete en dependiente de inteligencia artificial para informes:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Accede a Kimi 2.5.</li>
                    <li>Carga el documento "Informe II 2025 v4" de la carpeta de insumos. Pide como rol "Crear una presentación ejecutiva informal".</li>
                    <li>Selecciona un formato 'Académico' o 'Tecnológico Blueprint', requiriendo una extensión explícita de 26 a 30 diapositivas. Transfiere los esquemas obtenidos al formato final requerido y evalúa su coherencia técnica.</li>
                </ol>
            </div>
            <div class="activity-card" style="background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.2);border-radius:12px;padding:20px;margin-bottom:16px">
                <h4 style="color:var(--w);margin-bottom:12px">💻 Actividad 3: Creación de Simuladores Avanzados Financieros con Manus (60 min)</h4>
                <p style="margin-bottom:12px">Experimenta la codificación zero-shot guiando interfaces visuales:</p>
                <ol style="margin-left:20px;color:rgba(255,255,255,.8)">
                    <li>Ingresa en Manus AI u alternativa de despliegue sugerida. Entrégales este prompt: "Deseo invertir dinero ahorrado en tecnología e IA Generativa. Háblame de los retornos estandarizados del sector, riesgos y haz una App funcional y UI atractiva con simuladores accionarios para estas compañías".</li>
                    <li>Experimenta con la aplicación devuelta jugando con tu 'riesgo' e inversiones a 5 o 10 años, demostrando la capacidad del agente de crear software visual efímero con cálculo matemático interno.</li>
                </ol>
            </div>`,
                quiz: [
                    { q: "¿Qué significan las siglas MCP originadas por Anthropic en la evolución moderna de la Inteligencia Artificial?", o: ["Multiple Context Protocol", "Model Context Protocol", "Modular Controller Program", "Matrix Computacional Process"], c: 1 },
                    { q: "¿Por qué se denomina informalmente al MCP general como un 'USB-C de la Inteligencia Artificial' empresarial?", o: ["Debido a que únicamente funciona mediante conexiones cableadas de alto voltaje", "Porque erradica el Vendor Lock-in al brindar conectividad transversal estandarizada e integral de LLMs con cualquier base de datos y sistema operativo sin precisar desarrollos personalizados N x M", "Porque es una iniciativa patentada que se distribuye mediante chips de almacenamiento físico extraíble", "Porque su puerto visual es similar al de los conectores USB viejos"], c: 1 },
                    { q: "¿Cuál es una flaqueza notoria demostrada por las integraciones actuales MCP Workspace nativas en la interfaz de Gemini con cuentas de Gmail gratuitas de usuarios?", o: ["Borran automáticamente cualquier mensaje recibido de Microsoft Outlook por rivalidad de marca", "Presentan inestabilidades graves en el filtrado omitiendo y descartando en sus resúmenes asuntos prioritarios sin razón justificada en la bandeja", "No tienen capacidad de leer idiomas diferentes al esperanto o lenguajes en código binario y fallan.", "La interfaz exige pagar por cada correo leído un crédito unitario en token sin excepción"], c: 1 },
                    { q: "¿La interfaz de Claude cómo saca máximo provecho a sus MCP en comparación a meramente conectar servicios en la nube (como OneDrive o Dropbox)?", o: ["Solo habilita a manipular colores del sistema como temas oscuros web y avatares personalizados visuales en 2D.", "Posee un alcance mucho más profundo con un 'Connector Desktop' local que en sí permite operar la lectura, migración y cambio de extensiones de archivos físicos del propio sistema operativo origen de la computadora (ej: interactuar con Windows local)", "Inhabilita automáticamente su MCP durante la mañana para liberar servidores y economizar la gestión operativa de tráfico local de Norteamérica.", "Únicamente autoriza generar textos predeterminados a formato JSON rígidos, perdiendo versatilidad visual de carpetas en pantalla"], c: 1 },
                    { q: "¿Qué proeza técnica singular y destacable en manejo de archivos documentales (Mails) consigue el sistema agente de Genspark en su MCP?", o: ["Puede analizar la intención subyacente en hilos encadenados y revisar el interior de adjuntos complejos (como actas dañadas) sin perder latencia, formular su propio texto borrador para dar solución e inclusive despachar el envío por ti autorizando con clics simples en su chat.", "Traduce automáticamente los correos SPAM bloqueados convirtiéndolos en notificaciones seguras con códigos de cifrado reescritos.", "Transcribe únicamente audios muy breves enviados por canales de texto pero es incompetente para indagar PDF ajenos adosados a la plataforma externa.", "Permite bloquear y borrar contactos del CRM mediante peticiones psíquicas sin intervención manual de comandos logueados."], c: 0 },
                    { q: "¿Qué herramienta es citada como colosal e indispensable durante el Q2 de 2025 para el desarrollo y generación en vivo de pequeñas Apps financieras o interactivas con interfaz gráfica y sin código de por medio?", o: ["Kimi 2.5 (enfoque adaptativo 300K)", "Manus AI (especializada en iterar calculadoras visuales o Dashboards estocásticos a solicitud general)", "La extensión GPT Explorer de ChatGPT para uso primario y sin visualizador interactivo.", "El modo Desktop del antiguo GPT 3.0 en Discord."], c: 1 },
                    { q: "¿Cómo asiste Kimi 2.5 de manera sobresaliente a entornos corporativos o a nivel investigativo (universitario, reportes, C-Suite)?", o: ["Creando modelos algorítmicos complejos en lenguajes de alto nivel como Golang para servidores.", "Destierra a competidores como Gamma al tomar documentos enteros engorrosos transformando datos crudos velozmente a diapositivas ejecutivas extensas (ej. 30 slides formales) en esquemas elegibles como format 'Académico'.", "Restringido al área de ciberseguridad protegiendo módems caseros y bloqueando intentos de phishing.", "Inutilizado para el uso profesional derivado a sus reglas rígidas prefabricadas infantiles y dibujos caricaturescos que no pueden borrarse"], c: 1 },
                    { q: "¿Qué utilidad diferencial expone fundamentalmente el potente agente de Research 'Minimax' al enfrentar estudios y solicitudes complejas a gran escala?", o: ["Procesa consultas de investigación elaborando localmente código de Python transitorio visualizable en pestaña '/code' para renderizar gráficas informativas propias o reportes basados intrínsecamente en algoritmos validados por su flujo operativo.", "Codifica por naturaleza aplicaciones gráficas móviles y consolas retro interactivas, despreciando la ofimática.", "Simplemente lee Wikipedia y reescribe texto lúdico a forma de rimas, inhabilitado y ajedrezado sin capacidad de procesamiento puro analítico de archivos macro.", "Se destaca por su incapacidad para aceptar peticiones que exijan cálculos matemáticos largos remitiendose al modelo nativo."], c: 0 },
                    { q: "¿A qué problemática global y limitante pre-existente da fin la comunicación JSON de la arquitectura de MCP?", o: ["El Mxn Problem: Evitando construir centenares de integraciones a pulso entre cada LLM de las marcas existentes frente a las 5,000 Apps SaaS del mundo, estableciéndoles un protocolo bidireccional de acceso universal único.", "A la insuficiencia de memorias RAM de los usuarios promedios de laptops para jugar en la red.", "A erradicar los impuestos generados anualmente en bases de datos de Google por transacciones internacionales ilícitas.", "Termina de una vez por todas las latencias en descargas gratuitas generadoras de imágenes en GPU's ajenas prestadas."], c: 0 },
                    { q: "¿A la vez de su asombrosa autonomía y versatilidad funcional probada, qué aspecto se asume como el más riguroso en la agenda de arquitectos operando Agentes autónomos como herramientas principales a corto y medio plazo (Q3 en adelante)?", o: ["El incremento estrepitoso e incontrolable de costos de electricidad y banda ancha satelital por su empleo desmedido en oficinas de atención", "Las complicaciones de derechos de licencias y diseño estructural", "Gestionar meticulosamente la delegación restrictiva de permisos sensibles sobre CRMs e instaurar rutinas de control 'Human In The Loop' mitigando que acciones sin revisar (envíos destructivos o borrados) aniquilen al instante operaciones mercantiles viables.", "Enseñar obligatoriamente a todo el personal de la empresa programación pura para lograr activarlos ya que requiere 0 interfaz visual e implica comandos de consola estricta para el usuario de a pie"], c: 2 }
                ],
                memory: [{ t: "MCP", d: "Model Context Protocol. El estándar abierto 'USB-C' de conexión IA" }, { t: "Kimi", d: "Agente enfocado a generar Presentaciones Ejecutivas y redacción" }, { t: "Genspark", d: "Agente que manipula adjuntos de email en profundidad" }, { t: "Manus AI", d: "Agente ideal para codificar pequeñas Web Apps funcionales en Live UI" }, { t: "Minimax", d: "Para investigación algorítmica y autogenerar cálculos con Python interno" }, { t: "Vendor Lock-in", d: "Esclavitud limitante a una sola herramienta propietaria empresarial (evitado gracias al MCP)" }, { t: "JSON Manifests", d: "Los archivos que describen parámetros del Servidor hacia el LLM logrando un empalme estable y sin error de lectura" }],
                trivia: [{ q: "¿A qué protocolo open source previo inspirador de la estandarización para editores Visual Studio se remonta la idea primigenia del MCP creado por Anthropic para inteligencia artificial?", o: ["Language Server Protocol (LSP) fabricado por Microsoft", "Hypertext Transfer Protocol Secure (HTTPS)", "File Transfer Protocol (FTP)", "Simple Mail Transfer Protocol (SMTP)"], c: 0 }, { q: "¿Qué gigante multinacional fue el verdadero arquitecto, ideólogo y proveedor del protocolo universal MCP en noviembre 2024 previo a adoptarse globalmente?", o: ["OpenAI (ChatGPT)", "Google (Gemini Labs)", "Anthropic (Fabricante de la familia Claude)", "Meta Platforms (Zuckerberg)"], c: 2 }, { q: "¿Qué peligro abismal existe al otorgar autonomía ilimitada 'Zero-Click' y omitir procesos evaluadores humanos a una IA con MCP enlazada al Gmail de nuestra Pyme si nos encontramos con un correo conflictivo no priorizado?", o: ["Que colapse nuestra latencia de Wi-Fi", "Que emita unilateralmente rechazos formales, respuestas de mal tono, apruebe reembolsos por error o borre conversaciones clave sin que un supervisor comercial lo convalide deteniendo el siniestro a tiempo.", "Que genere demasiadas imágenes publicitarias de gatitos por aburrimiento", "No existe margen de error al ser inteligencias ultra superiores inquebrantables libres de alucinación"], c: 1 }, { q: "¿Gracias a qué particularidad se hizo tan popular internacionalmente n8n para la orquestación masiva y compleja de agentes desde comienzos y mediados del presente año?", o: ["Su costo puramente nulo en servidores Amazon de alta gama", "Su inmensurable expansión en capacidad de manejo nativo agéntico modular por bloques con la introducción universalizada de MCP al conectar más de mil integraciones de terceros arrastrando y soltando flujos visualmente lógicos.", "Única aplicación lúdica recomendada por programadores orientales para editar multimedia y audios.", "Sus campañas estáticas pre pagadas globalmente con IA de la década de 2010."], c: 1 }],
                classify: { cat1: "📦 Arquitectura y MCPs", cat2: "🤖 Plataformas Agénticas (2025)", items: [{ t: "Conexiones JSON / Manifiestos", c: 1 }, { t: "Manus AI (App Generators)", c: 2 }, { t: "Problema M x N Integrations", c: 1 }, { t: "Kimi 2.5 (Slides Generator)", c: 2 }, { t: "Claude Windows Connector", c: 1 }, { t: "Genspark (Mail Operator)", c: 2 }, { t: "Google Workspace Extension", c: 1 }, { t: "Minimax (Data Analytics)", c: 2 }] },
                hangman: [{ w: "ANTHROPIC", h: "La importante y selecta empresa multinacional IA encargada de incubar y patentar de libre difusión el MCP estandarizado" }, { w: "AGENTE", h: "Modelo que transiciona de simple 'Chatbot' a poseer herramientas actuando como un ejecutor autónomo integral empresarial" }, { w: "MANUS", h: "Aplicación y ecosistema demostrativo capaz de renderizar al momento de ser peticionado software de App Interactiva y calculadoras gráficas" }, { w: "KIMI", h: "Se demostró que procesa archivos académicos a la perfección en la presentación formal y es idóneo para transformar enormes informes en PPTs directas" }, { w: "MINIMAX", h: "Alcanza asombrosamente límites investigativos fabricando código estricto en Python subyacente para desplegar resultados gráficos validados" }, { w: "WORKSPACES", h: "Nube de la corporación Google cuya habilitación da pase directo a sus calendarios, gmail y nubes permitiendo conexión de Gemini con su propio MCP nativo y preinstalado" }, { w: "CLIENTE", h: "En arquitecturas universales MCP, aquél modelo interno que emite la orden y pide accesos en conjunción directa gestionando la conexión total." }],
                simResponses: { "mcp": "El <strong>MCP (Model Context Protocol)</strong> se ideó en 2024 por Anthropic para conectar modelos de lenguaje como GPT o Claude con APIs y softwares locales y globales a través de un simple JSON Universal eliminando las integraciones custom M x N interminables, haciéndola el estándar y puerto 'USB-C de las IAs'.", "agente": "A diferencia radical de un simple modelo de lenguaje (Chat), el bautizado <strong>Agente IA Autorregulado y Dirigente</strong> incorpora el 'MCP' en su mente. Dispone de vías para razonar al estar conectado orgánicamente a CRMs de empresa, pudiendo emitir acciones resolutorias in-site como abrir, enviar o archivar registros ajenos independientemente.", "kimi": "<strong>Kimi</strong> es destacado por nuestra cátedra como un ecosistema agéntico formidable focalizado para generar formatos. Destaca inmensamente al transformar papers aburridos corporativos (hasta con 500k de Token largo) en reportes dinámicos de Slide Deck y con estilos serios o visuales en un parpadeo, derrocando los escasos tokens pasados.", "genspark": "Al adosarle tus MCP de correo, notas y disco en internet, <strong>Genspark</strong> cruza líneas y no solo recita sobre los correos. Puede explorar tu bandeja en vivo, leer tus PDFs de adjuntos complejos sin extraviarse y hasta ser tu mensajero diligente redactando correos con un clic delegativo de reenvío por ti en piloto semiautomático.", "manus": "Existen agentes y Agentes Devs puros. <strong>Manus AI</strong> no te va a narrar cuánto subió Nvidia, sino que va a programar un frontend de calculadoras al momento y abrir la App web temporal demostrativa dotada de selectores gráficos interactuando local y sin tocar código subyacente adyacente tú mismo.", "minimax": "Para economistas o matemáticos del mercado actual, usar el agente <strong>Minimax</strong> revoluciona el análisis. Frente a un problema inmenso o bases de datos brutas él autoprogramará iterativamente un backend simulado para autoevaluar con Pandas o librerías de Python e imprimir gráficos impecables demostrables dentro de la consulta particular en sus Labs de Códice ('Files').", "default": "En torno a la Unidad Múltiple 6 puedo evacuar todas tus interrogantes acerca del nuevo paradigma agéntico del Q2 2025. Pregúntame sobre el MCP (El nuevo USB para IA) o detallados alcances de manus, kimi, genspark y minimáx superando cualquier chatbot tradicional y sus limitantes en seguridad." }
            },
"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"
with codecs.open(file_path, "r", "utf-8") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if 4780 <= i <= 4947:  # 0-indexed. Unit 6 begins around line 4781
        if i == 4780:
            new_lines.append(replacement)
        pass # replace them
    else:
        new_lines.append(line)

with codecs.open(file_path, "w", "utf-8") as f:
    f.writelines(new_lines)

print("Update completed successfully for Unit 6.")
