export default function Page() {
  return (
    <div className="min-h-screen">
      {/* Intro */}
      <section className="mx-auto max-w-6xl px-6 pt-10 pb-16">
        <div className="grid gap-12 lg:grid-cols-[1.1fr_0.9fr] items-center">
          <div className="space-y-6">
            <span className="inline-flex rounded-full bg-green-500/10 px-4 py-1 text-sm font-semibold uppercase tracking-[0.3em] text-green-300">
              Portfólio Profissional
            </span>

            <h1 className="max-w-3xl text-4xl font-semibold tracking-tight text-white sm:text-5xl">
              Olá, eu sou <span className="text-green-400">Diogo Augusto</span> — desenvolvedor fullstack focado em projetos web reais.
            </h1>

            <p className="max-w-2xl text-lg leading-8 text-slate-300">
              Crio aplicações rápidas e seguras para empresas do setor industrial e serviços, usando Next.js, Tailwind e Python/Django. Meu trabalho transforma processos manuais em sistemas digitais modernos.
            </p>

            <div className="flex flex-wrap gap-4">
              <a
                href="#projects"
                className="inline-flex items-center justify-center rounded-full bg-green-400 px-5 py-3 text-sm font-semibold text-slate-950 transition hover:bg-green-300"
              >
                Projetos
              </a>
              <a
                href="#contact"
                className="inline-flex items-center justify-center rounded-full border border-white/10 px-5 py-3 text-sm font-semibold text-white transition hover:border-green-300 hover:text-green-300"
              >
                Contato
              </a>
            </div>
          </div>

          <div className="rounded-[2rem] border border-white/10 bg-white/5 p-6 shadow-2xl shadow-black/20 backdrop-blur-xl">
            <img
              src="/perfil.png"
              alt="Foto de perfil de Diogo Augusto"
              className="h-72 w-full rounded-[1.75rem] object-cover shadow-inner shadow-black/30"
            />
            <div className="mt-6 space-y-4 text-slate-300">
              <div>
                <p className="text-xs uppercase tracking-[0.3em] text-green-300">Sobre mim</p>
                <p className="mt-2 leading-7">
                  Desenvolvedor que entrega soluções escaláveis, com experiência em portais corporativos, automações e integração de APIs financeiras.
                </p>
              </div>
              <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-3xl bg-slate-950/80 p-4">
                  <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Experiência</p>
                  <p className="mt-2 text-2xl font-semibold text-white">3+ anos</p>
                </div>
                <div className="rounded-3xl bg-slate-950/80 p-4">
                  <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Projetos</p>
                  <p className="mt-2 text-2xl font-semibold text-white">+15 entregues</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="skills" className="mx-auto max-w-6xl px-6 pb-16">
        <div className="space-y-6">
          <div className="space-y-3">
            <p className="text-sm uppercase tracking-[0.3em] text-green-300">Conhecimentos</p>
            <h2 className="text-3xl font-semibold text-white">Tecnologias e práticas que uso</h2>
          </div>

          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {[
              'Next.js',
              'React',
              'TypeScript',
              'Tailwind CSS',
              'Python',
              'Django',
              'PostgreSQL',
              'Prisma',
            ].map((skill) => (
              <div key={skill} className="rounded-3xl border border-white/10 bg-white/5 p-5 text-slate-200">
                {skill}
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="projects" className="mx-auto max-w-6xl px-6 pb-16">
        <div className="space-y-6">
          <div className="space-y-3">
            <p className="text-sm uppercase tracking-[0.3em] text-green-300">Projetos</p>
            <h2 className="text-3xl font-semibold text-white">Trabalhos profissionais recentes</h2>
          </div>

          <div className="grid gap-6 lg:grid-cols-3">
            {[
              {
                title: 'Portal do Cliente Pemill',
                desc: 'Sistema para gestão de pedidos e controle de produção industrial, com dashboards dinâmicos e automações de status.',
                tags: ['Next.js', 'Tailwind', 'PostgreSQL', 'Prisma'],
              },
              {
                title: 'Plataforma de Doações',
                desc: 'Aplicação segura para gestão de arrecadações, integrações com pagamento e relatórios de doações em tempo real.',
                tags: ['Django', 'REST API', 'Stripe', 'Supabase'],
              },
              {
                title: 'Gestão de Impressão 3D',
                desc: 'Painel para acompanhar produção, custos e arquivos de impressão com interface clara para equipe técnica.',
                tags: ['TypeScript', 'Node.js', 'AWS', 'Three.js'],
              },
            ].map((project) => (
              <article key={project.title} className="rounded-[2rem] border border-white/10 bg-white/5 p-6 shadow-2xl shadow-black/10 transition hover:border-green-400/40 hover:bg-white/10">
                <h3 className="text-xl font-semibold text-green-300">{project.title}</h3>
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
        </div>
      </section>

      <section id="experience" className="mx-auto max-w-6xl px-6 pb-16">
        <div className="rounded-[2rem] border border-white/10 bg-white/5 p-8 shadow-2xl shadow-black/10 backdrop-blur-xl">
          <div className="space-y-6">
            <p className="text-sm uppercase tracking-[0.3em] text-green-300">Experiência</p>
            <h2 className="text-3xl font-semibold text-white">Como eu trabalho</h2>
            <div className="grid gap-6 lg:grid-cols-2">
              {[
                {
                  title: 'Desenvolvedor Júnior',
                  company: 'Pemill Fundição e Usinagem',
                  detail: 'Melhorei o Portal do Cliente com novas telas e automações, reduzindo retrabalho e acelerando processos.',
                },
                {
                  title: 'Freelancer Técnico',
                  company: 'Soluções para clientes B2B',
                  detail: 'Entreguei sistemas administrativos e sites com foco em desempenho, usabilidade e manutenção.',
                },
              ].map((item) => (
                <div key={item.title} className="rounded-3xl border border-white/10 bg-slate-950/80 p-6">
                  <p className="text-sm uppercase tracking-[0.2em] text-slate-500">{item.company}</p>
                  <h3 className="mt-3 text-xl font-semibold text-white">{item.title}</h3>
                  <p className="mt-4 text-slate-300 leading-7">{item.detail}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section id="contact" className="mx-auto max-w-6xl px-6 pb-20">
        <div className="rounded-[2rem] border border-white/10 bg-green-500/10 p-8 shadow-2xl shadow-black/10 backdrop-blur-xl">
          <div className="grid gap-8 lg:grid-cols-[0.9fr_0.6fr] items-center">
            <div className="space-y-4">
              <p className="text-sm uppercase tracking-[0.3em] text-green-300">Contato</p>
              <h2 className="text-3xl font-semibold text-white">Vamos conversar sobre o seu próximo projeto.</h2>
              <p className="text-slate-300 leading-7">
                Estou disponível para novos desafios em desenvolvimento web, automação e integrações corporativas.
              </p>
              <div className="space-y-4">
                <div>
                  <p className="text-sm uppercase tracking-[0.2em] text-slate-500">Email</p>
                  <p className="mt-2 text-lg font-semibold text-white">diogoaugusto7123@gmail.com</p>
                </div>
                <div>
                  <p className="text-sm uppercase tracking-[0.2em] text-slate-500">WhatsApp</p>
                  <p className="mt-2 text-lg font-semibold text-white">(31) 99381-2100</p>
                </div>
              </div>
            </div>
            <div className="rounded-[2rem] border border-white/10 bg-slate-950/80 p-8 text-slate-300">
              <p className="text-sm uppercase tracking-[0.3em] text-green-300">Redes Sociais</p>
              <div className="mt-6 flex flex-wrap gap-4">
                {[{
                  github: 'https://github.com',
                  linkedin:'https://Linkendi.com',
                  instagram:'https://Instagram.com',
              }].map((social) => (
                  <a
                    key={social.github}
                    href={`https://${social.github}.com`}
                    target="_blank"
                    rel="noreferrer"
                    className="inline-flex rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-sm font-semibold text-white transition hover:border-green-300 hover:bg-green-500/10"
                  >
                    
                  </a>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
