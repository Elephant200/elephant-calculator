"use client";

// Global "jump to any tool" palette. Open with ⌘K / Ctrl-K (or the header
// button, which dispatches "elephant:command-open"). Selecting a tool navigates
// to the calculator with that operation pre-selected; if the calculator is
// already mounted it also fires "elephant:navigate" so it updates live.

import { useEffect, useMemo, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { CATEGORIES } from "../lib/tools";

type Entry = {
  opId: string;
  catId: string;
  label: string;
  catLabel: string;
  blurb: string;
};

const ENTRIES: Entry[] = CATEGORIES.flatMap((c) =>
  c.operations.map((o) => ({
    opId: o.id,
    catId: c.id,
    label: o.label,
    catLabel: c.label,
    blurb: o.blurb,
  }))
);

export default function CommandPalette() {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [active, setActive] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLDivElement>(null);

  // Open/close wiring: ⌘K / Ctrl-K toggles; header button & Escape too.
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setOpen((v) => !v);
      } else if (e.key === "Escape") {
        setOpen(false);
      }
    }
    function onOpen() {
      setOpen(true);
    }
    window.addEventListener("keydown", onKey);
    window.addEventListener("elephant:command-open", onOpen);
    return () => {
      window.removeEventListener("keydown", onKey);
      window.removeEventListener("elephant:command-open", onOpen);
    };
  }, []);

  // Reset state each time it opens and focus the input.
  useEffect(() => {
    if (open) {
      setQuery("");
      setActive(0);
      requestAnimationFrame(() => inputRef.current?.focus());
    }
  }, [open]);

  const results = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return ENTRIES.slice(0, 60);
    return ENTRIES.filter(
      (e) =>
        e.label.toLowerCase().includes(q) ||
        e.catLabel.toLowerCase().includes(q) ||
        e.blurb.toLowerCase().includes(q)
    ).slice(0, 60);
  }, [query]);

  useEffect(() => {
    setActive(0);
  }, [query]);

  function choose(entry: Entry | undefined) {
    if (!entry) return;
    setOpen(false);
    window.dispatchEvent(
      new CustomEvent("elephant:navigate", {
        detail: { catId: entry.catId, opId: entry.opId },
      })
    );
    router.push(`/calculator?cat=${entry.catId}&op=${entry.opId}`);
  }

  function onListKey(e: React.KeyboardEvent) {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActive((a) => Math.min(a + 1, results.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActive((a) => Math.max(a - 1, 0));
    } else if (e.key === "Enter") {
      e.preventDefault();
      choose(results[active]);
    }
  }

  // Keep the active row scrolled into view.
  useEffect(() => {
    const el = listRef.current?.querySelector<HTMLElement>(`[data-idx="${active}"]`);
    el?.scrollIntoView({ block: "nearest" });
  }, [active]);

  if (!open) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-start justify-center px-4 pt-[12vh]"
      style={{ background: "color-mix(in srgb, var(--c-ink) 38%, transparent)" }}
      onMouseDown={() => setOpen(false)}
    >
      <div
        className="panel w-full max-w-[620px] overflow-hidden"
        onMouseDown={(e) => e.stopPropagation()}
        onKeyDown={onListKey}
      >
        <div className="border-b border-[var(--rule)] p-3">
          <input
            ref={inputRef}
            className="text-input"
            placeholder="Search all tools — try “determinant”, “prime”, “hexagon”…"
            value={query}
            spellCheck={false}
            onChange={(e) => setQuery(e.target.value)}
          />
        </div>
        <div ref={listRef} className="max-h-[52vh] overflow-y-auto thin-scroll p-1.5">
          {results.length === 0 && (
            <p className="px-3 py-6 text-center font-mono text-[13px] text-[var(--muted)]">
              No tools match “{query}”.
            </p>
          )}
          {results.map((e, i) => (
            <button
              key={`${e.catId}:${e.opId}`}
              data-idx={i}
              type="button"
              onMouseEnter={() => setActive(i)}
              onClick={() => choose(e)}
              className="flex w-full items-center justify-between gap-3 rounded-md px-3 py-2 text-left transition-colors"
              style={{ background: i === active ? "var(--surface-sunk)" : "transparent" }}
            >
              <span className="min-w-0">
                <span
                  className="block font-display text-[15px]"
                  style={{ color: i === active ? "var(--accent-deep)" : "var(--text)" }}
                >
                  {e.label}
                </span>
                <span className="block truncate font-mono text-[11px] text-[var(--muted)]">
                  {e.blurb}
                </span>
              </span>
              <span className="soft-chip shrink-0">{e.catLabel}</span>
            </button>
          ))}
        </div>
        <div className="flex items-center justify-between border-t border-[var(--rule)] px-3 py-2 font-mono text-[11px] text-[var(--muted)]">
          <span>{results.length} tool{results.length === 1 ? "" : "s"}</span>
          <span>↑↓ to move · ↵ to open · esc to close</span>
        </div>
      </div>
    </div>
  );
}
