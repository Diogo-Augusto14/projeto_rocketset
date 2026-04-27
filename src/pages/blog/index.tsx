import { HeroSection } from "@/components/Hero/hero";
import { Layout } from "@/components/layout/layout";

export default function Blog() {
  return (
    <div>
      <HeroSection>
        <div>
          <div className="grid grid-cols-4 gap-1 text-white items-center">
            {" "}
            {/* Adicionei items-start para não esticarem verticalmente */}
            {/* Espaçador inicial (opcional, se quiser centralizar os blocos) */}
            <div className="col-span-1"></div>
            {/* Bloco 1: Ocupa 2 colunas (Maior) */}
            <div className="text-2xl font-bold m-1 text-white col-span-1 backdrop-blur-md bg-cyan-100/20 p-8 rounded-3xl border border-cyan-200/20 shadow-2xl">
              <p className="m-5">
                O impacto de Neymar na Seleção Brasileira é gigantesco e divide
                opiniões, mas os números são incontestáveis. Como o maior
                artilheiro da história da Amarelinha (superando Pelé em gols
                oficiais), ele assumiu o protagonismo em uma era de entressafra
                de craques, carregando a responsabilidade técnica do time por
                mais de uma década.
              </p>
            </div>
            {/* Bloco 2: Ocupa 1 coluna (Metade do tamanho do primeiro) */}
            <div className="text-2xl font-bold m-1 text-white col-span-1">
              <p className="m-5 backdrop-blur-md bg-cyan-100/20 p-8 rounded-3xl border border-cyan-200/20 shadow-2xl">
                A dúvida sobre a presença de Neymar na Seleção Brasileira para a
                Copa do Mundo de 2026 atingiu um novo patamar após ele ter sido
                deixado de fora da convocação de março de 2026 pelo técnico
                Carlo Ancelotti para os últimos amistosos preparatórios.
              </p>
              <p className="m-5 backdrop-blur-md bg-cyan-100/20 p-8 rounded-3xl border border-cyan-200/20 shadow-2xl">
                Recentemente, em abril de 2026, a ausência de sua figurinha no
                álbum oficial da Copa reforçou os questionamentos sobre sua
                participação no torneio.
              </p>
            </div>
          </div>
        </div>
      </HeroSection>
      <article className="max-w-3xl mx-auto py-20 px-6">
        <h1 className="text-4xl font-bold mb-8 text-white">
          A Lacuna Técnica: Por que a ausência de Neymar ainda assombra a
          Seleção
        </h1>

        <section className="space-y-6 text-muted-foreground leading-relaxed">
          <p className="text-xl text-blue-400 font-medium italic">
            "Não é apenas sobre gols, é sobre a gravidade que ele exerce no
            campo."
          </p>

          <p>
            Desde sua ascensão meteórica no Santos, Neymar Jr. tornou-se o
            epicentro do futebol brasileiro. Falar que ele faz falta é chover no
            molhado, mas a análise tática revela um buraco muito mais profundo
            do que a simples ausência de um "camisa 10". Quando Neymar está em
            campo, o sistema defensivo adversário é obrigado a se reorganizar.
            Ele atrai dois, às vezes três marcadores, criando espaços que
            jogadores como Vinícius Jr. e Rodrygo ainda estão aprendendo a
            explorar sem o "guarda-costas" técnico ao lado.
          </p>

          <h2 className="text-2xl font-semibold text-white mt-10">
            O Criador de Caos
          </h2>
          <p>
            A Seleção Brasileira atual sofre de um mal comum no futebol moderno:
            o excesso de tática e a escassez de improviso. Neymar é o último dos
            "mágicos" que consegue resolver um jogo travado em um palmo de
            terreno. Sem ele, o Brasil torna-se um time previsível, de
            transições rápidas pelas pontas, mas com pouca criatividade pelo
            centro.
          </p>

          <div className="bg-secondary/30 p-8 rounded-lg border border-border my-10">
            <p className="text-center text-lg font-light">
              "Sem o Ney, o Brasil joga como um relógio suíço: funcional, mas
              sem alma. Com ele, jogamos como música clássica: complexo,
              arriscado e inesquecível."
            </p>
          </div>

          <h2 className="text-2xl font-semibold text-white">
            As Estatísticas não Mentem
          </h2>
          <p>
            Os números de assistências e passes decisivos de Neymar na era
            pós-Tite mostram que ele participa de quase 60% das ações ofensivas
            que resultam em gol. Quando ele não está, a responsabilidade cai
            sobre jovens que, embora brilhantes em seus clubes, ainda sentem o
            peso de serem os protagonistas absolutos da Amarelinha.
          </p>

          {/* Repetição para gerar scroll */}
          {[...Array(5)].map((_, i) => (
            <p key={i}>
              A falta que ele faz é sentida no drible que quebra a linha, na
              falta sofrida na entrada da área que esfria o jogo, e na
              capacidade de segurar a bola sob pressão. Enquanto o futebol
              brasileiro busca um sucessor, a sombra do craque continua pairando
              sobre cada convocação. Precisamos entender que Neymar não é o
              problema, mas sim a solução que muitas vezes mascarou deficiências
              coletivas da nossa equipe.
            </p>
          ))}

          <p className="text-sm pt-10">
            Conclusão: Enquanto a próxima geração não assume as rédeas da
            criatividade, continuaremos olhando para o departamento médico ou
            para as ligas estrangeiras esperando o retorno do nosso último
            grande camisa 10.
          </p>
        </section>
      </article>
    </div>
  );
}
