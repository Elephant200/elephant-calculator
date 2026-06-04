import Link from "next/link";

function ElephantMark() {
  // Compact elephant silhouette — head, trunk and ear.
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden>
      <path d="M3.4 6.1C5 4 7.6 2.8 10.4 2.8c4.6 0 8.1 3.3 8.1 7.8 0 1.5-.2 2.6-.2 3.8 0 1.3.5 1.9 1.3 2.4.7.4 1 .9 1 1.6 0 1.1-.9 1.9-2.1 1.9-1.6 0-2.7-1.2-2.7-3.1v-3c0-.6-.4-1-1-1s-1 .4-1 1v4.7c0 .3-.2.5-.5.5h-1.4c-.3 0-.5-.2-.5-.5v-3.2c-.9.4-1.9.6-3 .6-.5 0-1 0-1.5-.1v2.7c0 .3-.2.5-.5.5H4c-.3 0-.5-.2-.5-.5v-3.6C2 14.6 1.2 12.8 1.2 10.6c0-1.7.8-3.2 2.2-4.5Zm3.7 2.1a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4Z" />
    </svg>
  );
}

export default function Header() {
  return (
    <header className="site-header">
      <Link href="/" className="brandmark">
        <span className="brand-glyph">
          <ElephantMark />
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
