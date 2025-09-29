import React from 'react';

interface GlobalScoreProps {
  score: number;
}

const GlobalScore: React.FC<GlobalScoreProps> = ({ score }) => {
  const getScoreColor = (score: number) => {
    if (score >= 0.8) return '#009E60'; // Vert
    if (score >= 0.6) return '#FF7A00'; // Orange
    return '#FF4757'; // Rouge
  };

  const strokeDasharray = `${score * 283} 283`; // 283 = 2π * 45 (rayon du cercle)

  return (
    <div className="global-score">
      <div className="score-circle">
        <svg width="120" height="120" viewBox="0 0 120 120">
          <circle
            cx="60"
            cy="60"
            r="45"
            fill="none"
            stroke="#e0e0e0"
            strokeWidth="8"
          />
          <circle
            cx="60"
            cy="60"
            r="45"
            fill="none"
            stroke={getScoreColor(score)}
            strokeWidth="8"
            strokeDasharray={strokeDasharray}
            strokeDashoffset="0"
            transform="rotate(-90 60 60)"
            className="score-progress"
          />
        </svg>
        <div className="score-text">
          <span className="score-value" style={{ color: getScoreColor(score) }}>
            {score.toFixed(2)}
          </span>
          <span className="score-label">Score Global</span>
        </div>
      </div>
      <div className="score-breakdown">
        <div className="breakdown-item">
          <span className="breakdown-label">Performance (40%)</span>
          <div className="breakdown-bar">
            <div
              className="breakdown-fill"
              style={{ width: '85%', backgroundColor: '#009E60' }}
            ></div>
          </div>
        </div>
        <div className="breakdown-item">
          <span className="breakdown-label">Fairness (30%)</span>
          <div className="breakdown-bar">
            <div
              className="breakdown-fill"
              style={{ width: '78%', backgroundColor: '#FF7A00' }}
            ></div>
          </div>
        </div>
        <div className="breakdown-item">
          <span className="breakdown-label">Robustesse (20%)</span>
          <div className="breakdown-bar">
            <div
              className="breakdown-fill"
              style={{ width: '82%', backgroundColor: '#009E60' }}
            ></div>
          </div>
        </div>
        <div className="breakdown-item">
          <span className="breakdown-label">Durabilité (10%)</span>
          <div className="breakdown-bar">
            <div
              className="breakdown-fill"
              style={{ width: '90%', backgroundColor: '#009E60' }}
            ></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default GlobalScore;