import Link from "next/link";
import { Logo } from "../logo";

export const Footer = () => {
  return (
    <footer className="border-t border-gray-500/20 bg-slate-950/80">
      <div className="mx-auto flex max-w-6xl flex-col gap-6 px-6 py-8 text-slate-400 md:flex-row md:items-center md:justify-between">
        <Logo />
        <nav className="flex flex-wrap items-center gap-4 text-sm text-slate-300">
          <Link href="/termos" className="hover:text-white">
            Termos de uso
          </Link>
          <Link href="/politicas" className="hover:text-white">
            Políticas
          </Link>
          <Link href="/feedback" className="hover:text-white">
            Feedback
          </Link>
        </nav>
      </div>
    </footer>
  );
};
