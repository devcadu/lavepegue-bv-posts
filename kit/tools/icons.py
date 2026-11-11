# Ícones simples (traço) usados nos slides — cor herdada (currentColor)
S = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'

ICONS = {
    "clock": f'<svg {S}><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "washer": f'<svg {S}><rect x="4" y="3" width="16" height="18" rx="2.5"/><circle cx="12" cy="13" r="4.5"/><path d="M7 6.5h2M15.5 6.5h1"/><path d="M9.5 13.5c1 .8 2 .8 3 0s2-.8 3 0"/></svg>',
    "dryer": f'<svg {S}><rect x="4" y="3" width="16" height="18" rx="2.5"/><circle cx="12" cy="13" r="4.5"/><path d="M7 6.5h2"/><path d="M10.5 11.2c.6.6.6 1.2 0 1.8s-.6 1.2 0 1.8M13.5 11.2c.6.6.6 1.2 0 1.8s-.6 1.2 0 1.8"/></svg>',
    "coin": f'<svg {S}><rect x="3" y="6" width="18" height="12" rx="2.5"/><circle cx="12" cy="12" r="2.6"/><path d="M6.5 9.5v.01M17.5 14.5v.01"/></svg>',
    "fold": f'<svg {S}><path d="M4 9h16v4H4zM5 13h14v4H5zM6 17h12v3H6z"/><path d="M9 9V6.5a3 3 0 0 1 6 0V9"/></svg>',
    "person": f'<svg {S}><circle cx="12" cy="8" r="3.6"/><path d="M5 20c.8-3.6 3.6-5.6 7-5.6s6.2 2 7 5.6"/></svg>',
    "scooter": f'<svg {S}><circle cx="6" cy="17" r="2.6"/><circle cx="18" cy="17" r="2.6"/><path d="M8.6 17h6.8l2-6h-4M13.4 11l-2 6M15 7h3l1.5 4"/><rect x="3" y="8" width="6" height="5" rx="1"/></svg>',
    "pin": f'<svg {S}><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.6"/></svg>',
    "pinfill": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 22s-7.5-6.6-7.5-12.3a7.5 7.5 0 0 1 15 0C19.5 15.4 12 22 12 22zm0-9.3a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/></svg>',
    "chat": f'<svg {S}><path d="M4 18.5 5.3 15A8 8 0 1 1 8.8 19L4 18.5z"/><path d="M9 10.5h6M9 13.5h4"/></svg>',
    "camera": f'<svg {S}><path d="M4 8h3l1.6-2.4h6.8L17 8h3v11H4z"/><circle cx="12" cy="13.2" r="3.6"/></svg>',
    "spark": f'<svg {S}><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6.3 6.3l2.4 2.4M15.3 15.3l2.4 2.4M17.7 6.3l-2.4 2.4M8.7 15.3l-2.4 2.4"/></svg>',
    "calendar": f'<svg {S}><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>',
    "rain": f'<svg {S}><path d="M7 15a4.5 4.5 0 1 1 1-8.9A5.5 5.5 0 0 1 18.5 8 3.6 3.6 0 0 1 18 15z"/><path d="M8 18l-1 2.5M12 18l-1 2.5M16 18l-1 2.5"/></svg>',
    "closet": f'<svg {S}><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M12 3v18M10 11v2M14 11v2"/></svg>',
    "nose": f'<svg {S}><path d="M4 10c3-4 6-4 8 0s5 4 8 0M4 15c3-4 6-4 8 0s5 4 8 0"/></svg>',
    "arrow": f'<svg {S} stroke-width="2.6"><path d="M5 12h13M13 6l6 6-6 6"/></svg>',
}

def icon(name):
    return ICONS[name]
