import Link from "next/link";

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
        <Link href="/" className="header-link">
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
