export const HeroSection = ({children}: {children: React.ReactNode}) =>{
return (
    <section className="w-screen min-h-[700] relative z-10 bg-gradient-to-t from-vermelho-700 via-vermelho-300 to-vermelho-200 rounded-sm ">
    {children}
    </section>
)
}