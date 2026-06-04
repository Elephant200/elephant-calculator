import type { NextConfig } from "next";

// The browser talks to the Next.js origin only; requests to /api/* are proxied
// server-side to the FastAPI backend. This keeps the frontend same-origin and
// sidesteps CORS entirely. Override the target with API_PROXY_TARGET in prod.
const apiTarget = process.env.API_PROXY_TARGET ?? "http://127.0.0.1:8000";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: `${apiTarget}/api/:path*`,
      },
    ];
  },
};

export default nextConfig;
