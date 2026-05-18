import Link from "next/link";
import { Button } from "./ui/button";
import { Logo } from "./logo";

export const Header = () => {
  return (
    <header className="sticky top-0 z-30 border-b border-white/10 bg-slate-950/90 backdrop-blur-xl">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <Logo />

        <nav className="hidden items-center gap-6 text-sm text-slate-200 md:flex">
          <Link href="/" className="transition hover:text-white">
            Início
          </Link>
          <Link href="#projects" className="transition hover:text-white">
            Projetos
          </Link>
          <Link href="#contact" className="transition hover:text-white">
            Contato
          </Link>
          <Link href="/blog" className="transition hover:text-white">
            Blog
          </Link>
        </nav>

        <Button asChild size="sm">
          <Link href="#contact">Vamos conversar</Link>
        </Button>
      </div>
    </header>
  );
};