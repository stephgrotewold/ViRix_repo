// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CovidStats from './components/CovidStats';
import logo from './components/logo/logo.png';
import Footer from './components/Footer'; // Ajusta la ruta según tu estructura
import Info from './components/Info';
import Tips from './components/Tips';
import AboutUs from './components/AboutUs';
import './App.css';

function App() {
  return (
      <Router>
          <div className="app-container">
              <header className="app-header">
                  <img src={logo} alt="ViRix Logo" className="logo" />
                  <div className="slogan">
                    <p className="slogan" style={{ color: 'white' }}>Spot the risk, stay safe</p>
                  </div>
                  <nav className="nav-bar">
                      <Link to="/">Map</Link>
                      <Link to="/info">Info</Link>
                      <Link to="/about">About Us</Link>
                      <Link to="/tips">Tips</Link>
                  </nav>
              </header>
              <main>
                  <Routes>
                      <Route path="/" element={<CovidStats />} />
                      <Route path="/info" element={<Info />} />
                      <Route path="/tips" element={<Tips />} />
                      <Route path="/about" element={<AboutUs />} />

                      {/* Otras rutas */}
                  </Routes>
              </main>
              <Footer />
          </div>
      </Router>
  );
}

export default App;