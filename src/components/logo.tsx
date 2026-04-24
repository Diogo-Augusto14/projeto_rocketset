import Image from "next/image";
import Link from "next/link";

export const Logo = () => {
  return (
    <Link href="/">
      <Image src="/logo.png" alt="logo" width={116} height={32} />
    </Link>
  );
};
