// frontend/src/App.js
import React from 'react';
import ProductShowcase from './components/Showcase/ProductShowcase';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="app-header">
        <h1 className="glow-text" onClick={() => window.location.reload()}>
          Fierce Features
        </h1>
      </header>
      <ProductShowcase />
    </div>
  );
}

export default App;
