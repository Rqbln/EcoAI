import React from 'react';
import { plotUrl } from '../lib/api';


export default function PlotCard({ serviceId, title, kind }: { serviceId: string; title: string; kind: string }) {
const [src, setSrc] = React.useState(plotUrl(serviceId, kind));
const refresh = () => setSrc(plotUrl(serviceId, kind));


return (
<div className="plot-card">
<div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:'var(--spacing-small)'}}>
<div>
<div className="badge badge-success">{serviceId}</div>
<h3>{title}</h3>
</div>
<button className="btn btn-secondary" onClick={refresh}>🔄 Refresh</button>
</div>
<img src={src} alt={`${title} plot`} style={{maxWidth: '100%', height: 'auto'}} />
</div>
);
}