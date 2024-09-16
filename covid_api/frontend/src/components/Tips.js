// src/components/Tips.js
import React from 'react';
import './Tips.css';
import masks from './images/masks.jpg';
import wash from './images/wash.jpg';
import water from './images/water.jpg';
import wipes from './images/wipes.jpg';
import vaccine from './images/vaccine.jpg';
import distance from './images/distance.jpg';

const Tips = () => {
    return (
        <div className="tips-container">
            <h2 style={{ color: '#333', marginBottom: '20px', fontWeight: 'bold' }}>Prevention Tips</h2>
            <p>To reduce the risk of contracting or spreading COVID-19, consider implementing the following prevention methods:</p>
            
            <h3>Personal Hygiene</h3>
            <img src={wash} alt="Washing hands" className="tips-image"/>
            <ul>
                <li><strong>Wash Your Hands:</strong> Wash your hands frequently with soap and water for at least 20 seconds, especially after being in a public place, or after coughing or sneezing. Use hand sanitizer with at least 60% alcohol if soap and water are not available.</li>
                <li><strong>Avoid Touching Your Face:</strong> Avoid touching your eyes, nose, and mouth with unwashed hands to prevent the virus from entering your body.</li>
                <li><strong>Respiratory Hygiene:</strong> Always cover your mouth and nose with a tissue or your elbow when you cough or sneeze, and dispose of the tissue safely. Wash your hands immediately after.</li>
            </ul>

            <h3>Mask Wearing</h3>
            <img src={masks} alt="Wearing masks" className="tips-image"/>
            <ul>
                <li><strong>Wear Masks in Public:</strong> Wear a mask that covers your nose and mouth when you are in public settings, especially when social distancing measures are difficult to maintain. Choose masks with multiple layers and a snug fit.</li>
                <li><strong>Avoid Touching the Mask:</strong> Avoid touching the front of your mask while wearing it. Always wash your hands before putting on and after taking off your mask.</li>
                <li><strong>Proper Mask Care:</strong> Wash reusable masks regularly, and replace disposable masks if they become damp or dirty.</li>
            </ul>

            <h3>Social Distancing</h3>
            <img src={distance} alt="Social Distancing" className="tips-image"/>
            <ul>
                <li><strong>Maintain Distance:</strong> Stay at least 6 feet (2 meters) away from others who are not from your household, especially if they are coughing, sneezing, or not wearing a mask.</li>
                <li><strong>Avoid Crowded Places:</strong> Avoid gathering in large groups and stay away from crowded spaces like restaurants, bars, gyms, and public transport when possible.</li>
                <li><strong>Stay Home When Possible:</strong> Stay home as much as possible, especially if you feel unwell or have been in contact with someone who has tested positive for COVID-19.</li>
            </ul>

            <h3>Vaccination</h3>
            <img src={vaccine} alt="Vaccination" className="tips-image"/>
            <ul>
                <li><strong>Get Vaccinated:</strong> Get vaccinated when eligible. Vaccines are a crucial tool in preventing severe illness and slowing the spread of the virus.</li>
                <li><strong>Keep Up with Booster Shots:</strong> Follow guidelines regarding booster shots to maintain immunity, especially if new variants of concern emerge.</li>
            </ul>

            <h3>Healthy Lifestyle</h3>
            <img src={water} alt="Drinking water" className="tips-image"/>
            <ul>
                <li><strong>Boost Your Immune System:</strong> Eat a balanced diet, exercise regularly, get adequate sleep, and manage stress to keep your immune system strong.</li>
                <li><strong>Stay Hydrated:</strong> Drink plenty of fluids to maintain good health and assist in flushing toxins from your body.</li>
            </ul>

            <h3>Environmental Cleaning</h3>
            <img src={wipes} alt="Disinfecting surfaces" className="tips-image"/>
            <ul>
                <li><strong>Disinfect Surfaces:</strong> Regularly clean and disinfect frequently touched objects and surfaces, such as doorknobs, light switches, and mobile devices.</li>
                <li><strong>Ventilate Indoor Spaces:</strong> Open windows and doors to improve ventilation and reduce the concentration of airborne contaminants in indoor environments.</li>
            </ul>

            <h3>What to Do if Exposed</h3>
            <ul>
                <li><strong>Quarantine:</strong> If you have been in close contact with someone who has COVID-19, quarantine yourself for the recommended period, usually 14 days, to prevent potential spread.</li>
                <li><strong>Monitor Symptoms:</strong> Be vigilant about monitoring for symptoms of COVID-19, such as fever, cough, and shortness of breath. Get tested if you develop symptoms or suspect you have been exposed to the virus.</li>
                <li><strong>Seek Medical Advice:</strong> Consult with healthcare professionals for guidance on testing, quarantine, and treatment if you suspect you have been exposed to COVID-19.</li>
            </ul>
        </div>
    );
};

export default Tips;