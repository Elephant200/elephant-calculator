'use client';

import { useAuth } from '../../../context/AuthContext';
import { useRouter } from 'next/navigation';

export default function Register() {
  const { login } = useAuth();
  const router = useRouter();

  const handleRegister = (e: React.FormEvent) => {
    e.preventDefault();
    login('Elephant200');
    router.push('/');
  };

  return (
    <div className="flex items-center justify-center h-full" style={{ paddingTop: '4rem' }}>
      <div className="w-full max-w-sm p-6 bg-white border rounded-lg shadow-md">
        <h1 className="text-2xl font-bold text-center mb-6">Register</h1>
        <form onSubmit={handleRegister} className="space-y-4">
          <div>
            <label htmlFor="username" className="block text-sm font-medium">
              Username
            </label>
            <input
              type="text"
              id="username"
              className="mt-1 w-full px-4 py-2 border rounded-md shadow-sm"
              placeholder="Enter your username"
            />
          </div>
          <div>
            <label htmlFor="password" className="block text-sm font-medium">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="mt-1 w-full px-4 py-2 border rounded-md shadow-sm"
              placeholder="Create a password"
            />
          </div>
          <button
            type="submit"
            className="w-full px-4 py-2 text-white bg-black rounded-md hover:opacity-90 transition"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
}
