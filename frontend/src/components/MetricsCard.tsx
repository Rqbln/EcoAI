import React from 'react';

interface Metric {
  label: string;
  value: string | number;
  color?: string;
}

interface MetricsCardProps {
  title: string;
  metrics: Metric[];
  className?: string;
}

const MetricsCard: React.FC<MetricsCardProps> = ({ title, metrics, className = '' }) => {
  return (
    <div className={`metrics-card ${className}`}>
      <h3 className="card-title">{title}</h3>
      <div className="metrics-list">
        {metrics.map((metric, index) => (
          <div key={index} className="metric-item">
            <span className="metric-label">{metric.label}</span>
            <span
              className="metric-value"
              style={{ color: metric.color || '#333' }}
            >
              {metric.value}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MetricsCard;