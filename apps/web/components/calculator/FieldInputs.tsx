"use client";

import type { Field } from "../../lib/tools";
import type { FormValue } from "../../lib/request";

interface FieldInputProps {
  field: Field;
  value: FormValue;
  onChange: (value: FormValue) => void;
}

export function FieldInput({ field, value, onChange }: FieldInputProps) {
  switch (field.type) {
    case "vector":
      return (
        <VectorInput
          label={field.label}
          value={value as string[]}
          onChange={(v) => onChange(v)}
        />
      );
    case "matrix":
      return (
        <MatrixInput
          label={field.label}
          value={value as string[][]}
          onChange={(v) => onChange(v)}
        />
      );
    case "bool":
      return (
        <ToggleInput
          checked={Boolean(value)}
          label={field.label}
          onChange={(v) => onChange(v)}
        />
      );
    case "select":
      return (
        <select
          className="text-input cursor-pointer"
          aria-label={field.label}
          value={value as string}
          onChange={(e) => onChange(e.target.value)}
        >
          {(field.options ?? []).map((o) => (
            <option key={o.value} value={o.value}>
              {o.label}
            </option>
          ))}
        </select>
      );
    case "textlist":
      return (
        <textarea
          className="text-input"
          aria-label={field.label}
          rows={4}
          spellCheck={false}
          value={value as string}
          onChange={(e) => onChange(e.target.value)}
        />
      );
    default:
      return (
        <input
          className="text-input"
          aria-label={field.label}
          inputMode={field.type === "text" ? "text" : "decimal"}
          spellCheck={false}
          value={value as string}
          placeholder={field.type === "text" ? "" : "0"}
          onChange={(e) => onChange(e.target.value)}
        />
      );
  }
}

function ToggleInput({
  checked,
  label,
  onChange,
}: {
  checked: boolean;
  label: string;
  onChange: (v: boolean) => void;
}) {
  return (
    <button
      type="button"
      role="switch"
      aria-checked={checked}
      onClick={() => onChange(!checked)}
      className="inline-flex items-center gap-3 select-none"
    >
      <span
        className="relative inline-block h-[24px] w-[44px] rounded-full transition-colors"
        style={{
          background: checked ? "var(--accent)" : "var(--surface-sunk)",
          border: "1px solid var(--rule)",
        }}
      >
        <span
          className="absolute top-[2px] h-[18px] w-[18px] rounded-full transition-all"
          style={{
            left: checked ? "22px" : "2px",
            background: "var(--surface)",
            boxShadow: "0 1px 2px rgba(0,0,0,0.3)",
          }}
        />
      </span>
      <span className="font-mono text-[13px] text-[var(--text-soft)]">
        {label}
      </span>
    </button>
  );
}

function VectorInput({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string[];
  onChange: (v: string[]) => void;
}) {
  const setCell = (i: number, cell: string) => {
    const next = [...value];
    next[i] = cell;
    onChange(next);
  };
  const add = () => onChange([...value, "0"]);
  const remove = () => value.length > 1 && onChange(value.slice(0, -1));

  return (
    <div className="flex flex-wrap items-center gap-2">
      <span className="font-mono text-[22px] text-[var(--muted)] leading-none">
        [
      </span>
      {value.map((cell, i) => (
        <input
          key={i}
          className="num-cell"
          aria-label={`${label} component ${i + 1}`}
          style={{ width: 60 }}
          inputMode="decimal"
          value={cell}
          onChange={(e) => setCell(i, e.target.value)}
        />
      ))}
      <span className="font-mono text-[22px] text-[var(--muted)] leading-none">
        ]
      </span>
      <div className="flex gap-1 ml-1">
        <StepButton label="−" onClick={remove} disabled={value.length <= 1} />
        <StepButton label="+" onClick={add} />
      </div>
    </div>
  );
}

function MatrixInput({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string[][];
  onChange: (v: string[][]) => void;
}) {
  const rows = value.length;
  const cols = value[0]?.length ?? 0;

  const setCell = (r: number, c: number, cell: string) => {
    const next = value.map((row) => [...row]);
    next[r][c] = cell;
    onChange(next);
  };
  const resize = (nextRows: number, nextCols: number) => {
    if (nextRows < 1 || nextCols < 1 || nextRows > 6 || nextCols > 6) return;
    const next: string[][] = [];
    for (let r = 0; r < nextRows; r++) {
      const row: string[] = [];
      for (let c = 0; c < nextCols; c++) {
        row.push(value[r]?.[c] ?? "0");
      }
      next.push(row);
    }
    onChange(next);
  };

  return (
    <div className="flex flex-wrap items-start gap-3">
      <div
        className="grid gap-1.5 p-2 rounded-md"
        style={{
          gridTemplateColumns: `repeat(${cols}, minmax(0, 1fr))`,
          background: "var(--surface-sunk)",
          borderLeft: "2px solid var(--ink)",
          borderRight: "2px solid var(--ink)",
        }}
      >
        {value.map((row, r) =>
          row.map((cell, c) => (
            <input
              key={`${r}-${c}`}
              className="num-cell"
              aria-label={`${label} row ${r + 1} column ${c + 1}`}
              style={{ width: 56 }}
              inputMode="decimal"
              value={cell}
              onChange={(e) => setCell(r, c, e.target.value)}
            />
          ))
        )}
      </div>
      <div className="flex flex-col gap-2 font-mono text-[11px] text-[var(--muted)]">
        <div className="flex items-center gap-1">
          <span className="w-10">rows</span>
          <StepButton label="−" onClick={() => resize(rows - 1, cols)} />
          <span className="w-4 text-center text-[var(--text)]">{rows}</span>
          <StepButton label="+" onClick={() => resize(rows + 1, cols)} />
        </div>
        <div className="flex items-center gap-1">
          <span className="w-10">cols</span>
          <StepButton label="−" onClick={() => resize(rows, cols - 1)} />
          <span className="w-4 text-center text-[var(--text)]">{cols}</span>
          <StepButton label="+" onClick={() => resize(rows, cols + 1)} />
        </div>
      </div>
    </div>
  );
}

function StepButton({
  label,
  onClick,
  disabled,
}: {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className="font-mono text-[15px] leading-none grid place-items-center h-7 w-7 rounded-md transition-colors disabled:opacity-40"
      style={{ background: "var(--surface)", border: "1px solid var(--rule)" }}
    >
      {label}
    </button>
  );
}
