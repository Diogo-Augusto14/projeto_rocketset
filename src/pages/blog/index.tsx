import { Layout } from "@/components/layout/layout";

export default function Blog() {
  return (
    
      <article className="max-w-3xl mx-auto py-20 px-6">
        <h1 className="text-4xl font-bold mb-8 text-white">
          A Lacuna Técnica: Por que a ausência de Neymar ainda assombra a Seleção
        </h1>

        <section className="space-y-6 text-muted-foreground leading-relaxed">
          <p className="text-xl text-blue-400 font-medium italic">
            "Não é apenas sobre gols, é sobre a gravidade que ele exerce no campo."
          </p>

          <p>
            Desde sua ascensão meteórica no Santos, Neymar Jr. tornou-se o epicentro do futebol brasileiro. 
            Falar que ele faz falta é chover no molhado, mas a análise tática revela um buraco muito mais 
            profundo do que a simples ausência de um "camisa 10". Quando Neymar está em campo, o sistema 
            defensivo adversário é obrigado a se reorganizar. Ele atrai dois, às vezes três marcadores, 
            criando espaços que jogadores como Vinícius Jr. e Rodrygo ainda estão aprendendo a explorar 
            sem o "guarda-costas" técnico ao lado.
          </p>

          <h2 className="text-2xl font-semibold text-white mt-10">O Criador de Caos</h2>
          <p>
            A Seleção Brasileira atual sofre de um mal comum no futebol moderno: o excesso de tática e a 
            escassez de improviso. Neymar é o último dos "mágicos" que consegue resolver um jogo travado 
            em um palmo de terreno. Sem ele, o Brasil torna-se um time previsível, de transições rápidas 
            pelas pontas, mas com pouca criatividade pelo centro.
          </p>

          <div className="bg-secondary/30 p-8 rounded-lg border border-border my-10">
            <p className="text-center text-lg font-light">
              "Sem o Ney, o Brasil joga como um relógio suíço: funcional, mas sem alma. 
              Com ele, jogamos como música clássica: complexo, arriscado e inesquecível."
            </p>
          </div>

          <h2 className="text-2xl font-semibold text-white">As Estatísticas não Mentem</h2>
          <p>
            Os números de assistências e passes decisivos de Neymar na era pós-Tite mostram que ele 
            participa de quase 60% das ações ofensivas que resultam em gol. Quando ele não está, 
            a responsabilidade cai sobre jovens que, embora brilhantes em seus clubes, ainda sentem 
            o peso de serem os protagonistas absolutos da Amarelinha.
          </p>

          {/* Repetição para gerar scroll */}
          {[...Array(5)].map((_, i) => (
            <p key={i}>
              A falta que ele faz é sentida no drible que quebra a linha, na falta sofrida na entrada 
              da área que esfria o jogo, e na capacidade de segurar a bola sob pressão. Enquanto o 
              futebol brasileiro busca um sucessor, a sombra do craque continua pairando sobre cada 
              convocação. Precisamos entender que Neymar não é o problema, mas sim a solução que 
              muitas vezes mascarou deficiências coletivas da nossa equipe.
            </p>
          ))}

          <p className="text-sm pt-10">
            Conclusão: Enquanto a próxima geração não assume as rédeas da criatividade, 
            continuaremos olhando para o departamento médico ou para as ligas estrangeiras 
            esperando o retorno do nosso último grande camisa 10.
          </p>
        </section>
      </article>
    
  );
}