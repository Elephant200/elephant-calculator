import type { NextConfig } from "next";

// Local Next.js development proxies to the separately-running FastAPI server.
// On Vercel, /api/* is handled by the Python function configured in vercel.json.
const apiTarget = process.env.API_PROXY_TARGET;
const shouldProxyApi = apiTarget || !process.env.VERCEL;

const nextConfig: NextConfig = {
  async rewrites() {
    if (!shouldProxyApi) return [];

    return [
      {
        source: "/api/:path*",
        destination: `${apiTarget ?? "http://127.0.0.1:8000"}/api/:path*`,
      },
    ];
  },
};

export default nextConfig;
