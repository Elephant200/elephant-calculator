'use client';

import Link from 'next/link';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-white shadow-md">
      <div className="container mx-auto flex justify-between items-center py-4 px-6 border-b border-gray-200">
        {/* Brand */}
        <Link href="/" className="text-2xl font-bold text-gray-900">
          The Elephant Calculator
        </Link>

        {/* Navigation Links */}
        <div className="flex items-center space-x-6">
          <Link
            href="/calculator"
            className="px-4 py-2 rounded-md text-gray-700 hover:bg-gray-100 transition"
          >
            Calculator
          </Link>
          <Link
            href="/reviews"
            className="px-4 py-2 rounded-md text-gray-700 hover:bg-gray-100 transition"
          >
            Reviews
          </Link>
          <Link
            href="/auth/login"
            className="px-4 py-2 rounded-md text-gray-700 hover:bg-gray-100 transition"
          >
            Login
          </Link>
          <Link
            href="/auth/register"
            className="px-4 py-2 rounded-md text-gray-700 hover:bg-gray-100 transition"
          >
            Register
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
