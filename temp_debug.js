const fs = require('fs');
let txt = fs.readFileSync('plataforma-ia-corregida-final.html', 'utf-8');
txt = txt.replace(/alert\('Esta unidad aún no está disponible.'\);/g, `console.log('Unidad desbloqueada superior');`);

const splitPoint = `            </div>\`,
                videos: \`<p style=\"font-size:13px;color:var(--gr);margin-bottom:20px\">Selección de videos sobre integración de IA avanzada en flujos de automatización.</p>
            <h4 class=\"tool-category\">🧠 IA y Pipelines de Datos</h4>\`

const pyContent = fs.readFileSync('gen_u11_mega.py', 'utf-8');
const planMatch = pyContent.match(/html_u11_plan = """([\s\S]*?)"""/);
const sumMatch = pyContent.match(/html_u11_summary_mega_designed = """([\s\S]*?)"""/);

const replacement = `            </div>\`,
            },
            11: {
                pres: "https://docs.google.com/presentation/d/15D4uwKuz-prDefHPPQNot_yB4BNGJpRU1_aAGBubtAw/embed",
                title: "Unidad 11: Incorporación de IA en la programación de automatizaciones",
                subtitle: "Minería, análisis de datos y cálculos asistidos por IA",
                breadcrumb: "Módulo 3 <span>›</span> Automatización",
                plan: ${planMatch[1]},
                summary: \`${sumMatch[1]}\`,
                videos: \`<p style=\"font-size:13px;color:var(--gr);margin-bottom:20px\">Selección de videos sobre integración de IA avanzada en flujos de automatización.</p>
            <h4 class=\"tool-category\">🧠 IA y Pipelines de Datos</h4>`;

// Try both \n and \r\n
const s1 = splitPoint;
const s2 = splitPoint.replace(/\n/g, '\r\n');

if (txt.includes(s1)) {
    txt = txt.replace(s1, replacement);
    fs.writeFileSync('plataforma-ia-corregida-final.html', txt);
    console.log('Replaced successfully');
} else if (txt.includes(s2)) {
    txt = txt.replace(s2, replacement.replace(/\n/g, '\r\n'));
    fs.writeFileSync('plataforma-ia-corregida-final.html', txt);
    console.log('Replaced successfully with CRLF');
} else {
    console.log('Split point not found!');
}