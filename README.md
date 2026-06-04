# The Elephant Calculator

The Elephant Calculator is a FastAPI + Next.js monorepo for a multi-purpose calculator with vector, matrix, geometry, prime, high-precision decimal, Pythagorean triple, triangle-solving, and CAS tools.

The original calculator code now lives in a reusable Python package, while the API, web app, and generated API contract are separate workspace packages.

## Workspace Layout

```text
apps/
  api/          FastAPI application
  web/          Next.js application
packages/
  calculator/   Reusable Python calculator services and CLI
  api-contract/ Generated OpenAPI schema and TypeScript types
```

## Tooling

- `uv` manages Python environments, dependency locking, and package execution.
- `pnpm` manages JavaScript workspaces.
- `turbo` orchestrates build, dev, test, lint, and code generation tasks.
- Python 3.14 is preferred for local development when available, but packages support Python 3.12+.

If `pnpm` is not installed, enable it with Corepack:

```bash
corepack enable
corepack prepare pnpm@10.12.1 --activate
```

## Setup

```bash
uv sync --all-packages --all-extras
pnpm install
pnpm generate:api-types
```

## Run

Start the FastAPI backend:

```bash
pnpm dev:api
```

The API docs are available at [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs).

Start the Next.js frontend:

```bash
pnpm dev:web
```

The web app provides a full calculator workspace over every API domain
(vectors, matrices, primes, geometry, the triangle solver, high-precision
arithmetic, the CAS, and Pythagorean triples). The browser only talks to the
Next.js origin: requests to `/api/*` are proxied server-side to FastAPI (see
`apps/web/next.config.ts`), so no CORS configuration is needed in development.
Override the backend target with `API_PROXY_TARGET` when deploying.

Run the legacy interactive calculator CLI:

```bash
uv run --package elephant-calculator elephant-calculator
```

## Development Commands

```bash
pnpm build
pnpm lint
pnpm test
pnpm generate:api-types
```

The API contract package is generated from FastAPI's OpenAPI schema:

1. `apps/api` writes `packages/api-contract/openapi.json`.
2. `packages/api-contract` runs `openapi-typescript`.
3. `apps/web` imports types from `@elephant-calculator/api-contract`.

## API Entrypoint

```bash
uv run --package elephant-calculator-api uvicorn elephant_calculator_api.main:app --reload
```

Routes remain under `/api/...`; for example:

- `/api/vectors/add`
- `/api/matrices/multiply/matrix`, `/api/matrices/multiply/vector`
- `/api/geometry/area/circle`, `/api/geometry/volume/ellipsoid`
- `/api/irrationals/add`, `/api/irrationals/arccos`, `/api/irrationals/arctan`
- `/api/cas/expand`, `/api/cas/solve-differential`

Set `ELEPHANT_CORS_ORIGINS` (comma-separated) to enable CORS when serving the
API directly to a browser on another origin.
