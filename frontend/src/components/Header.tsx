import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="header">
      <div className="header-content">
        <div className="header-left">
          <div className="logo">🧭</div>
          <div className="header-text">
            <h1 className="title">🌱 EcoAI Dashboard – Sustainable AI</h1>
            <p className="subtitle">
              IA Responsable : Performance + Équité + Robustesse + Durabilité
            </p>
          </div>
        </div>
        <div className="header-right">
          <span className="team-name">Team "EcoAI-Pioneers" 🚀</span>
        </div>
      </div>
    </header>
  );
};

export default Header;