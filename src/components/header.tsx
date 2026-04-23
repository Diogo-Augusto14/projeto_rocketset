import Link from "next/link";
import { Button } from "./ui/button";
import { useRouter } from "next/router";
import { cn } from "@/lib/utils";
import { ActiveLink } from "./active-link/active-link";

export const Header = () => {
  const router = useRouter();


  return (
    <header
      className="fixed top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60"
    >
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          <Link href="/" className="font-bold text-xl">
            logo
          </Link>
          
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