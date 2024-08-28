// src/App.js
import React from 'react';
import CovidStats from './components/CovidStats';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>COVID-19 Stats</h1>
      </header>
      <main>
        <CovidStats />
      </main>
    </div>
  );
}

export default App;