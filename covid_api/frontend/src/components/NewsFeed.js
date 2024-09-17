// src/components/NewsFeed.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './NewsFeed.css';

const NewsFeed = () => {
    const [articles, setArticles] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchNews = async () => {
            try {
                const response = await axios.get('https://newsapi.org/v2/everything?q=COVID-19&sortBy=publishedAt&language=en&apiKey=8eecf67953b64ce184bc8ba69886fc6e');
                const filteredArticles = response.data.articles.filter(article => 
                    (article.title && article.title.toLowerCase().includes('covid')) ||
                    (article.description && article.description.toLowerCase().includes('covid'))
                );
                
                const uniqueArticles = [];
                const titles = new Set();
                filteredArticles.forEach(article => {
                    if (!titles.has(article.title)) {
                        uniqueArticles.push(article);
                        titles.add(article.title);
                    }
                });

                setArticles(uniqueArticles);
            } catch (error) {
                console.error('Error fetching news:', error);
                if (error.response) {
                    console.log('Response data:', error.response.data);
                    console.log('Response status:', error.response.status);
                }
                setError('Failed to load news articles. Please try again later.');
            }
            
        };

        fetchNews();
    }, []);

    return (
        <div className="news-feed-container">
            <h2 style={{ color: 'white', fontWeight: 'bold' }}>Latest COVID-19 News</h2>
            {error && <p className="error-message">{error}</p>}
            <ul>
                {articles.slice(0, 5).map((article, index) => (
                    <li key={index} className="news-article">
                        <a href={article.url} target="_blank" rel="noopener noreferrer">
                            <h3>{article.title}</h3>
                            <p>{article.description}</p>
                        </a>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default NewsFeed;