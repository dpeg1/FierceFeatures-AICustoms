import React from 'react';
import styled from 'styled-components';

const Title = styled.h1`
  color: #ff4081;
  font-size: 64px;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-top: 20px;
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

const Header = () => {
  return (
    <Title>Fierce Features - AI Customs</Title>
  );
};

export default Header;
