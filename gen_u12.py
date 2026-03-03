# -*- coding: utf-8 -*-
import codecs
import re

html_u12_plan = """ {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Diseñar flujos de trabajo en plataformas Low-Code (Make y n8n).", "Integrar IA como nodo cognitivo en automatizaciones.", "Desarrollar Chatbots y Asistentes de soporte (ej. Telegram y Correos)."] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Arquitectura lógica de Workflows (Triggers, Filtros, Acciones).", "Estructuración de Peticiones y Respuestas (Prompt Engineering en Nodos).", "Clasificación semántica y enrutamiento automatizado de emails."] },
                        { icon: "⏱️", title: "Tiempo Estimado", items: ["Fundamentos de Workflow Visual: 3 horas", "Laboratorio Make (Asistente de Correos): 4 horas", "Laboratorio n8n (Agentes conversacionales): 4 horas", "Dedicación Semanal Sugerida: 11 horas."] },
                        { icon: "📚", title: "Ubicación Curricular", items: ["Unidad 12 del Módulo 3.", "Conecta la IA predictiva (U11) con integradores empresariales nativos.", "Siguiente Hito: Proyecto Integrador (U13)."] },
                        { icon: "📝", title: "Resumen Temático", items: ["Diferencia entre Automatización tradicional y Automatización con IA.", "Plataformas Visuales: Nodos, Triggers y Módulos de Make / n8n.", "Ejemplos Prácticos: Respuestas inteligentes, Human-in-the-loop y Webhooks."] },
                        { icon: "✅", title: "Sistema de Validación", items: ["Flujo validado de Correos en Make: 40%", "Demostración Funcional Bot n8n: 40%", "Rutas condicionales (Debugging JSON): 20%"] }
                    ]
                }"""

html_u12_summary_designed = """<h3>🕸️ Sinergia de Nodos: Automatización Intelectual con Make y n8n</h3>
            <p>La <strong>Unidad 12</strong> evoluciona nuestra perspectiva sobre el control de procesos. Pasamos del código puro (Python) a plataformas de integración visual Low-Code como <strong>Make</strong> y <strong>n8n</strong>. Aquí, la automatización tradicional (reglas fijas "Si A, entonces B") se fusiona con la <em>Inteligencia Artificial</em> para procesar ambigüedad, analizar contexto y generar respuestas dinámicas.</p>
            
            <div class="case"><ul>
                <li><strong>El Paradigma Visual (Arquitectura en Grafo):</strong> Las tareas operativas se ensamblan en un lienzo visual. Todo inicia con un <em>Trigger (Disparador)</em> omnisciente (ej. "Llega un correo nuevo"), seguido de <em>Módulos de Acción</em> o Filtros condicionales.</li>
                <li><strong>El Nodo Cognitivo (IA en el Flujo):</strong> En vez de simples comandos de copiado y pegado, introducimos a la IA (ej. OpenAI, Anthropic) como un nodo pensante capaz de resumir, extraer entidades o redactar respuestas, lidiando con el caos de la información no estructurada.</li>
            </ul></div>

            <h3>🤖 Casos Empresariales y Agentes Conversacionales</h3>
            <p>El poder de estas herramientas reside en su aplicabilidad diaria en ecosistemas de negocios. Desde asistentes simples de clasificación hasta chatbots con memoria persistente.</p>
            
            <div class="example"><ul>
                <li><strong>Soporte Inteligente de Correos (Make):</strong> El Trigger lee los correos entrantes. Un nodo IA analiza el sentimiento (Queja, Consulta, Urgente) y enruta el hilo. Acto seguido, otro nodo redacta un borrador. Aplicando la regla <em>'Human-in-the-loop'</em>, un humano revisa el borrador antes de pulsar "Enviar".</li>
                <li><strong>Agentes Conversacionales (n8n & Telegram):</strong> Usando herramientas open-source como n8n y la API de BotFather, se crea un asistente interactivo que conversa con los clientes. Para evitar la amnesia tras cada mensaje, se ensambla un nodo de <em>Memoria de Sesión</em>, dotando al robot de contexto real en pláticas prolongadas.</li>
            </ul></div>
            
            <div class="bib"><h3>💼 Elevación del Perfil Tecnológico</h3>
            <p>El dominio de Make y n8n catapulta al egresado desde un ejecutor de reportes hasta un <strong>Arquitecto de Sistemas Conectados</strong>. Saber diseñar esquemas multi-ruta y blindarlos frente a errores (Manejo de rutas de error / Fallbacks API), te convierte en una pieza fundamental para reducir cuellos de botella y modernizar exponencialmente las operaciones diarias de cualquier compañía actual.</p>
            </div>"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    txt = f.read()

# Normalize line endings
txt = txt.replace("\r\n", "\n")

# Reconstruir la división lógica para U12 similar a como lo hicimos
split_point = "                videos: `<p style=\"font-size:13px;color:var(--gr);margin-bottom:20px\">Selección de videos sobre desarrollo de agentes e integraciones visuales con IA.</p>"

replacement_point = f"""                videos: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Selección de videos sobre desarrollo de agentes e integraciones visuales con IA.</p>
            <h4 class="tool-category">⚡ n8n y Make: Automatización de Agentes</h4>`
            }},
            12: {{
                pres: "https://docs.google.com/presentation/d/1_2460QqvqVYU5XYb4bsHw7nGZxylAll-ATq69g7UE1E/embed",
                title: "Unidad 12: Desarrollo de agentes y automatizaciones",
                subtitle: "Creación de flujos de trabajo avanzados con Make e integración de agentes IA en n8n",
                breadcrumb: "Módulo 3 <span>›</span> Automatización",
                plan: {html_u12_plan},
                summary: `{html_u12_summary_designed}`,
                videos: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px">Selección de videos sobre desarrollo de agentes e integraciones visuales con IA.</p>"""

if split_point in txt:
    txt = txt.replace(split_point, replacement_point)
    print("Inyección U12 completada con éxito.")
else:
    print("ERROR FATAL: El split point no coincide en la sintaxis de U12.")

# Save back to file
with codecs.open(file_path, "w", "utf-8") as f:
    f.write(txt)
