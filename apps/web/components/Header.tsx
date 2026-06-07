import Link from "next/link";
import CommandTrigger from "./CommandTrigger";

export default function Header() {
  return (
    <header className="site-header">
      <Link href="/" className="brandmark">
        <span className="brand-glyph">
          <img src="/favicon.ico" alt="" width={22} height={22} />
        </span>
        <span>
          The Elephant <span className="font-display">Calculator</span>
        </span>
      </Link>
      <nav className="flex items-center gap-1">
        <CommandTrigger />
        <Link href="/" className="header-link hidden sm:inline-flex">
          Overview
        </Link>
        <Link href="/calculator" className="header-link">
          Workspace
        </Link>
        <a
          href="/api/docs"
          target="_blank"
          rel="noreferrer"
          className="header-link"
        >
          API ↗
        </a>
      </nav>
    </header>
  );
}
