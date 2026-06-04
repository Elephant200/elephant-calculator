// Thin typed wrapper around the Elephant Calculator API. All requests go to the
// same Next.js origin under /api and are proxied to FastAPI (see next.config.ts).

export type ApiErrorShape = {
  detail: string;
  error_type?: string;
  path?: string;
};

export class ApiError extends Error {
  errorType: string;
  status: number;
  constructor(message: string, errorType: string, status: number) {
    super(message);
    this.name = "ApiError";
    this.errorType = errorType;
    this.status = status;
  }
}

type QueryValue = string | number | boolean | undefined | null;

export interface CallOptions {
  method?: "GET" | "POST";
  body?: unknown;
  query?: Record<string, QueryValue>;
}

function buildQuery(query?: Record<string, QueryValue>): string {
  if (!query) return "";
  const params = new URLSearchParams();
  for (const [key, value] of Object.entries(query)) {
    if (value === undefined || value === null || value === "") continue;
    params.set(key, String(value));
  }
  const qs = params.toString();
  return qs ? `?${qs}` : "";
}

export async function callApi<T>(
  path: string,
  options: CallOptions = {}
): Promise<T> {
  const { method = "POST", body, query } = options;
  const url = `/api${path}${buildQuery(query)}`;

  let res: Response;
  try {
    res = await fetch(url, {
      method,
      headers: body !== undefined ? { "Content-Type": "application/json" } : {},
      body: body !== undefined ? JSON.stringify(body) : undefined,
    });
  } catch {
    throw new ApiError(
      "Could not reach the calculation server. Is the API running?",
      "Network Error",
      0
    );
  }

  const raw = await res.text();
  let parsed: unknown = raw;
  if (raw) {
    try {
      parsed = JSON.parse(raw);
    } catch {
      /* leave as string */
    }
  }

  if (!res.ok) {
    const err = parsed as ApiErrorShape;
    const message =
      (err && typeof err === "object" && err.detail) ||
      `Request failed (${res.status})`;
    const type =
      (err && typeof err === "object" && err.error_type) || `HTTP ${res.status}`;
    throw new ApiError(String(message), String(type), res.status);
  }

  return parsed as T;
}
