# -*- coding: utf-8 -*-
import codecs
import re

html_u6_plan_concise = """ {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Comprender la evolución hacia ecosistemas de agentes autónomos.", "Dominar el protocolo MCP (Model Context Protocol).", "Implementar integraciones MCP en plataformas analíticas.", "Operar sistemas de plataformas agénticas especializadas."] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Implementación segura de conexiones MCP en Workspace.", "Orquestación de tareas logísticas asíncronas complejas.", "Evaluación crítica del 'Vendor Lock-in'.", "Contrarrestar alucinaciones sistémicas en agentes altamente autónomos."] },
                        { icon: "⏱️", title: "Tiempo Estimado", items: ["Sesiones magistrales: 12 horas", "Trabajo asincrónico: 3 horas", "Práctica en Labs MCP: 5 horas", "Dedicación total estimada: 20 horas."] },
                        { icon: "📚", title: "Ubicación Curricular", items: ["Módulo 2: Herramientas IA.", "Corresponde a la Unidad 6 del programa.", "Prerequisito: Unidad 5.", "Posterior: Unidad 7."] },
                        { icon: "📝", title: "Resumen de Contenidos", items: ["Historia de LLMs al ecosistema MCP.", "Arquitectura MCP y JSON-RPC.", "Plataformas: Kimi 2.5 y Genspark.", "Constructores: Manus AI.", "Investigadores: Minimax."] },
                        { icon: "✅", title: "Sistema de Evaluación", items: ["Configuración de entorno MCP: 30%", "Revisión de Aplicativos web con Manus AI: 30%", "Entregable final con Kimi 2.5: 20%", "Encuestas y Quiz: 20%"] }
                    ]
                }"""

html_u7_plan_concise = """ {
                    grid: [
                        { icon: "🎯", title: "Objetivos de Aprendizaje", items: ["Diferenciar el Vibe Coding de la Ingeniería de Especificación.", "Utilizar Google AI Studio y el ecosistema Vertex AI.", "Dominar los controles paramétricos de Gemini (Top-P, Top-K).", "Comprender el 'Review-Driven Development Framework'.", "Implementar protocolos de 'Human-In-The-Loop'."] },
                        { icon: "💡", title: "Competencias a Desarrollar", items: ["Diseño modular de Prompts estructurados.", "Configuración de arquitectura en plataformas IDE Agent-First.", "Evaluación y auditoría de Diffs de código generado.", "Control estricto de comandos destructivos en Terminal Proxy."] },
                        { icon: "⏱️", title: "Tiempo Estimado", items: ["Sesiones sincrónicas: 8 horas", "Prácticas de despliegue: 2 a 3 horas", "Code Execution en AI Studio: 3 horas", "Dedicación semanal total: 13 horas."] },
                        { icon: "📚", title: "Ubicación Curricular", items: ["Bloque general del Módulo 2.", "Unidad 7: Nivel Superior de especialidad Técnico.", "Prerequisito: Unidad 6.", "Siguiente estación: Unidad 8 (Proyecto Integrador)."] },
                        { icon: "📝", title: "Resumen de Contenidos", items: ["Paradigma Vibe Coding y sus limitaciones.", "La Triada de AI Studio: Freeform, Structured, Code Execution.", "Gemini 1.5 Pro vs Gemini Flash en contexto de razonamiento.", "Manejo de IDE Agent-First (Antigravity, Cursor AI).", "Redacción del Prompt Maestro Estructural."] },
                        { icon: "✅", title: "Sistema Integral Evaluativo", items: ["Prácticas de Code Execution en AI Studio: 30%", "Orquestación en IDE local y aprobación de Diffs: 40%", "Planificación con Artifacts: 15%", "Pruebas Formativas (Quizzes y Trivias): 15%"] }
                    ]
                }"""

file_path = "c:\\Users\\Marlon\\Documents\\Centro de trabajo Cedecc\\Plataforma IA\\plataforma-ia-corregida-final.html"

with codecs.open(file_path, "r", "utf-8") as f:
    content = f.read()

# Replace U6 plan
content = re.sub(
    r'(6:\s*\{[\s\S]*?breadcrumb[\s\S]*?plan:\s*)\{[\s\S]*?\}(\s*,\s*summary:\s*`)',
    lambda m: f"{m.group(1)}{html_u6_plan_concise}{m.group(2)}",
    content,
    flags=re.DOTALL
)

# Replace U7 plan
content = re.sub(
    r'(7:\s*\{[\s\S]*?breadcrumb[\s\S]*?plan:\s*)\{[\s\S]*?\}(\s*,\s*summary:\s*`)',
    lambda m: f"{m.group(1)}{html_u7_plan_concise}{m.group(2)}",
    content,
    flags=re.DOTALL
)

with codecs.open(file_path, "w", "utf-8") as f:
    f.write(content)

print("U6 and U7 plans replaced with concise versions while preserving prefixes.")
