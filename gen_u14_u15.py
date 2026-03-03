# -*- coding: utf-8 -*-
import codecs
import re

html_u14_plan = """ {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Dominar la arquitectura de Modelos de Difusión Text-to-Image.", "Aprender a estructurar el Prompt Fotográfico Maestro a nivel profesional.", "Identificar capacidades avanzadas: Upscaling, Inpainting y Outpainting."] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Ingeniería de Prompts Visuales (Sujeto + Acción + Contexto + Estilo + Parámetros).", "Restauración, edición y expansión estructural de imágenes (DALL-E, Midjourney).", "Traducción de conceptos abstractos a fotomontajes de calidad cinematográfica."] },
                        { icon: "⏱️", title: "Tiempo Estimado", items: ["Fundamentos de Difusión Latente: 3 horas", "Laboratorio de Prompt Engineering Visual: 4 horas", "Prácticas de Inpainting / Outpainting: 4 horas", "Dedicación Semanal Sugerida: 11 horas."] },
                        { icon: "📚", title: "Ubicación Curricular", items: ["Comienzo del Módulo 4: Multimedia y Contenido.", "Abre la frontera creativa audiovisual tras la sección de automatización.", "Siguiente Hito: Unidad 15 (Generación de Video)."] },
                        { icon: "📝", title: "Resumen Temático", items: ["De Text-to-Image al Diseño Asistido: Midjourney, Stable Diffusion.", "Fórmula Maestra del Prompt (Lighting, Camera, Bokeh).", "Manipulación fotográfica: Cambio de atmósfera, estilos, y reparación."] },
                        { icon: "✅", title: "Sistema de Validación", items: ["Generación de 5 Retratos Fotorrealistas (Prompt Mastery): 35%", "Restauración de fondo y sujeto (Inpainting): 35%", "Prueba Formativa Visual: 30%"] }
                    ]
                }"""

html_u14_summary = """<h3>🖼️ La Revolución del Píxel Inteligente: IA Generativa Visual</h3>
            <p>La <strong>Unidad 14</strong> inaugura el Módulo 4 adentrándose en el territorio conceptual de la "Difusión Latente". En lugar de lidiar con fotógrafos logísticos o repositorios de imágenes genéricas (Stock), la IA permite la concepción de activos visuales desde cero, guiando el <em>renderizado semántico</em> a través del lenguaje natural.</p>
            
            <div class="case"><ul>
                <li><strong>El Arte del Prompt Visual (La Ingeniería de la Visión):</strong> El núcleo operativo radica en la estructura. Desglosamos la fórmula profesional: <strong>Sujeto + Acción + Contexto + Estilo + Parámetros Técnicos</strong>. Dejamos de pedir "un perro" para exigir "un golden retriever joven corriendo en la playa al atardecer, luz volumétrica dorada, lente 50mm, f/1.8, hiperrealismo arquitectónico".</li>
                <li><strong>Capacidades Estructurales (Manejo de Fronteras):</strong> Operamos más allá de la simple generación con técnicas de bisturí gráfico. Usamos <em>Inpainting</em> para remover sombras u objetos indeseados reconstruyendo el fondo coherentemente, y el <em>Outpainting</em> para expandir el horizonte visual fotográfico más allá de sus marcos originales generados.</li>
            </ul></div>

            <h3>💡 Transformación en la Arquitectura de Medios</h3>
            <p>La inserción de agentes como <strong>Midjourney</strong>, <strong>Stable Diffusion</strong> o <strong>DALL-E 3</strong> redefine el rol del diseñador de ser un 'arrastrador de píxeles' a un 'Director Creativo' que orquesta ideas complejas, acortando tiempos logísticos de semanas a frenéticos segundos de inferencia visual.</p>
            """

html_u15_plan = """ {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Dominar la arquitectura de orquestación Text-to-Video.", "Generar presentadores virtuales (Avatares) y locuciones hiper-realistas.", "Optimizar y automatizar el embudo de edición y recorte para redes sociales."] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Creación automatizada de vídeos corporativos partiendo solo de guiones y artículos textuales.", "Aplicación de cortes dinámicos y subtitulado reactivo con reconocimiento de voz (Whisper).", "Desarrollo masivo de micropíldoras para formatos verticales (TikTok/Reels)."] },
                        { icon: "⏱️", title: "Tiempo Estimado", items: ["Modelos Text-to-Video: 3 horas", "Práctica de Avatares Sintéticos: 3 horas", "Laboratorio de Edición Inteligente (CapCut/Pictory): 5 horas", "Dedicación Semanal Sugerida: 11 horas."] },
                        { icon: "📚", title: "Ubicación Curricular", items: ["Segunda fase del Módulo 4.", "Aplica los principios gráficos de la U14 al lienzo en movimiento.", "Siguiente Hito: Unidad 16 (Análisis de Datos Avanzados)."] },
                        { icon: "📝", title: "Resumen Temático", items: ["Creación automatizada: Pictory, Sora y la nueva era viral.", "Presentadores Avatares: HeyGen y Synthesia.", "Edición Inteligente y Recortes Virales (CapCut)."] },
                        { icon: "✅", title: "Sistema de Validación", items: ["Producción de Video Corporativo Automático: 40%", "Generación Múltiple de Clips Verticales con Avatares: 40%", "Prueba Formativa Multimedia: 20%"] }
                    ]
                }"""

html_u15_summary = """<h3>🎬 Direción de Cine Sintética: Del Texto al Movimiento Fluido</h3>
            <p>La <strong>Unidad 15</strong> aborda el Santo Grial de la producción de contenido: la democratización del Video. Mediante integradores algorítmicos asincrónicos, el proceso de edición tediosa desaparece para ceder el paso a ecosistemas que infieren cortes, transiciones y melodías basados puramente en contexto narrativo.</p>

            <div class="case"><ul>
                <li><strong>El Paradigma Text-to-Video e Inteligencia de Montaje:</strong> Herramientas como <em>Pictory</em> y <em>Canva Video AI</em> logran que un artículo de blog o un documento técnico se transforme automáticamente en un guion audiovisual, buscando en repositorios de clips que coincidan semánticamente e incrustando subtítulos sincronizados.</li>
                <li><strong>El Factor Humanoide (Avatares Inteligentes):</strong> Abordamos despliegues con orquestadores hiper-realistas (ej. <em>HeyGen</em>) donde clones digitales dotados de microexpresiones biológicas precisas articulan discursos complejos en más de 40 idiomas clonando tonalidades empáticas con inmediatez.</li>
            </ul></div>

            <h3>✂️ Edición Post-Algorítmica y Recortes Virales</h3>
            <p>Se erradica el modelo manual frame a frame. Usando herramientas como <em>CapCut</em>, el estudiante aprende a depositar una hora de conferencia en la IA para que esta detecte silencios, identifique los ganchos virales analíticos y recorte silenciosamente 15 micropíldoras nativas para TikTok o Reels, abaratando los costos logísticos operacionales de Community Management a cero.</p>
            """

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    txt = f.read()

# Normalize line endings
txt = txt.replace("\r\n", "\n")

# Reemplazamos partes de U14
txt = re.sub(
    r'(14:\s*\{.*?plan:\s*)\{[\s\S]*?\}(\s*,\s*summary:\s*)`[\s\S]*?`',
    lambda m: f"{m.group(1)}{html_u14_plan}{m.group(2)}`{html_u14_summary}`",
    txt,
    flags=re.DOTALL
)

# Reemplazamos partes de U15
txt = re.sub(
    r'(15:\s*\{.*?plan:\s*)\{[\s\S]*?\}(\s*,\s*summary:\s*)`[\s\S]*?`',
    lambda m: f"{m.group(1)}{html_u15_plan}{m.group(2)}`{html_u15_summary}`",
    txt,
    flags=re.DOTALL
)

# Save back to file
with codecs.open(file_path, "w", "utf-8") as f:
    f.write(txt)

print("Inyección U14 y U15 completada con éxito manteniéndolas concisas y con el diseño CSS aplicado.")
