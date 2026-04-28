import Link from "next/link";
import { Button } from "./ui/button";
import { useRouter } from "next/router";
import { Logo } from "./logo";
import { ActiveLink } from "./active-link/active-link";

export const Header = () => {
  const router = useRouter();


  return (
    <header
      className="bg-blue-900/10 backdrop-blur-md"
    >
      <div className="flex h-full items-center justify-center">
        <div className="flex h-auto items-center justify-between">
          <Logo />
          
          <nav className="flex items-center gap-6">
            <ActiveLink href="/">Início</ActiveLink>
            <ActiveLink href="/blog">Blog</ActiveLink>
            <Button variant="secondary">Começar</Button>
          </nav>
        </div>
      </div>
    </header>
  );
};