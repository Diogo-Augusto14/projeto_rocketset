import { HeroSection } from "@/components/Hero/hero";
import { Layout } from "@/components/layout/layout";

export default function BlogIA() {
  return (
    <div>
      <HeroSection>
        <div></div>
      </HeroSection>

      <article className="max-w-[1200px] mx-auto py-20 px-6">
        <h1 className="text-4xl font-bold mb-8 text-white">
          A Morte do "Digitador de Código" e a Ascensão do Engenheiro de
          Intenção
        </h1>

        <section className="space-y-6 text-muted-foreground leading-relaxed">
          <div className="grid grid-cols-2 items-center text-white">
            <div className="justify-items-end">
              <p className="p-5 m-5 bg-white rounded-[30px] bg-gradient-to-b from-cyan-200 to-gray-600/50 shadow-2xl shadow-gray-800 max-w-[250px]">
                "A IA é excelente em gerar respostas, mas o humano continua
                sendo o único capaz de fazer as perguntas que realmente
                importam."
              </p>
              <p className="p-5 m-5 bg-white rounded-[30px] bg-gradient-to-b from-cyan-200 to-gray-600/50 shadow-2xl shadow-gray-800 max-w-[250px]">
                Contudo, a programação nunca foi sobre digitar; foi sobre
                resolver problemas de negócio ambíguos sob restrições reais —
                algo onde a IA, presa a padrões do passado, ainda tropeça.
              </p>
            </div>
            <div>
              <p className="p-5 m-5 bg-white rounded-[30px] bg-gradient-to-b from-cyan-200 to-gray-600/50 shadow-2xl shadow-gray-800 max-w-[219px]">
                Estamos vivendo o fim da era da sintaxe. Ferramentas como Devin
                e Copilot transformaram o ato de escrever código em uma{" "}
                <strong>commodity</strong>. O que antes exigia domínio profundo
                de bibliotecas e frameworks, hoje é resolvido em milissegundos
                por modelos probabilísticos.
              </p>
            </div>
          </div>

          {/* NOVO BLOCO */}
          <p className="text-white/80">
            Durante décadas, o desenvolvedor foi o gargalo criativo das empresas
            de tecnologia. A escassez de profissionais que dominavam linguagens
            como C++, Java ou, mais recentemente, TypeScript e Rust, conferia um
            poder de barganha enorme a quem sabia escrever código funcional.
            Essa escassez artificial criou uma cultura de gatekeeping técnico —
            onde o valor do profissional era medido pela quantidade de sintaxe
            memorizada e pela velocidade com que escrevia loops sem consultar a
            documentação.
          </p>

          <p className="text-white/80">
            Mas esse cenário começou a ruir silenciosamente. Primeiro vieram os
            autocompletes inteligentes. Depois, o GitHub Copilot. Em seguida,
            assistentes capazes de gerar funções inteiras a partir de um
            comentário em inglês. E hoje, agentes autônomos como o Devin são
            capazes de receber um ticket do Jira e entregar um pull request
            revisado. O código em si — a sintaxe pura — deixou de ser o ativo
            escasso. O novo ativo escasso é a{" "}
            <strong className="text-white">intenção bem formulada</strong>.
          </p>

          <h2 className="text-2xl font-semibold text-white mt-10">
            A Diferença entre Predição e Inovação
          </h2>
          <p>
            Uma IA trabalha com a média da inteligência humana contida em seu
            dataset. Ela é, por definição, conservadora: ela prevê o que{" "}
            <em>provavelmente</em> viria a seguir. Já a inovação disruptiva
            nasce do improvável. O "pulo do gato" não é estatístico; é a
            capacidade de conectar áreas desconexas — como filosofia, design e
            infraestrutura — para criar soluções que a lógica probabilística
            jamais sugeriria.
          </p>

          <p className="text-white/80">
            Pense no surgimento do iPhone em 2007. Nenhum modelo treinado nos
            dados de 2005 teria sugerido eliminar o teclado físico de um
            celular. Nenhum sistema probabilístico teria apostado numa interface
            puramente touchscreen para o mercado corporativo. Essa foi uma
            decisão humana, carregada de visão de produto, tolerância ao risco e
            uma compreensão quase filosófica de como as pessoas <em>queriam</em>{" "}
            se relacionar com a tecnologia — não de como elas <em>estavam</em>{" "}
            se relacionando. Isso é o que a IA não faz: ela não enxerga o que
            ainda não existe nos dados.
          </p>

          <p className="text-white/80">
            O desenvolvedor do futuro não será avaliado pela quantidade de
            linguagens que domina, mas pela clareza com que consegue articular
            problemas complexos em instruções que uma IA possa executar com
            precisão cirúrgica. Essa habilidade — que chamaremos de{" "}
            <strong className="text-white">engenharia de intenção</strong> — é
            uma síntese entre escrita técnica, pensamento sistêmico e visão de
            produto. É, em essência, uma nova forma de liderança tecnológica.
          </p>

          <div className="rounded-lg bg-gradient-to-b from-blue-100/10 to-blue-300/30 p-8 shadow-xl my-10 backdrop-blur-md">
            <p className="text-center text-lg font-medium text-blue-900">
              "Confiar o núcleo de uma empresa 100% a uma IA é como colocar um
              avião no piloto automático sem ninguém na cabine: é eficiente no
              céu limpo, mas é a presença humana que salva a aeronave em meio à
              tempestade de variáveis imprevisíveis."
            </p>
          </div>

          <h2 className="text-2xl font-semibold text-white">
            O Filtro Ético e a Responsabilidade Técnica
          </h2>
          <p>
            O grande gargalo da automação total é o{" "}
            <strong>vazio de responsabilidade</strong>. LLMs podem introduzir
            alucinações técnicas ou sugerir padrões obsoletos com
            vulnerabilidades críticas. No fim do dia, quem assina a segurança
            dos dados e a ética do algoritmo é um ser humano. O desenvolvedor
            deixa de ser um "pedreiro digital" para se tornar um auditor de
            sistemas e guardião da integridade técnica.
          </p>

          {/* NOVO BLOCO ÉTICO */}
          <p className="text-white/80">
            Esse ponto merece ser aprofundado. Em abril de 2023, um advogado
            norte-americano usou o ChatGPT para redigir uma peça jurídica e
            citou precedentes que simplesmente não existiam — alucinações do
            modelo apresentadas com a confiança de fatos verificados. O juiz
            aplicou sanções severas. O caso tornou-se um símbolo do risco de
            delegar a validação da realidade a sistemas probabilísticos. No
            mundo do software, o equivalente são dependências com
            vulnerabilidades conhecidas geradas por sugestão de IA sem revisão
            humana, rotas de API expostas por código auto-completado sem análise
            de superfície de ataque, ou lógicas de negócio implementadas
            "funcionalmente" mas em desacordo com a regulamentação vigente.
          </p>

          <p className="text-white/80">
            A responsabilidade técnica, portanto, não desaparece com a IA — ela
            se <em>concentra</em>. Antes, ela era distribuída entre dezenas de
            desenvolvedores que cada um revisava seu próprio código. Agora, com
            um único engenheiro capaz de produzir o volume de código antes
            gerado por uma equipe inteira, o peso da revisão crítica recai sobre
            menos pessoas com mais poder. É uma equação que exige maturidade
            técnica e ética proporcionalmente maiores.
          </p>

          <div className="grid grid-cols-2 items-start gap-4 text-white my-6">
            <p className="p-5 bg-white rounded-[30px] bg-gradient-to-b from-cyan-200 to-gray-600/50 shadow-2xl shadow-gray-800">
              <strong>O desenvolvedor como curador:</strong> Assim como um
              editor literário não escreve o livro, mas garante que ele seja
              coerente, preciso e impactante, o engenheiro de software moderno
              atua como curador do output da IA — validando, refinando e
              assumindo a autoria final do que é entregue.
            </p>
            <p className="p-5 bg-white rounded-[30px] bg-gradient-to-b from-cyan-200 to-gray-600/50 shadow-2xl shadow-gray-800">
              <strong>O desenvolvedor como estrategista:</strong> Entender{" "}
              <em>por que</em> uma feature deve existir, qual o impacto no
              modelo de negócio e quais os trade-offs de cada abordagem
              arquitetural — essas são perguntas que nenhum modelo responde com
              propriedade, porque exigem contexto organizacional que nenhum
              dataset captura.
            </p>
          </div>

          <h2 className="text-2xl font-semibold text-white mt-10">
            A Nova Pilha de Habilidades: O que o Mercado Vai Exigir
          </h2>

          <p className="text-white/80">
            Se o código bruto se tornou commodity, qual é a nova pilha de
            habilidades que diferencia um engenheiro sênior de um júnior na era
            da IA? A resposta é contraintuitiva: as habilidades mais valorizadas
            serão aquelas consideradas "soft" pela cultura tech tradicional.
          </p>

          <p className="text-white/80">
            <strong className="text-white">Pensamento sistêmico</strong> — a
            capacidade de enxergar como componentes interdependentes se afetam
            mutuamente — será o diferencial número um. Uma IA pode implementar
            um microsserviço com maestria, mas não compreende como aquele
            microsserviço vai se comportar sob carga durante uma campanha de
            Black Friday que vai triplicar o tráfego inesperadamente. Projetar
            para falha, pensar em resiliência e antecipar cenários de borda é
            uma habilidade profundamente humana.
          </p>

          <p className="text-white/80">
            <strong className="text-white">
              Comunicação técnica de alto nível
            </strong>{" "}
            — a habilidade de traduzir objetivos de negócio em especificações
            técnicas precisas e vice-versa — também se tornará uma vantagem
            competitiva decisiva. Profissionais que conseguem sentar com o CEO e
            o CTO ao mesmo tempo, falar a língua de ambos e orquestrar a IA para
            executar o que ambos precisam, terão um valor de mercado
            exponencial.
          </p>

          <p className="text-white/80">
            Por último, <strong className="text-white">visão de produto</strong>{" "}
            — a capacidade de entender o usuário final, antecipar suas dores e
            desenhar experiências que resolvam problemas reais antes mesmo de
            serem articulados — permanece exclusivamente humana. Dados de
            comportamento podem informar, mas não inspirar. A empatia não é um
            algoritmo.
          </p>

          <div className="rounded-lg bg-gradient-to-b from-blue-100/10 to-blue-300/30 p-8 shadow-xl my-10 backdrop-blur-md">
            <p className="text-center text-lg font-medium text-blue-900">
              "O desenvolvedor que domina a IA não é aquele que sabe mais
              prompts — é aquele que sabe exatamente qual problema precisa ser
              resolvido antes de abrir qualquer ferramenta."
            </p>
          </div>

          <h2 className="text-2xl font-semibold text-white mt-10">
            O Paradoxo da Produtividade: Fazer Mais, Entender Menos?
          </h2>

          <p className="text-white/80">
            Existe um risco sombrio no horizonte que poucos estão discutindo com
            a seriedade necessária: o paradoxo da produtividade gerada por IA. À
            medida que geramos mais código em menos tempo, corremos o risco de
            construir sistemas que ninguém compreende completamente. Bases de
            código que crescem mais rápido do que a capacidade humana de
            auditá-las. Arquiteturas que funcionam, mas cujo raciocínio interno
            é opaco — um reflexo da própria opacidade dos modelos que as
            geraram.
          </p>

          <p className="text-white/80">
            Isso não é ficção científica. É uma extrapolação direta do que já
            acontece com sistemas de machine learning em produção: modelos que
            funcionam estatisticamente bem, mas cujas decisões individuais são
            inexplicáveis. Agora, imagine esse problema escalado para toda a
            infraestrutura de software de uma empresa. O desenvolvedor do futuro
            precisará ser, antes de tudo, um{" "}
            <strong className="text-white">guardião da legibilidade</strong> —
            alguém que impõe ordem semântica e documentação de intenção sobre um
            output que, deixado à própria sorte, tende ao caos estrutural.
          </p>

          <p className="text-white/80">
            Esse papel de guardião é simultaneamente técnico e filosófico. Ele
            exige que o engenheiro se pergunte não apenas "isso funciona?" mas
            "isso é compreensível?", "isso pode ser mantido daqui a dois anos
            por alguém que nunca viu esse código?", "se esse sistema falhar às
            3h da manhã, o engenheiro de plantão vai conseguir diagnosticar o
            problema?". Essas perguntas não têm resposta no dataset de
            treinamento de nenhum modelo.
          </p>

          <h2 className="text-2xl font-semibold text-white mt-10">
            Quem Vai Prosperar — e Quem Vai Desaparecer
          </h2>

          <div className="grid grid-cols-2 items-start gap-4 text-white my-6">
            <div>
              <p className="p-5 bg-white rounded-[30px] bg-gradient-to-b from-cyan-200 to-gray-600/50 shadow-2xl shadow-gray-800">
                <strong>Perfis em risco de substituição:</strong>{" "}
                Desenvolvedores que atuam como tradutores de requisitos em
                código, sem agregar visão crítica. Profissionais que se recusam
                a incorporar IA no fluxo de trabalho por apego à identidade de
                "quem escreve código". Especialistas em tecnologias de nicho sem
                capacidade de abstração para novos paradigmas.
              </p>
            </div>
            <div>
              <p className="p-5 bg-white rounded-[30px] bg-gradient-to-b from-cyan-200 to-gray-600/50 shadow-2xl shadow-gray-800">
                <strong>Perfis com valorização exponencial:</strong> Arquitetos
                de sistemas que entendem tanto o negócio quanto a
                infraestrutura. Engenheiros com forte senso crítico para revisão
                e auditoria de código gerado por IA. Profissionais que combinam
                habilidades técnicas com comunicação estratégica e visão de
                produto.
              </p>
            </div>
          </div>

          <p className="text-white/80">
            A transição não será suave para todos. Historicamente, toda
            revolução tecnológica cria mais empregos do que destrói — mas os
            empregos criados raramente exigem as mesmas habilidades dos empregos
            destruídos. O tecelão manual não se tornou operador de tear mecânico
            da noite para o dia. A diferença é que, desta vez, a velocidade da
            transição é ordens de magnitude mais rápida. O ciclo de
            obsolescência de habilidades que antes levava décadas agora leva
            anos.
          </p>

          <p className="text-white/80">
            A boa notícia é que a programação, em sua essência mais profunda,
            sempre foi sobre resolver problemas — e problemas continuarão
            existindo em abundância. A questão não é se haverá trabalho, mas se
            os profissionais de hoje estão desenvolvendo as habilidades certas
            para executá-lo. Curiosidade intelectual, capacidade de aprendizado
            contínuo e disposição para reconfigurar a própria identidade
            profissional serão as verdadeiras vantagens competitivas da próxima
            década.
          </p>

          <p>
            O futuro pertence aos <strong>Arquitetos de Sistemas</strong>. A
            resistência à obsolescência não está na velocidade com que você
            aprende uma nova linguagem, mas na profundidade da sua análise
            crítica e na sua visão de produto. A IA não veio para ser sua
            concorrente, mas para ser o teclado mais potente que você já teve em
            mãos.
          </p>

          <h2 className="text-2xl font-semibold text-white mt-10">
            Como se Preparar: Um Roteiro Prático
          </h2>

          <p className="text-white/80">
            Diante de tudo isso, o que fazer de forma concreta? Primeiro,
            incorpore ferramentas de IA ao seu fluxo de trabalho imediatamente —
            não como uma ameaça a ser tolerada, mas como um par de programação
            disponível 24 horas por dia. Aprenda a escrever prompts com precisão
            técnica. Documente suas intenções antes de codificar. Pratique o
            hábito de revisar criticamente todo output gerado por IA, assim como
            revisaria o código de um desenvolvedor júnior talentoso mas que
            ainda comete erros de contexto.
          </p>

          <p className="text-white/80">
            Segundo, invista deliberadamente nas habilidades que a IA não
            replicará: leia sobre arquitetura de sistemas, sobre design de
            produto, sobre comunicação técnica. Estude casos de falhas
            sistêmicas famosas — o colapso do Knight Capital, o bug do Boeing
            737 MAX, o desastre do Mars Climate Orbiter. Esses casos ensinam
            mais sobre pensamento sistêmico do que qualquer curso de algoritmos.
          </p>

          <p className="text-white/80">
            Terceiro, cultive perspectiva interdisciplinar. Os maiores saltos
            tecnológicos da história vieram de pessoas capazes de conectar
            domínios distintos: Shannon aplicou álgebra booleana às
            comunicações, Jobs trouxe caligrafia ao design de interfaces,
            Berners-Lee aplicou o conceito de hipertexto à rede global. A
            especialização profunda ainda importa, mas ela precisa coexistir com
            uma curiosidade genuinamente ampla sobre como o mundo funciona além
            da tela do seu editor de código.
          </p>

          <p className="text-sm pt-10 border-t border-white/10">
            <strong>Conclusão:</strong> A IA substituirá quem apenas traduz
            requisitos em código. Para quem desenha, questiona e lidera a
            tecnologia, ela será apenas o motor que permitirá você chegar muito
            mais longe, em muito menos tempo. A pergunta que cada desenvolvedor
            precisa responder hoje não é "a IA vai me substituir?" — mas sim
            "que tipo de profissional preciso me tornar para que a IA trabalhe
            para mim, e não contra mim?" A resposta está menos em linhas de
            código e mais em profundidade de pensamento.
          </p>
        </section>
      </article>
    </div>
  );
}
