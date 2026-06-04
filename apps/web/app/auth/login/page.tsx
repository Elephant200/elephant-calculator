"use client";

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
      <div className="panel tool-shell w-full max-w-sm p-6">
        <h1 className="font-display mb-6 text-center text-2xl font-bold">Login</h1>
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
            />
          </div>
          <button
            type="submit"
            className="btn btn-accent w-full"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
