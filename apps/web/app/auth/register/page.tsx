"use client";

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
      <div className="panel tool-shell w-full max-w-sm p-6">
        <h1 className="font-display mb-6 text-center text-2xl font-bold">
          Register
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
              placeholder="Create a password"
            />
          </div>
          <button
            type="submit"
            className="btn btn-accent w-full"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
}
