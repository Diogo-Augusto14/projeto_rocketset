"use client";

import { useEffect, useState } from "react";

// ── R7: Funções nomeadas ────────────────────────────────────────────────────

// Calcula anos de experiência desde o início do curso
function calcularExperiencia(anoInicio: number): number {
  const anoAtual = new Date().getFullYear();
  return anoAtual - anoInicio;
}

// Calcula tempo restante para formatura em meses
function calcularTempoFormatura(mesConclusao: number, anoConclusao: number): number {
  const hoje = new Date();
  const formatura = new Date(anoConclusao, mesConclusao - 1);
  const diffMs = formatura.getTime() - hoje.getTime();
  return Math.max(0, Math.round(diffMs / (1000 * 60 * 60 * 24 * 30)));
}

// Valida campo de email básico
function validarEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Valida formulário de contato completo
function validarFormulario(nome: string, email: string, mensagem: string): string[] {
  const erros: string[] = [];
  if (!nome.trim()) erros.push("Nome é obrigatório");
  if (!validarEmail(email)) erros.push("Email inválido");
  if (mensagem.trim().length < 10) erros.push("Mensagem muito curta (mínimo 10 caracteres)");
  return erros;
}

// Determina perfil com base nas respostas do quiz
function calcularPerfil(respostas: string[]): string {
  const front = respostas.filter((r) => r === "front").length;
  const back = respostas.filter((r) => r === "back").length;
  if (front > back) return "Front-end";
  if (back > front) return "Back-end";
  return "Full Stack";
}

// ── R2: Variáveis JS reais ──────────────────────────────────────────────────
const nome = "Diogo Augusto";
const curso = "Desenvolvimento Web";
const bio =
  "Desenvolvedor fullstack focado em projetos reais para o setor industrial e serviços. Crio aplicações rápidas, seguras e escaláveis usando Next.js, Tailwind e Python/Django.";
const anoInicio = 2022;

// ── R6: Array de objetos (projetos) ────────────────────────────────────────
const projetos = [
  {
    titulo: "Portal do Cliente Pemill",
    desc: "Sistema para gestão de pedidos e controle de produção industrial, com dashboards dinâmicos e automações de status.",
    tags: ["Next.js", "Tailwind", "PostgreSQL", "Prisma"],
  },
  {
    titulo: "Plataforma de Doações",
    desc: "Aplicação segura para gestão de arrecadações, integração com pagamento e relatórios em tempo real.",
    tags: ["Django", "REST API", "Stripe", "Supabase"],
  },
  {
    titulo: "Gestão de Impressão 3D",
    desc: "Painel para acompanhar produção, custos e arquivos de impressão com interface clara para equipe técnica.",
    tags: ["TypeScript", "Node.js", "AWS", "Three.js"],
  },
];

// ── R6: Array de habilidades ────────────────────────────────────────────────
const habilidades = [
  "Next.js", "React", "TypeScript", "Tailwind CSS",
  "Python", "Django", "PostgreSQL", "Prisma",
];

// ── Perguntas do quiz ───────────────────────────────────────────────────────
const perguntasQuiz = [
  { texto: "O que te empolga mais?", opcA: "Criar interfaces bonitas", opcB: "Modelar bancos de dados" },
  { texto: "Seu superpoder seria:", opcA: "CSS perfeito em qualquer tela", opcB: "API nunca cai" },
  { texto: "Você prefere resolver:", opcA: "Animações e UX", opcB: "Lógica e performance" },
];

export default function Page() {
  // ── R3: Operadores/cálculos ─────────────────────────────────────────────
  const experiencia = calcularExperiencia(anoInicio); // anos desde início
  const mesesFormatura = calcularTempoFormatura(12, 2025); // conclusão dez/2025
  const totalProjetos = projetos.length * 5; // estimativa de projetos entregues

  // ── R9: Fetch de API externa ────────────────────────────────────────────
  const [frase, setFrase] = useState<string>("Carregando frase motivacional…");
  useEffect(() => {
    // Busca frase motivacional de API pública
    fetch("https://api.adviceslip.com/advice")
      .then((res) => res.json())
      .then((data) => setFrase(data.slip.advice))
      .catch(() => setFrase("A persistência é o caminho do êxito. — Charles Chaplin"));
  }, []);

  // ── R4: Quiz condicional ────────────────────────────────────────────────
  const [quizAtivo, setQuizAtivo] = useState(false);
  const [etapaQuiz, setEtapaQuiz] = useState(0);
  const [respostas, setRespostas] = useState<string[]>([]);
  const [resultado, setResultado] = useState<string | null>(null);

  function responderQuiz(resp: string) {
    const novas = [...respostas, resp];
    if (etapaQuiz + 1 >= perguntasQuiz.length) {
      // R4: condicional que modifica a interface
      setResultado(calcularPerfil(novas));
    } else {
      setEtapaQuiz(etapaQuiz + 1);
    }
    setRespostas(novas);
  }

  function reiniciarQuiz() {
    setEtapaQuiz(0);
    setRespostas([]);
    setResultado(null);
    setQuizAtivo(false);
  }

  // ── R8: Formulário com validação ────────────────────────────────────────
  const [formNome, setFormNome] = useState("");
  const [formEmail, setFormEmail] = useState("");
  const [formMsg, setFormMsg] = useState("");
  const [formErros, setFormErros] = useState<string[]>([]);
  const [formEnviado, setFormEnviado] = useState(false);

  function enviarFormulario() {
    // Valida antes de enviar
    const erros = validarFormulario(formNome, formEmail, formMsg);
    setFormErros(erros);
    if (erros.length === 0) {
      // R4: condicional que altera interface após validação
      setFormEnviado(true);
    }
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">

      {/* ── Intro / Sobre mim (R2) ─────────────────────────────────────── */}
      <section className="mx-auto max-w-6xl px-6 pt-10 pb-16">
        <div className="grid gap-12 lg:grid-cols-[1.1fr_0.9fr] items-center">
          <div className="space-y-6">
            <span className="inline-flex rounded-full bg-green-500/10 px-4 py-1 text-sm font-semibold uppercase tracking-[0.3em] text-green-300">
              Portfólio Profissional
            </span>
            {/* R2: nome e curso via variáveis JS */}
            <h1 className="text-4xl font-semibold tracking-tight sm:text-5xl">
              Olá, eu sou{" "}
              <span className="text-green-400">{nome}</span> — desenvolvedor fullstack focado em projetos web reais.
            </h1>
            <p className="text-lg leading-8 text-slate-300">{bio}</p>
            <p className="text-sm text-slate-400">Curso: <span className="text-white font-medium">{curso}</span></p>

            <div className="flex flex-wrap gap-4">
              <a href="#projects" className="inline-flex items-center justify-center rounded-full bg-green-400 px-5 py-3 text-sm font-semibold text-slate-950 transition hover:bg-green-300">
                Projetos
              </a>
              <a href="#contact" className="inline-flex items-center justify-center rounded-full border border-white/10 px-5 py-3 text-sm font-semibold text-white transition hover:border-green-300 hover:text-green-300">
                Contato
              </a>
            </div>
          </div>

          <div className="rounded-[2rem] border border-white/10 bg-white/5 p-6 shadow-2xl shadow-black/20 backdrop-blur-xl">
            <div className="h-72 w-full rounded-[1.75rem] bg-slate-800 flex items-center justify-center text-slate-500 text-6xl">
              👨‍💻
            </div>
            <div className="mt-6 space-y-4 text-slate-300">
              <p className="text-xs uppercase tracking-[0.3em] text-green-300">Sobre mim</p>
              <p className="leading-7">{bio}</p>
              {/* R3: cálculos com operadores */}
              <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-3xl bg-slate-950/80 p-4">
                  <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Experiência</p>
                  <p className="mt-2 text-2xl font-semibold text-white">{experiencia}+ anos</p>
                </div>
                <div className="rounded-3xl bg-slate-950/80 p-4">
                  <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Projetos</p>
                  <p className="mt-2 text-2xl font-semibold text-white">+{totalProjetos} entregues</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── R3: Calculadora de tempo ──────────────────────────────────────── */}
      <section className="mx-auto max-w-6xl px-6 pb-16">
        <div className="rounded-[2rem] border border-white/10 bg-white/5 p-6">
          <p className="text-sm uppercase tracking-[0.3em] text-green-300 mb-2">Calculadora do Curso</p>
          <h2 className="text-2xl font-semibold text-white mb-4">Seu progresso no tempo</h2>
          <div className="grid sm:grid-cols-3 gap-4">
            <div className="rounded-2xl bg-slate-950/80 p-4">
              <p className="text-xs text-slate-500 uppercase tracking-widest">Ano de início</p>
              <p className="mt-1 text-3xl font-bold text-green-400">{anoInicio}</p>
            </div>
            <div className="rounded-2xl bg-slate-950/80 p-4">
              <p className="text-xs text-slate-500 uppercase tracking-widest">Anos no curso</p>
              {/* R3: operador aritmético */}
              <p className="mt-1 text-3xl font-bold text-green-400">{new Date().getFullYear() - anoInicio}</p>
            </div>
            <div className="rounded-2xl bg-slate-950/80 p-4">
              <p className="text-xs text-slate-500 uppercase tracking-widest">Meses p/ formatura</p>
              <p className="mt-1 text-3xl font-bold text-green-400">{mesesFormatura === 0 ? "Formado!" : mesesFormatura}</p>
            </div>
          </div>
        </div>
      </section>

      {/* ── R5: Habilidades em loop ───────────────────────────────────────── */}
      <section id="skills" className="mx-auto max-w-6xl px-6 pb-16">
        <p className="text-sm uppercase tracking-[0.3em] text-green-300 mb-2">Conhecimentos</p>
        <h2 className="text-3xl font-semibold text-white mb-6">Tecnologias e práticas que uso</h2>
        {/* R5: lista gerada com loop (map = laço de repetição) */}
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {habilidades.map((skill) => (
            <div key={skill} className="rounded-3xl border border-white/10 bg-white/5 p-5 text-slate-200 hover:border-green-400/40 transition">
              {skill}
            </div>
          ))}
        </div>
      </section>

      {/* ── R4: Quiz condicional ──────────────────────────────────────────── */}
      <section className="mx-auto max-w-6xl px-6 pb-16">
        <div className="rounded-[2rem] border border-white/10 bg-white/5 p-8">
          <p className="text-sm uppercase tracking-[0.3em] text-green-300 mb-2">Quiz Interativo</p>
          <h2 className="text-3xl font-semibold text-white mb-4">Você é mais Front-end ou Back-end?</h2>

          {/* R4: if/else — exibe conteúdo diferente conforme estado */}
          {!quizAtivo && !resultado && (
            <button
              onClick={() => setQuizAtivo(true)}
              className="rounded-full bg-green-400 px-5 py-3 text-sm font-semibold text-slate-950 hover:bg-green-300 transition"
            >
              Iniciar quiz →
            </button>
          )}

          {quizAtivo && !resultado && (
            <div className="space-y-4">
              <p className="text-slate-300">{perguntasQuiz[etapaQuiz].texto}</p>
              <div className="flex gap-4">
                <button onClick={() => responderQuiz("front")} className="flex-1 rounded-2xl border border-white/10 p-4 hover:border-green-400 hover:text-green-300 transition text-left">
                  🎨 {perguntasQuiz[etapaQuiz].opcA}
                </button>
                <button onClick={() => responderQuiz("back")} className="flex-1 rounded-2xl border border-white/10 p-4 hover:border-green-400 hover:text-green-300 transition text-left">
                  ⚙️ {perguntasQuiz[etapaQuiz].opcB}
                </button>
              </div>
              <p className="text-xs text-slate-500">Pergunta {etapaQuiz + 1} de {perguntasQuiz.length}</p>
            </div>
          )}

          {resultado && (
            <div className="space-y-4">
              <p className="text-2xl font-bold text-green-400">Seu perfil: {resultado} 🚀</p>
              <p className="text-slate-300">
                {resultado === "Front-end"
                  ? "Você ama criar interfaces e experiências visuais incríveis!"
                  : resultado === "Back-end"
                  ? "Você prefere a robustez das APIs e bancos de dados!"
                  : "Você domina os dois mundos — parabéns, Full Stack!"}
              </p>
              <button onClick={reiniciarQuiz} className="rounded-full border border-white/10 px-4 py-2 text-sm hover:border-green-300 transition">
                Refazer quiz
              </button>
            </div>
          )}
        </div>
      </section>

      {/* ── R6: Projetos (array de objetos) ──────────────────────────────── */}
      <section id="projects" className="mx-auto max-w-6xl px-6 pb-16">
        <p className="text-sm uppercase tracking-[0.3em] text-green-300 mb-2">Projetos</p>
        <h2 className="text-3xl font-semibold text-white mb-6">Trabalhos profissionais recentes</h2>
        {/* R6: array de objetos renderizado com map */}
        <div className="grid gap-6 lg:grid-cols-3">
          {projetos.map((project) => (
            <article key={project.titulo} className="rounded-[2rem] border border-white/10 bg-white/5 p-6 transition hover:border-green-400/40 hover:bg-white/10">
              <h3 className="text-xl font-semibold text-green-300">{project.titulo}</h3>
              <p className="mt-4 text-slate-300 leading-7">{project.desc}</p>
              <div className="mt-6 flex flex-wrap gap-2">
                {project.tags.map((tag) => (
                  <span key={tag} className="rounded-full border border-white/10 bg-green-500/10 px-3 py-1 text-[11px] uppercase tracking-[0.2em] text-green-300">
                    {tag}
                  </span>
                ))}
              </div>
            </article>
          ))}
        </div>
      </section>

      {/* ── R9: Frase de API externa ──────────────────────────────────────── */}
      <section className="mx-auto max-w-6xl px-6 pb-16">
        <div className="rounded-[2rem] border border-green-400/20 bg-green-500/5 p-8 text-center">
          <p className="text-sm uppercase tracking-[0.3em] text-green-300 mb-4">Frase do Dia (API pública)</p>
          {/* R9: resultado do fetch async */}
          <blockquote className="text-xl italic text-slate-200">"{frase}"</blockquote>
        </div>
      </section>

      {/* ── Experiência ──────────────────────────────────────────────────── */}
      <section id="experience" className="mx-auto max-w-6xl px-6 pb-16">
        <div className="rounded-[2rem] border border-white/10 bg-white/5 p-8">
          <p className="text-sm uppercase tracking-[0.3em] text-green-300 mb-2">Experiência</p>
          <h2 className="text-3xl font-semibold text-white mb-6">Como eu trabalho</h2>
          <div className="grid gap-6 lg:grid-cols-2">
            {[
              { titulo: "Desenvolvedor Júnior", empresa: "Pemill Fundição e Usinagem", detalhe: "Melhorei o Portal do Cliente com novas telas e automações, reduzindo retrabalho e acelerando processos." },
              { titulo: "Freelancer Técnico", empresa: "Soluções para clientes B2B", detalhe: "Entreguei sistemas administrativos e sites com foco em desempenho, usabilidade e manutenção." },
            ].map((item) => (
              <div key={item.titulo} className="rounded-3xl border border-white/10 bg-slate-950/80 p-6">
                <p className="text-sm uppercase tracking-[0.2em] text-slate-500">{item.empresa}</p>
                <h3 className="mt-3 text-xl font-semibold text-white">{item.titulo}</h3>
                <p className="mt-4 text-slate-300 leading-7">{item.detalhe}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── R8: Formulário com validação ──────────────────────────────────── */}
      <section id="contact" className="mx-auto max-w-6xl px-6 pb-20">
        <div className="rounded-[2rem] border border-white/10 bg-green-500/10 p-8">
          <p className="text-sm uppercase tracking-[0.3em] text-green-300 mb-2">Contato</p>
          <h2 className="text-3xl font-semibold text-white mb-6">Vamos conversar sobre o seu próximo projeto.</h2>

          <div className="grid gap-8 lg:grid-cols-2 items-start">
            <div className="space-y-4 text-slate-300">
              <p className="leading-7">Estou disponível para novos desafios em desenvolvimento web, automação e integrações corporativas.</p>
              <div>
                <p className="text-sm uppercase tracking-[0.2em] text-slate-500">Email</p>
                <p className="mt-1 text-lg font-semibold text-white">diogoaugusto7123@gmail.com</p>
              </div>
              <div>
                <p className="text-sm uppercase tracking-[0.2em] text-slate-500">WhatsApp</p>
                <p className="mt-1 text-lg font-semibold text-white">(31) 99381-2100</p>
              </div>
              <div className="flex gap-3 pt-2">
                {[
                  { label: "GitHub", href: "https://github.com" },
                  { label: "LinkedIn", href: "https://linkedin.com" },
                  { label: "Instagram", href: "https://instagram.com" },
                ].map((s) => (
                  <a key={s.label} href={s.href} target="_blank" rel="noreferrer"
                    className="rounded-2xl border border-white/10 bg-white/5 px-4 py-2 text-sm font-semibold hover:border-green-300 hover:bg-green-500/10 transition">
                    {s.label}
                  </a>
                ))}
              </div>
            </div>

            {/* R8: Formulário com validação via JS */}
            <div className="rounded-[2rem] border border-white/10 bg-slate-950/80 p-6 space-y-4">
              {formEnviado ? (
                // R4: condicional que altera interface
                <div className="text-center py-8">
                  <p className="text-3xl mb-2">✅</p>
                  <p className="text-green-300 font-semibold">Mensagem enviada com sucesso!</p>
                  <button onClick={() => { setFormEnviado(false); setFormNome(""); setFormEmail(""); setFormMsg(""); }}
                    className="mt-4 text-sm text-slate-400 hover:text-white transition">
                    Enviar outra mensagem
                  </button>
                </div>
              ) : (
                <>
                  <div>
                    <label className="block text-xs uppercase tracking-widest text-slate-400 mb-1">Nome</label>
                    <input
                      type="text"
                      value={formNome}
                      onChange={(e) => setFormNome(e.target.value)}
                      className="w-full rounded-xl bg-white/5 border border-white/10 px-4 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-green-400"
                      placeholder="Seu nome"
                    />
                  </div>
                  <div>
                    <label className="block text-xs uppercase tracking-widest text-slate-400 mb-1">Email</label>
                    <input
                      type="email"
                      value={formEmail}
                      onChange={(e) => setFormEmail(e.target.value)}
                      className="w-full rounded-xl bg-white/5 border border-white/10 px-4 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-green-400"
                      placeholder="seu@email.com"
                    />
                  </div>
                  <div>
                    <label className="block text-xs uppercase tracking-widest text-slate-400 mb-1">Mensagem</label>
                    <textarea
                      value={formMsg}
                      onChange={(e) => setFormMsg(e.target.value)}
                      rows={4}
                      className="w-full rounded-xl bg-white/5 border border-white/10 px-4 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-green-400 resize-none"
                      placeholder="Descreva seu projeto..."
                    />
                  </div>
                  {/* R4: erros condicionais */}
                  {formErros.length > 0 && (
                    <ul className="space-y-1">
                      {formErros.map((e) => (
                        <li key={e} className="text-sm text-red-400">⚠ {e}</li>
                      ))}
                    </ul>
                  )}
                  <button
                    onClick={enviarFormulario}
                    className="w-full rounded-full bg-green-400 py-3 text-sm font-semibold text-slate-950 hover:bg-green-300 transition"
                  >
                    Enviar mensagem →
                  </button>
                </>
              )}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}