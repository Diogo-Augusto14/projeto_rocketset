export default function Page() {
  return (
    <div className="grid grid-cols-4 justify-center mt-[50px]">
      <div className="col-span-1"></div>

      {/* Coluna da Foto de Perfil */}
      <div className="col-span-1 p-4 flex flex-col items-center justify-center gap-4 mr-[90px]">
        <img
          src="/perfil.png"
          alt="Foto de Perfil"
          className="w-full h-full rounded-full shadow-lg"
        />
        <p className="text-center font-medium text-white">
          Diogo Augusto Oliveira das Graças
        </p>
      </div>

      
      <div className="col-span-1   p-6 rounded-lg flex flex-col gap-8 text-white">
        
        
        <div className="flex flex-col gap-3">
          <p className="font-bold">Redes Sociais:</p>
          <div className="flex flex-wrap gap-4">
            <img src="/github.svg" alt="Github" className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer" />
            <img src="/facebook.svg" alt="Facebook" className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer" />
            <img src="/instragam.svg" alt="Instagram" className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer" />
            <img src="/Linkend.svg" alt="Linkedin" className="w-8 h-8 rounded-full shadow-lg hover:scale-110 transition-transform cursor-pointer" />
          </div>
        </div>

        
        <div className="flex flex-col gap-2">
          <p className="text-2xl font-bold">
            Resumo Profissional:
          </p>
          <p className="text-gray-200">Programador júnior em início de carreira</p>
        </div>
      </div>

      <div className="col-span-1"></div>
    </div>
  );
}