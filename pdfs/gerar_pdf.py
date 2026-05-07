from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import Flowable
from reportlab.lib.colors import HexColor

# ── Colors ──────────────────────────────────────────────────────────────────
DARK_BG     = HexColor('#0f172a')
ACCENT      = HexColor('#6366f1')
ACCENT2     = HexColor('#818cf8')
LIGHT_BG    = HexColor('#f1f5f9')
CODE_BG     = HexColor('#1e293b')
CODE_LINE   = HexColor('#334155')
TEXT_DARK   = HexColor('#1e293b')
TEXT_MUTED  = HexColor('#64748b')
WHITE       = colors.white
SUCCESS     = HexColor('#22c55e')
WARNING     = HexColor('#f59e0b')
ERROR       = HexColor('#ef4444')
BORDER      = HexColor('#e2e8f0')

W, H = A4


# ── Custom Flowables ─────────────────────────────────────────────────────────
class ColoredRect(Flowable):
    def __init__(self, width, height, fill_color, radius=4):
        super().__init__()
        self.width = width
        self.height = height
        self.fill_color = fill_color
        self.radius = radius

    def draw(self):
        self.canv.setFillColor(self.fill_color)
        self.canv.roundRect(0, 0, self.width, self.height, self.radius, fill=1, stroke=0)


class SectionHeader(Flowable):
    """Numbered section header with colored left bar."""
    def __init__(self, number, title, width):
        super().__init__()
        self.number = number
        self.title = title
        self.width = width
        self.height = 36

    def draw(self):
        c = self.canv
        # Accent bar
        c.setFillColor(ACCENT)
        c.rect(0, 0, 5, self.height, fill=1, stroke=0)
        # Number circle
        c.setFillColor(ACCENT)
        c.circle(22, self.height / 2, 11, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 11)
        num_str = str(self.number)
        c.drawCentredString(22, self.height / 2 - 4, num_str)
        # Title
        c.setFillColor(TEXT_DARK)
        c.setFont('Helvetica-Bold', 16)
        c.drawString(42, self.height / 2 - 6, self.title)


class NoteBox(Flowable):
    """Colored info/warning/tip box."""
    def __init__(self, text, kind='info', width=None):
        super().__init__()
        self._text = text
        self.kind = kind
        self._width = width or (W - 4*cm)
        self.height = 0   # calculated later

    def wrap(self, availWidth, availHeight):
        self._width = availWidth
        # estimate height
        lines = self._text.count('\n') + 1
        self.height = max(40, lines * 14 + 20)
        return self._width, self.height

    def draw(self):
        c = self.canv
        palette = {
            'info':    (HexColor('#eff6ff'), HexColor('#3b82f6'), '💡 Dica'),
            'warning': (HexColor('#fffbeb'), WARNING,              '⚠️  Atenção'),
            'tip':     (HexColor('#f0fdf4'), SUCCESS,              '✅ Boas Práticas'),
            'error':   (HexColor('#fef2f2'), ERROR,                '❌ Evite'),
        }
        bg, border, label = palette.get(self.kind, palette['info'])
        c.setFillColor(bg)
        c.roundRect(0, 0, self._width, self.height, 6, fill=1, stroke=0)
        c.setStrokeColor(border)
        c.setLineWidth(1.5)
        c.roundRect(0, 0, self._width, self.height, 6, fill=0, stroke=1)
        # left accent
        c.setFillColor(border)
        c.rect(0, 0, 4, self.height, fill=1, stroke=0)
        # label
        c.setFillColor(border)
        c.setFont('Helvetica-Bold', 8)
        c.drawString(12, self.height - 13, label)
        # body text
        c.setFillColor(TEXT_DARK)
        c.setFont('Helvetica', 8.5)
        lines = self._text.split('\n')
        y = self.height - 26
        for line in lines:
            c.drawString(12, y, line)
            y -= 12


# ── Styles ───────────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    def s(name, **kw):
        return ParagraphStyle(name, **kw)

    styles = {
        'body': s('body', fontName='Helvetica', fontSize=10, leading=16,
                  textColor=TEXT_DARK, alignment=TA_JUSTIFY, spaceAfter=8),
        'body_sm': s('body_sm', fontName='Helvetica', fontSize=9, leading=14,
                     textColor=TEXT_DARK, alignment=TA_LEFT, spaceAfter=6),
        'h2': s('h2', fontName='Helvetica-Bold', fontSize=13, leading=20,
                textColor=TEXT_DARK, spaceBefore=18, spaceAfter=8),
        'h3': s('h3', fontName='Helvetica-Bold', fontSize=11, leading=16,
                textColor=ACCENT, spaceBefore=12, spaceAfter=6),
        'code': s('code', fontName='Courier', fontSize=8, leading=13,
                  textColor=HexColor('#e2e8f0'), backColor=CODE_BG,
                  leftIndent=8, rightIndent=8, spaceBefore=4, spaceAfter=4),
        'code_label': s('code_label', fontName='Helvetica-Bold', fontSize=7.5,
                        textColor=ACCENT2, spaceBefore=8, spaceAfter=2),
        'bullet': s('bullet', fontName='Helvetica', fontSize=10, leading=15,
                    textColor=TEXT_DARK, leftIndent=16, bulletIndent=4,
                    spaceAfter=4),
        'caption': s('caption', fontName='Helvetica-Oblique', fontSize=8,
                     textColor=TEXT_MUTED, alignment=TA_CENTER, spaceAfter=10),
        'toc_item': s('toc_item', fontName='Helvetica', fontSize=10, leading=18,
                      textColor=TEXT_DARK, leftIndent=12),
        'toc_sub': s('toc_sub', fontName='Helvetica', fontSize=9, leading=16,
                     textColor=TEXT_MUTED, leftIndent=28),
        'cover_title': s('cover_title', fontName='Helvetica-Bold', fontSize=36,
                         textColor=WHITE, alignment=TA_CENTER, leading=44),
        'cover_sub': s('cover_sub', fontName='Helvetica', fontSize=14,
                       textColor=HexColor('#c7d2fe'), alignment=TA_CENTER, leading=20),
        'cover_meta': s('cover_meta', fontName='Helvetica', fontSize=10,
                        textColor=HexColor('#94a3b8'), alignment=TA_CENTER),
    }
    return styles


# ── Page templates ────────────────────────────────────────────────────────────
def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # Gradient strip
    for i in range(80):
        t = i / 80
        r = int(99 + (15 - 99) * t) / 255
        g = int(102 + (23 - 102) * t) / 255
        b = int(241 + (42 - 241) * t) / 255
        canvas.setFillColorRGB(r, g, b, alpha=0.7)
        canvas.rect(0, H * 0.72 - i * 3, W, 3, fill=1, stroke=0)
    # Top decorative circles
    canvas.setFillColor(HexColor('#6366f1'))
    canvas.circle(W - 60, H - 60, 80, fill=1, stroke=0)
    canvas.setFillColor(HexColor('#4f46e5'))
    canvas.circle(W - 30, H - 30, 45, fill=1, stroke=0)
    canvas.setFillColor(HexColor('#818cf8'))
    canvas.circle(60, 60, 50, fill=1, stroke=0)
    canvas.restoreState()


def normal_page(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, H - 22*mm, W, 22*mm, fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, H - 23*mm, W, 1.5, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(2*cm, H - 15*mm, 'Web Push Notifications no Next.js')
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(HexColor('#94a3b8'))
    canvas.drawRightString(W - 2*cm, H - 15*mm, doc.title or '')
    # Footer
    canvas.setFillColor(LIGHT_BG)
    canvas.rect(0, 0, W, 14*mm, fill=1, stroke=0)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, 14*mm, W - 2*cm, 14*mm)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(2*cm, 5*mm, 'Guia Completo — Next.js & Web Push API')
    canvas.drawRightString(W - 2*cm, 5*mm, f'Página {doc.page}')
    canvas.restoreState()


# ── Code block helper ─────────────────────────────────────────────────────────
def code_block(lines, label=None, styles=None):
    items = []
    if label:
        items.append(Paragraph(label, styles['code_label']))
    # wrap in a table for background
    rows = []
    for line in lines:
        safe = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        rows.append([Paragraph(safe, styles['code'])])
    t = Table(rows, colWidths=[W - 4*cm - 16])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CODE_BG),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (0, 0), 8),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 8),
        ('INNERPADING', (0, 0), (-1, -1), 2),
        ('ROUNDEDCORNERS', [6]),
    ]))
    items.append(t)
    items.append(Spacer(1, 6))
    return items


def bullet(text, st):
    return Paragraph(f'<bullet>•</bullet> {text}', st['bullet'])


# ── Build document ────────────────────────────────────────────────────────────
def build():
    path = 'WebPushNextjs.pdf'
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=3*cm, bottomMargin=2.2*cm,
        title='Guia Completo',
    )
    st = build_styles()
    story = []

    # ══════════════════════════════════════════════════════════════════════════
    # CAPA
    # ══════════════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 5*cm))
    story.append(Paragraph('Dominando Web Push', st['cover_title']))
    story.append(Paragraph('Notifications no Next.js', st['cover_title']))
    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph('Guia Completo — Arquitetura, Segurança, UX e Produção', st['cover_sub']))
    story.append(Spacer(1, 1.2*cm))

    # chips
    chips_data = [['Service Worker', 'VAPID', 'Web Push API', 'Next.js 14+', 'TypeScript']]
    chips = Table(chips_data, colWidths=[2.8*cm, 1.8*cm, 2.8*cm, 2.5*cm, 2.5*cm])
    chips.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), ACCENT),
        ('TEXTCOLOR', (0, 0), (-1, -1), WHITE),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROUNDEDCORNERS', [10]),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, WHITE),
    ]))
    story.append(chips)
    story.append(Spacer(1, 1.8*cm))
    story.append(Paragraph('2025 — Versão 2.0', st['cover_meta']))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # SUMÁRIO
    # ══════════════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 0.4*cm))
    story.append(Paragraph('<b>Sumário</b>', ParagraphStyle('toc_h', fontName='Helvetica-Bold',
                 fontSize=20, textColor=TEXT_DARK, spaceAfter=16)))
    story.append(HRFlowable(width='100%', thickness=2, color=ACCENT, spaceAfter=12))

    toc = [
        ('1', 'Introdução & Conceitos Fundamentais', [
            'O que são Push Notifications?', 'Por que usar no Next.js?', 'Suporte a navegadores']),
        ('2', 'Arquitetura Completa do Sistema', [
            'Visão geral dos componentes', 'Diagrama de fluxo', 'Protocolo Web Push']),
        ('3', 'Configuração do Ambiente', [
            'Pré-requisitos', 'Geração das chaves VAPID', 'Variáveis de ambiente']),
        ('4', 'O Service Worker (sw.js)', [
            'Registro e ciclo de vida', 'Evento push', 'Evento notificationclick', 'Estratégias de cache']),
        ('5', 'Frontend — React Client Component', [
            'Solicitando permissão', 'Gerenciando assinaturas', 'UX e estados de loading']),
        ('6', 'Backend — Server Actions', [
            'Configuração do web-push', 'Persistência em banco de dados', 'Segmentação de usuários']),
        ('7', 'Segurança & Boas Práticas', [
            'Chaves VAPID', 'TTL e expiração', 'Rate limiting']),
        ('8', 'Notificações Avançadas', [
            'Ações interativas', 'Notificações silenciosas', 'Push com imagem']),
        ('9', 'Deploy & Produção', [
            'Vercel, Railway e VPS', 'Banco de dados em produção', 'Monitoramento']),
        ('10', 'Troubleshooting', [
            'Erros comuns', 'Debugging do SW', 'Checklist final']),
    ]

    for num, title, subs in toc:
        story.append(Paragraph(f'<b>{num}.</b>  {title}', st['toc_item']))
        for sub in subs:
            story.append(Paragraph(f'↳  {sub}', st['toc_sub']))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 1
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(1, 'Introdução & Conceitos Fundamentais', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>O que são Web Push Notifications?</b>', st['h2']))
    story.append(Paragraph(
        'Web Push Notifications são mensagens enviadas por um servidor diretamente para o '
        'navegador do usuário, mesmo quando o site não está aberto. Elas utilizam o protocolo '
        '<b>Web Push Protocol (RFC 8030)</b> combinado com a API de Service Workers para '
        'entregar mensagens em tempo real de forma confiável e segura.',
        st['body']))
    story.append(Paragraph(
        'O fluxo básico envolve três partes distintas: o <b>servidor de aplicação</b> (seu backend '
        'Next.js), o <b>servidor de Push</b> (operado pelo Google, Apple ou Mozilla) e o '
        '<b>navegador do usuário</b> com seu Service Worker registrado.',
        st['body']))

    story.append(NoteBox(
        'As Web Push Notifications são suportadas em Chrome, Firefox, Edge, Safari (iOS 16.4+)\n'
        'e Opera. São baseadas em padrões abertos — não dependem de SDKs proprietários.',
        'info'))
    story.append(Spacer(1, 8))

    story.append(Paragraph('<b>Por que usar Push Notifications no Next.js?</b>', st['h2']))
    for item in [
        '<b>Reengajamento:</b> Traga usuários de volta ao site sem precisar de um app nativo.',
        '<b>Tempo real:</b> Notifique sobre eventos críticos instantaneamente (pedidos, alertas).',
        '<b>Server Actions:</b> Next.js 14+ permite disparar notificações direto de ações do servidor.',
        '<b>App Router:</b> Compatível com a nova arquitetura de componentes do Next.js.',
        '<b>PWA:</b> Combinado com um manifest.json, transforma seu site em um Progressive Web App.',
        '<b>Sem push nativo:</b> Elimina a necessidade de React Native ou Flutter para alertas simples.',
    ]:
        story.append(bullet(item, st))
    story.append(Spacer(1, 8))

    story.append(Paragraph('<b>Comparativo: Push Web vs Push Nativo</b>', st['h3']))
    comp_data = [
        ['Critério', 'Push Web', 'Push Nativo (iOS/Android)'],
        ['Instalação de app', 'Não necessária', 'Obrigatória'],
        ['Custo de infra', 'Baixo (FCM grátis)', 'Médio (APN $ + FCM)'],
        ['Permissão do usuário', 'Via browser popup', 'Via OS popup'],
        ['Suporte offline', 'Limitado', 'Completo'],
        ['Ações ricas', 'Até 2 ações', 'Múltiplas ações'],
        ['Taxa de opt-in', '~5-15%', '~40-60%'],
        ['Implementação', 'Web stack padrão', 'Código nativo / SDK'],
    ]
    comp = Table(comp_data, colWidths=[4.5*cm, 5*cm, 5.5*cm])
    comp.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(comp)
    story.append(Spacer(1, 14))

    story.append(Paragraph('<b>Suporte a Navegadores (2025)</b>', st['h3']))
    browser_data = [
        ['Navegador', 'Versão Mínima', 'Suporte Push', 'Observações'],
        ['Chrome / Chromium', '42+', '✅ Completo', 'Usa FCM (Firebase)'],
        ['Firefox', '44+', '✅ Completo', 'Usa autopush.mozilla.org'],
        ['Edge', '17+', '✅ Completo', 'Usa WNS / FCM'],
        ['Safari (macOS)', '16+', '✅ Completo', 'Requer APNS key'],
        ['Safari (iOS)', '16.4+', '✅ PWA only', 'Apenas em home screen'],
        ['Opera', '29+', '✅ Completo', 'Usa FCM'],
        ['IE / Samsung Internet', '-', '❌ Sem suporte', 'Fallback necessário'],
    ]
    bt = Table(browser_data, colWidths=[3.5*cm, 3*cm, 3*cm, 5.5*cm])
    bt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8.5),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(bt)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 2
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(2, 'Arquitetura Completa do Sistema', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Visão Geral dos Componentes</b>', st['h2']))
    story.append(Paragraph(
        'A arquitetura de Web Push Notifications no Next.js é composta por quatro camadas '
        'bem definidas que trabalham em conjunto. Entender cada camada é fundamental para '
        'implementar um sistema robusto e escalável.',
        st['body']))

    arch_data = [
        ['Camada', 'Tecnologia', 'Responsabilidade'],
        ['Service Worker', 'sw.js (navegador)', 'Receber e exibir notificações em background'],
        ['Frontend', 'React Client Component', 'Pedir permissão, gerenciar assinatura'],
        ['Backend', 'Next.js Server Actions', 'Disparar notificações via web-push'],
        ['Banco de Dados', 'PostgreSQL / MongoDB', 'Persistir assinaturas dos usuários'],
        ['Push Server', 'FCM / APNs / Mozilla', 'Rotear notificações para o navegador correto'],
    ]
    at = Table(arch_data, colWidths=[4*cm, 4.5*cm, 7*cm])
    at.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
    ]))
    story.append(at)
    story.append(Spacer(1, 14))

    story.append(Paragraph('<b>Diagrama de Fluxo Completo</b>', st['h2']))
    steps = [
        ('1', 'Registro', 'O site carrega e registra o Service Worker (sw.js) via navigator.serviceWorker.register()'),
        ('2', 'Permissão', 'O usuário clica em "Ativar notificações". O browser exibe o popup de permissão do sistema operacional.'),
        ('3', 'Assinatura', 'PushManager.subscribe() gera um objeto PushSubscription contendo endpoint único e chaves de criptografia.'),
        ('4', 'Persistência', 'O frontend envia o PushSubscription ao backend via Server Action. O backend salva no banco de dados vinculado ao usuário.'),
        ('5', 'Disparo', 'Quando um evento ocorre, o backend busca as assinaturas relevantes e chama webpush.sendNotification().'),
        ('6', 'Roteamento', 'A biblioteca web-push envia um HTTP POST para o Push Server (FCM/APNs), que roteia para o dispositivo correto.'),
        ('7', 'Recepção', 'O Service Worker acorda via evento "push", processa os dados e chama showNotification().'),
        ('8', 'Interação', 'O usuário vê a notificação. Ao clicar, o evento "notificationclick" é disparado e o site é aberto.'),
    ]
    for num, title, desc in steps:
        row_data = [[
            Paragraph(f'<b>{num}</b>', ParagraphStyle('n', fontName='Helvetica-Bold',
                      fontSize=11, textColor=WHITE, alignment=TA_CENTER)),
            Paragraph(f'<b>{title}</b>\n{desc}', ParagraphStyle('d', fontName='Helvetica',
                      fontSize=9, textColor=TEXT_DARK, leading=14))
        ]]
        rt = Table(row_data, colWidths=[1*cm, W - 4*cm - 1.4*cm])
        color = ACCENT if int(num) % 2 == 1 else ACCENT2
        rt.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), color),
            ('BACKGROUND', (1, 0), (1, 0), WHITE if int(num) % 2 == 1 else LIGHT_BG),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('LEFTPADDING', (1, 0), (1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
        ]))
        story.append(rt)
    story.append(Spacer(1, 14))

    story.append(Paragraph('<b>O Protocolo Web Push (RFC 8030)</b>', st['h2']))
    story.append(Paragraph(
        'O protocolo Web Push define como os servidores de aplicação se comunicam com os '
        'servidores de Push. Cada notificação é criptografada usando <b>ECDH (Elliptic Curve '
        'Diffie-Hellman)</b> com as chaves do objeto PushSubscription, garantindo que apenas '
        'o navegador do usuário consiga descriptografar o conteúdo.',
        st['body']))
    story.append(NoteBox(
        'A criptografia é feita em duas camadas:\n'
        '1. Content-Encoding: aes128gcm (RFC 8291) — criptografa o payload\n'
        '2. VAPID (RFC 8292) — autentica o servidor de origem\n'
        'A biblioteca web-push cuida de toda essa complexidade automaticamente.',
        'tip'))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 3
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(3, 'Configuração do Ambiente', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Pré-requisitos</b>', st['h2']))
    for item in [
        'Node.js 18.17+ (LTS recomendado)',
        'Next.js 14+ com App Router habilitado',
        'HTTPS obrigatório em produção (localhost funciona em desenvolvimento)',
        'Conta no banco de dados (PostgreSQL recomendado para produção)',
    ]:
        story.append(bullet(item, st))
    story.append(Spacer(1, 8))

    story.append(Paragraph('<b>Instalação das Dependências</b>', st['h3']))
    story += code_block([
        '# Instalar a biblioteca web-push',
        'npm install web-push',
        '',
        '# Tipos TypeScript (opcional mas recomendado)',
        'npm install -D @types/web-push',
        '',
        '# Para banco de dados (exemplo com Prisma + PostgreSQL)',
        'npm install prisma @prisma/client',
        'npx prisma init',
    ], '📦  Terminal — Instalação', st)

    story.append(Paragraph('<b>Gerando as Chaves VAPID</b>', st['h2']))
    story.append(Paragraph(
        'As chaves VAPID (Voluntary Application Server Identification) são um par de chaves '
        'criptográficas que identificam seu servidor de aplicação. Elas garantem que apenas '
        'você possa enviar notificações para seus usuários. As chaves são geradas uma única '
        'vez e reutilizadas em toda a vida do projeto.',
        st['body']))

    story += code_block([
        '# Método 1: Via CLI do web-push (recomendado)',
        'npx web-push generate-vapid-keys',
        '',
        '# Saída esperada:',
        '# Public Key:',
        '# BEl8BHjZCv5Nn4iMrGMJuNHbHRCL4Fhq5u5y...',
        '# Private Key:',
        '# Xt_jGdmh7Nm1cQbKFJEt_MsUyQYd3RHHQ...',
        '',
        '# Método 2: Via código Node.js',
        'const webpush = require("web-push");',
        'const vapidKeys = webpush.generateVAPIDKeys();',
        'console.log(vapidKeys.publicKey);',
        'console.log(vapidKeys.privateKey);',
    ], '🔑  Geração de Chaves VAPID', st)

    story.append(NoteBox(
        'NUNCA gere novas chaves VAPID em produção sem invalidar todas as assinaturas existentes!\n'
        'Ao trocar as chaves, todos os usuários precisam se re-inscrever.\n'
        'Armazene as chaves em um gerenciador de segredos (Vault, AWS Secrets Manager).',
        'warning'))
    story.append(Spacer(1, 8))

    story.append(Paragraph('<b>Configurando Variáveis de Ambiente</b>', st['h3']))
    story += code_block([
        '# .env.local',
        '',
        '# Chave pública VAPID — prefixo NEXT_PUBLIC_ pois é usada no frontend',
        'NEXT_PUBLIC_VAPID_PUBLIC_KEY=BEl8BHjZCv5Nn4iMrGMJuNH...',
        '',
        '# Chave privada VAPID — NUNCA prefixar com NEXT_PUBLIC_',
        'VAPID_PRIVATE_KEY=Xt_jGdmh7Nm1cQbKFJEt_MsUy...',
        '',
        '# Email de contato (obrigatório pelo protocolo VAPID)',
        'VAPID_EMAIL=seu-email@dominio.com',
        '',
        '# String de conexão com o banco de dados',
        'DATABASE_URL=postgresql://user:pass@host:5432/pushdb',
    ], '⚙️  .env.local — Variáveis de Ambiente', st)

    story += code_block([
        '# .gitignore — certifique-se que .env.local está ignorado',
        '.env.local',
        '.env.*.local',
        '',
        '# Verifique com:',
        'git check-ignore -v .env.local',
        '# Saída esperada: .gitignore:N  .env.local',
    ], '🔒  .gitignore — Protegendo Segredos', st)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 4
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(4, 'O Service Worker (sw.js)', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Ciclo de Vida do Service Worker</b>', st['h2']))
    story.append(Paragraph(
        'O Service Worker passa por três fases principais: <b>instalação</b> (install), '
        '<b>ativação</b> (activate) e <b>funcionamento</b> (fetch/push). '
        'Compreender esse ciclo é essencial para evitar bugs de cache e notificações duplicadas.',
        st['body']))

    story += code_block([
        '// public/sw.js — Arquivo completo do Service Worker',
        '',
        '// ── Fase 1: Instalação ──────────────────────────────────────────────',
        'self.addEventListener("install", (event) => {',
        '  console.log("[SW] Instalando...");',
        '  // skipWaiting() faz o novo SW ativar imediatamente sem esperar',
        '  // o antigo ser descarregado. Use com cuidado em produção.',
        '  self.skipWaiting();',
        '});',
        '',
        '// ── Fase 2: Ativação ────────────────────────────────────────────────',
        'self.addEventListener("activate", (event) => {',
        '  console.log("[SW] Ativado. Controlando clientes...");',
        '  // clients.claim() faz o SW assumir controle de todas as abas',
        '  // abertas imediatamente, sem precisar recarregar a página.',
        '  event.waitUntil(clients.claim());',
        '});',
    ], '📄  sw.js — Instalação e Ativação', st)

    story += code_block([
        '// ── Fase 3: Recebendo Notificações ─────────────────────────────────',
        'self.addEventListener("push", function (event) {',
        '  // Verifica se há dados no payload',
        '  if (!event.data) return;',
        '',
        '  const data = event.data.json();',
        '',
        '  const options = {',
        '    body: data.body,',
        '    icon: data.icon || "/icons/icon-192x192.png",',
        '    badge: "/icons/badge-72x72.png",',
        '    image: data.image,              // Imagem grande (banner)',
        '    vibrate: [200, 100, 200],        // Padrão de vibração',
        '    tag: data.tag || "default",      // Agrupa notifs do mesmo tipo',
        '    renotify: true,                  // Vibra mesmo com tag igual',
        '    requireInteraction: data.persist || false, // Não auto-dismiss',
        '    silent: data.silent || false,    // Sem som/vibração',
        '    timestamp: Date.now(),           // Timestamp da chegada',
        '    actions: data.actions || [],     // Botões de ação',
        '    data: {',
        '      url: data.url || "/",          // URL a abrir ao clicar',
        '      id: data.id,                   // ID para tracking',
        '    },',
        '  };',
        '',
        '  event.waitUntil(',
        '    self.registration.showNotification(data.title, options)',
        '  );',
        '});',
    ], '🔔  sw.js — Recebendo e Exibindo Notificações', st)

    story += code_block([
        '// ── Fase 4: Clique na Notificação ──────────────────────────────────',
        'self.addEventListener("notificationclick", function (event) {',
        '  event.notification.close();',
        '',
        '  const url = event.notification.data?.url || "/";',
        '  const action = event.action; // ID do botão clicado (se houver)',
        '',
        '  event.waitUntil(',
        '    clients.matchAll({ type: "window", includeUncontrolled: true })',
        '      .then((clientList) => {',
        '        // Se o site já está aberto em alguma aba, foca nela',
        '        for (const client of clientList) {',
        '          if (client.url === url && "focus" in client) {',
        '            return client.focus();',
        '          }',
        '        }',
        '        // Senão, abre uma nova aba',
        '        if (clients.openWindow) {',
        '          return clients.openWindow(url);',
        '        }',
        '      })',
        '  );',
        '});',
        '',
        '// ── Fase 5: Notificação Fechada ─────────────────────────────────────',
        'self.addEventListener("notificationclose", function (event) {',
        '  // Útil para analytics: saber que o usuário descartou a notificação',
        '  const data = event.notification.data;',
        '  console.log("[SW] Notificação fechada sem clique:", data?.id);',
        '  // Aqui você poderia enviar um beacon de analytics',
        '});',
    ], '👆  sw.js — Tratando Cliques e Fechamento', st)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 5
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(5, 'Frontend — React Client Component', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Estrutura Completa do Componente</b>', st['h2']))
    story.append(Paragraph(
        'O componente de gerenciamento de Push Notifications deve ser robusto, '
        'lidar com todos os estados possíveis (loading, erro, não suportado, inscrito, '
        'não inscrito) e fornecer uma UX clara ao usuário.',
        st['body']))

    story += code_block([
        '"use client";',
        'import { useState, useEffect, useCallback } from "react";',
        'import { subscribeUser, unsubscribeUser, sendNotification } from "@/app/actions";',
        '',
        '// Converte chave VAPID Base64URL para Uint8Array (requisito do PushManager)',
        'function urlBase64ToUint8Array(base64String: string): Uint8Array {',
        '  const padding = "=".repeat((4 - (base64String.length % 4)) % 4);',
        '  const base64 = (base64String + padding)',
        '    .replace(/-/g, "+").replace(/_/g, "/");',
        '  const rawData = window.atob(base64);',
        '  return new Uint8Array([...rawData].map((c) => c.charCodeAt(0)));',
        '}',
        '',
        'type NotificationState = "idle" | "loading" | "subscribed" |',
        '                         "unsubscribed" | "denied" | "unsupported";',
        '',
        'export default function PushNotificationManager() {',
        '  const [state, setState] = useState<NotificationState>("idle");',
        '  const [subscription, setSubscription] = useState<PushSubscription|null>(null);',
        '  const [error, setError] = useState<string | null>(null);',
        '  const [message, setMessage] = useState("");',
    ], '⚛️  components/PushNotificationManager.tsx — Parte 1', st)

    story += code_block([
        '  // Verificar suporte e assinatura existente ao montar',
        '  useEffect(() => {',
        '    const checkSupport = async () => {',
        '      if (!("serviceWorker" in navigator) || !("PushManager" in window)) {',
        '        setState("unsupported");',
        '        return;',
        '      }',
        '      if (Notification.permission === "denied") {',
        '        setState("denied");',
        '        return;',
        '      }',
        '      const reg = await navigator.serviceWorker.register("/sw.js", {',
        '        scope: "/",',
        '        updateViaCache: "none",',
        '      });',
        '      const sub = await reg.pushManager.getSubscription();',
        '      if (sub) {',
        '        setSubscription(sub);',
        '        setState("subscribed");',
        '      } else {',
        '        setState("unsubscribed");',
        '      }',
        '    };',
        '    checkSupport();',
        '  }, []);',
    ], '⚛️  components/PushNotificationManager.tsx — Parte 2 (useEffect)', st)

    story += code_block([
        '  const subscribeToPush = useCallback(async () => {',
        '    setState("loading");',
        '    setError(null);',
        '    try {',
        '      const reg = await navigator.serviceWorker.ready;',
        '      const sub = await reg.pushManager.subscribe({',
        '        userVisibleOnly: true,',
        '        applicationServerKey: urlBase64ToUint8Array(',
        '          process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!',
        '        ),',
        '      });',
        '      setSubscription(sub);',
        '      setState("subscribed");',
        '      await subscribeUser(JSON.parse(JSON.stringify(sub)));',
        '    } catch (err: any) {',
        '      setError(err.message);',
        '      setState("unsubscribed");',
        '    }',
        '  }, []);',
        '',
        '  const unsubscribeFromPush = useCallback(async () => {',
        '    setState("loading");',
        '    await subscription?.unsubscribe();',
        '    setSubscription(null);',
        '    setState("unsubscribed");',
        '    await unsubscribeUser();',
        '  }, [subscription]);',
    ], '⚛️  components/PushNotificationManager.tsx — Parte 3 (handlers)', st)

    story.append(NoteBox(
        'Use useCallback() em funções de efeito colateral para evitar re-renders\n'
        'desnecessários ao passar como props ou usar em useEffect com dependências.',
        'tip'))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 6
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(6, 'Backend — Server Actions', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Schema do Banco de Dados (Prisma)</b>', st['h2']))
    story.append(Paragraph(
        'Em produção, as assinaturas devem ser salvas em um banco de dados real, '
        'vinculadas ao usuário autenticado. Abaixo um schema Prisma completo para '
        'PostgreSQL.',
        st['body']))

    story += code_block([
        '// prisma/schema.prisma',
        'generator client {',
        '  provider = "prisma-client-js"',
        '}',
        '',
        'datasource db {',
        '  provider = "postgresql"',
        '  url      = env("DATABASE_URL")',
        '}',
        '',
        'model User {',
        '  id            String         @id @default(cuid())',
        '  email         String         @unique',
        '  name          String?',
        '  subscriptions PushSubscription[]',
        '  createdAt     DateTime       @default(now())',
        '}',
        '',
        'model PushSubscription {',
        '  id        String   @id @default(cuid())',
        '  userId    String',
        '  user      User     @relation(fields: [userId], references: [id])',
        '  endpoint  String   @unique',  
        '  p256dh    String   // Chave pública de criptografia',
        '  auth      String   // Segredo de autenticação',
        '  userAgent String?  // Identificação do browser',
        '  createdAt DateTime @default(now())',
        '  updatedAt DateTime @updatedAt',
        '',
        '  @@index([userId])',
        '}',
    ], '🗄️  prisma/schema.prisma — Schema Completo', st)

    story += code_block([
        '"use server";',
        'import webpush from "web-push";',
        'import { prisma } from "@/lib/prisma";',
        'import { auth } from "@/lib/auth"; // seu sistema de autenticação',
        '',
        'webpush.setVapidDetails(',
        '  `mailto:${process.env.VAPID_EMAIL}`,',
        '  process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!,',
        '  process.env.VAPID_PRIVATE_KEY!,',
        ');',
        '',
        'export async function subscribeUser(sub: any) {',
        '  const session = await auth(); // NextAuth / Clerk / etc.',
        '  if (!session?.user?.id) throw new Error("Não autenticado");',
        '',
        '  await prisma.pushSubscription.upsert({',
        '    where: { endpoint: sub.endpoint },',
        '    create: {',
        '      userId:   session.user.id,',
        '      endpoint: sub.endpoint,',
        '      p256dh:   sub.keys.p256dh,',
        '      auth:     sub.keys.auth,',
        '      userAgent: sub.userAgent,',
        '    },',
        '    update: { updatedAt: new Date() },',
        '  });',
        '  return { success: true };',
        '}',
    ], '⚙️  app/actions.ts — subscribeUser com Banco de Dados', st)

    story += code_block([
        'export async function sendNotificationToUser(',
        '  userId: string,',
        '  payload: { title: string; body: string; url?: string; icon?: string }',
        ') {',
        '  const subscriptions = await prisma.pushSubscription.findMany({',
        '    where: { userId },',
        '  });',
        '',
        '  const results = await Promise.allSettled(',
        '    subscriptions.map(async (sub) => {',
        '      try {',
        '        await webpush.sendNotification(',
        '          { endpoint: sub.endpoint,',
        '            keys: { p256dh: sub.p256dh, auth: sub.auth } },',
        '          JSON.stringify(payload)',
        '        );',
        '      } catch (err: any) {',
        '        // Assinatura expirada ou inválida — remover do banco',
        '        if (err.statusCode === 410 || err.statusCode === 404) {',
        '          await prisma.pushSubscription.delete({',
        '            where: { id: sub.id },',
        '          });',
        '        }',
        '        throw err;',
        '      }',
        '    })',
        '  );',
        '  return results;',
        '}',
    ], '📤  app/actions.ts — Enviando para Usuário com Limpeza Automática', st)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 7
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(7, 'Segurança & Boas Práticas', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Chaves VAPID — Gerenciamento Seguro</b>', st['h2']))
    for item in [
        'Gere as chaves VAPID <b>uma única vez</b> por domínio e armazene com segurança.',
        'Use um <b>gerenciador de segredos</b>: AWS Secrets Manager, HashiCorp Vault, Doppler.',
        'Nunca commite chaves no repositório — use <b>.env.local</b> e variáveis de CI/CD.',
        'Rotacione as chaves apenas em emergências (comprometimento). Invalida todos os subscribers.',
        'Monitore o <b>email VAPID</b> — o servidor de Push pode enviar alertas de abuso.',
    ]:
        story.append(bullet(item, st))
    story.append(Spacer(1, 8))

    story.append(Paragraph('<b>TTL (Time To Live) e Expiração</b>', st['h3']))
    story.append(Paragraph(
        'O TTL define por quanto tempo um servidor de Push deve tentar entregar '
        'uma notificação caso o dispositivo esteja offline. Configure-o com base '
        'na urgência do conteúdo.',
        st['body']))
    ttl_data = [
        ['Tipo de Notificação', 'TTL Recomendado', 'Exemplo'],
        ['Tempo real / urgente', '0 segundos', 'Alerta de fraude, autenticação 2FA'],
        ['Transacional', '3600 (1 hora)', 'Confirmação de pedido, pagamento'],
        ['Engajamento', '86400 (24h)', 'Newsletter, promoção do dia'],
        ['Conteúdo evergreen', '604800 (1 semana)', 'Novo artigo, feature update'],
    ]
    ttl = Table(ttl_data, colWidths=[5*cm, 4*cm, 6*cm])
    ttl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(ttl)
    story.append(Spacer(1, 8))

    story += code_block([
        '// Configurando TTL ao enviar notificação',
        'await webpush.sendNotification(',
        '  subscription,',
        '  JSON.stringify(payload),',
        '  {',
        '    TTL: 3600,        // 1 hora em segundos',
        '    urgency: "normal", // "very-low" | "low" | "normal" | "high"',
        '    topic: "orders",   // Substitui notifs anteriores do mesmo tópico',
        '  }',
        ');',
    ], '⏱️  Configurando TTL e Urgência', st)

    story.append(Paragraph('<b>Rate Limiting — Evitando Spam</b>', st['h2']))
    story += code_block([
        '// lib/rateLimiter.ts — Usando Upstash Redis + ratelimit',
        'import { Ratelimit } from "@upstash/ratelimit";',
        'import { Redis } from "@upstash/redis";',
        '',
        'const ratelimit = new Ratelimit({',
        '  redis: Redis.fromEnv(),',
        '  limiter: Ratelimit.slidingWindow(5, "1 h"), // 5 notifs/usuário/hora',
        '  analytics: true,',
        '});',
        '',
        'export async function checkRateLimit(userId: string) {',
        '  const { success, reset } = await ratelimit.limit(userId);',
        '  if (!success) {',
        '    const waitSeconds = Math.ceil((reset - Date.now()) / 1000);',
        '    throw new Error(`Rate limit atingido. Tente em ${waitSeconds}s`);',
        '  }',
        '}',
    ], '🚦  Rate Limiting com Upstash Redis', st)

    story.append(NoteBox(
        'Nunca envie mais de 1 notificação por hora para o mesmo usuário em conteúdo\n'
        'de marketing. Para notificações críticas (2FA, alertas de fraude), sem limite.\n'
        'Monitore sua taxa de opt-out — acima de 5% indica abuso de frequência.',
        'warning'))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 8
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(8, 'Notificações Avançadas', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Notificações com Ações (Botões Interativos)</b>', st['h2']))
    story.append(Paragraph(
        'Notificações com ações permitem que o usuário interaja sem abrir o site, '
        'como confirmar um pedido ou marcar uma tarefa como concluída. Suportado '
        'em Chrome e Edge (até 2 ações por notificação).',
        st['body']))

    story += code_block([
        '// No Service Worker: definindo as ações',
        'const options = {',
        '  body: "Seu pedido #4521 foi confirmado!",',
        '  icon: "/icons/icon-192.png",',
        '  actions: [',
        '    {',
        '      action: "view-order",   // ID da ação',
        '      title: "Ver Pedido",    // Texto do botão',
        '      icon: "/icons/bag.png", // Ícone do botão (opcional)',
        '    },',
        '    {',
        '      action: "dismiss",',
        '      title: "Dispensar",',
        '      icon: "/icons/x.png",',
        '    },',
        '  ],',
        '  data: { orderId: "4521", url: "/orders/4521" },',
        '};',
        '',
        '// Tratando o clique na ação específica',
        'self.addEventListener("notificationclick", (event) => {',
        '  event.notification.close();',
        '  const { action, notification } = event;',
        '  const { orderId, url } = notification.data;',
        '',
        '  if (action === "view-order") {',
        '    event.waitUntil(clients.openWindow(url));',
        '  } else if (action === "dismiss") {',
        '    // Apenas fecha — nenhuma ação adicional',
        '  } else {',
        '    // Clique no corpo da notificação',
        '    event.waitUntil(clients.openWindow("/"));',
        '  }',
        '});',
    ], '🎯  Notificações com Botões de Ação', st)

    story.append(Paragraph('<b>Notificação com Imagem (Rich Push)</b>', st['h2']))
    story += code_block([
        '// Backend: payload com imagem',
        'const payload = {',
        '  title: "Nova promoção: 50% OFF",',
        '  body: "Apenas hoje! Corra antes que acabe.",',
        '  icon: "/icons/icon-192.png",',
        '  image: "https://cdn.seusite.com/banner-promo.jpg", // 2:1 ratio ideal',
        '  url: "/promocoes",',
        '  tag: "promo-50",  // Substitui notificação anterior com mesmo tag',
        '};',
        '',
        'await webpush.sendNotification(subscription, JSON.stringify(payload));',
    ], '🖼️  Rich Push — Notificação com Imagem Banner', st)

    story.append(Paragraph('<b>Notificações Silenciosas (Data Push)</b>', st['h2']))
    story.append(Paragraph(
        'Notificações silenciosas entregam dados ao Service Worker sem mostrar '
        'nada ao usuário. Úteis para sincronização de dados em background.',
        st['body']))
    story += code_block([
        '// Backend: enviar payload sem título/body visível',
        'const silentPayload = {',
        '  silent: true,',
        '  type: "sync-data",',
        '  data: { userId: "123", newMessages: 5 }',
        '};',
        '',
        '// Service Worker: tratar sem exibir notificação',
        'self.addEventListener("push", (event) => {',
        '  const data = event.data.json();',
        '',
        '  if (data.silent) {',
        '    // Sincronizar dados sem notificar o usuário',
        '    event.waitUntil(',
        '      syncDataInBackground(data.data)',
        '    );',
        '    return; // Não chama showNotification()',
        '  }',
        '',
        '  // Push normal com notificação visual',
        '  event.waitUntil(',
        '    self.registration.showNotification(data.title, { body: data.body })',
        '  );',
        '});',
    ], '🔇  Data Push — Sincronização Silenciosa', st)

    story.append(NoteBox(
        'Atenção: O userVisibleOnly: true na assinatura OBRIGA que toda notificação\n'
        'recebida seja exibida ao usuário. Notificações verdadeiramente silenciosas\n'
        'só são possíveis com userVisibleOnly: false, que está desabilitado no Chrome.',
        'error'))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 9
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(9, 'Deploy & Produção', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Deploy na Vercel</b>', st['h2']))
    for item in [
        'Configure as variáveis de ambiente no dashboard da Vercel (Settings > Environment Variables).',
        'O sw.js deve estar na pasta <b>public/</b> para ser acessível em /sw.js.',
        'Certifique-se que o domínio usa <b>HTTPS</b> — a Vercel fornece automaticamente.',
        'Server Actions funcionam nativamente — nenhuma configuração extra necessária.',
    ]:
        story.append(bullet(item, st))
    story.append(Spacer(1, 8))

    story += code_block([
        '// next.config.js — Configurações recomendadas para produção',
        'const nextConfig = {',
        '  headers: async () => [',
        '    {',
        '      source: "/sw.js",',
        '      headers: [',
        '        // Service Workers devem ter Cache-Control: no-cache',
        '        // para que updates sejam aplicados rapidamente',
        '        { key: "Cache-Control", value: "no-cache, no-store, must-revalidate" },',
        '        { key: "Content-Type", value: "application/javascript; charset=utf-8" },',
        '      ],',
        '    },',
        '  ],',
        '};',
        '',
        'module.exports = nextConfig;',
    ], '⚙️  next.config.js — Headers do Service Worker', st)

    story.append(Paragraph('<b>Banco de Dados em Produção — PostgreSQL no Supabase</b>', st['h2']))
    story += code_block([
        '# 1. Criar conta em supabase.com e criar projeto',
        '',
        '# 2. Copiar a connection string do painel SQL',
        '# DATABASE_URL=postgresql://postgres:[SENHA]@db.[ID].supabase.co:5432/postgres',
        '',
        '# 3. Rodar as migrations',
        'npx prisma migrate deploy',
        '',
        '# 4. Gerar o client atualizado',
        'npx prisma generate',
        '',
        '# Alternativas ao Supabase:',
        '# - Neon (serverless PostgreSQL nativo para Vercel)',
        '# - PlanetScale (MySQL serverless)',
        '# - MongoDB Atlas (NoSQL)',
        '# - Railway (PostgreSQL completo com backups)',
    ], '🗄️  Configurando Banco de Dados em Produção', st)

    story.append(Paragraph('<b>Monitoramento e Observabilidade</b>', st['h2']))
    monitor_data = [
        ['Métrica', 'Ferramenta', 'O que monitorar'],
        ['Taxa de entrega', 'Logs do web-push', 'Status codes 201 (sucesso) vs 4xx/5xx'],
        ['Assinaturas ativas', 'Dashboard próprio', 'Total, crescimento, churn diário'],
        ['Erros de SW', 'Sentry / Datadog', 'Exceções no service worker'],
        ['Taxa de cliques (CTR)', 'Analytics custom', 'Notificationclick events'],
        ['Rate de opt-out', 'Eventos do browser', 'Usuários que bloquearam permissão'],
    ]
    mt = Table(monitor_data, colWidths=[3.5*cm, 3.5*cm, 8*cm])
    mt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(mt)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # CAPÍTULO 10
    # ══════════════════════════════════════════════════════════════════════════
    story.append(SectionHeader(10, 'Troubleshooting & Checklist Final', W - 4*cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Erros Comuns e Soluções</b>', st['h2']))
    errors = [
        ('DOMException: Registration failed',
         'O sw.js não está na pasta public/ ou contém erros de sintaxe.\n'
         'Solução: Abra DevTools > Application > Service Workers para ver o erro exato.'),
        ('NotAllowedError: permission denied',
         'O usuário bloqueou ou o site não tem HTTPS.\n'
         'Solução: Use HTTPS em produção. Em dev, localhost funciona sem HTTPS.'),
        ('Error: 410 Gone (Push Server)',
         'A assinatura expirou ou o usuário desinstalou o browser.\n'
         'Solução: Remova automaticamente assinaturas com status 410 do banco.'),
        ('Error: 401 Unauthorized (VAPID)',
         'Chaves VAPID incorretas ou mal formatadas.\n'
         'Solução: Regere as chaves e verifique se NEXT_PUBLIC_ está no prefixo correto.'),
        ('SW não atualiza após mudanças',
         'O navegador cacheia o Service Worker.\n'
         'Solução: Use updateViaCache: "none" no register() e Cache-Control: no-cache no header.'),
    ]
    for error, solution in errors:
        story.append(Paragraph(f'<b>❌ {error}</b>', st['h3']))
        story.append(Paragraph(solution.replace('\n', ' '), st['body_sm']))
        story.append(Spacer(1, 4))

    story.append(Paragraph('<b>Checklist de Deploy em Produção</b>', st['h2']))
    checks = [
        '[ ] sw.js está em public/sw.js e acessível via /sw.js',
        '[ ] HTTPS configurado no domínio de produção',
        '[ ] Variáveis VAPID configuradas no servidor (não commitar no git)',
        '[ ] Cache-Control: no-cache no header do /sw.js',
        '[ ] Banco de dados com tabela de assinaturas criada (migrations rodadas)',
        '[ ] Limpeza automática de assinaturas expiradas (status 410/404)',
        '[ ] Rate limiting ativado para evitar spam',
        '[ ] Testado em Chrome, Firefox e Safari (iOS 16.4+ em PWA)',
        '[ ] TTL configurado de acordo com urgência das notificações',
        '[ ] Logs e monitoramento de erros configurados (Sentry/Datadog)',
        '[ ] Permissão solicitada em contexto (não na entrada do site)',
        '[ ] Fallback para usuários sem suporte a Service Workers',
    ]
    for check in checks:
        story.append(Paragraph(check, st['bullet']))

    story.append(Spacer(1, 14))
    story.append(NoteBox(
        'Dica final: Solicite permissão de notificação APENAS após o usuário realizar\n'
        'uma ação que demonstre intenção (ex: clicar em "Ativar notificações"). Popups\n'
        'imediatos na entrada do site têm taxa de aceitação de apenas 3-5%.\n'
        'Contexto correto = 30-50% de aceitação!',
        'tip'))

    # ══════════════════════════════════════════════════════════════════════════
    # BUILD
    # ══════════════════════════════════════════════════════════════════════════
    doc.build(
        story,
        onFirstPage=cover_page,
        onLaterPages=normal_page,
    )
    print(f"PDF gerado: {path}")


build()