<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Delivery Route Optimizer</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet-routing-machine@latest/dist/leaflet-routing-machine.css" />
  
  <style>
    :root {
      --bg: #0d1117;
      --panel-bg: #161b22;
      --border: #30363d;
      --accent: #00e5a0;
      --accent-hover: #00ffb3;
      --route-color: #0090ff;
      --text: #c9d1d9;
      --text-muted: #8b949e;
      --depot: #ffd700;
      --font: 'Inter', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: var(--font); background: var(--bg); color: var(--text); height: 100vh; display: flex; overflow: hidden; }

    /* App Layout */
    .sidebar { width: 360px; background: var(--panel-bg); border-right: 1px solid var(--border); display: flex; flex-direction: column; z-index: 1000; box-shadow: 2px 0 10px rgba(0,0,0,0.5); }
    .main-content { flex: 1; position: relative; }
    #map { height: 100%; width: 100%; background: #0a0e16; }

    /* Sidebar Content */
    .header { padding: 20px; border-bottom: 1px solid var(--border); }
    .header h1 { font-size: 18px; color: #fff; display: flex; align-items: center; gap: 8px; letter-spacing: 0.5px; }
    .header h1 svg { width: 22px; height: 22px; fill: var(--accent); }
    
    .input-section { padding: 20px; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.1); }
    .input-group { margin-bottom: 12px; }
    .input-group label { display: block; font-size: 11px; color: var(--text-muted); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.8px; font-weight: 600; }
    .input-group input { width: 100%; padding: 10px; background: var(--bg); border: 1px solid var(--border); color: var(--text); border-radius: 6px; font-family: var(--font); outline: none; transition: border-color 0.2s, box-shadow 0.2s; }
    .input-group input:focus { border-color: var(--accent); box-shadow: 0 0 0 2px rgba(0,229,160,0.1); }
    .input-group input::placeholder { color: #4b5563; }

    .btn { display: inline-flex; align-items: center; justify-content: center; width: 100%; padding: 11px; border-radius: 6px; font-weight: 600; cursor: pointer; transition: all 0.2s; border: none; font-family: var(--font); font-size: 14px; gap: 8px; letter-spacing: 0.3px; }
    .btn-primary { background: var(--accent); color: #000; }
    .btn-primary:hover { background: var(--accent-hover); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,229,160,0.2); }
    .btn-danger { background: transparent; color: #ff7b72; border: 1px solid var(--border); }
    .btn-danger:hover { background: rgba(255,123,114,0.1); border-color: #ff7b72; }
    .btn-secondary { background: transparent; color: var(--text); border: 1px solid var(--border); }
    .btn-secondary:hover { background: var(--bg); border-color: var(--text-muted); }

    .action-buttons { padding: 15px 20px 0; }
    
    .optimize-btn-wrapper { padding: 20px; border-top: 1px solid var(--border); background: var(--panel-bg); }

    .stops-container { flex: 1; overflow-y: auto; padding: 15px 20px; }
    .stops-container::-webkit-scrollbar { width: 6px; }
    .stops-container::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

    .stop-item { display: flex; align-items: center; gap: 12px; padding: 12px; background: var(--bg); border: 1px solid var(--border); border-radius: 8px; margin-bottom: 10px; transition: transform 0.2s, border-color 0.2s; }
    .stop-item:hover { border-color: var(--text-muted); transform: translateX(2px); }
    
    .stop-icon { width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; color: #000; flex-shrink: 0; }
    .stop-icon.depot { background: var(--depot); }
    .stop-icon.point { background: var(--accent); }
    
    .stop-details { flex: 1; min-width: 0; }
    .stop-name { font-size: 13px; font-weight: 600; color: #fff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .stop-coords { font-size: 11px; color: var(--text-muted); margin-top: 4px; font-family: monospace; }
    
    .stop-remove { background: none; border: none; color: var(--text-muted); cursor: pointer; padding: 4px; border-radius: 4px; transition: all 0.2s; display: flex; align-items: center; justify-content: center; }
    .stop-remove:hover { color: #ff7b72; background: rgba(255,123,114,0.1); }

    .empty-state { text-align: center; color: var(--text-muted); padding: 40px 10px; font-size: 13px; line-height: 1.5; }
    .empty-state svg { width: 40px; height: 40px; margin-bottom: 12px; opacity: 0.4; }

    /* Results Overlay */
    .results-overlay { position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); background: rgba(22, 27, 34, 0.95); border: 1px solid var(--border); padding: 15px 30px; border-radius: 12px; backdrop-filter: blur(8px); display: none; gap: 40px; z-index: 1000; box-shadow: 0 10px 40px rgba(0,0,0,0.6); }
    .results-overlay.active { display: flex; animation: slideUp 0.3s ease-out; }
    .result-stat { text-align: center; }
    .result-value { font-size: 22px; font-weight: 700; color: var(--accent); font-family: monospace; }
    .result-label { font-size: 10px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 6px; font-weight: 600; }

    /* Loading Overlay */
    .loading-overlay { position: absolute; inset: 0; background: rgba(10, 14, 22, 0.85); backdrop-filter: blur(4px); z-index: 2000; display: none; align-items: center; justify-content: center; flex-direction: column; color: var(--accent); }
    .loading-overlay.active { display: flex; }
    .spinner { width: 44px; height: 44px; border: 3px solid rgba(0, 229, 160, 0.15); border-top-color: var(--accent); border-radius: 50%; animation: spin 0.8s linear infinite; margin-bottom: 20px; }

    @keyframes spin { to { transform: rotate(360deg); } }
    @keyframes slideUp { from { opacity: 0; transform: translate(-50%, 20px); } to { opacity: 1; transform: translate(-50%, 0); } }

    /* Leaflet Routing Machine Customization */
    .leaflet-routing-container { background: var(--panel-bg) !important; border: 1px solid var(--border) !important; color: var(--text) !important; font-family: var(--font) !important; box-shadow: 0 5px 20px rgba(0,0,0,0.5) !important; border-radius: 8px !important; }
    .leaflet-routing-alt, .leaflet-routing-alt-minimized { background: transparent !important; }
    .leaflet-routing-alt h2, .leaflet-routing-alt h3 { color: #fff !important; font-weight: 600 !important; }
    .leaflet-routing-alt td { color: var(--text) !important; }
    tr.leaflet-routing-alt-minimized { background: transparent !important; }
    .leaflet-routing-icon { filter: invert(1); } /* Basic invert for icons in dark mode */
    
    /* Map Hint */
    .map-hint { position: absolute; top: 20px; left: 50%; transform: translateX(-50%); background: rgba(22,27,34,0.9); padding: 10px 20px; border-radius: 20px; border: 1px solid var(--border); font-size: 12px; font-weight: 500; color: var(--text-muted); z-index: 1000; pointer-events: none; backdrop-filter: blur(4px); box-shadow: 0 4px 12px rgba(0,0,0,0.3); transition: opacity 0.3s; }

    /* Custom Leaflet Markers */
    .custom-marker { background: var(--accent); color: #000; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px; box-shadow: 0 2px 5px rgba(0,0,0,0.5); border: 2px solid #fff; }
    .custom-marker.depot { background: var(--depot); }

    .autocomplete-item:hover { background: var(--bg); color: var(--accent) !important; }

    /* Directions Panel */
    .directions-panel { position: absolute; top: 0; right: -400px; width: 360px; height: 100%; background: var(--panel-bg); border-left: 1px solid var(--border); z-index: 1001; transition: right 0.3s ease; display: flex; flex-direction: column; box-shadow: -2px 0 10px rgba(0,0,0,0.5); }
    .directions-panel.open { right: 0; }
    .directions-header { padding: 20px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
    .directions-header h2 { font-size: 16px; color: #fff; }
    .directions-list { flex: 1; overflow-y: auto; padding: 0; }
    .directions-list::-webkit-scrollbar { width: 6px; }
    .directions-list::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
    .direction-item { padding: 15px 20px; border-bottom: 1px solid var(--border); font-size: 13px; color: var(--text); display: flex; gap: 10px; align-items: flex-start; }
    .direction-item:hover { background: rgba(0,0,0,0.1); }
    .direction-icon { font-size: 16px; width: 20px; text-align: center; color: var(--accent); }
    .direction-text { flex: 1; }
    .direction-dist { font-size: 11px; color: var(--text-muted); font-family: monospace; margin-top: 4px; display: block; }

    /* Leaflet popup overrides */
    .leaflet-popup-content-wrapper { background: var(--panel-bg); color: var(--text); border: 1px solid var(--border); border-radius: 8px; }
    .leaflet-popup-tip { background: var(--panel-bg); }
  </style>
</head>
<body>

  <div class="sidebar">
    <div class="header">
      <h1>
        <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
        RouteOpt Pro
      </h1>
    </div>

    <div class="input-section">
      <div class="input-group" style="position: relative;">
        <label>Location Name</label>
        <input type="text" id="loc-name" placeholder="Type a place or leave blank to click map" autocomplete="off" />
        <div id="autocomplete-results" style="position: absolute; top: 100%; left: 0; width: 100%; background: var(--panel-bg); border: 1px solid var(--border); border-radius: 6px; z-index: 2000; max-height: 200px; overflow-y: auto; display: none; box-shadow: 0 4px 12px rgba(0,0,0,0.5);"></div>
      </div>
      <div style="display: flex; gap: 10px; margin-bottom: 12px;">
        <div class="input-group" style="flex: 1; margin: 0;">
          <input type="number" id="loc-lat" placeholder="Latitude" step="0.0001" />
        </div>
        <div class="input-group" style="flex: 1; margin: 0;">
          <input type="number" id="loc-lon" placeholder="Longitude" step="0.0001" />
        </div>
      </div>
      <button class="btn btn-secondary" id="btn-add">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
        Add Stop
      </button>
    </div>

    <div class="action-buttons">
      <button class="btn btn-danger" id="btn-clear">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
        Clear All Stops
      </button>
    </div>

    <div class="stops-container" id="stops-list">
      <!-- Dynamic list injected here -->
    </div>

    <div class="optimize-btn-wrapper">
      <div class="input-group" style="margin-bottom: 15px;">
        <label style="display:flex; justify-content:space-between;">Transport Mode</label>
        <select id="transport-mode" style="width: 100%; padding: 10px; background: var(--bg); border: 1px solid var(--border); color: var(--text); border-radius: 6px; font-family: var(--font); outline: none; transition: border-color 0.2s;">
          <option value="driving">🚗 Driving (Car/Truck)</option>
          <option value="bike">🚲 Cycling (Bicycle)</option>
          <option value="foot">🚶 Walking (Foot)</option>
        </select>
      </div>
      <button class="btn btn-primary" id="btn-optimize">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
        Optimize Route (Greedy)
      </button>
    </div>
  </div>

  <div class="main-content">
    <div id="map"></div>
    <div class="map-hint" id="map-hint">Click anywhere on the map to place a stop</div>
    
    <div class="results-overlay" id="results">
      <div class="result-stat">
        <div class="result-value" id="res-dist">--</div>
        <div class="result-label">Total Distance</div>
      </div>
      <div class="result-stat">
        <div class="result-value" id="res-time">--</div>
        <div class="result-label">Est. Time</div>
      </div>
      <div class="result-stat">
        <div class="result-value" id="res-stops">--</div>
        <div class="result-label">Total Stops</div>
      </div>
      <div style="border-left: 1px solid var(--border); padding-left: 30px; display: flex; flex-direction: column; gap: 8px;">
        <button id="btn-show-directions" class="btn btn-secondary" style="font-size: 11px; padding: 6px 12px; height: auto;">📍 Directions</button>
        <button id="btn-export" class="btn btn-secondary" style="font-size: 11px; padding: 6px 12px; height: auto;">🖨️ Manifest</button>
        <button id="btn-simulate" class="btn btn-secondary" style="font-size: 11px; padding: 6px 12px; height: auto;">▶️ Simulate</button>
        <button id="btn-live-nav" class="btn btn-primary" style="font-size: 11px; padding: 6px 12px; height: auto; background: #4285F4; border-color: #4285F4; color: white;">📱 Live Nav</button>
      </div>
    </div>

    <div class="loading-overlay" id="loading">
      <div class="spinner"></div>
      <div style="font-weight: 700; letter-spacing: 1.5px; font-size: 13px;" id="loading-text">COMPUTING ROUTE...</div>
    </div>

    <!-- Directions Panel -->
    <div class="directions-panel" id="directions-panel">
      <div class="directions-header">
        <h2>Turn-by-Turn Directions</h2>
        <button id="close-directions" class="btn btn-secondary" style="padding: 4px 8px; font-size: 12px; width: auto; height: auto;">Close</button>
      </div>
      <div class="directions-list" id="directions-list"></div>
    </div>
  </div>

  <!-- Scripts -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <!-- Leaflet Routing Machine -->
  <script src="https://unpkg.com/leaflet-routing-machine@latest/dist/leaflet-routing-machine.js"></script>

  <script>
    // App State
    let stops = [];
    let routingControl = null;
    let markersLayer = L.layerGroup();

    // Initialize Leaflet Map
    const map = L.map('map', { zoomControl: true }).setView([17.44, 78.39], 12);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap &copy; CARTO'
    }).addTo(map);
    markersLayer.addTo(map);

    // DOM Elements
    const elList = document.getElementById('stops-list');
    const elLat = document.getElementById('loc-lat');
    const elLon = document.getElementById('loc-lon');
    const elName = document.getElementById('loc-name');
    const elHint = document.getElementById('map-hint');
    const elResults = document.getElementById('results');
    const elLoading = document.getElementById('loading');
    const elLoadingText = document.getElementById('loading-text');
    const elResultsContainer = document.getElementById('autocomplete-results');

    let autocompleteTimeout;
    elName.addEventListener('input', (e) => {
      const val = e.target.value.trim();
      if (!val || val.length < 3) {
        elResultsContainer.style.display = 'none';
        return;
      }
      
      clearTimeout(autocompleteTimeout);
      autocompleteTimeout = setTimeout(async () => {
        try {
          const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(val)}&limit=5`);
          const data = await res.json();
          if (data && data.length > 0) {
            elResultsContainer.innerHTML = data.map(item => `
              <div class="autocomplete-item" style="padding: 10px; border-bottom: 1px solid var(--border); cursor: pointer; font-size: 12px; color: var(--text);" 
                   onclick="selectAutocomplete('${item.display_name.replace(/'/g, "\\'")}', ${item.lat}, ${item.lon})">
                ${item.display_name}
              </div>
            `).join('');
            elResultsContainer.style.display = 'block';
          } else {
            elResultsContainer.style.display = 'none';
          }
        } catch (e) {
          console.error("Autocomplete error:", e);
        }
      }, 400); // 400ms debounce
    });

    window.selectAutocomplete = function(name, lat, lon) {
      document.getElementById('loc-name').value = name.split(',')[0];
      document.getElementById('loc-lat').value = parseFloat(lat).toFixed(5);
      document.getElementById('loc-lon').value = parseFloat(lon).toFixed(5);
      document.getElementById('autocomplete-results').style.display = 'none';
    };

    document.addEventListener('click', (e) => {
      if (!elName.contains(e.target) && !elResultsContainer.contains(e.target)) {
        elResultsContainer.style.display = 'none';
      }
    });

    let animationMarker = null;
    let animationFrameId = null;
    let routeCoordinates = [];

    document.getElementById('btn-simulate').addEventListener('click', () => {
      if (!routeCoordinates || routeCoordinates.length === 0) return;
      
      if (animationMarker) {
        map.removeLayer(animationMarker);
        cancelAnimationFrame(animationFrameId);
      }

      const mode = document.getElementById('transport-mode').value;
      let svgIcon = `
        <svg width="24" height="24" viewBox="0 0 24 24">
          <rect x="5" y="2" width="14" height="20" rx="4" fill="#FFC107"/>
          <rect x="7" y="6" width="10" height="5" fill="#222"/>
          <rect x="7" y="15" width="10" height="5" fill="#222"/>
        </svg>
      `; 

      if (mode === 'bike') {
        svgIcon = `
          <svg width="24" height="24" viewBox="0 0 24 24">
            <line x1="12" y1="3" x2="12" y2="21" stroke="#00e5a0" stroke-width="2"/>
            <circle cx="12" cy="5" r="4" fill="#222" stroke="#00e5a0" stroke-width="2"/>
            <circle cx="12" cy="19" r="4" fill="#222" stroke="#00e5a0" stroke-width="2"/>
            <line x1="7" y1="11" x2="17" y2="11" stroke="#00e5a0" stroke-width="2"/>
          </svg>
        `;
      }
      if (mode === 'foot') {
        svgIcon = `
          <svg width="24" height="24" viewBox="0 0 24 24">
            <rect x="5" y="9" width="14" height="6" rx="3" fill="#0090ff"/>
            <circle cx="12" cy="12" r="5" fill="#ffd5b5"/>
          </svg>
        `;
      }

      const simulateIcon = L.divIcon({
        className: '',
        html: `<div style="width:24px; height:24px; filter: drop-shadow(0 3px 5px rgba(0,0,0,0.6)); transition: transform 0.1s linear;">${svgIcon}</div>`,
        iconSize: [24, 24],
        iconAnchor: [12, 12]
      });

      animationMarker = L.marker([routeCoordinates[0].lat, routeCoordinates[0].lng], { icon: simulateIcon, zIndexOffset: 1000 }).addTo(map);

      let i = 0;
      const speed = Math.max(1, Math.floor(routeCoordinates.length / 300)); 

      function animate() {
        if (i < routeCoordinates.length - 1) {
          const current = routeCoordinates[i];
          let nextIdx = i + speed;
          if (nextIdx >= routeCoordinates.length) nextIdx = routeCoordinates.length - 1;
          const next = routeCoordinates[nextIdx];

          animationMarker.setLatLng([current.lat, current.lng]);
          
          if (current.lat !== next.lat || current.lng !== next.lng) {
             const lat1 = current.lat * Math.PI / 180;
             const lon1 = current.lng * Math.PI / 180;
             const lat2 = next.lat * Math.PI / 180;
             const lon2 = next.lng * Math.PI / 180;
             
             const y = Math.sin(lon2 - lon1) * Math.cos(lat2);
             const x = Math.cos(lat1) * Math.sin(lat2) - Math.sin(lat1) * Math.cos(lat2) * Math.cos(lon2 - lon1);
             let bearing = Math.atan2(y, x) * 180 / Math.PI;

             const iconEl = animationMarker.getElement();
             if (iconEl && iconEl.firstChild) {
                iconEl.firstChild.style.transform = `rotate(${bearing}deg)`;
             }
          }

          i += speed;
          animationFrameId = requestAnimationFrame(animate);
        } else {
          animationMarker.setLatLng([routeCoordinates[routeCoordinates.length - 1].lat, routeCoordinates[routeCoordinates.length - 1].lng]);
        }
      }
      
      animate();
    });

    document.getElementById('btn-export').addEventListener('click', () => {
      if (stops.length === 0) return;
      
      const distText = document.getElementById('res-dist').innerText;
      const timeText = document.getElementById('res-time').innerText;

      let html = `
        <html>
        <head>
          <title>Driver Manifest - RouteOpt Pro</title>
          <style>
            body { font-family: 'Helvetica Neue', Arial, sans-serif; padding: 40px; color: #333; }
            h1 { color: #000; border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 20px; }
            .summary { margin-bottom: 30px; font-size: 16px; background: #f5f5f5; padding: 15px; border-radius: 6px; border: 1px solid #ddd; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; font-size: 14px; }
            th { background-color: #111; color: #fff; }
            .depot { font-weight: bold; background-color: #fff9c4; }
          </style>
        </head>
        <body>
          <h1>📦 Driver Route Manifest</h1>
          <div class="summary">
            <strong>Total Stops:</strong> ${stops.length} &nbsp;|&nbsp; 
            <strong>Total Distance:</strong> ${distText} &nbsp;|&nbsp; 
            <strong>Estimated Time:</strong> ${timeText}
          </div>
          <table>
            <thead>
              <tr>
                <th style="width: 80px;">Stop #</th>
                <th>Location Name</th>
                <th style="width: 200px;">Coordinates (Lat, Lon)</th>
                <th style="width: 150px;">Status / Signature</th>
              </tr>
            </thead>
            <tbody>
      `;

      stops.forEach((s, i) => {
        const isDepot = i === 0;
        html += `
          <tr class="${isDepot ? 'depot' : ''}">
            <td>${isDepot ? 'Depot' : i}</td>
            <td><strong>${s.name}</strong></td>
            <td style="font-family: monospace;">${s.lat.toFixed(4)}, ${s.lng.toFixed(4)}</td>
            <td>_________________</td>
          </tr>
        `;
      });

      html += `
            </tbody>
          </table>
          <div style="margin-top: 50px; font-size: 12px; color: #777; text-align: center;">
            Generated by RouteOpt Pro &bull; Please drive safely.
          </div>
        </body>
        </html>
      `;

      const printWindow = window.open('', '_blank');
      printWindow.document.write(html);
      printWindow.document.close();
      printWindow.focus();
      
      setTimeout(() => {
        printWindow.print();
      }, 500);
    });

    document.getElementById('btn-live-nav').addEventListener('click', () => {
      if (stops.length < 2) return;
      
      const origin = `${stops[0].lat},${stops[0].lng}`;
      const destination = `${stops[stops.length-1].lat},${stops[stops.length-1].lng}`;
      
      let waypoints = '';
      if (stops.length > 2) {
        const middleStops = stops.slice(1, stops.length - 1);
        waypoints = '&waypoints=' + middleStops.map(s => `${s.lat},${s.lng}`).join('|');
      }

      const modeVal = document.getElementById('transport-mode').value;
      let travelmode = 'driving';
      if (modeVal === 'foot') travelmode = 'walking';
      if (modeVal === 'bike') travelmode = 'bicycling';

      const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${destination}${waypoints}&travelmode=${travelmode}`;
      
      window.open(googleMapsUrl, '_blank');
    });

    document.getElementById('btn-show-directions').addEventListener('click', () => {
      document.getElementById('directions-panel').classList.add('open');
    });
    document.getElementById('close-directions').addEventListener('click', () => {
      document.getElementById('directions-panel').classList.remove('open');
    });

    function getDirectionIcon(type) {
      if (!type) return '•';
      if (type.includes('Left')) return '↩️';
      if (type.includes('Right')) return '↪️';
      if (type.includes('Straight')) return '⬆️';
      if (type.includes('Roundabout')) return '🔄';
      if (type.includes('Destination')) return '🏁';
      if (type.includes('Waypoint')) return '📍';
      return '•';
    }

    // Haversine Distance Helper (for Nearest-Neighbor)
    function distance(lat1, lon1, lat2, lon2) {
      const R = 6371; // km
      const rad = Math.PI / 180;
      const dLat = (lat2 - lat1) * rad;
      const dLon = (lon2 - lon1) * rad;
      const a = Math.sin(dLat/2)**2 + Math.cos(lat1*rad)*Math.cos(lat2*rad)*Math.sin(dLon/2)**2;
      return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    }

    // Handle Map Click
    map.on('click', function(e) {
      const lat = parseFloat(e.latlng.lat.toFixed(5));
      const lng = parseFloat(e.latlng.lng.toFixed(5));
      
      // Auto-fill inputs momentarily
      elLat.value = lat;
      elLon.value = lng;
      
      const isDepot = stops.length === 0;
      let name = elName.value.trim() || (isDepot ? 'Warehouse (Depot)' : `Delivery Stop ${stops.length + 1}`);
      
      addStop(name, lat, lng);
      
      // Clear inputs
      elLat.value = '';
      elLon.value = '';
      elName.value = '';
    });

    // Add Stop via Button (with optional Geocoding)
    document.getElementById('btn-add').addEventListener('click', async () => {
      let lat = parseFloat(elLat.value);
      let lng = parseFloat(elLon.value);
      let name = elName.value.trim();
      const isDepot = stops.length === 0;
      
      // If lat/lng missing but name provided, try Geocoding
      if (isNaN(lat) || isNaN(lng)) {
        if (!name) {
          alert('Please enter a location name or click on the map.');
          return;
        }
        
        // Use Nominatim Geocoding API
        elLoadingText.innerText = "GEOCODING LOCATION...";
        elLoading.classList.add('active');
        
        try {
          const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(name)}&limit=1`);
          const data = await res.json();
          elLoading.classList.remove('active');
          
          if (data && data.length > 0) {
            lat = parseFloat(data[0].lat).toFixed(5);
            lng = parseFloat(data[0].lon).toFixed(5);
            name = data[0].display_name.split(',')[0]; // Simplify name
          } else {
            alert('Location not found. Try a different name or click the map directly.');
            return;
          }
        } catch (e) {
          elLoading.classList.remove('active');
          alert('Error reaching geocoding service.');
          return;
        }
      }

      if (!name) name = isDepot ? 'Warehouse (Depot)' : `Delivery Stop ${stops.length + 1}`;
      
      addStop(name, parseFloat(lat), parseFloat(lng));
      
      // Reset
      elLat.value = '';
      elLon.value = '';
      elName.value = '';
      elLoadingText.innerText = "COMPUTING ROUTE...";
    });

    function addStop(name, lat, lng) {
      stops.push({ name, lat, lng, id: Date.now() });
      updateUI();
      clearRoute();
      
      // Fit bounds if more than 1 stop
      if (stops.length > 1 && !routingControl) {
        const bounds = L.latLngBounds(stops.map(s => [s.lat, s.lng]));
        map.fitBounds(bounds, { padding: [50, 50], maxZoom: 15 });
      } else if (stops.length === 1) {
        map.setView([lat, lng], 14);
      }
    }

    function removeStop(id) {
      stops = stops.filter(s => s.id !== id);
      updateUI();
      clearRoute();
    }

    document.getElementById('btn-clear').addEventListener('click', () => {
      stops = [];
      clearRoute();
      updateUI();
    });

    function clearRoute() {
      if (routingControl) {
        map.removeControl(routingControl);
        routingControl = null;
      }
      elResults.classList.remove('active');
    }

    // Refresh Sidebar and Map Markers
    function updateUI() {
      markersLayer.clearLayers();
      
      const btnOptimize = document.getElementById('btn-optimize');
      if (stops.length < 2) {
        btnOptimize.disabled = true;
        btnOptimize.style.opacity = '0.5';
        btnOptimize.style.cursor = 'not-allowed';
      } else {
        btnOptimize.disabled = false;
        btnOptimize.style.opacity = '1';
        btnOptimize.style.cursor = 'pointer';
      }

      if (stops.length === 0) {
        elList.innerHTML = `
          <div class="empty-state">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <div style="font-weight: 600; color: #c9d1d9;">No locations added</div>
            <div style="margin-top: 6px;">Type a place name, or click directly on the interactive map.</div>
          </div>
        `;
        elHint.style.opacity = '1';
        return;
      }

      elHint.style.opacity = '0';
      
      // Update List
      elList.innerHTML = stops.map((s, i) => {
        const isDepot = i === 0;
        return `
          <div class="stop-item">
            <div class="stop-icon ${isDepot ? 'depot' : 'point'}">${isDepot ? 'D' : i}</div>
            <div class="stop-details">
              <div class="stop-name">${s.name}</div>
              <div class="stop-coords">${s.lat.toFixed(4)}, ${s.lng.toFixed(4)}</div>
            </div>
            <button class="stop-remove" onclick="removeStop(${s.id})" title="Remove">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
          </div>
        `;
      }).join('');

      // Draw custom markers ONLY when routing is not active
      if (!routingControl) {
        stops.forEach((s, i) => {
          const isDepot = i === 0;
          const icon = L.divIcon({
            className: '',
            html: `<div class="custom-marker ${isDepot ? 'depot' : ''}">${isDepot ? 'D' : i}</div>`,
            iconSize: [28, 28],
            iconAnchor: [14, 14]
          });
          L.marker([s.lat, s.lng], { icon })
            .addTo(markersLayer)
            .bindPopup(`<div style="font-weight:600;font-size:14px;margin-bottom:4px;color:var(--accent);">${s.name}</div><div style="font-family:monospace;color:var(--text-muted);font-size:11px;">${s.lat}, ${s.lng}</div>`);
        });
      }
    }

    // Nearest-Neighbor algorithm for sorting
    function greedyRoute(stopsArray) {
      if (stopsArray.length < 2) return stopsArray;
      
      const sorted = [stopsArray[0]]; // Start at Depot
      const unvisited = stopsArray.slice(1);
      
      while (unvisited.length > 0) {
        let last = sorted[sorted.length - 1];
        let nearestIdx = 0;
        let minDist = Infinity;
        
        for (let i = 0; i < unvisited.length; i++) {
          let dist = distance(last.lat, last.lng, unvisited[i].lat, unvisited[i].lng);
          if (dist < minDist) { 
            minDist = dist; 
            nearestIdx = i; 
          }
        }
        
        sorted.push(unvisited[nearestIdx]);
        unvisited.splice(nearestIdx, 1);
      }
      return sorted;
    }

    function renderRoute(orderedStops) {
      // Clear static markers to avoid overlapping with routing markers
      markersLayer.clearLayers();
      if (routingControl) map.removeControl(routingControl);

      const waypoints = orderedStops.map(s => L.latLng(s.lat, s.lng));

      const mode = document.getElementById('transport-mode').value;

      // Setup Leaflet Routing Machine for real road routing
      routingControl = L.Routing.control({
        waypoints: waypoints,
        router: L.Routing.osrmv1({
          serviceUrl: 'https://router.project-osrm.org/route/v1',
          profile: mode
        }),
        lineOptions: {
          styles: [
            // Thick glowing neon blue line following actual roads
            { color: '#0050aa', opacity: 0.6, weight: 8 },
            { color: 'var(--route-color)', opacity: 1, weight: 4 }
          ]
        },
        createMarker: function(i, wp, nWps) {
          const isDepot = i === 0;
          const icon = L.divIcon({
            className: '',
            html: `<div class="custom-marker ${isDepot ? 'depot' : ''}" style="width:32px; height:32px; font-size:14px; box-shadow: 0 4px 10px rgba(0,0,0,0.8);">${isDepot ? 'D' : i}</div>`,
            iconSize: [32, 32],
            iconAnchor: [16, 16]
          });
          return L.marker(wp.latLng, { draggable: false, icon: icon })
            .bindPopup(`<div style="font-weight:bold">${orderedStops[i]?.name || 'Waypoint'}</div>`);
        },
        show: false,
        addWaypoints: false,
        draggableWaypoints: false,
        fitSelectedRoutes: true,
        routeWhileDragging: false
      }).addTo(map);

      // Event: Route successfully found
      routingControl.on('routesfound', function(e) {
        elLoading.classList.remove('active');
        const summary = e.routes[0].summary;
        const instructions = e.routes[0].instructions;
        routeCoordinates = e.routes[0].coordinates;
        
        // Display statistics
        document.getElementById('res-dist').innerText = (summary.totalDistance / 1000).toFixed(1) + ' km';
        
        const mode = document.getElementById('transport-mode').value;
        let totalTimeSeconds = summary.totalTime;
        
        // The public OSRM server only provides 'driving' times. 
        // We artificially simulate Walking and Cycling speeds here:
        if (mode === 'foot') {
           totalTimeSeconds = summary.totalDistance / 1.38; // ~5 km/h
        } else if (mode === 'bike') {
           totalTimeSeconds = summary.totalDistance / 4.16; // ~15 km/h
        }

        const mins = Math.round(totalTimeSeconds / 60);
        const hours = Math.floor(mins / 60);
        const remMins = mins % 60;
        document.getElementById('res-time').innerText = hours > 0 ? `${hours}h ${remMins}m` : `${mins} min`;
        
        document.getElementById('res-stops').innerText = orderedStops.length;
        
        // Populate instructions
        const dirList = document.getElementById('directions-list');
        dirList.innerHTML = instructions.map(inst => `
          <div class="direction-item">
            <div class="direction-icon">${getDirectionIcon(inst.type)}</div>
            <div class="direction-text">
              ${inst.text}
              <span class="direction-dist">${inst.distance > 0 ? (inst.distance >= 1000 ? (inst.distance/1000).toFixed(1) + ' km' : inst.distance + ' m') : ''}</span>
            </div>
          </div>
        `).join('');

        elResults.classList.add('active');
      });

      // Event: Routing error
      routingControl.on('routingerror', function(e) {
        elLoading.classList.remove('active');
        console.error("Routing Error:", e);
        alert('Routing engine failed to compute a path. The locations might be too far from road networks, or the routing service is temporarily unavailable.');
        updateUI(); // Restore static markers
      });
    }

    // Handle Optimize Button Click
    document.getElementById('btn-optimize').addEventListener('click', () => {
      if (stops.length < 2) {
        alert('You need at least 2 stops to optimize a route (Depot + Delivery).');
        return;
      }

      elLoadingText.innerText = "COMPUTING ROUTE...";
      elLoading.classList.add('active');

      // 1. Calculate optimized sequence using Nearest-Neighbor
      stops = greedyRoute(stops);
      
      // Update sidebar UI with the new optimized sequence
      updateUI(); 

      // 2. Render route following real roads using Leaflet Routing Machine
      renderRoute(stops);
    });

    // Auto-update route when changing transport mode
    document.getElementById('transport-mode').addEventListener('change', () => {
      if (stops.length >= 2) {
        elLoadingText.innerText = "RECALCULATING...";
        elLoading.classList.add('active');
        renderRoute(stops);
      }
    });
  </script>
</body>
</html>
