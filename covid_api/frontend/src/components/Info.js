// src/components/Info.js
import React from 'react';
import './Info.css';
import breath from './images/breath.jpg';
import cough from './images/cough.jpg';
import temp from './images/temp.jpg';
import test from './images/test.jpg';
import emergency from './images/emergency.jpg';

const Info = () => {
    return (
        <div className="info-container">
            <h2 style={{ color: '#333', marginBottom: '20px', fontWeight: 'bold' }}>COVID-19 Information</h2>
            <p>COVID-19, caused by the SARS-CoV-2 virus, primarily affects the respiratory system but can impact other parts of the body. It spreads quickly through respiratory droplets from an infected person, even if they show no symptoms.</p>
            
            <h3>Symptoms</h3>
            <div className="symptoms-images">
                <img src={temp} alt="Fever" className="symptom-image"/>
                <img src={cough} alt="Cough" className="symptom-image"/>
                <img src={breath} alt="Shortness of breath" className="symptom-image"/>
            </div>
            <ul>
                <li>Fever or chills</li>
                <li>Cough</li>
                <li>Shortness of breath or difficulty breathing</li>
                <li>Fatigue</li>
                <li>Body aches and headaches</li>
                <li>New loss of taste or smell</li>
                <li>Sore throat, sinus congestion, or runny nose</li>
                <li>Nausea, vomiting, or diarrhea</li>
            </ul>

            <h3>Risk Factors</h3>
            <p>Certain individuals are at a higher risk of severe illness from COVID-19, including:</p>
            <ul>
                <li>Older adults (65+ years)</li>
                <li>Individuals with chronic conditions such as cancer, heart disease, diabetes, chronic lung diseases, and compromised immune systems</li>
                <li>Those who are overweight, smokers, or have undergone organ transplants</li>
            </ul>

            <h3>What to Do If Infected</h3>
            <img src={test} alt="COVID-19 testing" className="info-image"/>
            <p>If diagnosed with COVID-19:</p>
            <ul>
                <li>Mild cases can often be managed at home with over-the-counter medications, increased fluid intake, and rest.</li>
                <li>Seek emergency care if you experience symptoms like shortness of breath, persistent chest pain, confusion, or bluish lips/face.</li>
                <li>For children, watch for multisystem inflammatory syndrome (MIS-C), which requires immediate medical attention.</li>
            </ul>

            <h3>Emergency Contact Information</h3>
            <p>It is essential to have access to emergency numbers and healthcare providers in your country. Check your local health department's resources for accurate information. For example:</p>
            <ul>
                <li>United States: CDC Hotline</li>
                <li>United Kingdom: NHS 111</li>
                <li>India: Ministry of Health & Family Welfare Helpline</li>
                <li>Australia: National Coronavirus Helpline</li>
                <img src={emergency} alt="Emergency room" className="info-image"/>
            </ul>
        </div>
    );
};

export default Info;