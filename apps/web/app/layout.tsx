import type { Metadata } from "next";
import {
  Bricolage_Grotesque,
  Hanken_Grotesk,
  JetBrains_Mono,
} from "next/font/google";
import Header from "../components/Header";
import { AuthProvider } from "../context/AuthContext";
import "./globals.css";

// --- Type system (swap these three to re-theme typography) ---
const display = Bricolage_Grotesque({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-display",
});

const body = Hanken_Grotesk({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-text",
});

const mono = JetBrains_Mono({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-mono",
});

export const metadata: Metadata = {
  title: "The Elephant Calculator",
  description:
    "A precision computing instrument on the savannah — vectors, matrices, geometry, primes, high-precision arithmetic, and a computer algebra system.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      className={`${display.variable} ${body.variable} ${mono.variable}`}
    >
      <body>
        <div className="savannah-sky" aria-hidden />
        <div className="paper-grid" aria-hidden />
        <AuthProvider>
          <Header />
          <main>{children}</main>
        </AuthProvider>
      </body>
    </html>
  );
}
