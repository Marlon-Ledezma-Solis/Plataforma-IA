# -*- coding: utf-8 -*-
"""
descargar_transcripciones.py
============================
Script para descargar transcripciones VTT de YouTube con medidas anti-bloqueo:
  - Pausa aleatoria entre descargas (15-35 seg)
  - Pausa larga adicional cada N videos
  - Usa cookies del navegador Chrome/Edge para autenticacion
  - Timeout configurable
  - Salta automaticamente lo que ya fue descargado

Requisitos:  pip install yt-dlp
Uso:         python -u descargar_transcripciones.py
"""

import subprocess
import sys
import os
import re
import glob
import time
import shutil
import random

# ─────────────────────────────────────────────────────────────────
# CONFIGURACION ANTI-BLOQUEO
# ─────────────────────────────────────────────────────────────────
BASE_DIR             = os.path.dirname(os.path.abspath(__file__))
PAUSA_MIN            = 15    # segundos minimos entre videos
PAUSA_MAX            = 35    # segundos maximos entre videos
PAUSA_LARGA_CADA     = 5    # hacer pausa larga cada N videos procesados
PAUSA_LARGA_SEG      = 90   # segundos de la pausa larga
TIMEOUT_CMD          = 90   # timeout maximo por comando (segundos)

# ─────────────────────────────────────────────────────────────────
# LISTA DE VIDEOS FALTANTES
# NOTA: Los nombres de carpeta y de titulo deben coincidir EXACTAMENTE
#       con las carpetas existentes en disco.
# ─────────────────────────────────────────────────────────────────
VIDEOS = [
    # ── UNIDAD 7 ──────────────────────────────
    (
        "Unidad 7 Uso de la plataforma de Google IA Studio",
        "Vibe Coding e Ingenieria",
        "https://www.youtube.com/watch?v=LTm8FgcNHJc",
    ),
    (
        "Unidad 7 Uso de la plataforma de Google IA Studio",
        "Uso de Google AI Studio",
        "https://www.youtube.com/watch?v=txTSUu4mcfM",
    ),
    (
        "Unidad 7 Uso de la plataforma de Google IA Studio",
        "IDE Agent-First",
        "https://www.youtube.com/watch?v=ZwAExZYwDJ4",
    ),
    # ── UNIDAD 9 ──────────────────────────────
    (
        "Unidad 9 Uso de Python para automatizaci\u00f3n y optimizaci\u00f3n de procesos",
        "Programacion basica Python",
        "https://www.youtube.com/watch?v=ZAGuwlGQk1g",
    ),
    (
        "Unidad 9 Uso de Python para automatizaci\u00f3n y optimizaci\u00f3n de procesos",
        "Carpinteria para Mineria de Datos",
        "https://www.youtube.com/watch?v=f17iFNUQ5DE",
    ),
    (
        "Unidad 9 Uso de Python para automatizaci\u00f3n y optimizaci\u00f3n de procesos",
        "Carpinteria para Analisis de Ventas",
        "https://www.youtube.com/watch?v=dD0i2ijQwhY",
    ),
    (
        "Unidad 9 Uso de Python para automatizaci\u00f3n y optimizaci\u00f3n de procesos",
        "Automatizacion de Procesamiento de Archivos",
        "https://www.youtube.com/watch?v=vJw1t_jmE_I",
    ),
    # ── UNIDAD 11 ─────────────────────────────
    (
        "Unidad 11 Incorporaci\u00f3n de IA en la programaci\u00f3n de automatizaciones",
        "Procesamiento de archivos y calculos con IA",
        "https://www.youtube.com/watch?v=FVm0OAdAfA0",
    ),
    (
        "Unidad 11 Incorporaci\u00f3n de IA en la programaci\u00f3n de automatizaciones",
        "Mineria y Analisis de Datos con IA",
        "https://www.youtube.com/watch?v=ucb3Kya-AAI",
    ),
    # ── UNIDAD 12 ─────────────────────────────
    (
        "Unidad 12 Desarrollo de agentes y automatizaciones",
        "Teoria de automatizacion de procesos con IA",
        "https://www.youtube.com/watch?v=1my9JuVjeRQ",
    ),
    (
        "Unidad 12 Desarrollo de agentes y automatizaciones",
        "Creacion de flujos de trabajo con Make",
        "https://www.youtube.com/watch?v=u6wAiwFnNiM",
    ),
    (
        "Unidad 12 Desarrollo de agentes y automatizaciones",
        "Creacion de chatbots con n8n",
        "https://www.youtube.com/watch?v=3xf899ycLvs",
    ),
    # ── UNIDAD 14 ─────────────────────────────
    (
        "Unidad 14 Automatizaci\u00f3n y reconocimiento de im\u00e1genes",
        "Reconocimiento de Imagenes",
        "https://www.youtube.com/watch?v=hE8iD1eVyB0",
    ),
    (
        "Unidad 14 Automatizaci\u00f3n y reconocimiento de im\u00e1genes",
        "La Ingenieria del Prompt",
        "https://www.youtube.com/watch?v=vWzsZ3hlLTk",
    ),
    (
        "Unidad 14 Automatizaci\u00f3n y reconocimiento de im\u00e1genes",
        "Herramientas del Ecosistema",
        "https://www.youtube.com/watch?v=q6dAq5Z12pU",
    ),
    (
        "Unidad 14 Automatizaci\u00f3n y reconocimiento de im\u00e1genes",
        "Casos Practicos de Automatizacion",
        "https://www.youtube.com/watch?v=CbtIkOkAq-8",
    ),
    # ── UNIDAD 15 ─────────────────────────────
    (
        "Unidad 15 Automatizaci\u00f3n de contenido de videos con IA",
        "Automatizacion de Video con IA",
        "https://www.youtube.com/watch?v=QLqzuMUnvWE",
    ),
    (
        "Unidad 15 Automatizaci\u00f3n de contenido de videos con IA",
        "Herramientas de IA para Video",
        "https://www.youtube.com/watch?v=NaoN4-J6XJM",
    ),
    (
        "Unidad 15 Automatizaci\u00f3n de contenido de videos con IA",
        "Caso Practico - Edicion y Video",
        "https://www.youtube.com/watch?v=HpvZCCHxECw",
    ),
    # ── UNIDAD 19 (agregar link cuando este disponible) ───────────
    # (
    #     "Unidad 19 Generaci\u00f3n de un proyecto aplicado",
    #     "Titulo del video",
    #     "https://www.youtube.com/watch?v=XXXX",
    # ),
]


# ─────────────────────────────────────────────────────────────────
# FUNCIONES
# ─────────────────────────────────────────────────────────────────

def limpiar_vtt(contenido):
    """Convierte texto VTT a texto plano legible sin timestamps ni duplicados."""
    contenido = re.sub(r"WEBVTT.*?\n", "", contenido)
    contenido = re.sub(
        r"\d{1,2}:\d{2}:\d{2}[.,]\d{3}\s*-->\s*\d{1,2}:\d{2}:\d{2}[.,]\d{3}[^\n]*\n",
        "", contenido,
    )
    contenido = re.sub(r"^\d+\s*$", "", contenido, flags=re.MULTILINE)
    contenido = re.sub(r"<[^>]+>", "", contenido)
    contenido = re.sub(r"(align|position|line|size):[^\n]+", "", contenido)

    # Eliminar lineas duplicadas consecutivas
    lineas, resultado, anterior = contenido.splitlines(), [], ""
    for linea in lineas:
        limpia = linea.strip()
        if limpia and limpia != anterior:
            resultado.append(limpia)
            anterior = limpia
        elif not limpia and anterior != "":
            resultado.append("")
            anterior = ""

    return "\n".join(resultado).strip()


def buscar_cookies():
    """Detecta si hay un navegador disponible para extraer cookies."""
    for navegador in ["chrome", "edge", "firefox", "brave"]:
        try:
            result = subprocess.run(
                ["yt-dlp", "--cookies-from-browser", navegador,
                 "--skip-download", "--no-playlist",
                 "https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
                capture_output=True, text=True, timeout=15,
            )
            if "ERROR" not in result.stderr or "unavailable" in result.stderr.lower():
                return navegador
        except Exception:
            continue
    return None


def descargar_un_video(carpeta_rel, titulo, url, browser=None):
    """
    Descarga subtitulos de YouTube para un video.
    Retorna: 'ok', 'saltado', 'sin_subs', 'error'
    """
    carpeta_abs   = os.path.join(BASE_DIR, carpeta_rel)
    archivo_final = os.path.join(carpeta_abs, f"transcripcion_{titulo}.txt")

    # Saltar si ya existe
    if os.path.exists(archivo_final):
        return "saltado"

    # Verificar que la carpeta destino exista
    if not os.path.isdir(carpeta_abs):
        print(f"    [AVISO] Carpeta no encontrada: {carpeta_rel}")
        print(f"            Buscando carpeta similar...")
        # Buscar carpeta que empiece igual (por si hay diferencias de encoding)
        partes = carpeta_rel.split(" ")
        num_unidad = partes[1] if len(partes) > 1 else ""
        for d in os.listdir(BASE_DIR):
            if os.path.isdir(os.path.join(BASE_DIR, d)):
                d_partes = d.split(" ")
                if len(d_partes) > 1 and d_partes[1] == num_unidad:
                    carpeta_abs = os.path.join(BASE_DIR, d)
                    archivo_final = os.path.join(carpeta_abs, f"transcripcion_{titulo}.txt")
                    print(f"            Usando: {d}")
                    break
        else:
            print(f"    [ERROR] No se encontro carpeta para Unidad {num_unidad}")
            return "error"

        # Verificar de nuevo si ya existe tras encontrar la carpeta
        if os.path.exists(archivo_final):
            return "saltado"

    tmp_dir = os.path.join(BASE_DIR, "_tmp_dl")
    os.makedirs(tmp_dir, exist_ok=True)

    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", "es,es-419,en",
        "--convert-subs", "vtt",
        "--output", os.path.join(tmp_dir, "%(id)s.%(ext)s"),
        "--no-playlist",
        "--socket-timeout", "20",
        "--sleep-interval", "3",      # pausa interna entre requests de yt-dlp
        "--max-sleep-interval", "8",
        "--add-header", "Accept-Language:es-ES,es;q=0.9",
    ]

    if browser:
        cmd += ["--cookies-from-browser", browser]

    cmd.append(url)

    try:
        resultado = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=TIMEOUT_CMD,
        )
        salida = resultado.stdout + resultado.stderr

        if "Video unavailable" in salida or "not available" in salida.lower():
            return "sin_subs"

        # Buscar VTT descargado
        vtts = glob.glob(os.path.join(tmp_dir, "*.vtt"))
        if not vtts:
            return "sin_subs"

        # Preferir español > ingles
        elegido = next(
            (f for ext in [".es.", ".es-419.", ".en."]
             for f in vtts if ext in os.path.basename(f)),
            vtts[0],
        )

        with open(elegido, "r", encoding="utf-8", errors="replace") as f:
            texto = limpiar_vtt(f.read())

        with open(archivo_final, "w", encoding="utf-8") as f:
            f.write(texto)

        return "ok"

    except subprocess.TimeoutExpired:
        return "error"
    except Exception as e:
        print(f"    [EXCEPCION] {e}")
        return "error"
    finally:
        for f in glob.glob(os.path.join(tmp_dir, "*.vtt")):
            try: os.remove(f)
            except: pass


# ─────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────

def main():
    print("=" * 62)
    print("  DESCARGADOR DE TRANSCRIPCIONES - PLATAFORMA IA CEDECC")
    print("=" * 62)

    # Detectar navegador para cookies
    print("\n[*] Buscando navegador para cookies de YouTube...")
    sys.stdout.flush()
    browser = None
    for nav in ["chrome", "edge", "brave", "firefox"]:
        path_nav = shutil.which(nav)
        if path_nav:
            browser = nav
            print(f"    Navegador detectado: {nav}")
            break
    if not browser:
        print("    Sin navegador detectado — se usara modo anonimo")
    sys.stdout.flush()

    total    = len(VIDEOS)
    ok_list  = []
    skip_list, noSub_list, err_list = [], [], []
    procesados = 0

    print(f"\n[*] Total de videos en la lista: {total}")
    print(f"[*] Pausa entre descargas: {PAUSA_MIN}-{PAUSA_MAX} seg")
    print(f"[*] Pausa larga cada {PAUSA_LARGA_CADA} videos: {PAUSA_LARGA_SEG} seg")
    print()
    sys.stdout.flush()

    unidad_actual = ""
    for idx, (carpeta, titulo, url) in enumerate(VIDEOS, 1):
        # Separador de unidad
        if carpeta != unidad_actual:
            unidad_actual = carpeta
            partes = carpeta.split(" ")
            print(f"\n{'='*62}")
            print(f"  {partes[0]} {partes[1]}: {' '.join(partes[2:])}")
            print(f"{'='*62}")

        print(f"\n  [{idx}/{total}] {titulo}")
        print(f"          {url}")
        sys.stdout.flush()

        estado = descargar_un_video(carpeta, titulo, url, browser)
        procesados += 1

        if estado == "ok":
            print(f"          --> [GUARDADO]")
            ok_list.append(titulo)
        elif estado == "saltado":
            print(f"          --> [YA EXISTE - se salto]")
            skip_list.append(titulo)
        elif estado == "sin_subs":
            print(f"          --> [SIN SUBTITULOS - video sin captions]")
            noSub_list.append((titulo, url))
        else:
            print(f"          --> [ERROR]")
            err_list.append((titulo, url))

        sys.stdout.flush()

        # Pausa entre videos (excepto si fue saltado o es el ultimo)
        if estado != "saltado" and idx < total:
            # Pausa larga cada N videos procesados
            if procesados % PAUSA_LARGA_CADA == 0:
                print(f"\n  [PAUSA LARGA] Esperando {PAUSA_LARGA_SEG}s para evitar bloqueos...")
                sys.stdout.flush()
                time.sleep(PAUSA_LARGA_SEG)
            else:
                pausa = random.randint(PAUSA_MIN, PAUSA_MAX)
                print(f"  [pausa] {pausa}s antes del siguiente video...")
                sys.stdout.flush()
                time.sleep(pausa)

    # Limpiar temporal
    tmp_dir = os.path.join(BASE_DIR, "_tmp_dl")
    if os.path.exists(tmp_dir):
        try: shutil.rmtree(tmp_dir)
        except: pass

    # Resumen
    print(f"\n{'='*62}")
    print("  RESULTADO FINAL")
    print(f"{'='*62}")
    print(f"  Guardados exitosamente : {len(ok_list)}")
    print(f"  Ya existian (saltados) : {len(skip_list)}")
    print(f"  Sin subtitulos         : {len(noSub_list)}")
    print(f"  Con error              : {len(err_list)}")

    if ok_list:
        print("\n  Guardados:")
        for t in ok_list:
            print(f"    + {t}")

    if noSub_list:
        print("\n  Sin subtitulos (necesitan descarga manual o Whisper):")
        for t, u in noSub_list:
            print(f"    - {t}")
            print(f"      {u}")

    if err_list:
        print("\n  Errores (reintentar individualmente):")
        for t, u in err_list:
            print(f"    ! {t}")
            print(f"      {u}")

    print(f"\n{'='*62}")
    print("  PROCESO COMPLETADO")
    print(f"{'='*62}")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
