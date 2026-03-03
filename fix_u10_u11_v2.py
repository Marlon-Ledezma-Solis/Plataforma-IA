# -*- coding: utf-8 -*-
import codecs
import re

from gen_u11_mega import html_u11_plan, html_u11_summary_mega_designed

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    txt = f.read()

# Normalize line endings to avoid split point missing
txt = txt.replace("\r\n", "\n")

# 1. Eliminar el alert bloqueador de JS
txt = txt.replace("alert('Esta unidad aún no está disponible.');", "console.log('Unidad desbloqueada superior');")

# 2. Reconstruir la división lógica
split_point = "            </div>`,\n                videos: `<p style=\"font-size:13px;color:var(--gr);margin-bottom:20px\">Selección de videos sobre integración de IA avanzada en flujos de automatización.</p>"

replacement_point = f"""            </div>`,
            }},
            11: {{
                pres: "https://docs.google.com/presentation/d/15D4uwKuz-prDefHPPQNot_yB4BNGJpRU1_aAGBubtAw/embed",
                title: "Unidad 11: Incorporación de IA en la programación de automatizaciones",
                subtitle: "Minería, análisis de datos y cálculos asistidos por IA",
                breadcrumb: "Módulo 3 <span>›</span> Automatización",
                plan: {html_u11_plan},
                summary: `{html_u11_summary_mega_designed}`,
                videos: `<p style="font-size:13px;color:var(--gr);margin-bottom:20px\">Selección de videos sobre integración de IA avanzada en flujos de automatización.</p>"""

if split_point in txt:
    txt = txt.replace(split_point, replacement_point)
    print("Inyección U11 y separación U10 completada con éxito real.")
else:
    print("ERROR FATAL: El split point no coincide en la sintaxis exacta del archivo.")

# Save back to file explicitly with standard \n (or whatever codecs handles)
with codecs.open(file_path, "w", "utf-8") as f:
    f.write(txt)
