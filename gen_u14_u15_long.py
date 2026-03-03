# -*- coding: utf-8 -*-
import codecs
import re

html_u14_summary = """<h3>🖼️ La Revolución del Píxel Inteligente: IA Generativa Visual y Modelos de Difusión</h3>
            <p>La <strong>Unidad 14</strong> inaugura el Módulo 4 adentrándose en el vasto y vanguardista territorio conceptual de la "Difusión Latente". En lugar de lidiar con fotógrafos logísticos, complicadas sesiones en estudio o repositorios de imágenes genéricas (bancos de Stock), la Inteligencia Artificial permite la concepción de activos visuales desde cero y con una precisión milimétrica, guiando el <em>renderizado semántico</em> a través del lenguaje natural escrito.</p>
            
            <div class="case"><h4>El Arte del Prompt Visual: La Ingeniería de la Visión Sintética</h4>
            <p>El núcleo operativo de herramientas como Midjourney o DALL-E radica en la estructura semántica. Desglosamos la fórmula profesional que separa a los aficionados de los directores de arte algorítmicos: <strong>Sujeto + Acción + Contexto + Estilo + Parámetros Técnicos</strong>. Dejamos de pedir simplemente "un perro" para exigir "un golden retriever joven corriendo en la playa al atardecer, luz volumétrica dorada, lente 50mm, f/1.8, hiperrealismo arquitectónico". Esta precisión léxica es la que invoca la fidelidad fotográfica de la red neuronal.</p>
            <ul>
                <li><strong>El Sujeto y su Textura:</strong> No basta con nombrar el objeto; hay que definir su materialidad (roble cepillado, cuero mate, vidrio templado) para que la IA simule la interacción física de la luz sobre él.</li>
                <li><strong>El Estilo y la Atmósfera:</strong> Desde el Fotorrealismo hasta el Cyberpunk distópico, pasando por el diseño plano corporativo o el Impresionismo pictórico. La IA bebe de la historia del arte y del diseño contemporáneo para empapar la imagen del <em>mood</em> exacto requerido por la estrategia de marketing.</li>
            </ul></div>

            <h3>💡 Manipulación Fotográfica Algorítmica: Más Allá del Marco</h3>
            <p>Operamos mucho más allá de la simple generación de un lienzo en blanco introduciendo técnicas de bisturí gráfico asistidas por redes neuronales predictivas, las cuales transforman radicalmente el flujo de post-producción tradicional:</p>

            <div class="example"><ul>
                <li><strong>Inpainting (La Goma de Borrar Inteligente):</strong> Permite seleccionar una anomalía, un objeto no deseado o una persona dentro de la fotografía, para que la IA lo elimine y reconstruya el fondo (Background) de forma matemáticamente coherente con el entorno, la perspectiva y la sombra original.</li>
                <li><strong>Outpainting (La Expansión del Horizonte):</strong> Cuando una imagen tiene el encuadre perfecto pero proporciones equivocadas, el Outpainting "alucina" con estricto rigor lo que existe más allá de los bordes reales de la foto. Si tienes un retrato cuadrado, la IA genera el resto del estudio o paisaje para convertirlo en un formato panorámico 16:9 hiperrealista.</li>
                <li><strong>Upscaling (Redimensionamiento Estructural):</strong> A diferencia de ampliar píxeles y difuminar (el escalado tradicional de Photoshop), la IA deduce y reinventa la textura faltante (poros de la piel, hebras de tela, hojas de árboles) para convertir una imagen de baja resolución en un activo de altísima definición (4K/8K) apto para impresión comercial en gran formato.</li>
            </ul></div>
            
            <div class="bib"><h3>💼 Elevación Formativa en Diseño</h3>
            <p>La inserción de agentes gráficos redefine el rol del diseñador moderno, pasando de ser un 'arrastrador de píxeles manual' a un 'Director Creativo' perenne que orquesta narrativas visuales complejas, acortando tiempos logísticos de días enteros a frenéticos segundos de inferencia visual algorítmica. Un profesional domina este ecosistema no para saltarse el diseño, sino para escalar la calidad del mismo hasta niveles astronómicos.</p>
            </div>"""

html_u15_summary = """<h3>🎬 Dirección de Cine Sintética: Del Texto al Movimiento Fluido</h3>
            <p>La <strong>Unidad 15</strong> aborda lo que para muchos analistas es el Santo Grial de la producción de contenido digital: la democratización del Video y el Motion Graphics. Históricamente bloqueado por las murallas del presupuesto en equipo de cámara, luces y software de edición de alta curva de aprendizaje (Premiere/After Effects), ahora el video se orquesta mediante integradores algorítmicos asincrónicos. El tedioso proceso de cortar y pegar fotogramas cede el paso a ecosistemas que infieren cortes, transiciones y melodías basados puramente en tu narrativa textual.</p>

            <div class="case"><h4>El Paradigma Text-to-Video y la Edición Generativa</h4>
            <p>Plataformas maduras y adaptables como <em>Pictory</em>, <em>Canva Video AI</em> o las capacidades cognitivas de <em>CapCut</em> logran hazañas que antes requerían departamentos enteros de producción:</p>
            <ul>
                <li><strong>Inferencia de Guion a Metraje:</strong> Entregas un artículo de blog corporativo o un documento técnico de Word a la IA, y esta genera automáticamente un guion estructurado en escenas. Acto continuo, busca en inmensos repositorios de clips libres de derechos para emparejar semánticamente el texto narrado con la visualización exacta en pantalla (B-Roll).</li>
                <li><strong>Subtitulado Reactivo (Whisper/Speech-to-Text):</strong> Gracias a modelos avanzados de percepción de voz, la herramienta transcribe meticulosamente el audio hablado, sincronizando subtítulos dinámicos palabra por palabra con animaciones llamativas que retienen la atención en el scroll vertical de las redes sociales.</li>
            </ul></div>

            <h3>👤 El Factor Humanoide: Avatares y Clonación Auditiva</h3>
            <p>Ya no es indispensable enfrentar el miedo a la cámara ni organizar engorrosos sets de grabación corporativos. Abordamos despliegues con orquestadores hiper-realistas (como <em>HeyGen</em> o <em>Synthesia</em>) donde clones digitales dotados de microexpresiones biológicas toman el relevo protagónico.</p>
            
            <div class="example"><ul>
                <li><strong>Presentadores Sintéticos Perfiles:</strong> Seleccionas un Avatar acorde al segmento demográfico de tu campaña publicitaria. Escribes el guion, y el sistema sintetiza en segundos un video donde el clon articula tu discurso con naturalidad facial asombrosa, respiraciones y movimiento de párpados.</li>
                <li><strong>Traducción Asíncrona Multi-Idioma:</strong> Grabar un curso modular para Latinoamérica ya no limita el mercado; la IA clona tu tonalidad vocal exacta y dobla (lip-sync impecable) tu video original a más de 40 idiomas (portugués, inglés, alemán, etc.), dándote alcance global sin salir de la oficina local.</li>
            </ul></div>

            <div class="bib"><h3>✂️ Post-Producción Algorítmica y Recortes Virales</h3>
            <p>Se erradica el modelo artesanal 'frame a frame'. Se sumerge al cursante en herramientas potentes como <em>CapCut Studio</em>, aprendiendo a depositar una hora de conferencia ininterrumpida en la bandeja de la IA. El procesador algorítmico detecta silencios muertos (para eliminarlos), localiza automáticamente los ganchos narrativos (momentos álgidos de aplausos o frases célebres) y recorta de manera silente 15 micropíldoras perfectas en formato vertical nativo para TikTok, YouTube Shorts o Instagram Reels. Esto desploma por completo los costos operacionales en cualquier agencia de Community Management y multiplica el volumen de producción diaria.</p>
            </div>"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    txt = f.read()

# Normalize line endings
txt = txt.replace("\r\n", "\n")

# Reemplazamos partes de U14 (summary) respetando lo existente
txt = re.sub(
    r'(14:\s*\{.*?plan:\s*\{.*?\}(\s*,\s*summary:\s*)`[\s\S]*?)`(\s*, videos:)',
    lambda m: f"{m.group(1)}{html_u14_summary}`{m.group(3)}",
    txt,
    flags=re.DOTALL
)

# Como el regex arriba anida muy profundo, vamos a usar un approach más simple buscando el summary por separado
# 1. Sacar el U14 summary viejo y meter el nuevo
u14_snippet_old_regex = r'(14:\s*\{[\s\S]*?summary:\s*)`[\s\S]*?`(\s*,\s*videos:\s*`)'
txt = re.sub(u14_snippet_old_regex, lambda m: f"{m.group(1)}`{html_u14_summary}`{m.group(2)}", txt)

# 2. Sacar el U15 summary viejo y meter el nuevo
u15_snippet_old_regex = r'(15:\s*\{[\s\S]*?summary:\s*)`[\s\S]*?`(\s*,\s*videos:\s*`)'
txt = re.sub(u15_snippet_old_regex, lambda m: f"{m.group(1)}`{html_u15_summary}`{m.group(2)}", txt)


with codecs.open(file_path, "w", "utf-8") as f:
    f.write(txt)

print("Inyección extensa U14 y U15 completada.")
