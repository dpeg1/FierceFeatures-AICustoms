import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Stars } from '@react-three/drei';
import styled from 'styled-components';
import ProductShowcase from './components/Showcase/ProductShowcase';

// Styled Components
const Container = styled.div`
  width: 100vw;
  height: 100vh;
  background: radial-gradient(ellipse at center, #0d0d0d 0%, #030303 100%);
  overflow: hidden;
`;

const Header = styled.h1`
  color: #ff4081;
  font-size: 64px;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-top: 50px;
  animation: neon-glow 1.5s infinite alternate;
  text-shadow: 0 0 8px #ff4081, 0 0 16px #ff4081;
  
  @keyframes neon-glow {
    0% {
      text-shadow: 0 0 8px #ff4081, 0 0 16px #ff4081;
    }
    100% {
      text-shadow: 0 0 20px #ff4081, 0 0 40px #ff4081;
    }
  }
`;

function App() {
  return (
    <Container>
      <Header>Fierce Features - AI Customs</Header>
      <Canvas>
        <OrbitControls />
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <Stars />
      </Canvas>
      <ProductShowcase />
    </Container>
  );
}

export default App;
