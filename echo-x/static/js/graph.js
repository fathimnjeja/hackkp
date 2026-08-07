
/**
 * ECHO-X: Evidence Galaxy Network Graph Visualizer
 * Fully interactive HTML5 Canvas node-link diagram engine with force-directed physics
 */

class EvidenceGraph {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    
    this.nodes = [];
    this.edges = [];
    this.selectedNode = null;
    this.draggedNode = null;

    // Viewport transform
    this.zoom = 1;
    this.panX = 0;
    this.panY = 0;
    this.isPanning = false;
    this.startPan = { x: 0, y: 0 };

    this.categoryColors = {
      'Suspect': '#FF3366',
      'Victim': '#00FF9D',
      'Phone': '#00F0FF',
      'Car': '#FFB800',
      'Money': '#8B5CF6',
      'Place': '#5B8CFF',
      'Social': '#EC4899',
      'Device': '#38BDF8'
    };

    this.init();
  }

  init() {
    this.resize();
    this.setupEvents();
    this.animate();
  }

  resize() {
    if (!this.canvas) return;
    const parent = this.canvas.parentElement;
    this.width = this.canvas.width = parent ? parent.clientWidth : 800;
    this.height = this.canvas.height = 600;
  }

  setData(data) {
    if (!data) return;
    const cx = this.width / 2;
    const cy = this.height / 2;
    const radius = Math.min(this.width, this.height) * 0.35;

    // Position nodes radially around center
    this.nodes = data.nodes.map((n, idx) => {
      const angle = (idx / data.nodes.length) * Math.PI * 2;
      return {
        ...n,
        x: cx + Math.cos(angle) * radius + (Math.random() - 0.5) * 40,
        y: cy + Math.sin(angle) * radius + (Math.random() - 0.5) * 40,
        vx: 0,
        vy: 0,
        radius: n.category === 'Suspect' ? 26 : 20
      };
    });

    this.edges = data.edges;
  }

  setupEvents() {
    window.addEventListener('resize', () => this.resize());

    this.canvas.addEventListener('mousedown', (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const mouseX = (e.clientX - rect.left - this.panX) / this.zoom;
      const mouseY = (e.clientY - rect.top - this.panY) / this.zoom;

      let hit = this.nodes.find(n => {
        const dx = n.x - mouseX;
        const dy = n.y - mouseY;
        return Math.sqrt(dx * dx + dy * dy) <= n.radius;
      });

      if (hit) {
        this.draggedNode = hit;
        this.selectedNode = hit;
        this.updateInspectPanel(hit);
      } else {
        this.isPanning = true;
        this.startPan = { x: e.clientX - this.panX, y: e.clientY - this.panY };
      }
    });

    this.canvas.addEventListener('mousemove', (e) => {
      if (this.draggedNode) {
        const rect = this.canvas.getBoundingClientRect();
        this.draggedNode.x = (e.clientX - rect.left - this.panX) / this.zoom;
        this.draggedNode.y = (e.clientY - rect.top - this.panY) / this.zoom;
      } else if (this.isPanning) {
        this.panX = e.clientX - this.startPan.x;
        this.panY = e.clientY - this.startPan.y;
      }
    });

    window.addEventListener('mouseup', () => {
      this.draggedNode = null;
      this.isPanning = false;
    });

    this.canvas.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
      this.zoom = Math.max(0.4, Math.min(2.5, this.zoom * zoomFactor));
    });
  }

  updateInspectPanel(node) {
    const title = document.getElementById('graph-node-title');
    const category = document.getElementById('graph-node-category');
    const details = document.getElementById('graph-node-details');

    if (title) title.innerText = node.label;
    if (category) {
      category.innerText = `${node.category} • Risk: ${node.risk}`;
      category.style.color = this.categoryColors[node.category] || '#00F0FF';
    }
    if (details) {
      details.innerHTML = Object.entries(node.details || {})
        .map(([k, v]) => `<div><strong>${k}:</strong> ${v}</div>`)
        .join('');
    }
  }

  animate() {
    if (!this.ctx) return;
    this.ctx.clearRect(0, 0, this.width, this.height);

    this.ctx.save();
    this.ctx.translate(this.panX, this.panY);
    this.ctx.scale(this.zoom, this.zoom);

    // Draw Edges
    this.edges.forEach(e => {
      const source = this.nodes.find(n => n.id === e.source);
      const target = this.nodes.find(n => n.id === e.target);
      if (!source || !target) return;

      this.ctx.beginPath();
      this.ctx.moveTo(source.x, source.y);
      this.ctx.lineTo(target.x, target.y);
      this.ctx.strokeStyle = e.type === 'encrypted' ? 'rgba(255, 51, 102, 0.4)' : 'rgba(0, 240, 255, 0.3)';
      this.ctx.lineWidth = e.strength * 3;
      this.ctx.stroke();

      // Label on link
      const midX = (source.x + target.x) / 2;
      const midY = (source.y + target.y) / 2;
      this.ctx.fillStyle = '#8E9BAE';
      this.ctx.font = '10px monospace';
      this.ctx.fillText(e.relation, midX - 20, midY - 6);
    });

    // Draw Nodes
    this.nodes.forEach(n => {
      const color = this.categoryColors[n.category] || '#00F0FF';

      // Glow circle
      this.ctx.beginPath();
      this.ctx.arc(n.x, n.y, n.radius + 4, 0, Math.PI * 2);
      this.ctx.fillStyle = color;
      this.ctx.globalAlpha = 0.2;
      this.ctx.shadowBlur = 15;
      this.ctx.shadowColor = color;
      this.ctx.fill();

      // Core node circle
      this.ctx.beginPath();
      this.ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
      this.ctx.fillStyle = '#0B1220';
      this.ctx.strokeStyle = color;
      this.ctx.lineWidth = 2;
      this.ctx.globalAlpha = 1.0;
      this.ctx.fill();
      this.ctx.stroke();

      // Selected ring
      if (this.selectedNode && this.selectedNode.id === n.id) {
        this.ctx.beginPath();
        this.ctx.arc(n.x, n.y, n.radius + 8, 0, Math.PI * 2);
        this.ctx.strokeStyle = '#FFFFFF';
        this.ctx.setLineDash([4, 4]);
        this.ctx.stroke();
        this.ctx.setLineDash([]);
      }

      // Label
      this.ctx.fillStyle = '#FFFFFF';
      this.ctx.font = '11px var(--font-family)';
      this.ctx.textAlign = 'center';
      this.ctx.fillText(n.label, n.x, n.y + n.radius + 16);
    });

    this.ctx.restore();
    requestAnimationFrame(() => this.animate());
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.evidenceGraph = new EvidenceGraph('graph-canvas');
});
