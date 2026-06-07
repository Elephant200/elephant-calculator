"use client";

// Small header button that opens the global command palette. Decoupled from the
// palette via a window event so the header can stay mostly server-rendered.

export default function CommandTrigger() {
  return (
    <button
      type="button"
      aria-label="Search tools"
      onClick={() => window.dispatchEvent(new CustomEvent("elephant:command-open"))}
      className="header-link inline-flex items-center gap-2"
    >
      <span aria-hidden>Search</span>
      <kbd
        className="rounded px-1.5 py-0.5 text-[10px]"
        style={{ background: "var(--surface-sunk)", border: "1px solid var(--rule)" }}
      >
        ⌘K
      </kbd>
    </button>
  );
}
