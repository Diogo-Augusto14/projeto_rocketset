from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ── Output ──────────────────────────────────────────────────────────────────
OUTPUT = "guia_dados.pdf"

# ── Palette ──────────────────────────────────────────────────────────────────
GREEN      = colors.HexColor("#3ECF8E")   # Supabase green
DARK_BG    = colors.HexColor("#1C1C1C")
CODE_BG    = colors.HexColor("#1E1E2E")
CODE_FG    = colors.HexColor("#CDD6F4")
ACCENT     = colors.HexColor("#F59E0B")   # amber accent
LIGHT_GRAY = colors.HexColor("#F3F4F6")
BORDER     = colors.HexColor("#E5E7EB")
TEXT_MAIN  = colors.HexColor("#111827")
TEXT_MUTED = colors.HexColor("#6B7280")
WHITE      = colors.white

# ── Doc ──────────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2.5*cm, bottomMargin=2*cm,
)
W = A4[0] - 4*cm   # usable width

# ── Styles ───────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

sTitle = S("sTitle",
    fontName="Helvetica-Bold", fontSize=28, textColor=WHITE,
    alignment=TA_CENTER, spaceAfter=6)

sSubtitle = S("sSubtitle",
    fontName="Helvetica", fontSize=12, textColor=colors.HexColor("#A1A1AA"),
    alignment=TA_CENTER, spaceAfter=4)

sChapterNum = S("sChapterNum",
    fontName="Helvetica-Bold", fontSize=11, textColor=GREEN,
    spaceBefore=20, spaceAfter=2)

sChapter = S("sChapter",
    fontName="Helvetica-Bold", fontSize=20, textColor=TEXT_MAIN,
    spaceBefore=2, spaceAfter=8)

sSection = S("sSection",
    fontName="Helvetica-Bold", fontSize=13, textColor=TEXT_MAIN,
    spaceBefore=14, spaceAfter=4)

sSub = S("sSub",
    fontName="Helvetica-Bold", fontSize=11, textColor=colors.HexColor("#374151"),
    spaceBefore=10, spaceAfter=3)

sBody = S("sBody",
    fontName="Helvetica", fontSize=10, textColor=TEXT_MAIN,
    leading=16, alignment=TA_JUSTIFY, spaceAfter=6)

sBullet = S("sBullet",
    fontName="Helvetica", fontSize=10, textColor=TEXT_MAIN,
    leading=15, leftIndent=16, spaceAfter=3,
    bulletText="•", bulletIndent=4)

sCode = S("sCode",
    fontName="Courier", fontSize=8.5, textColor=CODE_FG,
    leading=13, leftIndent=10, rightIndent=10, spaceAfter=2)

sNote = S("sNote",
    fontName="Helvetica-Oblique", fontSize=9, textColor=colors.HexColor("#92400E"),
    leading=14, leftIndent=14, spaceAfter=4)

sCaption = S("sCaption",
    fontName="Helvetica", fontSize=8, textColor=TEXT_MUTED,
    alignment=TA_CENTER, spaceAfter=6)

sTip = S("sTip",
    fontName="Helvetica", fontSize=9.5, textColor=colors.HexColor("#065F46"),
    leading=14, leftIndent=12, spaceAfter=3)

# ── Helpers ───────────────────────────────────────────────────────────────────
def code_block(lines, lang=""):
    """Dark rounded code block."""
    content = "\n".join(lines)
    inner = Table(
        [[Paragraph(content.replace("\n", "<br/>"), sCode)]],
        colWidths=[W - 0.4*cm]
    )
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), CODE_BG),
        ("ROUNDEDCORNERS", [6]),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
    ]))
    
    if lang:
        # Aqui estava o erro de fechamento de parênteses
        label_text = Paragraph(lang, S("_l", fontName="Helvetica", fontSize=7.5, textColor=colors.HexColor("#6C7086")))
        label = Table(
            [[label_text], [inner]],
            colWidths=[W - 0.4*cm]
        )
        label.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#161622")),
            ("TOPPADDING",    (0,0), (-1,0), 5),
            ("BOTTOMPADDING", (0,0), (-1,0), 4),
            ("LEFTPADDING",   (0,0), (-1,0), 14),
            ("RIGHTPADDING",  (0,0), (-1,0), 14),
        ]))
        return label
    return inner

def section_bar(num_text, title_text):
    return [
        Paragraph(num_text, sChapterNum),
        Paragraph(title_text, sChapter),
        HRFlowable(width=W, thickness=1, color=BORDER, spaceAfter=4),
    ]

def tip_box(text):
    inner = Paragraph("💡 " + text, sTip)
    t = Table([[inner]], colWidths=[W - 0.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#ECFDF5")),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("ROUNDEDCORNERS", [4]),
        ("BOX", (0,0), (-1,-1), 1.5, colors.HexColor("#6EE7B7")),
    ]))
    return t

def warning_box(text):
    inner = Paragraph("⚠️  " + text, sNote)
    t = Table([[inner]], colWidths=[W - 0.4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#FFFBEB")),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 14),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BOX", (0,0), (-1,-1), 1.5, colors.HexColor("#FCD34D")),
    ]))
    return t

def make_table(headers, rows, col_widths=None):
    data = [[Paragraph(h, S("_th", fontName="Helvetica-Bold", fontSize=9,
                             textColor=WHITE)) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), S("_td", fontName="Helvetica", fontSize=9,
                                          textColor=TEXT_MAIN, leading=13)) for c in row])
    cw = col_widths or [W / len(headers)] * len(headers)
    t = Table(data, colWidths=cw)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  DARK_BG),
        ("BACKGROUND",    (0,1), (-1,-1), WHITE),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, LIGHT_GRAY]),
        ("GRID",          (0,0), (-1,-1), 0.5, BORDER),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
        ("ROUNDEDCORNERS",[4]),
    ]))
    return t

def spacer(h=0.3): return Spacer(1, h*cm)

# ── Cover ─────────────────────────────────────────────────────────────────────
def cover():
    # Hero banner
    hero = Table(
        [[Paragraph("Guia Completo", sTitle)],
         [Paragraph("JavaScript Moderno + Supabase", sSubtitle)],
         [Paragraph(".map() · CRUD · Auth · Tempo Real", sSubtitle)]],
        colWidths=[W]
    )
    hero.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), DARK_BG),
        ("TOPPADDING",    (0,0), (-1,-1), 28),
        ("BOTTOMPADDING", (0,0), (-1,-1), 28),
        ("LEFTPADDING",   (0,0), (-1,-1), 20),
        ("RIGHTPADDING",  (0,0), (-1,-1), 20),
        ("ROUNDEDCORNERS",[8]),
    ]))

    badge_style = S("badge", fontName="Helvetica-Bold", fontSize=9,
                    textColor=DARK_BG, alignment=TA_CENTER)
    badges = Table(
        [[Paragraph("JavaScript ES6+", badge_style),
          Paragraph("Supabase BaaS", badge_style),
          Paragraph("React Ready", badge_style),
          Paragraph("Full Stack", badge_style)]],
        colWidths=[W/4]*4
    )
    badges.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), GREEN),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
        ("RIGHTPADDING",  (0,0), (-1,-1), 4),
        ("ROUNDEDCORNERS",[4]),
    ]))

    desc = Paragraph(
        "Este guia une o poder do método <b>.map()</b> com a praticidade do "
        "<b>Supabase</b>, mostrando desde os fundamentos até padrões avançados "
        "usados em produção. Aprenda a transformar dados, integrar backends e "
        "construir aplicações modernas com JavaScript.",
        S("desc", fontName="Helvetica", fontSize=10, textColor=TEXT_MUTED,
          leading=16, alignment=TA_CENTER, spaceAfter=6))

    return [hero, spacer(0.5), badges, spacer(0.5), desc]

# ── CONTENT ───────────────────────────────────────────────────────────────────
story = []

# ─ Cover
story += cover()
story.append(PageBreak())

# ════════════════════════════════════════════════════════════════
#  PARTE 1 — .map()
# ════════════════════════════════════════════════════════════════
part_banner = Table(
    [[Paragraph("PARTE 1", S("pb", fontName="Helvetica-Bold", fontSize=10,
                              textColor=GREEN, alignment=TA_CENTER)),
      Paragraph("Dominando o .map() no JavaScript", S("pbt", fontName="Helvetica-Bold",
                fontSize=16, textColor=WHITE, alignment=TA_CENTER))]],
    colWidths=[2.5*cm, W-2.5*cm]
)
part_banner.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), DARK_BG),
    ("TOPPADDING",    (0,0), (-1,-1), 16),
    ("BOTTOMPADDING", (0,0), (-1,-1), 16),
    ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ("ROUNDEDCORNERS",[6]),
    ("LINEAFTER", (0,0), (0,-1), 1.5, GREEN),
]))
story.append(part_banner)
story.append(spacer(0.4))

# 1.1 Conceito
story += section_bar("1.1", "O Conceito Fundamental")
story.append(Paragraph(
    "O método <b>.map()</b> é uma das ferramentas mais poderosas da programação funcional "
    "no JavaScript. Ele permite iterar sobre um array e criar um <b>novo array</b> com base "
    "nas transformações aplicadas — sem jamais alterar o array original.", sBody))
story.append(spacer(0.2))
story.append(code_block([
    "const numeros = [1, 2, 3, 4];",
    "",
    "// Cria novo array com valores duplicados",
    "const duplicados = numeros.map(n => n * 2);",
    "",
    "console.log(duplicados); // [2, 4, 6, 8]",
    "console.log(numeros);    // [1, 2, 3, 4]  ← original intacto",
], "javascript"))
story.append(spacer(0.3))
story.append(tip_box(
    "Imutabilidade: .map() nunca modifica o array original. Cada chamada retorna "
    "um array completamente novo, o que torna o código mais previsível e fácil de depurar."))
story.append(spacer(0.3))

# 1.2 Anatomia
story += section_bar("1.2", "Anatomia da Função de Callback")
story.append(Paragraph(
    "A função passada ao <b>.map()</b> pode receber até três argumentos:", sBody))
story.append(Paragraph("elemento — o item atual do array.", sBullet))
story.append(Paragraph("índice — a posição do item (0, 1, 2 …).", sBullet))
story.append(Paragraph("array — o array original completo.", sBullet))
story.append(spacer(0.2))
story.append(code_block([
    "const frutas = ['maçã', 'banana', 'laranja'];",
    "",
    "const resultado = frutas.map((elemento, indice, arr) => {",
    "  return `[${indice}] ${elemento} (total: ${arr.length})`;",
    "});",
    "",
    "// ['[0] maçã (total: 3)',",
    "//  '[1] banana (total: 3)',",
    "//  '[2] laranja (total: 3)']",
], "javascript"))
story.append(spacer(0.3))

# 1.3 Casos de uso
story += section_bar("1.3", "Casos de Uso Comuns")

story.append(Paragraph("Extraindo propriedades de objetos (JSON de API)", sSub))
story.append(code_block([
    "const produtos = [",
    "  { id: 101, nome: 'Laptop', preco: 4500 },",
    "  { id: 102, nome: 'Mouse',  preco: 150  },",
    "];",
    "",
    "const soNomes  = produtos.map(p => p.nome);",
    "// ['Laptop', 'Mouse']",
    "",
    "const comDesconto = produtos.map(p => ({",
    "  ...p,",
    "  preco: p.preco * 0.9,   // 10% de desconto",
    "}));",
], "javascript"))
story.append(spacer(0.2))

story.append(Paragraph("Formatando strings", sSub))
story.append(code_block([
    "const emails = ['Ana', 'Bruno', 'Carla'];",
    "",
    "const slugs = emails.map(nome =>",
    "  nome.toLowerCase().replace(/\\s+/g, '-')",
    ");",
    "// ['ana', 'bruno', 'carla']",
], "javascript"))
story.append(spacer(0.2))

story.append(Paragraph("Encadeamento com .filter() e .reduce()", sSub))
story.append(code_block([
    "const pedidos = [",
    "  { id: 1, valor: 200, pago: true  },",
    "  { id: 2, valor: 450, pago: false },",
    "  { id: 3, valor: 100, pago: true  },",
    "];",
    "",
    "const totalPago = pedidos",
    "  .filter(p => p.pago)          // só pedidos pagos",
    "  .map(p => p.valor)            // extrai valores",
    "  .reduce((acc, v) => acc + v, 0); // soma",
    "",
    "console.log(totalPago); // 300",
], "javascript"))
story.append(spacer(0.3))

# 1.4 map vs forEach
story += section_bar("1.4", "Diferença Crucial: .map() vs .forEach()")
story.append(Paragraph(
    "Embora parecidos, os dois métodos têm propósitos distintos:", sBody))
story.append(spacer(0.2))
story.append(make_table(
    ["Método", "Retorno", "Quando usar"],
    [
        [".map()", "Novo Array", "Transformar / converter dados"],
        [".forEach()", "undefined", "Executar efeitos colaterais (log, salvar no DB, chamar API)"],
        [".filter()", "Novo Array (subset)", "Filtrar itens por condição"],
        [".reduce()", "Valor único", "Agregar / acumular valores"],
    ],
    col_widths=[2.5*cm, 3.5*cm, W-6*cm]
))
story.append(spacer(0.3))
story.append(warning_box(
    "Nunca use .map() apenas para efeitos colaterais (como console.log). "
    "Se não precisa do array retornado, prefira .forEach()."))
story.append(spacer(0.3))

# 1.5 React
story += section_bar("1.5", ".map() no React — Renderização de Listas")
story.append(Paragraph(
    "No React, o <b>.map()</b> é o padrão para renderizar listas de componentes "
    "dinamicamente a partir de dados. Cada item deve ter uma <b>prop key</b> única "
    "para que o React identifique mudanças de forma eficiente.", sBody))
story.append(spacer(0.2))
story.append(code_block([
    "function ListaProdutos({ produtos }) {",
    "  return (",
    "    <ul>",
    "      {produtos.map(produto => (",
    "        <li key={produto.id}>",
    "          <strong>{produto.nome}</strong>",
    "          <span> — R$ {produto.preco.toFixed(2)}</span>",
    "        </li>",
    "      ))}",
    "    </ul>",
    "  );",
    "}",
], "jsx"))
story.append(spacer(0.2))
story.append(tip_box(
    "Sempre use um identificador único (como id do banco) como key, nunca o "
    "índice do array — isso evita bugs de re-renderização quando a lista muda."))

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════
#  PARTE 2 — Supabase
# ════════════════════════════════════════════════════════════════
part_banner2 = Table(
    [[Paragraph("PARTE 2", S("pb2", fontName="Helvetica-Bold", fontSize=10,
                              textColor=GREEN, alignment=TA_CENTER)),
      Paragraph("Supabase com JavaScript", S("pbt2", fontName="Helvetica-Bold",
                fontSize=16, textColor=WHITE, alignment=TA_CENTER))]],
    colWidths=[2.5*cm, W-2.5*cm]
)
part_banner2.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), DARK_BG),
    ("TOPPADDING",    (0,0), (-1,-1), 16),
    ("BOTTOMPADDING", (0,0), (-1,-1), 16),
    ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ("ROUNDEDCORNERS",[6]),
    ("LINEAFTER", (0,0), (0,-1), 1.5, GREEN),
]))
story.append(part_banner2)
story.append(spacer(0.4))

story.append(Paragraph(
    "O <b>Supabase</b> é uma plataforma Backend-as-a-Service (BaaS) open-source, "
    "alternativa ao Firebase. Oferece banco de dados PostgreSQL, autenticação, "
    "armazenamento de ficheiros, funções serverless e funcionalidades em tempo real — "
    "tudo acessível via SDK JavaScript.", sBody))
story.append(spacer(0.2))

# 2.1 Instalação
story += section_bar("2.1", "Instalação e Configuração")
story.append(code_block(["npm install @supabase/supabase-js"], "bash"))
story.append(spacer(0.2))
story.append(Paragraph(
    "Obtenha a <b>URL do projeto</b> e a <b>Chave API (anon key)</b> em "
    "<i>Settings &gt; API</i> no dashboard do Supabase:", sBody))
story.append(code_block([
    "import { createClient } from '@supabase/supabase-js'",
    "",
    "const supabaseUrl = 'https://seu-projeto.supabase.co'",
    "const supabaseKey = 'sua-chave-anon-aqui'",
    "",
    "export const supabase = createClient(supabaseUrl, supabaseKey)",
], "javascript"))
story.append(spacer(0.2))
story.append(warning_box(
    "Nunca exponha sua service_role key no frontend! A anon key é segura para uso "
    "no cliente, pois o acesso é controlado pelas políticas RLS do banco."))
story.append(spacer(0.3))

# 2.2 CRUD
story += section_bar("2.2", "Operações de Banco de Dados (CRUD)")

story.append(Paragraph("CREATE — Inserir dados", sSub))
story.append(code_block([
    "const { data, error } = await supabase",
    "  .from('usuarios')",
    "  .insert([{ nome: 'Ana Silva', email: 'ana@email.com' }])",
    "  .select() // retorna o registro inserido",
    "",
    "if (error) console.error(error);",
    "else console.log('Inserido:', data);",
], "javascript"))
story.append(spacer(0.2))

story.append(Paragraph("READ — Consultar dados", sSub))
story.append(code_block([
    "// Buscar todos",
    "const { data } = await supabase.from('usuarios').select('*')",
    "",
    "// Selecionar colunas específicas",
    "const { data } = await supabase",
    "  .from('usuarios')",
    "  .select('nome, email')",
    "",
    "// Filtros encadeados",
    "const { data } = await supabase",
    "  .from('produtos')",
    "  .select('*')",
    "  .eq('categoria', 'eletronicos')",
    "  .gte('preco', 100)   // preco >= 100",
    "  .order('preco', { ascending: true })",
    "  .limit(10)",
], "javascript"))
story.append(spacer(0.2))

story.append(Paragraph("UPDATE — Atualizar dados", sSub))
story.append(code_block([
    "const { data, error } = await supabase",
    "  .from('usuarios')",
    "  .update({ nome: 'Ana Costa' })",
    "  .eq('id', 1)",
    "  .select()",
], "javascript"))
story.append(spacer(0.2))

story.append(Paragraph("DELETE — Remover dados", sSub))
story.append(code_block([
    "const { error } = await supabase",
    "  .from('usuarios')",
    "  .delete()",
    "  .eq('id', 1)",
], "javascript"))
story.append(spacer(0.3))

# 2.3 Auth
story += section_bar("2.3", "Autenticação")
story.append(code_block([
    "// Cadastro de novo usuário",
    "const { data, error } = await supabase.auth.signUp({",
    "  email: 'exemplo@email.com',",
    "  password: 'senha-segura',",
    "})",
    "",
    "// Login",
    "const { data, error } = await supabase.auth.signInWithPassword({",
    "  email: 'exemplo@email.com',",
    "  password: 'senha-segura',",
    "})",
    "",
    "// Logout",
    "await supabase.auth.signOut()",
    "",
    "// Sessão atual",
    "const { data: { user } } = await supabase.auth.getUser()",
], "javascript"))
story.append(spacer(0.2))
story.append(tip_box(
    "O Supabase também suporta login social (Google, GitHub, etc.) via OAuth — "
    "basta habilitar no dashboard em Authentication > Providers."))
story.append(spacer(0.3))

# 2.4 RLS
story += section_bar("2.4", "Row Level Security (RLS)")
story.append(Paragraph(
    "O RLS é o sistema de segurança do Supabase que controla quais linhas cada "
    "usuário pode ler ou modificar, diretamente no banco de dados.", sBody))
story.append(spacer(0.2))
story.append(code_block([
    "-- Habilitar RLS na tabela",
    "ALTER TABLE posts ENABLE ROW LEVEL SECURITY;",
    "",
    "-- Política: usuário só vê seus próprios posts",
    "CREATE POLICY 'user_posts' ON posts",
    "  FOR SELECT USING (auth.uid() = user_id);",
    "",
    "-- Política: usuário só insere posts para si mesmo",
    "CREATE POLICY 'insert_own' ON posts",
    "  FOR INSERT WITH CHECK (auth.uid() = user_id);",
], "sql"))
story.append(spacer(0.2))
story.append(warning_box(
    "Se suas consultas retornam listas vazias mesmo com dados na tabela, "
    "verifique as políticas RLS no painel do Supabase."))
story.append(spacer(0.3))

# 2.5 Realtime
story += section_bar("2.5", "Tempo Real (Realtime)")
story.append(Paragraph(
    "O Supabase permite escutar mudanças no banco em tempo real via WebSocket, "
    "ideal para chats, dashboards ao vivo e notificações.", sBody))
story.append(spacer(0.2))
story.append(code_block([
    "const channel = supabase",
    "  .channel('mudancas-posts')",
    "  .on(",
    "    'postgres_changes',",
    "    { event: '*', schema: 'public', table: 'posts' },",
    "    (payload) => {",
    "      console.log('Mudança recebida:', payload)",
    "    }",
    "  )",
    "  .subscribe()",
    "",
    "// Cancelar escuta quando componente desmonta",
    "// supabase.removeChannel(channel)",
], "javascript"))
story.append(spacer(0.3))

story.append(PageBreak())

# ════════════════════════════════════════════════════════════════
#  PARTE 3 — Combinando tudo
# ════════════════════════════════════════════════════════════════
part_banner3 = Table(
    [[Paragraph("PARTE 3", S("pb3", fontName="Helvetica-Bold", fontSize=10,
                              textColor=ACCENT, alignment=TA_CENTER)),
      Paragraph("Unindo .map() + Supabase na Prática", S("pbt3", fontName="Helvetica-Bold",
                fontSize=15, textColor=WHITE, alignment=TA_CENTER))]],
    colWidths=[2.5*cm, W-2.5*cm]
)
part_banner3.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), DARK_BG),
    ("TOPPADDING",    (0,0), (-1,-1), 16),
    ("BOTTOMPADDING", (0,0), (-1,-1), 16),
    ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ("ROUNDEDCORNERS",[6]),
    ("LINEAFTER", (0,0), (0,-1), 1.5, ACCENT),
]))
story.append(part_banner3)
story.append(spacer(0.4))

# 3.1
story += section_bar("3.1", "Buscando e Transformando Dados da API")
story.append(Paragraph(
    "O padrão mais comum no desenvolvimento moderno: buscar dados do Supabase "
    "e transformá-los com <b>.map()</b> antes de exibir.", sBody))
story.append(spacer(0.2))
story.append(code_block([
    "async function getProdutosFormatados() {",
    "  const { data, error } = await supabase",
    "    .from('produtos')",
    "    .select('id, nome, preco, estoque')",
    "    .eq('ativo', true)",
    "",
    "  if (error) throw error;",
    "",
    "  // .map() transforma cada objeto para o formato da UI",
    "  return data.map(produto => ({",
    "    id:         produto.id,",
    "    label:      produto.nome.toUpperCase(),",
    "    precoLabel: `R$ ${produto.preco.toFixed(2)}`,",
    "    disponivel: produto.estoque > 0,",
    "    badge:      produto.estoque < 5 ? '🔥 Últimas unidades' : null,",
    "  }));",
    "}",
], "javascript"))
story.append(spacer(0.3))

# 3.2
story += section_bar("3.2", "Componente React Completo")
story.append(Paragraph(
    "Exemplo de componente que combina Supabase para buscar dados e "
    "<b>.map()</b> para renderizar a lista:", sBody))
story.append(spacer(0.2))
story.append(code_block([
    "import { useEffect, useState } from 'react'",
    "import { supabase } from './supabaseClient'",
    "",
    "export function ListaProdutos() {",
    "  const [produtos, setProdutos] = useState([]);",
    "  const [loading, setLoading]   = useState(true);",
    "",
    "  useEffect(() => {",
    "    async function carregar() {",
    "      const { data } = await supabase",
    "        .from('produtos')",
    "        .select('*')",
    "        .order('nome');",
    "",
    "      setProdutos(data ?? []);",
    "      setLoading(false);",
    "    }",
    "    carregar();",
    "  }, []);",
    "",
    "  if (loading) return <p>Carregando...</p>;",
    "",
    "  return (",
    "    <ul>",
    "      {produtos.map(p => (",
    "        <li key={p.id}>",
    "          {p.nome} — R$ {p.preco.toFixed(2)}",
    "        </li>",
    "      ))}",
    "    </ul>",
    "  );",
    "}",
], "jsx"))
story.append(spacer(0.3))

# 3.3 Tabela de métodos Supabase
story += section_bar("3.3", "Referência Rápida — Métodos Supabase")
story.append(spacer(0.15))
story.append(make_table(
    ["Método", "Operação SQL", "Exemplo"],
    [
        [".select('*')", "SELECT *", "supabase.from('t').select('*')"],
        [".insert([...])", "INSERT INTO", ".insert([{col: val}])"],
        [".update({...})", "UPDATE SET", ".update({col: val}).eq('id', 1)"],
        [".delete()", "DELETE FROM", ".delete().eq('id', 1)"],
        [".eq(col, val)", "WHERE col = val", ".eq('status', 'ativo')"],
        [".gte(col, val)", "WHERE col >= val", ".gte('preco', 100)"],
        [".ilike(col, '%x%')", "ILIKE (case insensitive)", ".ilike('nome', '%ana%')"],
        [".order(col)", "ORDER BY", ".order('criado_em', {ascending: false})"],
        [".limit(n)", "LIMIT n", ".limit(20)"],
    ],
    col_widths=[3.2*cm, 3.2*cm, W-6.4*cm]
))
story.append(spacer(0.4))

# ── Final tips ────────────────────────────────────────────────────────────────
story += section_bar("3.4", "Boas Práticas — Resumo Final")

tips = [
    ("Imutabilidade com .map()",
     "Nunca modifique o array original. Use sempre o novo array retornado."),
    ("Tratamento de erros no Supabase",
     "Sempre verifique o campo error antes de usar data nas queries."),
    ("Key no React",
     "Use sempre o id único do banco como key ao renderizar listas com .map()."),
    ("RLS ligado",
     "Ative Row Level Security em todas as tabelas que contêm dados de usuários."),
    ("Variáveis de ambiente",
     "Guarde a URL e a anon key em variáveis de ambiente (.env), nunca no código."),
    (".map() encadeado",
     "Combine .filter().map() para filtrar e transformar em uma única pipeline."),
]

data_tips = [[
    Paragraph(t, S("_tt", fontName="Helvetica-Bold", fontSize=9, textColor=DARK_BG)),
    Paragraph(d, S("_td2", fontName="Helvetica", fontSize=9, textColor=TEXT_MAIN, leading=13))
] for t, d in tips]

tip_table = Table(data_tips, colWidths=[4.5*cm, W-4.5*cm])
tip_table.setStyle(TableStyle([
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [LIGHT_GRAY, WHITE]),
    ("GRID",          (0,0), (-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
    ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ("BACKGROUND",    (0,0), (0,-1), colors.HexColor("#F0FDF4")),
    ("ROUNDEDCORNERS",[4]),
]))
story.append(tip_table)
story.append(spacer(0.5))

# Footer note
footer_t = Table(
    [[Paragraph(
        "Guia Completo · JavaScript .map() + Supabase · 2025",
        S("ft", fontName="Helvetica", fontSize=8, textColor=TEXT_MUTED, alignment=TA_CENTER)
    )]],
    colWidths=[W]
)
footer_t.setStyle(TableStyle([
    ("TOPPADDING",    (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ("LINEABOVE",     (0,0), (-1,0), 0.5, BORDER),
]))
story.append(footer_t)

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print("PDF gerado:", OUTPUT)