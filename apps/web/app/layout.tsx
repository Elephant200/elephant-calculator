import { AuthProvider } from '../context/AuthContext';
import Navbar from '../components/Navbar';
import './globals.css';

export const metadata = {
  title: 'The Elephant Calculator',
  description: 'A powerful calculation tool.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <Navbar />
          <main>{children}</main>
        </AuthProvider>
      </body>
    </html>
  );
}
