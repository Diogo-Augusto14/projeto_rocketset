import { Html, Head, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html lang="en" className="scroll-smooth">
      <Head />
      <body className="antialiased bg-slate-950 text-slate-50">
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
