"use client";

import { useState } from "react";
import type { ResultKind, TableRow } from "../../lib/tools";
import { formatNumber } from "../../lib/format";

export function ResultView({
  kind,
  value,
  label,
}: {
  kind: ResultKind;
  value: unknown;
  label?: string;
}) {
  return (
    <div className="ink-bleed">
      <div className="flex items-center justify-between mb-3">
        <span className="eyebrow">{label ?? "Result"}</span>
        <CopyButton text={plainText(kind, value)} />
      </div>
      <Rendered kind={kind} value={value} />
    </div>
  );
}

function Rendered({ kind, value }: { kind: ResultKind; value: unknown }) {
  switch (kind) {
    case "scalar":
      return <Big>{formatNumber(Number(value))}</Big>;

    case "string":
      return (
        <div className="font-mono text-[18px] leading-relaxed break-words whitespace-pre-wrap text-[var(--text)]">
          {String(value)}
        </div>
      );

    case "bool": {
      const v = Boolean(value);
      return (
        <div className="flex items-center gap-3">
          <span
            className="grid place-items-center h-9 w-9 rounded-full font-mono text-[18px]"
            style={{
              background: v ? "var(--accent-2)" : "var(--c-elephant)",
              color: "#fff",
            }}
          >
            {v ? "✓" : "✕"}
          </span>
          <Big>{v ? "Prime" : "Not prime"}</Big>
        </div>
      );
    }

    case "vector":
      return <VectorOut values={value as number[]} />;

    case "intlist":
      return <Chips values={value as number[]} />;

    case "matrix":
      return <MatrixOut rows={value as number[][]} />;

    case "triples":
      return <Triples rows={value as number[][]} />;

    case "triangle":
      return <Triangle data={value as Record<string, number>} />;

    case "table":
      return <LabelledTable rows={value as TableRow[]} />;

    case "exprvector":
      return <ExprVector items={value as string[]} />;

    case "exprmatrix":
      return <ExprMatrix rows={value as string[][]} />;

    default:
      return <Big>{String(value)}</Big>;
  }
}

function Big({ children }: { children: React.ReactNode }) {
  return (
    <div
      className="font-mono font-medium text-[var(--text)] break-words"
      style={{ fontSize: "clamp(26px, 4vw, 40px)", lineHeight: 1.1 }}
    >
      {children}
    </div>
  );
}

function VectorOut({ values }: { values: number[] }) {
  return (
    <div className="flex flex-wrap items-center gap-2 font-mono">
      <Bracket>[</Bracket>
      {values.map((v, i) => (
        <span
          key={i}
          className="px-3 py-2 rounded-md text-[18px]"
          style={{ background: "var(--surface-sunk)" }}
        >
          {formatNumber(v)}
        </span>
      ))}
      <Bracket>]</Bracket>
    </div>
  );
}

function Bracket({ children }: { children: React.ReactNode }) {
  return (
    <span className="text-[34px] text-[var(--muted)] leading-none">
      {children}
    </span>
  );
}

function Chips({ values }: { values: number[] }) {
  return (
    <div className="flex flex-wrap gap-2 font-mono">
      {values.map((v, i) => (
        <span
          key={i}
          className="px-2.5 py-1 rounded-md text-[15px]"
          style={{
            background: "var(--surface-sunk)",
            border: "1px solid var(--rule-soft)",
          }}
        >
          {formatNumber(v)}
        </span>
      ))}
    </div>
  );
}

function MatrixOut({ rows }: { rows: number[][] }) {
  const cols = rows[0]?.length ?? 0;
  return (
    <div
      className="inline-grid gap-1.5 p-3 rounded-md font-mono"
      style={{
        gridTemplateColumns: `repeat(${cols}, minmax(0, 1fr))`,
        borderLeft: "2px solid var(--ink)",
        borderRight: "2px solid var(--ink)",
        background: "var(--surface-sunk)",
      }}
    >
      {rows.map((row, r) =>
        row.map((v, c) => (
          <span
            key={`${r}-${c}`}
            className="px-3 py-2 text-center text-[16px] rounded"
            style={{ background: "var(--surface)" }}
          >
            {formatNumber(v)}
          </span>
        ))
      )}
    </div>
  );
}

function Triples({ rows }: { rows: number[][] }) {
  return (
    <div>
      <div className="font-mono text-[13px] text-[var(--muted)] mb-2">
        {rows.length} triple{rows.length === 1 ? "" : "s"}
      </div>
      <div className="flex flex-wrap gap-2 font-mono max-h-[280px] overflow-y-auto thin-scroll">
        {rows.map((t, i) => (
          <span
            key={i}
            className="px-3 py-1.5 rounded-md text-[14px]"
            style={{
              background: "var(--surface-sunk)",
              border: "1px solid var(--rule-soft)",
            }}
          >
            ({t.join(", ")})
          </span>
        ))}
      </div>
    </div>
  );
}

function ExprVector({ items }: { items: string[] }) {
  return (
    <div className="flex items-stretch gap-3 font-mono">
      <span
        className="w-[3px] rounded"
        style={{ background: "var(--ink, var(--text))" }}
      />
      <div className="flex flex-col gap-2 py-1">
        {items.map((s, i) => (
          <span key={i} className="text-[18px] text-[var(--text)] break-words">
            {s}
          </span>
        ))}
      </div>
    </div>
  );
}

function ExprMatrix({ rows }: { rows: string[][] }) {
  const cols = rows[0]?.length ?? 0;
  return (
    <div
      className="inline-grid gap-1.5 p-3 rounded-md font-mono"
      style={{
        gridTemplateColumns: `repeat(${cols}, minmax(0, 1fr))`,
        borderLeft: "2px solid var(--text)",
        borderRight: "2px solid var(--text)",
        background: "var(--surface-sunk)",
      }}
    >
      {rows.map((row, r) =>
        row.map((s, c) => (
          <span
            key={`${r}-${c}`}
            className="px-3 py-2 text-center text-[15px] rounded"
            style={{ background: "var(--surface)" }}
          >
            {s}
          </span>
        ))
      )}
    </div>
  );
}

function LabelledTable({ rows }: { rows: TableRow[] }) {
  return (
    <div className="flex flex-col divide-y divide-[var(--rule-soft)] font-mono">
      {rows.map((r) => (
        <div
          key={r.label}
          className="flex items-baseline justify-between gap-6 py-2"
        >
          <span className="text-[14px] text-[var(--muted)]">{r.label}</span>
          <span className="text-[18px] text-[var(--text)] text-right break-all">
            {r.value}
          </span>
        </div>
      ))}
    </div>
  );
}

function Triangle({ data }: { data: Record<string, number> }) {
  const sides = ["a", "b", "c"];
  const angles = ["A", "B", "C"];
  return (
    <div className="flex flex-wrap gap-8">
      <Column title="Sides" keys={sides} data={data} />
      <Column title="Angles (°)" keys={angles} data={data} />
    </div>
  );
}

function Column({
  title,
  keys,
  data,
}: {
  title: string;
  keys: string[];
  data: Record<string, number>;
}) {
  return (
    <div>
      <div className="eyebrow mb-2">{title}</div>
      <div className="flex flex-col gap-1.5 font-mono">
        {keys.map((k) => (
          <div key={k} className="flex items-baseline gap-3">
            <span className="text-[var(--accent)] w-5 text-[18px]">{k}</span>
            <span className="text-[20px]">
              {data[k] != null ? formatNumber(data[k]) : "—"}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

function plainText(kind: ResultKind, value: unknown): string {
  switch (kind) {
    case "vector":
    case "intlist":
      return `[${(value as number[]).join(", ")}]`;
    case "matrix":
    case "exprmatrix":
      return (value as unknown[][]).map((r) => r.join("\t")).join("\n");
    case "exprvector":
      return (value as string[]).join("\n");
    case "triples":
      return (value as number[][]).map((t) => `(${t.join(", ")})`).join("\n");
    case "table":
      return (value as TableRow[])
        .map((r) => `${r.label}\t${r.value}`)
        .join("\n");
    case "triangle": {
      const d = value as Record<string, number>;
      return ["a", "b", "c", "A", "B", "C"]
        .map((k) => `${k} = ${d[k]}`)
        .join("\n");
    }
    default:
      return String(value);
  }
}

function CopyButton({ text }: { text: string }) {
  const [copied, setCopied] = useState(false);
  return (
    <button
      type="button"
      className="font-mono text-[11px] uppercase tracking-wider text-[var(--muted)] hover:text-[var(--text)] transition-colors"
      onClick={async () => {
        try {
          await navigator.clipboard.writeText(text);
          setCopied(true);
          setTimeout(() => setCopied(false), 1400);
        } catch {
          /* clipboard unavailable */
        }
      }}
    >
      {copied ? "copied ✓" : "copy"}
    </button>
  );
}
