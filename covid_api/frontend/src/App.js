import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Inicio from './components/Inicio';
import { slide as Menu } from 'react-burger-menu';
import logo from './components/logo/logo-horizontal.png';
import Footer from './components/Footer';
import Info from './components/Info';
import Tips from './components/Tips';
import HeatMap from './components/HeatMap';
import AboutUs from './components/AboutUs';
import HealthCenters from './components/HealthCenters'; 
import './App.css';

function App() {
    const [menuOpen, setMenuOpen] = useState(false);
    const [isMobile, setIsMobile] = useState(window.innerWidth < 768);

    useEffect(() => {
        const handleResize = () => {
            setIsMobile(window.innerWidth < 768);
        };

        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);

    const closeMenu = () => {
        setMenuOpen(false);
    };

    const handleMenuStateChange = (state) => {
        setMenuOpen(state.isOpen);
    };

    return (
        <Router>
            <div className="app-container">
                <header className="app-header">
                    <div className="header-content">
                        <img src={logo} alt="ViRix Logo" className="logo" />
                        <div className="slogan">
                            Spot the risk, stay safe
                        </div>
                        {isMobile ? (
                            <Menu 
                                right 
                                isOpen={menuOpen} 
                                onStateChange={handleMenuStateChange}
                                className="burger-menu" // Asegúrate de que haya un className definido
                            >
                                <Link to="/" onClick={closeMenu}>Inicio</Link>
                                <Link to="/info" onClick={closeMenu}>Info</Link>
                                <Link to="/tips" onClick={closeMenu}>Tips</Link>
                                <Link to="/about" onClick={closeMenu}>About Us</Link>
                                <Link to="/heatmap" onClick={closeMenu}>Heat Map</Link>
                                <Link to="/healthcenters" onClick={closeMenu}>Health Centers</Link>  
                            </Menu>
                        ) : (
                            <nav className="nav-bar">
                                <Link to="/">Inicio</Link>
                                <Link to="/info">Info</Link>
                                <Link to="/tips">Tips</Link>
                                <Link to="/about">About Us</Link>
                                <Link to='/heatmap'>Heat Map</Link>
                                <Link to="/healthcenters">Health Centers</Link>
                            </nav>
                        )}
                    </div>
                </header>
                <main>
                    <Routes>
                        <Route path="/inicio" element={<Inicio />} />
                        <Route path="/" element={<Inicio />} />
                        <Route path="/info" element={<Info />} />
                        <Route path="/tips" element={<Tips />} />
                        <Route path="/about" element={<AboutUs />} />
                        <Route path="/heatmap" element={<HeatMap />} />
                        <Route path="/healthcenters" element={<HealthCenters />} />
                    </Routes>
                </main>
                <Footer />
            </div>
        </Router>
    );
}

export default App;