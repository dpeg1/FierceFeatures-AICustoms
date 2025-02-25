import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Stars } from '@react-three/drei';
import { gsap } from 'gsap';
import styled from 'styled-components';

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

// 3D Animation Component
function FloatingCubes() {
  return (
    <mesh rotation={[10, 10, 0]}>
      <boxBufferGeometry attach="geometry" args={[2, 2, 2]} />
      <meshStandardMaterial attach="material" color="#ff4081" />
    </mesh>
  );
}

// Main App
function App() {
  React.useEffect(() => {
    gsap.from('h1', { opacity: 0, y: -50, duration: 1.5, ease: 'power3.out' });
  }, []);

  return (
    <Container>
      <Header>Make It Lash</Header>
      <Canvas>
        <OrbitControls />
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <Stars />
        <FloatingCubes />
      </Canvas>
    </Container>
  );
}

export default App;
