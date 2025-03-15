import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useGLTF } from '@react-three/drei';

const ProductModel = ({ modelPath }) => {
  const { scene } = useGLTF(modelPath);
  return <primitive object={scene} scale={2} />;
};

const ProductShowcase = () => {
  return (
    <div className="h-screen w-full">
      <Canvas>
        <ambientLight intensity={0.5} />
        <directionalLight position={[5, 5, 5]} />
        <OrbitControls enableZoom={true} />
        <ProductModel modelPath="/assets/model-placeholder.glb" />
      </Canvas>
    </div>
  );
};

export default ProductShowcase;
