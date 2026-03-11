import { useState, useEffect } from 'react';
import EstudiantesApp from './EstudiantesApp';
import Login from './Login';
import Register from './Register';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [currentView, setCurrentView] = useState('login'); // 'login' | 'register' | 'app'

  useEffect(() => {
    // Revisamos si el navegador ya tiene su JWT
    const token = localStorage.getItem('access_token');
    if (token) {
      setIsAuthenticated(true);
      setCurrentView('app');
    }
  }, []);

  const handleLoginSuccess = () => {
    setIsAuthenticated(true);
    setCurrentView('app');
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setIsAuthenticated(false);
    setCurrentView('login');
  };

  // Render condicional de pantallas
  if (isAuthenticated && currentView === 'app') {
    return <EstudiantesApp onLogout={handleLogout} />;
  }

  if (currentView === 'register') {
    return <Register onGoToLogin={() => setCurrentView('login')} />;
  }

  return <Login onLoginSuccess={handleLoginSuccess} onGoToRegister={() => setCurrentView('register')} />;
}

export default App;
