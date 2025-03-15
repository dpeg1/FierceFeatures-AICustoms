import React, { useEffect, useState } from 'react';
import { gsap } from 'gsap';
import axios from 'axios';

function MainApp() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    gsap.from('h1', { opacity: 0, y: -50, duration: 1.5, ease: 'power3.out' });

    axios.get('http://localhost:8000/')
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.error("Error fetching message:", error);
      });
  }, []);

  return (
    <div className="min-h-screen bg-black text-white p-10">
      <h1 className="text-4xl font-bold neon-text">Fierce Features, AI Customs</h1>
      <p className="mt-4 text-lg">Revolutionizing Lash and Brow Mapping with AI</p>
      <p className="mt-4 text-xl">Message from Backend: {message}</p>
    </div>
  );
}

export default MainApp;
