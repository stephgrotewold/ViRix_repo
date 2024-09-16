# ViRix - COVID-19 Information and Tracking WebApp

ViRix is a web application designed to provide up-to-date and accurate information about COVID-19, including prevention tips, news, and statistical data for countries around the world. The app includes interactive map visualizations and other useful information to help users stay informed about the pandemic.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)

## Features

- **COVID-19 Prevention Tips:** Display tips for preventing the spread of COVID-19.
- **Country-specific COVID-19 Data:** Search and display COVID-19 statistics for different countries, including total cases, new cases, and total deaths.
- **Map Visualization:** Interactive map showing the COVID-19 risk level for selected countries.
- **Latest News:** Display the latest news related to COVID-19.
- **Responsive Design:** User-friendly interface that works on various screen sizes.

## Technologies Used

- **Frontend:**
  - React.js
  - React-Leaflet for maps
  - Chart.js for data visualization
  - Axios for API requests
- **Backend:**
  - Node.js and Express (if applicable for API integration)
  - COVID-19 API for real-time data
- **Styling:**
  - CSS

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/virix-covid19-webapp.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd virix-covid19-webapp
   ```
3. **Install Dependencies:**
   ```bash
   npm install
   ```
4. **Run the Application:**
   ```bash
   npm start
   ```
   The application will start and be accessible at `http://localhost:3000`.

## Usage

1. **Search for COVID-19 Data by Country:**
   - Select a country from the dropdown and click on "Search" to view the latest COVID-19 statistics.
2. **View Prevention Tips:**
   - Scroll through the prevention tips to learn more about how to protect yourself and others.
3. **Explore the Map:**
   - View the risk level of COVID-19 on the map and explore different countries.
4. **Read the Latest News:**
   - Stay informed with the latest news related to COVID-19.

## API Integration

The project integrates with the following APIs to fetch real-time data and news:

1. **News API:** Fetches the latest news articles related to COVID-19.
   - Endpoint: `https://newsapi.org/v2/everything?q=COVID-19`

Ensure you have valid API keys for these services and update them in the project files.
