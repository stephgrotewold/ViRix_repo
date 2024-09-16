import React from 'react';
import './AboutUs.css';
import team from './images/team.jpg'; 
import team_p2 from './images/team_p2.jpg';

const AboutUs = () => {
    return (
        <div className="about-us-container">
            <h2>About Us</h2>
            <p>ViRix is a platform dedicated to providing up-to-date and accurate information about COVID-19 to help people stay informed and safe.</p>
            
            <h3>Our Mission</h3>
            <p>Our mission is to facilitate access to critical information about COVID-19 and promote healthy practices that help reduce the spread of the virus.</p>
            
            <h3>Who We Are</h3>
            <p>We are a team of students and professionals passionate about technology and public health. ViRix was created to provide a useful tool for the community, helping people stay informed about the COVID-19 situation in real time.</p>
            
            <h3>Our Story</h3>
            <p>The idea for ViRix was born during the pandemic, when we noticed the need for reliable and updated information about COVID-19. We decided to unite our skills and knowledge to create an application that makes information easy to find and raises awareness about prevention and handling of the virus.</p>
            
            <h3>Future Plans</h3>
            <p>We are committed to continuously improving ViRix, adding more features and expanding our reach to offer more detailed and relevant information for our users.</p>
            <div className="about-us-images">
                <img src={team} alt="Team" className="about-us-image"/>
                <img src={team_p2} alt="Team Part 2" className="about-us-image"/>
            </div>
        </div>
    );
};

export default AboutUs;