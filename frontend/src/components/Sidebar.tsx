import React from 'react';

interface SidebarProps {
  activeSection: string;
  onSectionChange: (section: string) => void;
  collapsed: boolean;
  onToggle: () => void;
}

const navigationItems = [
  { id: 'overview', label: 'Vue globale', icon: '📊' },
  { id: 'performance', label: 'Modèle & performance', icon: '⚡' },
  { id: 'fairness', label: 'Fairness & biais', icon: '⚖️' },
  { id: 'robustness', label: 'Robustesse', icon: '🛡️' },
  { id: 'sustainability', label: 'Durabilité', icon: '🌱' },
  { id: 'explainability', label: 'Explicabilité', icon: '💡' },
  { id: 'compliance', label: 'Conformité AI Act', icon: '📋' },
  { id: 'monitoring', label: 'Monitoring & drift', icon: '📈' },
  { id: 'conclusion', label: 'Conclusion', icon: '🎯' },
];

const Sidebar: React.FC<SidebarProps> = ({
  activeSection,
  onSectionChange,
  collapsed,
  onToggle
}) => {
  return (
    <>
      <button className="sidebar-toggle" onClick={onToggle}>
        {collapsed ? '☰' : '✕'}
      </button>
      <nav className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
        <ul className="sidebar-nav">
          {navigationItems.map((item) => (
            <li key={item.id}>
              <button
                className={`nav-item ${activeSection === item.id ? 'active' : ''}`}
                onClick={() => onSectionChange(item.id)}
                title={item.label}
              >
                <span className="nav-icon">{item.icon}</span>
                {!collapsed && <span className="nav-label">{item.label}</span>}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </>
  );
};

export default Sidebar;