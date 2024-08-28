import React, { useState } from 'react';
import axios from 'axios';

const CovidStats = () => {
    const [location, setLocation] = useState('');
    const [data, setData] = useState(null);
    const [error, setError] = useState('');

    const handleSearch = () => {
        if (!location) {
            setError("Please enter a valid location.");
            return;
        }

        axios.get(`http://localhost:8000/covid-data?location=${location}`)
            .then(response => {
                console.log(response.data); // Verifica los datos aquí
                setData(response.data);
            })
            .catch(error => {
                setError("Failed to fetch data. Please try again.");
                console.error("There was an error!", error);
            });
    };

    return (
        <div>
            <h2>COVID-19 Stats</h2>
            <input
                type="text"
                value={location}
                onChange={e => setLocation(e.target.value)}
                placeholder="Enter Location"
            />
            <button onClick={handleSearch}>Search</button>
            {error && <p style={{ color: "red" }}>{error}</p>}
            {data && (
                <table>
                    <thead>
                        <tr>
                            <th>Country</th>
                            <th>Total Cases</th>
                            <th>New Cases (Last 7 Days)</th>
                            <th>Total Deaths</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{data.country}</td>
                            <td>{data.totalCases}</td>
                            <td>{data.newCases}</td>
                            <td>{data.totalDeaths}</td>
                        </tr>
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default CovidStats;