import Link from "next/link";
import { CATEGORIES, ALL_OPERATIONS } from "../lib/tools";

export default function Home() {
  const totalCategories = CATEGORIES.length;
  const largestCategory = CATEGORIES.reduce((max, cat) =>
    cat.operations.length > max.operations.length ? cat : max
  );

  return (
    <div className="mx-auto max-w-[1180px] px-5 sm:px-8">
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
            letterSpacing: 0,
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
          className="mt-8 grid max-w-[760px] grid-cols-1 gap-3 sm:grid-cols-3 rise-in"
          style={{ animationDelay: "190ms" }}
        >
          <Metric value={ALL_OPERATIONS.length} label="tools" />
          <Metric value={totalCategories} label="domains" />
          <Metric value={largestCategory.operations.length} label={largestCategory.label} />
        </div>
        <div
          className="mt-9 flex flex-wrap items-center gap-4 rise-in"
          style={{ animationDelay: "260ms" }}
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

      <section className="pb-24">
        <div className="flex items-baseline justify-between mb-5">
          <h2
            className="font-display"
            style={{ fontSize: "clamp(22px, 3vw, 30px)" }}
          >
            What it computes
          </h2>
          <span className="eyebrow hidden sm:block">{totalCategories} disciplines</span>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {CATEGORIES.map((cat, i) => (
            <Link
              key={cat.id}
              href={`/calculator?cat=${cat.id}`}
              className="panel p-5 group rise-in transition-transform hover:-translate-y-1 tool-shell"
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
              <div className="mt-4 h-1.5 rounded-full bg-[var(--surface-sunk)] overflow-hidden">
                <div
                  className="h-full rounded-full bg-[var(--accent)]"
                  style={{
                    width: `${Math.max(
                      18,
                      (cat.operations.length / largestCategory.operations.length) * 100
                    )}%`,
                  }}
                />
              </div>
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

function Metric({ value, label }: { value: number; label: string }) {
  return (
    <div className="metric-tile">
      <div className="font-mono text-[24px] leading-none text-[var(--text)]">
        {value}
      </div>
      <div className="mt-1 font-mono text-[11px] uppercase text-[var(--muted)]">
        {label}
      </div>
    </div>
  );
}
