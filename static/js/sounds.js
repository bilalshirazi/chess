/* Chess Academy — synthesised move/capture sounds via Web Audio API */

(function () {
  let _ctx = null;
  let _on  = true;

  function getCtx() {
    if (!_ctx) _ctx = new (window.AudioContext || window.webkitAudioContext)();
    return _ctx;
  }

  // Filtered noise burst — sounds like a wooden chess piece tap
  function play(type) {
    if (!_on) return;
    try {
      const c = getCtx();
      if (c.state === 'suspended') c.resume();

      const isCapture = type === 'capture';
      const duration  = isCapture ? 0.13  : 0.08;
      const freq      = isCapture ? 420   : 880;
      const gain      = isCapture ? 0.55  : 0.38;
      const decay     = isCapture ? 7     : 10;

      // White noise buffer with exponential envelope
      const len  = Math.ceil(c.sampleRate * duration);
      const buf  = c.createBuffer(1, len, c.sampleRate);
      const data = buf.getChannelData(0);
      for (let i = 0; i < len; i++) {
        data[i] = (Math.random() * 2 - 1) * Math.exp(-(i / len) * decay);
      }

      const src = c.createBufferSource();
      src.buffer = buf;

      // Bandpass gives the woody "knock" character
      const bp = c.createBiquadFilter();
      bp.type = 'bandpass';
      bp.frequency.value = freq;
      bp.Q.value = 1.8;

      const gainNode = c.createGain();
      gainNode.gain.value = gain;

      src.connect(bp);
      bp.connect(gainNode);
      gainNode.connect(c.destination);
      src.start();
    } catch (_e) { /* audio unavailable — silently ignore */ }
  }

  function toggle() {
    _on = !_on;
    return _on;
  }

  function isOn() { return _on; }

  window.ChessSounds = { play, toggle, isOn };
})();
