import { Inter } from "next/font/google"; // ← add import
import { Header } from "@/components/header";
import { Footer } from "../footer/footer";

type LayoutProps = {
  children: React.ReactNode;
}

const inter = Inter({ subsets: ['latin'] });

export const Layout = ({ children }: LayoutProps) => {
  return (
    <div className={`${inter.className} relative flex min-h-screen flex-col dark `}>
      <Header />
      <main className="flex-1 flex flex-col mb-12">
        {children}
      </main>
      <Footer />
    </div>
  )
}