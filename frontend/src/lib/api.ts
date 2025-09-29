export type ServiceInfo = { id: string; name: string; url: string };


export async function listServices(): Promise<ServiceInfo[]> {
const res = await fetch('/api/services');
if (!res.ok) throw new Error('Failed to fetch services');
return res.json();
}


export function plotUrl(serviceId: string, kind: string) {
const q = new URLSearchParams({ kind, t: Date.now().toString() }).toString();
return `/api/plot/${serviceId}?${q}`;
}