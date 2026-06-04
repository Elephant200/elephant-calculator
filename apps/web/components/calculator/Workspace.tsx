"use client";

import { useEffect, useState } from "react";
import {
  CATEGORIES,
  ALL_OPERATIONS,
  type Category,
  type Operation,
  type ResultKind,
} from "../../lib/tools";
import {
  buildRequest,
  initFormState,
  initQueryState,
  ValidationError,
  type FormState,
  type FormValue,
  type QueryState,
} from "../../lib/request";
import { ApiError, callApi } from "../../lib/api";
import { FieldInput } from "./FieldInputs";
import { ResultView } from "./ResultView";

interface ResultEntry {
  id: string;
  opId: string;
  opLabel: string;
  categoryLabel: string;
  kind: ResultKind;
  resultLabel?: string;
  value: unknown;
  summary: string;
}

let entrySeq = 0;
// Unique across page reloads so localStorage-restored entries never collide
// with freshly computed ones (which previously both started at 1).
const nextEntryId = () => `${Date.now()}-${++entrySeq}`;

export default function Workspace() {
  const [activeCat, setActiveCat] = useState<Category>(CATEGORIES[0]);
  const [op, setOp] = useState<Operation>(CATEGORIES[0].operations[0]);
  const [values, setValues] = useState<FormState>(() =>
    initFormState(CATEGORIES[0].operations[0])
  );
  const [queryValues, setQueryValues] = useState<QueryState>(() =>
    initQueryState(CATEGORIES[0].operations[0])
  );
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<{ type: string; message: string } | null>(
    null
  );
  const [result, setResult] = useState<ResultEntry | null>(null);
  const [history, setHistory] = useState<ResultEntry[]>([]);
  const [search, setSearch] = useState("");

  // Restore the tape from a previous visit.
  useEffect(() => {
    try {
      const saved = localStorage.getItem("elephant-history");
      if (saved) setHistory(JSON.parse(saved));
    } catch {
      /* ignore corrupt storage */
    }
  }, []);
  useEffect(() => {
    try {
      localStorage.setItem("elephant-history", JSON.stringify(history));
    } catch {
      /* storage may be unavailable */
    }
  }, [history]);

  // Compute on ⌘/Ctrl+Enter from anywhere on the page.
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
        e.preventDefault();
        compute();
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  });

  function selectOperation(nextOp: Operation, cat: Category) {
    setActiveCat(cat);
    setOp(nextOp);
    setValues(initFormState(nextOp));
    setQueryValues(initQueryState(nextOp));
    setError(null);
    setResult(null);
  }

  function setFieldValue(name: string, value: FormValue) {
    setValues((prev) => ({ ...prev, [name]: value }));
  }
  function setQueryValue(name: string, value: string | boolean) {
    setQueryValues((prev) => ({ ...prev, [name]: value }));
  }

  async function compute() {
    setError(null);
    let request;
    try {
      request = buildRequest(op, values, queryValues);
    } catch (e) {
      if (e instanceof ValidationError) {
        setError({ type: "Check your input", message: e.message });
        return;
      }
      throw e;
    }

    setLoading(true);
    try {
      const value = await callApi<unknown>(op.endpoint, {
        method: op.method ?? "POST",
        body: request.body,
        query: request.query,
      });
      const entry: ResultEntry = {
        id: nextEntryId(),
        opId: op.id,
        opLabel: op.label,
        categoryLabel: activeCat.label,
        kind: op.result,
        resultLabel: op.resultLabel,
        value,
        summary: summarize(op.result, value),
      };
      setResult(entry);
      setHistory((prev) => [entry, ...prev].slice(0, 12));
    } catch (e) {
      if (e instanceof ApiError) {
        setError({ type: e.errorType, message: e.message });
      } else {
        setError({ type: "Unexpected error", message: String(e) });
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mx-auto max-w-[1240px] px-4 sm:px-6 lg:px-8 py-8">
      <div className="grid grid-cols-1 lg:grid-cols-[248px_1fr] gap-6 lg:gap-8">
        <Rail
          activeCat={activeCat}
          activeOpId={op.id}
          onSelect={selectOperation}
          search={search}
          onSearch={setSearch}
        />

        <div className="min-w-0">
          <OperationHeader op={op} category={activeCat} />

          <form
            className="panel p-5 sm:p-7 mt-4"
            onSubmit={(e) => {
              e.preventDefault();
              compute();
            }}
          >
            <div className="flex flex-col gap-5">
              {op.fields.length === 0 && (
                <p className="font-mono text-[13px] text-[var(--muted)]">
                  No inputs required — choose a precision and compute.
                </p>
              )}
              {op.fields.map((field) => (
                <div key={field.name}>
                  {field.type !== "bool" && (
                    <label className="field-label">{field.label}</label>
                  )}
                  <FieldInput
                    field={field}
                    value={values[field.name]}
                    onChange={(v) => setFieldValue(field.name, v)}
                  />
                  {field.help && (
                    <p className="mt-1.5 text-[13px] text-[var(--muted)]">
                      {field.help}
                    </p>
                  )}
                </div>
              ))}

              {op.query && op.query.length > 0 && (
                <div className="flex flex-wrap items-end gap-5 pt-1 border-t border-[var(--rule-soft)]">
                  {op.query.map((q) => (
                    <div key={q.name}>
                      {q.type === "bool" ? (
                        <label className="inline-flex items-center gap-2 cursor-pointer pt-3">
                          <input
                            type="checkbox"
                            checked={Boolean(queryValues[q.name])}
                            onChange={(e) =>
                              setQueryValue(q.name, e.target.checked)
                            }
                            className="accent-[var(--accent)] h-4 w-4"
                          />
                          <span className="font-mono text-[13px] text-[var(--text-soft)]">
                            {q.label}
                          </span>
                        </label>
                      ) : (
                        <div>
                          <label className="field-label">{q.label}</label>
                          <input
                            className="text-input"
                            style={{ width: 140 }}
                            inputMode="numeric"
                            value={String(queryValues[q.name] ?? "")}
                            onChange={(e) =>
                              setQueryValue(q.name, e.target.value)
                            }
                          />
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>

            <div className="flex items-center gap-3 mt-7">
              <button
                type="submit"
                className="btn btn-accent"
                disabled={loading}
              >
                {loading ? "Computing…" : "Compute"}
              </button>
              <button
                type="button"
                className="btn btn-ghost"
                onClick={() => selectOperation(op, activeCat)}
              >
                Reset
              </button>
            </div>
          </form>

          <ResultPanel error={error} result={result} />

          {history.length > 0 && (
            <HistoryTape
              history={history}
              onPick={(entry) => setResult(entry)}
              onClear={() => setHistory([])}
            />
          )}
        </div>
      </div>
    </div>
  );
}

const CATEGORY_OF = new Map<string, Category>(
  CATEGORIES.flatMap((c) => c.operations.map((o) => [o.id, c] as const))
);

function Rail({
  activeCat,
  activeOpId,
  onSelect,
  search,
  onSearch,
}: {
  activeCat: Category;
  activeOpId: string;
  onSelect: (op: Operation, cat: Category) => void;
  search: string;
  onSearch: (v: string) => void;
}) {
  const q = search.trim().toLowerCase();
  const matches = q
    ? ALL_OPERATIONS.filter((o) => {
        const cat = CATEGORY_OF.get(o.id)!;
        return (
          o.label.toLowerCase().includes(q) ||
          o.blurb.toLowerCase().includes(q) ||
          cat.label.toLowerCase().includes(q)
        );
      })
    : [];

  return (
    <aside className="lg:sticky lg:top-[84px] lg:self-start lg:max-h-[calc(100vh-104px)] lg:overflow-y-auto thin-scroll -mx-1 px-1">
      <input
        className="text-input mb-3"
        placeholder="Search tools…"
        value={search}
        onChange={(e) => onSearch(e.target.value)}
        spellCheck={false}
      />
      {q ? (
        <nav className="flex flex-col gap-0.5">
          {matches.length === 0 && (
            <p className="font-mono text-[12px] text-[var(--muted)] px-2 py-3">
              No tools match “{search}”.
            </p>
          )}
          {matches.map((o) => {
            const cat = CATEGORY_OF.get(o.id)!;
            const on = o.id === activeOpId;
            return (
              <button
                key={o.id}
                type="button"
                onClick={() => onSelect(o, cat)}
                className="text-left px-2.5 py-1.5 rounded-md transition-colors"
                style={{
                  background: on ? "var(--surface-sunk)" : "transparent",
                }}
              >
                <span
                  className="font-mono text-[13.5px]"
                  style={{ color: on ? "var(--accent-deep)" : "var(--text)" }}
                >
                  {o.label}
                </span>
                <span className="block text-[11px] text-[var(--muted)]">
                  {cat.label}
                </span>
              </button>
            );
          })}
        </nav>
      ) : (
      <nav className="flex flex-col gap-1">
        {CATEGORIES.map((cat) => {
          const active = cat.id === activeCat.id;
          return (
            <div key={cat.id}>
              <button
                type="button"
                onClick={() => onSelect(cat.operations[0], cat)}
                className="w-full text-left px-3 py-2 rounded-md transition-colors"
                style={{
                  background: active ? "var(--surface)" : "transparent",
                  border: active
                    ? "1px solid var(--rule)"
                    : "1px solid transparent",
                }}
              >
                <div className="font-display font-bold text-[15px]">
                  {cat.label}
                </div>
                <div className="text-[12px] text-[var(--muted)] leading-tight">
                  {cat.tagline}
                </div>
              </button>
              {active && (
                <div className="mt-1 mb-2 ml-2 pl-2 border-l border-[var(--rule)] flex flex-col">
                  {cat.operations.map((o) => {
                    const on = o.id === activeOpId;
                    return (
                      <button
                        key={o.id}
                        type="button"
                        onClick={() => onSelect(o, cat)}
                        className="text-left px-2.5 py-1.5 rounded-md text-[13.5px] font-mono transition-colors"
                        style={{
                          background: on ? "var(--surface-sunk)" : "transparent",
                          color: on ? "var(--accent-deep)" : "var(--text-soft)",
                          fontWeight: on ? 600 : 400,
                        }}
                      >
                        {o.label}
                      </button>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
      </nav>
      )}
    </aside>
  );
}

function OperationHeader({
  op,
  category,
}: {
  op: Operation;
  category: Category;
}) {
  return (
    <div className="rise-in" key={op.id}>
      <div className="eyebrow">{category.label}</div>
      <h1
        className="font-display mt-1"
        style={{ fontSize: "clamp(28px, 4vw, 40px)" }}
      >
        {op.label}
      </h1>
      <p className="mt-2 text-[var(--text-soft)] max-w-[60ch]">{op.blurb}</p>
    </div>
  );
}

function ResultPanel({
  error,
  result,
}: {
  error: { type: string; message: string } | null;
  result: ResultEntry | null;
}) {
  if (error) {
    return (
      <div
        className="mt-5 p-5 rounded-md ink-bleed"
        style={{
          background: "color-mix(in srgb, var(--accent) 8%, var(--surface))",
          border: "1px solid color-mix(in srgb, var(--accent) 45%, var(--rule))",
        }}
      >
        <div className="eyebrow" style={{ color: "var(--accent-deep)" }}>
          {error.type}
        </div>
        <p className="mt-1.5 font-mono text-[14px] text-[var(--text)] break-words">
          {error.message}
        </p>
      </div>
    );
  }

  if (result) {
    return (
      <div className="panel p-5 sm:p-7 mt-5">
        <ResultView
          kind={result.kind}
          value={result.value}
          label={result.resultLabel}
        />
      </div>
    );
  }

  return (
    <div
      className="mt-5 p-7 rounded-md text-center"
      style={{ border: "1px dashed var(--rule)" }}
    >
      <p className="font-mono text-[13px] text-[var(--muted)]">
        Enter values and press Compute to see the result.
      </p>
    </div>
  );
}

function HistoryTape({
  history,
  onPick,
  onClear,
}: {
  history: ResultEntry[];
  onPick: (entry: ResultEntry) => void;
  onClear: () => void;
}) {
  return (
    <div className="mt-8">
      <div className="flex items-center justify-between mb-2">
        <span className="eyebrow">Tape · recent results</span>
        <button
          type="button"
          className="font-mono text-[11px] uppercase tracking-wider text-[var(--muted)] hover:text-[var(--text)]"
          onClick={onClear}
        >
          clear
        </button>
      </div>
      <div className="flex flex-col divide-y divide-[var(--rule-soft)] panel overflow-hidden">
        {history.map((h) => (
          <button
            key={h.id}
            type="button"
            onClick={() => onPick(h)}
            className="flex items-center justify-between gap-4 px-4 py-2.5 text-left hover:bg-[var(--surface-sunk)] transition-colors"
          >
            <span className="font-mono text-[12px] text-[var(--muted)] shrink-0 w-[150px] truncate">
              {h.categoryLabel} · {h.opLabel}
            </span>
            <span className="font-mono text-[14px] text-[var(--text)] truncate text-right">
              {h.summary}
            </span>
          </button>
        ))}
      </div>
    </div>
  );
}

function summarize(kind: ResultKind, value: unknown): string {
  switch (kind) {
    case "matrix":
    case "exprmatrix": {
      const m = value as unknown[][];
      return `${m.length}×${m[0]?.length ?? 0} matrix`;
    }
    case "vector":
      return `[${(value as number[]).join(", ")}]`;
    case "exprvector":
      return `(${(value as string[]).join(", ")})`;
    case "intlist": {
      const a = value as number[];
      const head = a.slice(0, 6).join(", ");
      return a.length > 6 ? `[${head}, …]` : `[${head}]`;
    }
    case "triples":
      return `${(value as number[][]).length} triples`;
    case "triangle": {
      const d = value as Record<string, number>;
      return `a${fmt(d.a)} b${fmt(d.b)} c${fmt(d.c)}`;
    }
    case "bool":
      return value ? "prime" : "not prime";
    default: {
      const s = String(value);
      return s.length > 40 ? s.slice(0, 39) + "…" : s;
    }
  }
}

function fmt(n: number): string {
  if (n == null) return "?";
  return Number.isInteger(n) ? String(n) : n.toFixed(2);
}
