import { cn } from "@/lib/utils";
import Link, { LinkProps } from "next/link";
import { useRouter } from "next/router";

type ActiveLinkProps = {
  children: React.ReactNode;
} & LinkProps;

export const ActiveLink = ({ children, href, ...rest }: ActiveLinkProps) => {
  const router = useRouter();

  // Verifica se a rota atual é igual ao href ou se começa com o href (para sub-rotas)
  const isCurrentPath = 
    router.asPath === href || 
    router.asPath === rest.as || 
    (href !== "/" && router.asPath.startsWith(String(href)));

  return (
    <Link 
      href={href} 
      {...rest}
      className={cn(
        'text-sm font-medium transition-colors hover:text-blue-200',
        isCurrentPath ? 'text-blue-200 font-semibold' : 'text-gray-100'
      )}
    >
      {children}
    </Link>
  );
};