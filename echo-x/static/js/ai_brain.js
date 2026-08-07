
/**
 * ECHO-X: AI Reasoning Neural Radar & Holographic Brain Renderer
 */

class AIBrainVisualizer {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.angle = 0;
    this.init();
  }

  init() {
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.animate();
  }

  resize() {
    if (!this.canvas) return;
    const parent = this.canvas.parentElement;
    this.width = this.canvas.width = parent ? parent.clientWidth : 500;
    this.height = this.canvas.height = 350;
  }

  animate() {
    if (!this.ctx) return;
    this.ctx.clearRect(0, 0, this.width, this.height);

    const cx = this.width / 2;
    const cy = this.height / 2;
    const radius = 110;

    this.angle += 0.015;

    // Draw concentric radar circles
    for (let r = 40; r <= radius; r += 35) {
      this.ctx.beginPath();
      this.ctx.arc(cx, cy, r, 0, Math.PI * 2);
      this.ctx.strokeStyle = 'rgba(0, 240, 255, 0.15)';
      this.ctx.lineWidth = 1;
      this.ctx.stroke();
    }

    // Rotating sweep line
    this.ctx.beginPath();
    this.ctx.moveTo(cx, cy);
    this.ctx.lineTo(cx + Math.cos(this.angle) * radius, cy + Math.sin(this.angle) * radius);
    this.ctx.strokeStyle = '#00F0FF';
    this.ctx.lineWidth = 2;
    this.ctx.shadowBlur = 15;
    this.ctx.shadowColor = '#00F0FF';
    this.ctx.stroke();
    this.ctx.shadowBlur = 0;

    // Neural nodes
    const nodeCount = 8;
    for (let i = 0; i < nodeCount; i++) {
      const a = (i / nodeCount) * Math.PI * 2 + this.angle * 0.3;
      const nx = cx + Math.cos(a) * (radius - 10);
      const ny = cy + Math.sin(a) * (radius - 10);

      this.ctx.beginPath();
      this.ctx.arc(nx, ny, 6, 0, Math.PI * 2);
      this.ctx.fillStyle = i % 2 === 0 ? '#00F0FF' : '#8B5CF6';
      this.ctx.shadowBlur = 10;
      this.ctx.shadowColor = this.ctx.fillStyle;
      this.ctx.fill();

      // Connecting lines to center AI core
      this.ctx.beginPath();
      this.ctx.moveTo(cx, cy);
      this.ctx.lineTo(nx, ny);
      this.ctx.strokeStyle = 'rgba(139, 92, 246, 0.2)';
      this.ctx.stroke();
    }

    // Center Core AI
    this.ctx.beginPath();
    this.ctx.arc(cx, cy, 18, 0, Math.PI * 2);
    this.ctx.fillStyle = '#00F0FF';
    this.ctx.shadowBlur = 20;
    this.ctx.shadowColor = '#00F0FF';
    this.ctx.fill();
    this.ctx.shadowBlur = 0;

    this.ctx.fillStyle = '#000000';
    this.ctx.font = 'bold 9px var(--font-mono)';
    this.ctx.textAlign = 'center';
    this.ctx.fillText('AI CORE', cx, cy + 3);

    requestAnimationFrame(() => this.animate());
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.aiBrainVisualizer = new AIBrainVisualizer('brain-canvas');
});
