"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../../../context/AuthContext";

export default function Login() {
  const { login } = useAuth();
  const router = useRouter();

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    login("Elephant200");
    router.push("/");
  };

  return (
    <div className="flex min-h-[calc(100vh-64px)] items-center justify-center px-5 py-12">
      <div className="panel tool-shell w-full max-w-sm p-6 sm:p-7 rise-in">
        <div className="eyebrow text-center">The Elephant Calculator</div>
        <h1 className="font-display mt-2 mb-6 text-center text-2xl font-bold">
          Welcome back
        </h1>
        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label htmlFor="username" className="field-label">
              Username
            </label>
            <input
              type="text"
              id="username"
              className="text-input"
              placeholder="Enter your username"
              autoComplete="username"
            />
          </div>
          <div>
            <label htmlFor="password" className="field-label">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="text-input"
              placeholder="Enter your password"
              autoComplete="current-password"
            />
          </div>
          <button type="submit" className="btn btn-accent w-full">
            Login
          </button>
        </form>
        <p className="mt-5 text-center text-[13px] text-[var(--muted)]">
          New here?{" "}
          <Link
            href="/auth/register"
            className="text-[var(--accent)] underline-offset-2 hover:underline"
          >
            Create an account
          </Link>
        </p>
        <p className="mt-2 text-center font-mono text-[11px] text-[var(--muted)]">
          Demo only — any credentials sign you in.
        </p>
      </div>
    </div>
  );
}
