import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PhoneInput from 'react-phone-input-2';
import 'react-phone-input-2/lib/style.css';
import './HealthCenters.css';
import './Pagination.css';

const servicesOptions = [
    'COVID-19 Testing',
    'Vaccination Center',
    'Emergency Room',
    'Quarantine Facility',
    'Isolation Ward',
    'Telemedicine Services',
    'Mental Health Support',
    'Respiratory Care'
];

const countries = {
        'Afghanistan': [33.0, 65.0],
        'Albania': [41.3333, 19.8167],
        'Algeria': [28.0339, 1.6596],
        'American Samoa': [-14.2700, -170.1322],
        'Andorra': [42.5462, 1.6016],
        'Angola': [-11.2027, 17.8739],
        'Anguilla': [18.2206, -63.0686],
        'Antigua and Barbuda': [17.0608, -61.7964],
        'Argentina': [-38.4161, -63.6167],
        'Armenia': [40.0691, 45.0382],
        'Aruba': [12.5211, -69.9683],
        'Australia': [-25.2744, 133.7751],
        'Austria': [47.5162, 14.5501],
        'Azerbaijan': [40.1431, 47.5769],
        'Bahamas': [25.0343, -77.3963],
        'Bahrain': [25.9304, 50.6378],
        'Bangladesh': [23.6850, 90.3563],
        'Barbados': [13.1939, -59.5432],
        'Belarus': [53.7098, 27.9534],
        'Belgium': [50.5039, 4.4699],
        'Belize': [17.1899, -88.4976],
        'Benin': [9.3077, 2.3158],
        'Bermuda': [32.3078, -64.7505],
        'Bhutan': [27.5142, 90.4336],
        'Bolivia (Plurinational State of)': [-16.2902, -63.5887],
        'Bonaire, Sint Eustatius and Saba': [12.2019, -68.2624],
        'Bosnia and Herzegovina': [43.9159, 17.6791],
        'Botswana': [-22.3285, 24.6849],
        'Brazil': [-14.2350, -51.9253],
        'British Virgin Islands': [18.4207, -64.6399],
        'Brunei Darussalam': [4.5353, 114.7277],
        'Bulgaria': [42.7339, 25.4858],
        'Burkina Faso': [12.2383, -1.5616],
        'Burundi': [-3.3731, 29.9189],
        'Cabo Verde': [16.5388, -23.0418],
        'Cambodia': [12.5657, 104.9910],
        'Cameroon': [7.3697, 12.3547],
        'Canada': [56.1304, -106.3468],
        'Cayman Islands': [19.3133, -81.2546],
        'Central African Republic': [6.6111, 20.9394],
        'Chad': [15.4542, 18.7322],
        'Chile': [-35.6751, -71.5430],
        'China': [35.8617, 104.1954],
        'Colombia': [4.5709, -74.2973],
        'Comoros': [-11.6455, 43.3333],
        'Congo': [-0.2280, 15.8277],
        'Cook Islands': [-21.2367, -159.7777],
        'Costa Rica': [9.7489, -83.7534],
        'Côte d\'Ivoire': [7.5400, -5.5471],
        'Croatia': [45.1000, 15.2000],
        'Cuba': [21.5218, -77.7812],
        'Curacao': [12.1696, -68.9900],
        'Cyprus': [35.1264, 33.4299],
        'Czechia': [49.8175, 15.4730],
        'North Korea': [40.3399, 127.5101],
        'Democratic Republic of the Congo': [-4.0383, 21.7587],
        'Denmark': [56.2639, 9.5018],
        'Djibouti': [11.8251, 42.5903],
        'Dominica': [15.4140, -61.3709],
        'Dominican Republic': [18.7357, -70.1627],
        'Ecuador': [-1.8312, -78.1834],
        'Egypt': [26.8206, 30.8025],
        'El Salvador': [13.7942, -88.8965],
        'Equatorial Guinea': [1.6508, 10.2679],
        'Eritrea': [15.1794, 39.7823],
        'Estonia': [58.5953, 25.0136],
        'Eswatini': [-26.5225, 31.4659],
        'Ethiopia': [9.1450, 40.4897],
        'Falkland Islands (Malvinas)': [-51.7963, -59.5236],
        'Faroe Islands': [61.8926, -6.9118],
        'Fiji': [-17.7134, 178.0650],
        'Finland': [61.9241, 25.7482],
        'France': [46.6034, 1.8883],
        'French Guiana': [3.9339, -53.1258],
        'French Polynesia': [-17.6797, -149.4068],
        'Gabon': [-0.8037, 11.6094],
        'Gambia': [13.4432, -15.3101],
        'Georgia': [42.3154, 43.3569],
        'Germany': [51.0, 9.0],
        'Ghana': [7.9465, -1.0232],
        'Gibraltar': [36.1408, -5.3536],
        'Greece': [39.0742, 21.8243],
        'Greenland': [71.7069, -42.6043],
        'Grenada': [12.1165, -61.6790],
        'Guadeloupe': [16.2650, -61.5510],
        'Guam': [13.4443, 144.7937],
        'Guatemala': [15.7835, -90.2308],
        'Guernsey': [49.4657, -2.5853],
        'Guinea': [9.9456, -9.6966],
        'Guinea-Bissau': [11.8037, -15.1804],
        'Guyana': [4.8604, -58.9302],
        'Haiti': [18.9712, -72.2852],
        'Holy See': [41.9029, 12.4534],
        'Honduras': [15.2000, -86.2419],
        'Hungary': [47.1625, 19.5033],
        'Iceland': [64.9631, -19.0208],
        'India': [20.5937, 78.9629],
        'Indonesia': [-0.7893, 113.9213],
        'Iran (Islamic Republic of)': [32.4279, 53.6880],
        'Iraq': [33.2232, 43.6793],
        'Ireland': [53.4129, -8.2439],
        'Isle of Man': [54.2361, -4.5481],
        'Israel': [31.0461, 34.8516],
        'Italy': [41.8719, 12.5674],
        'Jamaica': [18.1096, -77.2975],
        'Japan': [36.2048, 138.2529],
        'Jersey': [49.2144, -2.1312],
        'Jordan': [30.5852, 36.2384],
        'Kazakhstan': [48.0196, 66.9237],
        'Kenya': [-1.2864, 36.8172],
        'Kiribati': [1.8709, -157.3624],
        'Kosovo': [42.6026, 20.9030],
        'Kuwait': [29.3117, 47.4818],
        'Kyrgyzstan': [41.2044, 74.7661],
        'Laos': [19.8563, 102.4955],
        'Latvia': [56.8796, 24.6032],
        'Lebanon': [33.8547, 35.8623],
        'Lesotho': [-29.6094, 28.2336],
        'Liberia': [6.4281, -9.4295],
        'Libya': [26.3351, 17.2283],
        'Liechtenstein': [47.1660, 9.5554],
        'Lithuania': [55.1694, 23.8813],
        'Luxembourg': [49.8153, 6.1296],
        'Madagascar': [-18.7669, 46.8691],
        'Malawi': [-13.2543, 34.3015],
        'Malaysia': [4.2105, 101.9758],
        'Maldives': [3.2028, 73.2207],
        'Mali': [17.5707, -3.9962],
        'Malta': [35.9375, 14.3754],
        'Marshall Islands': [7.1315, 171.1845],
        'Martinique': [14.6415, -61.0242],
        'Mauritania': [21.0079, -10.9408],
        'Mauritius': [-20.3484, 57.5522],
        'Mayotte': [-12.8275, 45.1662],
        'Mexico': [23.6345, -102.5528],
        'Micronesia (Federated States of)': [7.4251, 150.5508],
        'Moldova (Republic of)': [47.4116, 28.3699],
        'Monaco': [43.7333, 7.4167],
        'Mongolia': [46.8625, 103.8467],
        'Montenegro': [42.7087, 19.3744],
        'Montserrat': [16.7500, -62.2000],
        'Morocco': [31.7917, -7.0926],
        'Mozambique': [-18.6657, 35.5296],
        'Myanmar': [21.9139, 95.9559],
        'Namibia': [-22.5597, 17.0826],
        'Nauru': [-0.5228, 166.9315],
        'Nepal': [28.3949, 84.1240],
        'Netherlands': [52.3676, 4.9041],
        'New Caledonia': [-20.9043, 165.6180],
        'New Zealand': [-40.9006, 174.8860],
        'Nicaragua': [12.8654, -85.2072],
        'Niger': [17.6078, 8.0817],
        'Nigeria': [9.0820, 8.6753],
        'Niue': [-19.0544, -169.8672],
        'Norfolk Island': [-29.0408, 167.9547],
        'North Macedonia': [41.6086, 21.7453],
        'Northern Mariana Islands': [15.0979, 145.6739],
        'Norway': [60.4720, 8.4689],
        'Oman': [21.5126, 55.9233],
        'Pakistan': [30.3753, 69.3451],
        'Palau': [7.5149, 134.5825],
        'Palestine, State of': [31.9474, 35.3026],
        'Panama': [8.9824, -79.5190],
        'Papua New Guinea': [-6.3149, 143.9555],
        'Paraguay': [-23.4420, -58.4438],
        'Peru': [-9.1900, -75.0152],
        'Philippines': [12.8797, 121.7740],
        'Pitcairn': [-24.7036, -127.4393],
        'Poland': [51.9194, 19.1451],
        'Portugal': [39.3999, -8.2245],
        'Puerto Rico': [18.2208, -66.5901],
        'Qatar': [25.2760, 51.5201],
        'Réunion': [-21.1151, 55.5364],
        'Romania': [45.9432, 24.9668],
        'Russian Federation': [61.5240, 105.3188],
        'Rwanda': [-1.9403, 29.8739],
        'Saint Barthélemy': [17.9000, -62.8500],
        'Saint Helena': [-15.9650, -5.7000],
        'Saint Kitts and Nevis': [17.3578, -62.7829],
        'Saint Lucia': [13.9094, -60.9789],
        'Saint Martin (French part)': [18.0708, -63.0501],
        'Saint Pierre and Miquelon': [46.8500, -56.3333],
        'Saint Vincent and the Grenadines': [12.9843, -61.2872],
        'Samoa': [-13.7590, -172.1046],
        'San Marino': [43.9333, 12.4500],
        'Sao Tome and Principe': [0.1864, 6.6131],
        'Saudi Arabia': [23.8859, 45.0792],
        'Senegal': [14.6928, -14.0078],
        'Serbia': [44.0165, 21.0059],
        'Seychelles': [-4.6796, 55.4920],
        'Sierra Leone': [8.4606, -11.7799],
        'Singapore': [1.3521, 103.8198],
        'Sint Maarten (Dutch part)': [18.0420, -63.0584],
        'Slovakia': [48.6690, 19.6990],
        'Slovenia': [46.1512, 14.9955],
        'Solomon Islands': [-9.4280, 160.0000],
        'Somalia': [5.1521, 46.1996],
        'South Africa': [-30.5595, 22.9375],
        'South Georgia and the South Sandwich Islands': [-54.4291, -36.5879],
        'South Sudan': [6.8769, 31.3069],
        'Spain': [40.4637, -3.7492],
        'Sri Lanka': [7.8731, 80.7718],
        'State of Palestine': [31.9474, 35.3026],
        'Suriname': [3.9193, -56.0278],
        'Sweden': [60.1282, 18.6435],
        'Switzerland': [46.8182, 8.2275],
        'Syrian Arab Republic': [32.5144, 36.2765],
        'Taiwan': [23.6978, 120.9605],
        'Tajikistan': [38.8610, 71.2761],
        'Tanzania, United Republic of': [-6.3690, 34.8888],
        'Thailand': [15.8700, 100.9925],
        'Timor-Leste': [-8.8742, 125.7275],
        'Togo': [8.6195, 0.8248],
        'Tokelau': [-9.2000, -171.8500],
        'Tonga': [-21.1789, -175.1982],
        'Trinidad and Tobago': [10.6918, -61.2225],
        'Tunisia': [33.8869, 9.5375],
        'Turkey': [38.9637, 35.2433],
        'Turkmenistan': [38.9697, 59.5560],
        'Tuvalu': [-7.1095, 179.1940],
        'Uganda': [1.3733, 32.2903],
        'Ukraine': [48.3794, 31.1656],
        'United Arab Emirates': [23.4241, 53.8478],
        'United Kingdom of Great Britain and Northern Ireland': [55.3781, -3.4360],
        'United States of America': [37.0902, -95.7129],
        'Uruguay': [-32.5228, -55.7658],
        'Uzbekistan': [41.3775, 64.5853],
        'Vanuatu': [-15.3767, 166.9591],
        'Venezuela (Bolivarian Republic of)': [6.4238, -66.5897],
        'Viet Nam': [14.0583, 108.2772],
        'Western Sahara': [24.2155, -12.8858],
        'Yemen': [15.5524, 48.5164],
        'Zambia': [-13.1339, 27.8493],
        'Zimbabwe': [-19.0154, 29.1549]
    };

    const getCountryByCoordinates = (latitude, longitude) => {
        for (const [country, coords] of Object.entries(countries)) {
            if (coords[0] === latitude && coords[1] === longitude) {
                return country;
            }
        }
        return 'Unknown';
    };
    
    
    const HealthCenters = () => {
        const [centers, setCenters] = useState([]);
        const [name, setName] = useState('');
        const [address, setAddress] = useState('');
        const [phoneNumber, setPhoneNumber] = useState('');
        const [services, setServices] = useState('');
        const [country, setCountry] = useState('');
        const [editingCenter, setEditingCenter] = useState(null);
        const [page, setPage] = useState(1);
        const [totalPages, setTotalPages] = useState(1);
        const itemsPerPage = 10;
        
        useEffect(() => {
            fetchCenters();
        }, [page]);
    
        const fetchCenters = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/health_centers/`, {
                    params: {
                        skip: (page - 1) * itemsPerPage,
                        limit: itemsPerPage,
                    },
                });
        
                if (response.data && response.data.centers) {
                    const centersWithCountry = response.data.centers.map(center => ({
                        ...center,
                        id: center._id,
                        country: getCountryByCoordinates(center.latitude, center.longitude)
                    }));
        
                    setCenters(centersWithCountry);
                    setTotalPages(Math.ceil(response.data.total / itemsPerPage));
                } else {
                    console.error("Invalid response format:", response.data);
                }
            } catch (error) {
                console.error("Error fetching health centers:", error);
            }
        };
        
        const changePage = (newPage) => {
            if (newPage >= 1 && newPage <= totalPages) {
                setPage(newPage);  // Cambia la página solo si está dentro del rango
            }
        };
    
        const renderPagination = () => {
            const paginationItems = [];
            const range = 2; // Número de páginas a mostrar alrededor de la página actual
    
            for (let i = 1; i <= totalPages; i++) {
                if (i === 1 || i === totalPages || (i >= page - range && i <= page + range)) {
                    paginationItems.push(
                        <button
                            key={i}
                            className={i === page ? "current-page" : ""}
                            onClick={() => changePage(i)}
                        >
                            {i}
                        </button>
                    );
                } else if ((i === page - range - 1 || i === page + range + 1) && totalPages > 2 * range + 5) {
                    paginationItems.push(<span key={i} className="page-dots">...</span>);
                }
            }
    
            return paginationItems;
        };
    
    

        const addCenter = async () => {
            if (name && address && phoneNumber && services && country) {
                try {
                    const newCenter = {
                        name: name.trim(),
                        address: address.trim(),
                        phone_number: phoneNumber.trim(),
                        services: services.trim(),
                        latitude: countries[country][0],
                        longitude: countries[country][1]
                    };
        
                    console.log("Sending data:", newCenter); // Para depuración
        
                    const response = await axios.post(
                        'http://localhost:8000/health_centers/',
                        newCenter,
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        }
                    );
        
                    if (response.data) {
                        console.log("Center created successfully:", response.data);
                        await fetchCenters();
                        clearForm();
                    }
                } catch (error) {
                    console.error("Error creating health center:", error);
                    alert(error.response?.data?.detail || 'Error creating health center');
                }
            } else {
                alert('Please fill out all fields before adding a health center');
            }
        };
    
        const clearForm = () => {
            setName('');
            setAddress('');
            setPhoneNumber('');
            setServices('');
            setCountry('');
            setEditingCenter(null);
        };
    
        const deleteCenter = async (id) => {
            try {
                await axios.delete(`http://localhost:8000/health_centers/${id}`);
                // Update the centers list immediately after successful deletion
                setCenters(centers.filter((center) => center._id !== id));
                // If you're on a page that would be empty after deletion, go to previous page
                if (centers.length === 1 && page > 1) {
                    setPage(page - 1);
                } else {
                    // Otherwise, just refresh the current page
                    fetchCenters();
                }
            } catch (error) {
                console.error("Error deleting health center:", error);
            }
        };
    
        const editCenter = (center) => {
            setEditingCenter(center);
            setName(center.name);
            setAddress(center.address);
            setPhoneNumber(center.phone_number);
            setServices(center.services);
            setCountry(getCountryByCoordinates(center.latitude, center.longitude));
        };
    
        const updateCenter = async () => {
            if (!editingCenter || !editingCenter._id) {
                console.error("No center selected for update");
                return;
            }
        
            const updatedCenter = {
                name,
                address,
                phone_number: phoneNumber,
                services,
                latitude: countries[country][0],
                longitude: countries[country][1]
            };
        
            try {
                const response = await axios.put(
                    `http://localhost:8000/health_centers/${editingCenter._id}`,
                    updatedCenter
                );
                
                if (response.data) {
                    console.log("Center updated successfully:", response.data);
                    await fetchCenters(); // Recargar la lista
                    clearForm();
                }
            } catch (error) {
                console.error("Error updating health center:", error);
                alert("Error updating health center. Please try again.");
            }
        };
    
        return (
            <div className="health-centers-container">
                <div className="form-container">
                    <h2>{editingCenter ? 'Edit Health Center' : 'Add New Health Center'}</h2>
                    
                    <label>Enter Name</label>
                    <input
                        type="text"
                        placeholder="Name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                    
                    <label>Enter Address</label>
                    <input
                        type="text"
                        placeholder="Address"
                        value={address}
                        onChange={(e) => setAddress(e.target.value)}
                    />
                    
                    <label>Enter Phone Number</label>
                    <PhoneInput
                        country={'us'}
                        value={phoneNumber}
                        onChange={(phone) => setPhoneNumber(phone)}
                        inputProps={{
                            name: 'phone',
                            required: true,
                            autoFocus: true
                        }}
                    />
                    
                    <label>Select Service</label>
                    <select
                        value={services}
                        onChange={(e) => setServices(e.target.value)}
                    >
                        <option value="">Select Services</option>
                        {servicesOptions.map((service, index) => (
                            <option key={index} value={service}>{service}</option>
                        ))}
                    </select>
                    
                    <label>Select Country</label>
                    <select
                        value={country}
                        onChange={(e) => setCountry(e.target.value)}
                    >
                        <option value="">Select Country</option>
                        {Object.keys(countries).map((countryName, index) => (
                            <option key={index} value={countryName}>{countryName}</option>
                        ))}
                    </select>
                    
                    <div className="button-group">
                        {editingCenter && (
                            <button className="cancel-button" onClick={clearForm}>
                                Cancel
                            </button>
                        )}
                        <button className={editingCenter ? "update-button" : "add-button"} onClick={editingCenter ? updateCenter : addCenter}>
                            {editingCenter ? 'Update Center' : 'Add Center'}
                        </button>
                    </div>
                </div>
    
                <div className="list-container">
                    <h2>Existing Health Centers</h2>
                    <ul>
                        {centers.map((center) => (
                            <li key={center._id}> {/* Usa _id como clave única */}
                                <p><strong>{center.name}</strong> - {center.address}</p>
                                <p>Phone: {center.phone_number}</p>
                                <p>Services: {center.services}</p>
                                <p>Country: {center.country}</p>
                                <button className="edit-button" onClick={() => editCenter(center)}>Edit</button>
                                <button className="delete-button" onClick={() => deleteCenter(center._id)}>Delete</button>
                            </li>
                        ))}
                    </ul>
                    <div className="pagination">
                    <button onClick={() => changePage(page - 1)} disabled={page === 1}>Previous</button>
                    <span>Page {page} of {totalPages}</span>
                    <button onClick={() => changePage(page + 1)} disabled={page >= totalPages}>Next</button>
                     </div>
                </div>
            </div>
        );
    };
    
    export default HealthCenters;