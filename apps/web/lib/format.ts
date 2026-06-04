// Presentation helpers for numeric results.

export function formatNumber(value: number): string {
  if (!Number.isFinite(value)) return String(value);
  if (value === 0) return "0";
  const abs = Math.abs(value);
  // Use scientific notation for very large / very small magnitudes.
  if (abs >= 1e12 || abs < 1e-9) {
    return value.toExponential(6).replace(/\.?0+e/, "e");
  }
  // Round to a sensible precision, then trim trailing zeros.
  const rounded = Number(value.toPrecision(12));
  let out = String(rounded);
  if (out.includes(".")) {
    out = out.replace(/(\.\d*?)0+$/, "$1").replace(/\.$/, "");
  }
  return out;
}

export function formatVector(v: number[]): string {
  return `[ ${v.map(formatNumber).join(",  ")} ]`;
}
