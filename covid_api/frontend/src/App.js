// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CovidStats from './components/CovidStats';
import { slide as Menu } from 'react-burger-menu';
import logo from './components/logo/logo-horizontal.png';
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
                  <div className="header-content">
                      <img src={logo} alt="ViRix Logo" className="logo" />
                      <div className="slogan">
                          <p style={{ color: 'white' }}>Spot the risk, stay safe</p>
                      </div>
                      <Menu right>
                          <Link to="/">Map</Link>
                          <Link to="/info">Info</Link>
                          <Link to="/about">About Us</Link>
                          <Link to="/tips">Tips</Link>
                      </Menu>
                  </div>
              </header>
              <main>
                  <Routes>
                      <Route path="/map" component={CovidStats} />
                      <Route path="/" element={<CovidStats />} />
                      <Route path="/info" element={<Info />} />
                      <Route path="/tips" element={<Tips />} />
                      <Route path="/about" element={<AboutUs />} />
                  </Routes>
              </main>
              <Footer />
          </div>
      </Router>
  );
}

export default App;