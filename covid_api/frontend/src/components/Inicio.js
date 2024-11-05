import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet.heat';
import NewsFeed from './NewsFeed';
import Footer from './Footer';
import '../App.css';
import './Inicio.css';


const CovidStats = () => {
    return (
        <div>
            <div className="covid-stats-container">
                <h2>COVID-19 Global Statistics</h2>
                <p className="info-text" style={{ color: 'darkgrey' }}>
                    Stay informed with the latest COVID-19 data
                </p>
                
                {/* Mostrar el componente NewsFeed */}
                <NewsFeed />
                
                
            </div>
            {/* <Footer className="footer">© 2024 ViRix. All rights reserved.</Footer> */}
        </div>
    );
};

export default CovidStats;