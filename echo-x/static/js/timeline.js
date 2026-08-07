
/**
 * ECHO-X: Chronological Event Timeline Renderer
 */

class TimelineEngine {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.events = [];
    this.filter = 'all';
  }

  setEvents(events) {
    this.events = events;
    this.render();
  }

  setFilter(category) {
    this.filter = category;
    this.render();
  }

  render() {
    if (!this.container) return;

    const filtered = this.events.filter(e => {
      if (this.filter === 'all') return true;
      return e.category === this.filter;
    });

    if (filtered.length === 0) {
      this.container.innerHTML = '<div class="text-muted" style="padding: 20px;">No timeline events found for this filter category.</div>';
      return;
    }

    const categoryIcons = {
      phone: 'fa-phone-volume',
      gps: 'fa-location-dot',
      bank: 'fa-file-invoice-dollar',
      camera: 'fa-video',
      witness: 'fa-user-group',
      ai_reconstruction: 'fa-brain'
    };

    const categoryColors = {
      phone: '#00F0FF',
      gps: '#5B8CFF',
      bank: '#FFB800',
      camera: '#FF3366',
      witness: '#00FF9D',
      ai_reconstruction: '#8B5CF6'
    };

    this.container.innerHTML = filtered.map(ev => `
      <div class="timeline-node">
        <div class="glass-card" style="border-left: 3px solid ${categoryColors[ev.category] || '#00F0FF'}">
          <div class="card-header" style="margin-bottom: 8px;">
            <div style="display:flex; align-items:center; gap:10px;">
              <i class="fa-solid ${categoryIcons[ev.category] || 'fa-clock'}" style="color:${categoryColors[ev.category]}"></i>
              <strong style="font-size:14px;">${ev.title}</strong>
            </div>
            <span class="badge-status badge-active">${ev.time_label}</span>
          </div>
          <p style="font-size:12px; color:var(--text-muted); margin-bottom: 10px;">${ev.description}</p>
          <div style="display:flex; justify-content:space-between; font-size:11px; font-family:var(--font-mono); color:var(--text-dim);">
            <span><i class="fa-solid fa-location-dot"></i> ${ev.location || 'Metro Command'}</span>
            <span><i class="fa-solid fa-shield-halved"></i> Confidence: ${ev.confidence}%</span>
          </div>
        </div>
      </div>
    `).join('');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.timelineEngine = new TimelineEngine('timeline-events-container');
});
