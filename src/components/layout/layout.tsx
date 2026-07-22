import { Inter } from "next/font/google"; // ← add import
import { Header } from "@/components/header";
import { Footer } from "../footer/footer";

type LayoutProps = {
  children: React.ReactNode;
}

const inter = Inter({ subsets: ['latin'] });

export const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="bg-radial-[at_25%_25%] from-green-950 via-slate-950 to-black text-white selection:bg-green-500/30">
      <div className={`${inter.className} relative flex min-h-screen flex-col dark `}>
        <main className="flex-1 flex flex-col mb-1">
          {children}
        </main>
      </div>
    </div>
  )
}