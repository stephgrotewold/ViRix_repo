// CovidMap.js
import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const CovidMap = () => {
    return (
        <div id="map" style={{ height: "500px", width: "100%" }}>
            <MapContainer center={[20, 0]} zoom={2} minZoom={2} maxZoom={10}>
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />
                {/* Puedes agregar más componentes de Leaflet aquí, como Marker, Popup, etc. */}
            </MapContainer>
        </div>
    );
}

export default CovidMap;