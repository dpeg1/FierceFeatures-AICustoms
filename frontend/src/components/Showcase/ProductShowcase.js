import React, { useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';

const ProductModel = ({ modelPath }) => {
  const { scene } = useGLTF(modelPath);
  return <primitive object={scene} scale={2} />;
};

const categories = [
  { name: 'Lashes', modelPath: '/assets/lash-model.glb' },
  { name: 'Brows', modelPath: '/assets/brow-model.glb' },
  { name: 'Lash & Brow Combo', modelPath: '/assets/combo-model.glb' }
];

const ProductShowcase = () => {
  const [selectedCategory, setSelectedCategory] = useState(categories[0]);

  return (
    <div>
      <h2 style={{ color: '#ff4081', textAlign: 'center' }}>Choose Your Style</h2>
      <div style={{ display: 'flex', justifyContent: 'center', gap: '20px' }}>
        {categories.map((category) => (
          <button
            key={category.name}
            onClick={() => setSelectedCategory(category)}
            style={{
              padding: '10px 20px',
              border: 'none',
              borderRadius: '5px',
              background: '#ff4081',
              color: '#fff',
              cursor: 'pointer',
            }}
          >
            {category.name}
          </button>
        ))}
      </div>
      <Canvas>
        <ambientLight intensity={0.5} />
        <directionalLight position={[5, 5, 5]} />
        <OrbitControls enableZoom={true} />
        <ProductModel modelPath={selectedCategory.modelPath} />
      </Canvas>
    </div>
  );
};

export default ProductShowcase;
