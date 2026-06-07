"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../../../context/AuthContext";

export default function Register() {
  const { login } = useAuth();
  const router = useRouter();

  const handleRegister = (e: React.FormEvent) => {
    e.preventDefault();
    login("Elephant200");
    router.push("/");
  };

  return (
    <div className="flex min-h-[calc(100vh-64px)] items-center justify-center px-5 py-12">
      <div className="panel tool-shell w-full max-w-sm p-6 sm:p-7 rise-in">
        <div className="eyebrow text-center">The Elephant Calculator</div>
        <h1 className="font-display mt-2 mb-6 text-center text-2xl font-bold">
          Create your account
        </h1>
        <form onSubmit={handleRegister} className="space-y-4">
          <div>
            <label htmlFor="username" className="field-label">
              Username
            </label>
            <input
              type="text"
              id="username"
              className="text-input"
              placeholder="Choose a username"
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
              placeholder="Create a password"
              autoComplete="new-password"
            />
          </div>
          <button type="submit" className="btn btn-accent w-full">
            Register
          </button>
        </form>
        <p className="mt-5 text-center text-[13px] text-[var(--muted)]">
          Already have an account?{" "}
          <Link
            href="/auth/login"
            className="text-[var(--accent)] underline-offset-2 hover:underline"
          >
            Log in
          </Link>
        </p>
        <p className="mt-2 text-center font-mono text-[11px] text-[var(--muted)]">
          Demo only — no data is stored.
        </p>
      </div>
    </div>
  );
}
