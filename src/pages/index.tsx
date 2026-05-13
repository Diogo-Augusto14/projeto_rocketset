export default function Page() {
  return (
    <div className="min-h-screen ">
      
      {/* Header / Intro */}
      <header className="pt-10 pb-6 px-6 text-center">
        <h2 className="text-3xl md:text-4xl font-light tracking-tight">
          Olá! Sou <span className="font-bold text-green-400">Diogo Augusto</span>
        </h2>
      </header>

      {/* Hero Section */}
      <section className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-center gap-10 px-6 py-10">
        
        {/* Foto de Perfil */}
        <div className="relative group">
          <div className="absolute "></div>
          <img
            src="/perfil.png"
            alt="Diogo Augusto"
            className="relative w-48 h-48 md:w-56 md:h-56 rounded-full object-cover border-2 border-white/10 shadow-2xl  bg-green-500/0 rounded-full  hover:bg-green-900 transition duration-1000"
          />
          <p className="mt-4 text-center font-medium text-slate-300 md:text-lg">
            Diogo Augusto Oliveira das Graças
          </p>
        </div>

        
        <div className="flex flex-col gap-6 max-w-2xl text-center md:text-left">
          <div className="space-y-4">
            <h3 className="text-2xl font-bold text-green-400">Resumo Profissional</h3>
            <p className="text-slate-300 leading-relaxed text-lg">
              Programador Júnior focado em tecnologias modernas. Atualmente na 
              <span className="text-white font-semibold"> Pemill Fundição e Usinagem</span>, 
              liderando a evolução do Portal do Cliente com Next.js e Tailwind. 
              Minha stack combina a eficiência do <span className="text-emerald-400">React/Next.js</span> com 
              a robustez do <span className="text-emerald-400">Python/Django</span>.
            </p>
          </div>

          <div className="space-y-3">
            <p className="font-semibold text-sm uppercase tracking-widest text-slate-400">Conecte-se comigo:</p>
            <div className="flex flex-wrap justify-center md:justify-start gap-5">
              {['github', 'facebook', 'instagram', 'linkedin'].map((social) => (
                <img 
                  key={social}
                  src={`/${social}.svg`} 
                  alt={social} 
                  className="w-7 h-7 opacity-70 hover:opacity-100 hover:scale-110 transition-all cursor-pointer invert" 
                />
              ))}
            </div>
          </div>
        </div>
      </section>

      
      <section className="max-w-6xl mx-auto px-6 py-16">
        <h3 className="text-2xl font-bold mb-8 text-center md:text-left border-b border-white/10 pb-4">Projetos em Destaque</h3>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          
          
          {[
            {
              title: "Ministério Redenção",
              desc: "Plataforma para gestão eclesiástica e automação de doações. Integra pagamentos em tempo real e nuvem segura.",
              tags: ["Django", "Supabase", "Google Cloud", "Mercado Pago"]
            },
            {
              title: "Controle de Produção Pemill",
              desc: "Digitalização dos fluxos de fundição e usinagem. Substitui planilhas por dashboards dinâmicos em Next.js.",
              tags: ["Next.js", "Tailwind", "PostgreSQL", "Prisma"]
            },
            {
              title: "3D Print Manager",
              desc: "Gerenciamento para impressão 3D com cálculo de custos e visualização STL diretamente no navegador.",
              tags: ["Three Fiber", "Node.js", "TypeScript", "Amazon S3"]
            }
          ].map((proj, i) => (
            <div key={i} className="flex  flex-col justify-between p-6 rounded-2xl bg-white/5 backdrop-blur-md border border-white/10 hover:border-green-500/50 transition-colors group">
              <div>
                <h4 className="text-xl font-bold mb-4 text-green-400">{proj.title}</h4>
                <p className="text-slate-400 text-sm leading-relaxed mb-6 italic">
                  "{proj.desc}"
                </p>
                <div className="flex flex-wrap gap-2 mb-8">
                  {proj.tags.map(tag => (
                    <span key={tag} className="px-3 py-1 text-[10px] uppercase font-bold tracking-wider rounded-full bg-green-500/10 border border-green-500/20 text-green-300">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
              
              <button className="w-full py-3 rounded-xl bg-white/5 border border-white/10 hover:bg-green-600 hover:text-white transition-all font-medium active:scale-95">
                Ver Detalhes
              </button>
            </div>
          ))}

          {[
            {
              title: "Ministério Redenção",
              desc: "Plataforma para gestão eclesiástica e automação de doações. Integra pagamentos em tempo real e nuvem segura.",
              tags: ["Django", "Supabase", "Google Cloud", "Mercado Pago"]
            },
            {
              title: "Controle de Produção Pemill",
              desc: "Digitalização dos fluxos de fundição e usinagem. Substitui planilhas por dashboards dinâmicos em Next.js.",
              tags: ["Next.js", "Tailwind", "PostgreSQL", "Prisma"]
            },
            {
              title: "3D Print Manager",
              desc: "Gerenciamento para impressão 3D com cálculo de custos e visualização STL diretamente no navegador.",
              tags: ["Three Fiber", "Node.js", "TypeScript", "Amazon S3"]
            },
            {
              title: "3D Print Manager",
              desc: "Gerenciamento para impressão 3D com cálculo de custos e visualização STL diretamente no navegador.",
              tags: ["Three Fiber", "Node.js", "TypeScript", "Amazon S3"]
            },
            {
              title: "3D Print Manager",
              desc: "Gerenciamento para impressão 3D com cálculo de custos e visualização STL diretamente no navegador.",
              tags: ["Three Fiber ", "Node.js ", "TypeScript", "Amazon S3"]
            }
          ].map((process, i) => (
            
          ))}

        </div>
      </section>
    </div>
  );
}