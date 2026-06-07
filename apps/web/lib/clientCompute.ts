// Client-side calculators that run instantly in the browser, with no API round
// trip. Each function receives the already-parsed request body (see
// buildRequest) and returns a value matching its operation's ResultKind.
//
// Throwing a plain Error surfaces its message to the user as a validation note.

import { formatNumber } from "./format";
import type { TableRow } from "./tools";

// ---- Descriptive statistics ----------------------------------------------

function dataset(body: Record<string, unknown>): number[] {
  const data = body.data as number[] | undefined;
  if (!data || data.length === 0) {
    throw new Error("Enter at least one value.");
  }
  return data;
}

const sum = (xs: number[]) => xs.reduce((a, b) => a + b, 0);
const mean = (xs: number[]) => sum(xs) / xs.length;

function median(xs: number[]): number {
  const s = [...xs].sort((a, b) => a - b);
  const mid = Math.floor(s.length / 2);
  return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
}

function modes(xs: number[]): number[] {
  const counts = new Map<number, number>();
  for (const x of xs) counts.set(x, (counts.get(x) ?? 0) + 1);
  const max = Math.max(...counts.values());
  if (max === 1) return []; // every value unique → no mode
  return [...counts.entries()]
    .filter(([, c]) => c === max)
    .map(([v]) => v)
    .sort((a, b) => a - b);
}

// Sum of squared deviations from the mean.
function sumSqDev(xs: number[]): number {
  const m = mean(xs);
  return sum(xs.map((x) => (x - m) ** 2));
}

function variance(xs: number[], sample: boolean): number {
  const n = sample ? xs.length - 1 : xs.length;
  if (n <= 0) throw new Error("Sample variance needs at least two values.");
  return sumSqDev(xs) / n;
}

export function statsMean(body: Record<string, unknown>): number {
  return mean(dataset(body));
}

export function statsMedian(body: Record<string, unknown>): number {
  return median(dataset(body));
}

export function statsMode(body: Record<string, unknown>): number[] {
  const m = modes(dataset(body));
  if (m.length === 0) throw new Error("No mode — every value occurs once.");
  return m;
}

export function statsStdDev(body: Record<string, unknown>): number {
  const sample = body.sample !== false; // default to sample std dev
  return Math.sqrt(variance(dataset(body), sample));
}

export function statsSummary(body: Record<string, unknown>): TableRow[] {
  const xs = dataset(body);
  const s = [...xs].sort((a, b) => a - b);
  const popVar = variance(xs, false);
  const rows: [string, number][] = [
    ["Count", xs.length],
    ["Sum", sum(xs)],
    ["Mean", mean(xs)],
    ["Median", median(xs)],
    ["Minimum", s[0]],
    ["Maximum", s[s.length - 1]],
    ["Range", s[s.length - 1] - s[0]],
    ["Population variance", popVar],
    ["Population std dev", Math.sqrt(popVar)],
  ];
  if (xs.length > 1) {
    const sampVar = variance(xs, true);
    rows.push(["Sample variance", sampVar], ["Sample std dev", Math.sqrt(sampVar)]);
  }

  const out: TableRow[] = rows.map(([label, value]) => ({
    label,
    value: formatNumber(value),
  }));
  // Mode is rendered specially — it may be a set of values or absent.
  const m = modes(xs);
  out.push({ label: "Mode", value: m.length ? m.map(formatNumber).join(", ") : "none" });
  return out;
}

// ---- Number base conversion ----------------------------------------------

const DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz";

export function baseConvert(body: Record<string, unknown>): TableRow[] {
  const raw = String(body.number ?? "").trim();
  const fromBase = Number(body.from_base);

  if (!Number.isInteger(fromBase) || fromBase < 2 || fromBase > 36) {
    throw new Error("Source base must be a whole number from 2 to 36.");
  }
  if (raw === "") throw new Error("Enter a number to convert.");

  const negative = raw.startsWith("-");
  const body0 = (negative ? raw.slice(1) : raw).toLowerCase();
  if (body0 === "") throw new Error("Enter a number to convert.");

  let value = 0;
  for (const ch of body0) {
    const digit = DIGITS.indexOf(ch);
    if (digit < 0 || digit >= fromBase) {
      throw new Error(`"${ch}" is not a valid digit in base ${fromBase}.`);
    }
    value = value * fromBase + digit;
  }
  if (!Number.isSafeInteger(value)) {
    throw new Error("Value is too large to convert precisely.");
  }
  const sign = negative ? "-" : "";
  const to = (b: number) => sign + (value === 0 ? "0" : value.toString(b));

  return [
    { label: "Decimal (10)", value: to(10) },
    { label: "Binary (2)", value: to(2) },
    { label: "Octal (8)", value: to(8) },
    { label: "Hexadecimal (16)", value: to(16).toUpperCase() },
  ];
}
