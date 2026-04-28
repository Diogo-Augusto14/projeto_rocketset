export const HeroSection = ({ children }: { children: React.ReactNode }) => {
  return (
    <section className="relative w-full min-h-[700px] flex items-center justify-center overflow-hidden z-10 bg-gradient-to-br from-vermelho-700/50 via-vermelho-500/45 to-vermelho-300/40 rounded-b-[3rem] shadow-2xl">
      
      
      <div className="absolute inset-0 bg-black/15 pointer-events-none z-0"></div>
      <div className="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 flex justify-center">
        {children}
      </div>
      
    </section>
  );
};