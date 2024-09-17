import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { MapContainer, TileLayer, CircleMarker, Popup } from 'react-leaflet';
import countryCoordinates from './countryCoordinates';
import './HeatMap.css';

const HeatMap = () => {
    const [data, setData] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Hacer una solicitud GET a la API para obtener los datos
                const response = await axios.get('http://localhost:8000/heatmap-data'); // Asegúrate de que esta URL es correcta
                const fetchedData = response.data;

                // Calcular 'risk_level' para cada entrada
                const dataWithRisk = fetchedData.map(item => ({
                    ...item,
                    risk_level: determineRiskLevel(item.new_cases) // Asigna el 'risk_level' basado en 'new_cases'
                }));

                setData(dataWithRisk);
            } catch (error) {
                setError('Failed to fetch data. Please try again.');
                console.error('Error fetching COVID data:', error);
            }
        };

        fetchData();
    }, []);

    // Función para determinar el 'risk_level'
    const determineRiskLevel = (newCases) => {
        if (newCases > 100000) {
            return 'High';
        } else if (newCases > 10000) {
            return 'Medium';
        } else {
            return 'Low';
        }
    };

    const countryAliasMapping = {
        "Afghanistan": "Afghanistan",
        "Albania": "Albania",
        "Algeria": "Algeria",
        "American Samoa": "American Samoa",
        "Andorra": "Andorra",
        "Angola": "Angola",
        "Anguilla": "Anguilla",
        "Antigua and Barbuda": "Antigua and Barbuda",
        "Argentina": "Argentina",
        "Armenia": "Armenia",
        "Aruba": "Aruba",
        "Australia": "Australia",
        "Austria": "Austria",
        "Azerbaijan": "Azerbaijan",
        "Bahamas": "Bahamas",
        "Bahrain": "Bahrain",
        "Bangladesh": "Bangladesh",
        "Barbados": "Barbados",
        "Belarus": "Belarus",
        "Belgium": "Belgium",
        "Belize": "Belize",
        "Benin": "Benin",
        "Bermuda": "Bermuda",
        "Bhutan": "Bhutan",
        "Bolivia (Plurinational State of)": "Bolivia (Plurinational State of)",
        "Bonaire, Saint Eustatius and Saba": "Sint Eustatius",
        "Bosnia and Herzegovina": "Bosnia and Herzegovina",
        "Botswana": "Botswana",
        "Brazil": "Brazil",
        "British Virgin Islands": "British Virgin Islands",
        "Brunei Darussalam": "Brunei Darussalam",
        "Bulgaria": "Bulgaria",
        "Burkina Faso": "Burkina Faso",
        "Burundi": "Burundi",
        "Cabo Verde": "Cabo Verde",
        "Cambodia": "Cambodia",
        "Cameroon": "Cameroon",
        "Canada": "Canada",
        "Cayman Islands": "Cayman Islands",
        "Central African Republic": "Central African Republic",
        "Chad": "Chad",
        "Chile": "Chile",
        "China": "China",
        "Colombia": "Colombia",
        "Comoros": "Comoros",
        "Congo": "Congo",
        "Cook Islands": "Cook Islands",
        "Costa Rica": "Costa Rica",
        "Côte d'Ivoire": "Côte d'Ivoire",
        "Croatia": "Croatia",
        "Cuba": "Cuba",
        "Curaçao": "Curaçao",
        "Cyprus": "Cyprus",
        "Czechia": "Czechia",
        "Democratic People's Republic of Korea": "Democratic People's Republic of Korea",
        "Democratic Republic of the Congo": "Congo, Democratic Republic of the",
        "Denmark": "Denmark",
        "Djibouti": "Djibouti",
        "Dominica": "Dominica",
        "Dominican Republic": "Dominican Republic",
        "Ecuador": "Ecuador",
        "Egypt": "Egypt",
        "El Salvador": "El Salvador",
        "Equatorial Guinea": "Equatorial Guinea",
        "Eritrea": "Eritrea",
        "Estonia": "Estonia",
        "Eswatini": "Eswatini",
        "Ethiopia": "Ethiopia",
        "Falkland Islands (Malvinas)": "Falkland Islands (Malvinas)",
        "Faroe Islands": "Faroe Islands",
        "Fiji": "Fiji",
        "Finland": "Finland",
        "France": "France",
        "French Guiana": "French Guiana",
        "French Polynesia": "French Polynesia",
        "Gabon": "Gabon",
        "Gambia": "Gambia",
        "Georgia": "Georgia",
        "Germany": "Germany",
        "Ghana": "Ghana",
        "Gibraltar": "Gibraltar",
        "Greece": "Greece",
        "Greenland": "Greenland",
        "Grenada": "Grenada",
        "Guadeloupe": "Guadeloupe",
        "Guam": "Guam",
        "Guatemala": "Guatemala",
        "Guernsey": "Guernsey",
        "Guinea": "Guinea",
        "Guinea-Bissau": "Guinea-Bissau",
        "Guyana": "Guyana",
        "Haiti": "Haiti",
        "Holy See": "Holy See",
        "Honduras": "Honduras",
        "Hungary": "Hungary",
        "Iceland": "Iceland",
        "India": "India",
        "Indonesia": "Indonesia",
        "Iran (Islamic Republic of)": "Iran (Islamic Republic of)",
        "Iraq": "Iraq",
        "Ireland": "Ireland",
        "Isle of Man": "Isle of Man",
        "Israel": "Israel",
        "Italy": "Italy",
        "Jamaica": "Jamaica",
        "Japan": "Japan",
        "Jersey": "Jersey",
        "Jordan": "Jordan",
        "Kazakhstan": "Kazakhstan",
        "Kenya": "Kenya",
        "Kiribati": "Kiribati",
        "Kosovo": "Kosovo",
        "Kuwait": "Kuwait",
        "Kyrgyzstan": "Kyrgyzstan",
        "Lao People's Democratic Republic": "Lao People's Democratic Republic",
        "Latvia": "Latvia",
        "Lebanon": "Lebanon",
        "Lesotho": "Lesotho",
        "Liberia": "Liberia",
        "Libya": "Libya",
        "Liechtenstein": "Liechtenstein",
        "Lithuania": "Lithuania",
        "Luxembourg": "Luxembourg",
        "Madagascar": "Madagascar",
        "Malawi": "Malawi",
        "Malaysia": "Malaysia",
        "Maldives": "Maldives",
        "Mali": "Mali",
        "Malta": "Malta",
        "Marshall Islands": "Marshall Islands",
        "Martinique": "Martinique",
        "Mauritania": "Mauritania",
        "Mauritius": "Mauritius",
        "Mayotte": "Mayotte",
        "Mexico": "Mexico",
        "Micronesia (Federated States of)": "Micronesia (Federated States of)",
        "Monaco": "Monaco",
        "Mongolia": "Mongolia",
        "Montenegro": "Montenegro",
        "Montserrat": "Montserrat",
        "Morocco": "Morocco",
        "Mozambique": "Mozambique",
        "Myanmar": "Myanmar",
        "Namibia": "Namibia",
        "Nauru": "Nauru",
        "Nepal": "Nepal",
        "Netherlands (Kingdom of the)": "Netherlands",
        "New Caledonia": "New Caledonia",
        "New Zealand": "New Zealand",
        "Nicaragua": "Nicaragua",
        "Niger": "Niger",
        "Nigeria": "Nigeria",
        "Niue": "Niue",
        "North Macedonia": "North Macedonia",
        "Northern Mariana Islands": "Northern Mariana Islands",
        "Norway": "Norway",
        "occupied Palestinian territory, including east Jerusalem": "occupied Palestinian territory, including east Jerusalem",
        "Oman": "Oman",
        "Pakistan": "Pakistan",
        "Palau": "Palau",
        "Panama": "Panama",
        "Papua New Guinea": "Papua New Guinea",
        "Paraguay": "Paraguay",
        "Peru": "Peru",
        "Philippines": "Philippines",
        "Pitcairn": "Pitcairn",
        "Poland": "Poland",
        "Portugal": "Portugal",
        "Puerto Rico": "Puerto Rico",
        "Qatar": "Qatar",
        "Republic of Korea": "Republic of Korea",
        "Republic of Moldova": "Moldova (Republic of)",
        "Réunion": "Réunion",
        "Romania": "Romania",
        "Russian Federation": "Russian Federation",
        "Rwanda": "Rwanda",
        "Saint Barthélemy": "Saint Barthélemy",
        "Saint Helena": "Saint Helena, Ascension and Tristan da Cunha",
        "Saint Kitts and Nevis": "Saint Kitts and Nevis",
        "Saint Lucia": "Saint Lucia",
        "Saint Martin (French part)": "Saint Martin (French part)",
        "Saint Pierre and Miquelon": "Saint Pierre and Miquelon",
        "Saint Vincent and the Grenadines": "Saint Vincent and the Grenadines",
        "Samoa": "Samoa",
        "San Marino": "San Marino",
        "Sao Tome and Principe": "Sao Tome and Principe",
        "Saudi Arabia": "Saudi Arabia",
        "Senegal": "Senegal",
        "Serbia": "Serbia",
        "Seychelles": "Seychelles",
        "Sierra Leone": "Sierra Leone",
        "Singapore": "Singapore",
        "Sint Maarten (Dutch part)": "Sint Maarten (Dutch part)",
        "Slovakia": "Slovakia",
    "French Southern Territories": "French Southern Territories",
        "Heard Island and McDonald Islands": "Heard Island and McDonald Islands",
        "Hong Kong": "Hong Kong",
        "Macao": "Macao",
        "Moldova (Republic of)": "Moldova (Republic of)",
        "Netherlands": "Netherlands",
        "Norfolk Island": "Norfolk Island",
        "Svalbard and Jan Mayen": "Svalbard and Jan Mayen",
        "Swaziland": "Eswatini", // Alias for the previous name
        "Taiwan": "Taiwan",
        "Tanzania, United Republic of": "United Republic of Tanzania",
        "United Kingdom": "United Kingdom",
        "Western Sahara": "Western Sahara",
        "Congo, Democratic Republic of the": "Democratic Republic of the Congo",
        "Sint Eustatius": "Bonaire, Saint Eustatius and Saba",
        "Kosovo": "Kosovo","Netherlands (Kingdom of the)": "Netherlands",
        "Saint Barthélemy": "Saint Barthelemy",
        "British Virgin Islands": "Virgin Islands, British",
        "occupied Palestinian territory, including east Jerusalem": "Palestine",
        "Democratic Republic of the Congo": "Congo (Kinshasa)",
        "Curaçao": "Curacao",
        "Democratic People's Republic of Korea": "North Korea",
        "Kosovo (in accordance with UN Security Council resolution 1244 (1999))": "Kosovo",
        "Réunion": "Reunion",
        "Côte d'Ivoire": "Ivory Coast",
        "United Republic of Tanzania": "Tanzania",
        "Bonaire, Saint Eustatius and Saba": "Bonaire",
        "United States Virgin Islands": "Virgin Islands, U.S.",
        "Türkiye": "Turkey",
        "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
        "International conveyance (Diamond Princess)": "Diamond Princess",
        "Turks and Caicos Islands": "Turks and Caicos",
        "Antarctica": "Antarctica",
        "Bouvet Island": "Bouvet Island",
        "British Indian Ocean Territory": "British Indian Ocean Territory",
        "Cocos (Keeling) Islands": "Cocos (Keeling) Islands",
        "French Polynesia": "French Polynesia",
        "Heard Island and McDonald Islands": "Heard Island and McDonald Islands",
        "Holy See": "Holy See",
        "Pitcairn": "Pitcairn",
        "Saint Helena, Ascension and Tristan da Cunha": "Saint Helena",
        "South Georgia and the South Sandwich Islands": "South Georgia and the South Sandwich Islands"
    };

    // Obtener el color según el nivel de riesgo
    const getColorByRiskLevel = (riskLevel) => {
        switch (riskLevel) {
            case "High":
                return "red";
            case "Medium":
                return "yellow";
            case "Low":
                return "green";
            default:
                return "blue"; // Color por defecto
        }
    };

    return (
    <div className="heatmap-container">
        {error && <p className="error-message">{error}</p>}
        <MapContainer center={[20, 0]} zoom={2} className="leaflet-container">
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
            {data.map((item, index) => {
                // Verificar si el nombre del país necesita ser mapeado
                const countryName = countryAliasMapping[item.country] || item.country;
                const coords = countryCoordinates[countryName];
                
                // Verificar si las coordenadas están definidas
                if (!coords || coords.lat === undefined || coords.lng === undefined) {
                    console.warn(`No se encontraron coordenadas para: ${item.country}`);
                    return null; // Si no hay coordenadas, no renderizar el marcador
                }
                return (
                    <CircleMarker
                        key={index}
                        center={[coords.lat, coords.lng]}
                        radius={5}
                        color={getColorByRiskLevel(item.risk_level)} // Aplicar color según el nivel de riesgo
                    >
                        <Popup>
                            <div>
                                <strong>{item.country}</strong><br />
                                Cases: {item.cumulative_cases}<br />
                                Deaths: {item.cumulative_deaths}<br />
                                Risk Level: {item.risk_level}
                            </div>
                        </Popup>
                    </CircleMarker>
                );
            })}
        </MapContainer>
    </div>
  );
}

export default HeatMap;