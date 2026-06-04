import type { Operation, Field, QueryParam } from "./tools";

// Form state value shapes (what the inputs edit):
//   number/int/text → string
//   bool            → boolean
//   vector          → string[]
//   matrix          → string[][]
//   textlist        → string (newline-separated, split on submit)
export type FormValue = string | boolean | string[] | string[][];
export type FormState = Record<string, FormValue>;
export type QueryState = Record<string, string | boolean>;

export class ValidationError extends Error {}

export function initFormState(op: Operation): FormState {
  const state: FormState = {};
  for (const f of op.fields) {
    state[f.name] = initFieldValue(f);
  }
  return state;
}

function initFieldValue(f: Field): FormValue {
  switch (f.type) {
    case "vector":
      return (f.initial as number[]).map(String);
    case "matrix":
      return (f.initial as number[][]).map((row) => row.map(String));
    case "textlist":
      return (f.initial as string[]).join("\n");
    case "bool":
      return Boolean(f.initial);
    default:
      return String(f.initial ?? "");
  }
}

export function initQueryState(op: Operation): QueryState {
  const state: QueryState = {};
  for (const q of op.query ?? []) {
    state[q.name] = q.type === "bool" ? Boolean(q.initial) : String(q.initial);
  }
  return state;
}

function parseFiniteNumber(raw: string, label: string): number {
  const trimmed = raw.trim();
  if (trimmed === "") throw new ValidationError(`${label} is required.`);
  const n = Number(trimmed);
  if (!Number.isFinite(n))
    throw new ValidationError(`${label} must be a number (got "${raw}").`);
  return n;
}

function parseIntStrict(raw: string, label: string): number {
  const trimmed = raw.trim();
  if (trimmed === "") throw new ValidationError(`${label} is required.`);
  if (!/^-?\d+$/.test(trimmed))
    throw new ValidationError(`${label} must be a whole number (got "${raw}").`);
  return parseInt(trimmed, 10);
}

export interface BuiltRequest {
  body?: unknown;
  query?: Record<string, string | number | boolean>;
}

export function buildRequest(
  op: Operation,
  values: FormState,
  queryValues: QueryState
): BuiltRequest {
  const body: Record<string, unknown> = {};

  for (const f of op.fields) {
    const v = values[f.name];
    switch (f.type) {
      case "number": {
        const s = (v as string).trim();
        if (f.optional && s === "") break;
        body[f.name] = parseFiniteNumber(v as string, f.label);
        break;
      }
      case "int": {
        const s = (v as string).trim();
        if (f.optional && s === "") break;
        body[f.name] = parseIntStrict(v as string, f.label);
        break;
      }
      case "text": {
        const s = (v as string).trim();
        if (f.optional && s === "") break;
        if (s === "") throw new ValidationError(`${f.label} is required.`);
        body[f.name] = s;
        break;
      }
      case "bool":
        body[f.name] = Boolean(v);
        break;
      case "vector":
        body[f.name] = (v as string[]).map((cell, i) =>
          parseFiniteNumber(cell, `${f.label}[${i + 1}]`)
        );
        break;
      case "matrix":
        body[f.name] = (v as string[][]).map((row, r) =>
          row.map((cell, c) =>
            parseFiniteNumber(cell, `${f.label} (row ${r + 1}, col ${c + 1})`)
          )
        );
        break;
      case "textlist": {
        const lines = (v as string)
          .split("\n")
          .map((l) => l.trim())
          .filter(Boolean);
        if (lines.length === 0)
          throw new ValidationError(`${f.label} needs at least one entry.`);
        body[f.name] = lines;
        break;
      }
    }
  }

  const query: Record<string, string | number | boolean> = {};
  for (const q of op.query ?? []) {
    query[q.name] = coerceQuery(q, queryValues[q.name]);
  }

  const hasBody = op.fields.length > 0;
  return {
    body: hasBody ? body : undefined,
    query: op.query && op.query.length ? query : undefined,
  };
}

function coerceQuery(
  q: QueryParam,
  value: string | boolean
): string | number | boolean {
  if (q.type === "bool") return Boolean(value);
  return parseIntStrict(String(value), q.label);
}
