import React, { useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';
import './ProductShowcase.css';

const ProductModel = ({ modelPath }) => {
  const { scene } = useGLTF(modelPath);
  return <primitive object={scene} scale={2} />;
};

const categories = {
  'Lash Styles': [
    { name: 'Natural Lash', image: '/assets/placeholders/natural-lash.png' },
    { name: 'Dramatic Lash', image: '/assets/placeholders/dramatic-lash.png' },
    { name: 'Cat Eye Lash', image: '/assets/placeholders/cat-eye-lash.png' }
  ],
  'Brow Styles': [
    { name: 'Feathered Brow', image: '/assets/placeholders/feathered-brow.png' },
    { name: 'Bold Brow', image: '/assets/placeholders/bold-brow.png' }
  ],
  Accessories: [
    { name: 'Lash Glue', image: '/assets/placeholders/lash-glue.png' },
    { name: 'Brow Pencil', image: '/assets/placeholders/brow-pencil.png' }
  ]
};

const ProductShowcase = () => {
  const [selectedCategory, setSelectedCategory] = useState('Lash Styles');

  return (
    <div className="showcase-container">
      <h1 className="glow-text">Fierce Features - AI Customs</h1>

      <div className="category-buttons">
        {Object.keys(categories).map((category) => (
          <button
            key={category}
            className={selectedCategory === category ? 'active' : ''}
            onClick={() => setSelectedCategory(category)}
          >
            {category}
          </button>
        ))}
      </div>

      <div className="placeholder-gallery">
        {categories[selectedCategory].map((item) => (
          <div className="placeholder-item" key={item.name}>
            <img src={item.image} alt={item.name} className="placeholder-img" />
            <p>{item.name}</p>
          </div>
        ))}
      </div>

      <Canvas>
        <ambientLight intensity={0.5} />
        <directionalLight position={[5, 5, 5]} />
        <OrbitControls enableZoom={true} />
        <ProductModel modelPath="/assets/lash-model.glb" />
      </Canvas>
    </div>
  );
};

export default ProductShowcase;
