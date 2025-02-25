// Importing Necessary Libraries
import React, { useEffect } from 'react';
import { gsap } from 'gsap';

// MainApp Component
function MainApp() {
  useEffect(() => {
    gsap.from('h1', { opacity: 0, y: -50, duration: 1.5, ease: 'power3.out' });
  }, []);

  return (
    <div className="App">
      <h1>Welcome to Fierce Features, AI Customs</h1>
      <p>This is the clean version of MainApp!</p>
    </div>
  );
}

export default MainApp;
