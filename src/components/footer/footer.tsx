import Link from "next/link";
import Image from "next/image";
import { Logo } from "../logo";

export const Footer = () => {
  return (
    <footer className="border-tbg-gray-500/50">
      <div className="flex h-full items-center justify-center">
        <div className="flex flex-col md:flex-row justify-between ms:justify-start ">
          <Logo />
          <nav className="flex flex-col md:flex-row items-center gap-4 text-sm text-blue-900">
            <Link href="/termos"className="hover:text-blue-200">termos de uso</Link>
            <Link href="/politicas"className="hover:text-blue-200">politicas</Link>
            <Link href="/feedback" className="hover:text-blue-200">feedback</Link>
          </nav>
        </div>
      </div>
    </footer>
  );
};
