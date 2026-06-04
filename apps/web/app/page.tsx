import Link from "next/link";
import { CATEGORIES, ALL_OPERATIONS } from "../lib/tools";

export default function Home() {
  return (
    <div className="mx-auto max-w-[1180px] px-5 sm:px-8">
      {/* ---- Hero ---- */}
      <section className="pt-16 sm:pt-24 pb-14">
        <div
          className="eyebrow rise-in"
          style={{ animationDelay: "0ms" }}
        >
          {ALL_OPERATIONS.length} tools · one instrument
        </div>
        <h1
          className="font-display mt-4 rise-in"
          style={{
            fontSize: "clamp(44px, 8vw, 96px)",
            lineHeight: 0.98,
            letterSpacing: "-0.03em",
            animationDelay: "60ms",
          }}
        >
          The Elephant
          <br />
          <span style={{ color: "var(--accent)" }}>Calculator</span>
        </h1>
        <p
          className="mt-6 max-w-[58ch] text-[18px] sm:text-[20px] text-[var(--text-soft)] rise-in"
          style={{ animationDelay: "140ms" }}
        >
          A precision computing instrument with the memory of a herd — vectors
          and matrices, geometry, primes, arbitrary-precision arithmetic, and a
          full computer-algebra system, all wrapped around one fast Python
          engine.
        </p>
        <div
          className="mt-9 flex flex-wrap items-center gap-4 rise-in"
          style={{ animationDelay: "220ms" }}
        >
          <Link href="/calculator" className="btn btn-accent">
            Open the workspace →
          </Link>
          <a
            href="/api/docs"
            target="_blank"
            rel="noreferrer"
            className="btn btn-ghost"
          >
            Browse the API
          </a>
        </div>
      </section>

      {/* ---- Capability grid ---- */}
      <section className="pb-24">
        <div className="flex items-baseline justify-between mb-5">
          <h2
            className="font-display"
            style={{ fontSize: "clamp(22px, 3vw, 30px)" }}
          >
            What it computes
          </h2>
          <span className="eyebrow hidden sm:block">eight disciplines</span>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {CATEGORIES.map((cat, i) => (
            <Link
              key={cat.id}
              href="/calculator"
              className="panel p-5 group rise-in transition-transform hover:-translate-y-1"
              style={{ animationDelay: `${120 + i * 55}ms` }}
            >
              <div className="flex items-start justify-between">
                <h3
                  className="font-display"
                  style={{ fontSize: "20px" }}
                >
                  {cat.label}
                </h3>
                <span
                  className="font-mono text-[12px] px-2 py-0.5 rounded-full"
                  style={{
                    background: "var(--surface-sunk)",
                    color: "var(--muted)",
                  }}
                >
                  {cat.operations.length}
                </span>
              </div>
              <p className="mt-2 text-[15px] text-[var(--text-soft)]">
                {cat.tagline}
              </p>
              <div className="mt-4 font-mono text-[12px] text-[var(--muted)] flex flex-wrap gap-x-3 gap-y-1">
                {cat.operations.slice(0, 4).map((o) => (
                  <span key={o.id}>{o.label}</span>
                ))}
                {cat.operations.length > 4 && (
                  <span style={{ color: "var(--accent)" }}>
                    +{cat.operations.length - 4} more
                  </span>
                )}
              </div>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
