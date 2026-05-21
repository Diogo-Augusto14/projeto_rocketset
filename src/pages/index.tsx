export default function Page() {
  return (
    <div>
      <div className="relative grid grid-cols-4 justify-center mt-[50px] overflow-hidden">
        <div className="col-span-1"></div>

        {/* Coluna da Foto de Perfil */}
        <div className="col-span-1 p-4 flex flex-col items-center text-center justify-center gap-4 mr-[90px]">
          <img
            src="/perfil.png"
            alt="Foto de Perfil"
            className="w-48 h-48 rounded-full shadow-lg shadow-green-900 object-cover"
          />
          <p className="font-medium text-white">
            Diogo Augusto Oliveira das Graças
          </p>
        </div>

        <div className="col-span-2 p-6 rounded-lg flex flex-col gap-8 text-white max-w-xl">
          <div className="flex flex-col gap-3">
            <p className="font-bold">Redes Sociais:</p>
            <div className="flex flex-wrap gap-4">
              {/* Seus ícones aqui... */}
              <img
                src="/github.svg"
                alt="Github"
                className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer"
              />
              <img
                src="/facebook.svg"
                alt="Facebook"
                className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer"
              />
              <img
                src="/instragam.svg"
                alt="Instagram"
                className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer"
              />
              <img
                src="/Linkend.svg"
                alt="Linkedin"
                className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer"
              />
            </div>
          </div>

          <div className="flex flex-col gap-2">
            <p className="text-2xl font-bold">Resumo Profissional:</p>
            <p className="text-slate-100 leading-relaxed">
              "Programador Júnior focado em tecnologias modernas de
              desenvolvimento web. Atualmente atuo na Pemill Fundição e
              Usinagem, liderando a evolução do Portal do Cliente com Next.js e
              Tailwind. Minha stack principal envolve JavaScript (Next.js/React)
              e Python (Django), combinando eficiência visual e performance de
              dados para criar ferramentas que facilitam a interação entre
              empresa e cliente."
            </p>
          </div>
        </div>

        {/* Card de Projetos corrigido */}
      </div>
      <div className="grid grid-cols-5 h-[300px]">
        <div className=""></div>
        <div className=" rounded-[20px] bg-white/10 backdrop-blur-sm border border-white/10 shadow-[0_0_15px_rgba(34,197,94,0.3)] justify-center m-[5px] text-center  ">
          <p className="text-white mt-4 mb-4">
            {" "}
            <strong>Ministerio Redençao</strong>
          </p>
          <p className="text-white mt-4 pb-4 pl-8 text-start">
            "Plataforma desenvolvida para gestão eclesiástica e automação de
            doações. O sistema integra o processamento de pagamentos em tempo
            real e armazena dados de forma segura na nuvem, facilitando a
            administração financeira e o engajamento da comunidade."
          </p>
          <div className="grid grid-cols-3 ">
          <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  transition-all duration-300 hover:bg-green-700 hover:scale-105">Django</div>
           <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  transition-all duration-300 hover:bg-green-700 hover:scale-105">Supabase</div>
            <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  transition-all duration-300 hover:bg-green-700 hover:scale-105">Google Cloud </div>
            <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  transition-all duration-300 hover:bg-green-700 hover:scale-105 col-start-2">Mercado Papo</div>
          </div>
          <div>

          
            <button className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 shadow-[0_0_15px_rgba(34,197,94,0.3)] justify-center m-[5px] mb-8 text-center p-3 transition-all duration-300 hover:bg-green-700 hover:scale-105 cursor-pointer">
              Ver Projeto
            </button>
          </div>
        </div>

        <div className="rounded-[20px] bg-white/10 backdrop-blur-sm border border-white/10 shadow-[0_0_15px_rgba(34,197,94,0.3)] justify-center m-[5px] text-center">
          <p className="text-white mt-4 mb-4">
            <strong>Controle de Produção Pemill</strong>
          </p>
          <p className="text-white mt-4 pb-4 pl-8 text-start">
            "Sistema interno focado na digitalização dos fluxos de fundição e
            usinagem. Permite o acompanhamento de ordens de serviço, controle de
            estoque de matéria-prima e monitoramento de produtividade,
            substituindo planilhas manuais por um dashboard dinâmico em
            Next.js."
          </p>
          <div className="grid grid-cols-3 ">
          <div >
            {" "}
            <span>TAILWIND</span>
          </div>
          <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  text-center transition-all duration-300 hover:bg-green-700 hover:scale-105 p-1">
            {" "}
            CSS{" "}
          </div>
          <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  text-center transition-all duration-300 hover:bg-green-700 hover:scale-105 p-1">
            {" "}
            POSTGRESQL{" "}
          </div>
          <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  text-center transition-all duration-300 hover:bg-green-700 hover:scale-105 col-start-2 p-1 ">
            PRISMA ORM{" "}
          </div>
             </div>
          <div>
            <button className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 shadow-[0_0_15px_rgba(34,197,94,0.3)] justify-center m-[5px] mb-8 text-center p-3 transition-all duration-300 hover:bg-green-700 hover:scale-105 cursor-pointer">
              Ver Projeto
            </button>
          </div>
          
        </div>

        <div className="rounded-[20px] bg-white/10 backdrop-blur-sm border border-white/10 shadow-[0_0_15px_rgba(34,197,94,0.3)] justify-center m-[5px] text-center">
          <p className="text-white mt-4 mb-4">
            <strong>3D Print Manager</strong>
          </p>
          <p className="text-white mt-4 pb-4 pl-8 text-start">
            "Ferramenta de gerenciamento para entusiastas de impressão 3D. O
            projeto permite o upload de arquivos STL, cálculo automático de
            custos de filamento e organização de fila de impressão, utilizando
            visualização 3D no navegador para pré-visualização dos modelos."
          </p>
          <div className="grid grid-cols-3 ">
            <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  transition-all duration-300 hover:bg-green-700 hover:scale-105">
              {" "}
              REACT THREE FIBER{" "}
            </div>
            <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  text-center transition-all duration-300 hover:bg-green-700 hover:scale-105 p-1">
              {" "}
              NODE.JS{" "}
            </div>
            <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  text-center transition-all duration-300 hover:bg-green-700 hover:scale-105 p-1">
              {" "}
              TYPESCRIPT{" "}
            </div>
            <div className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]  m-[9px]  text-center transition-all duration-300 hover:bg-green-700 hover:scale-105 col-start-2 p-1">
              {" "}
              AMAZON S3{" "}
            </div>
          </div>
          <div>
            <button className="rounded-[10px] bg-white/10 backdrop-blur-sm border border-white/10 shadow-[0_0_15px_rgba(34,197,94,0.3)] justify-center m-[5px] mb-8 text-center p-3 transition-all duration-300 hover:bg-green-700 hover:scale-105 cursor-pointer">
              Ver Projeto
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
