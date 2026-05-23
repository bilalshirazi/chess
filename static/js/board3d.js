/* Chess Openings Academy — Three.js 3D board */

(function () {
  const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

  // Unicode chess symbols keyed by FEN character
  const SYMBOLS = {
    P: '♙', R: '♖', N: '♘', B: '♗', Q: '♕', K: '♔',
    p: '♟', r: '♜', n: '♞', b: '♝', q: '♛', k: '♚',
  };

  // ── texture factory ──────────────────────────────────────────────
  function makeTexture(fenChar) {
    const isWhite = fenChar === fenChar.toUpperCase();
    const symbol  = SYMBOLS[fenChar];
    const canvas  = document.createElement('canvas');
    canvas.width  = 160;
    canvas.height = 160;
    const ctx = canvas.getContext('2d');

    // outer glow / shadow so pieces read well on both square colours
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 2;
    ctx.shadowBlur    = 12;
    ctx.shadowColor   = isWhite ? 'rgba(0,0,0,0.55)' : 'rgba(255,255,255,0.25)';

    ctx.font         = 'bold 108px serif';
    ctx.textAlign    = 'center';
    ctx.textBaseline = 'middle';

    // outline stroke for contrast
    ctx.lineWidth   = 6;
    ctx.strokeStyle = isWhite ? '#1a1a1a' : '#e0e0e0';
    ctx.strokeText(symbol, 80, 82);

    ctx.fillStyle = isWhite ? '#f5f5f5' : '#1a1a1a';
    ctx.fillText(symbol, 80, 82);

    return new THREE.CanvasTexture(canvas);
  }

  // ── Chess3DBoard class ───────────────────────────────────────────
  class Chess3DBoard {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;

      this.pieceMeshes = [];
      this.textures    = {};

      this._buildRenderer();
      this._buildScene();
      this._buildBoard();
      this._buildLights();
      this._buildTextures();
      this._buildControls();
      this._animate();
      this._setupResize();
    }

    // ── setup ──────────────────────────────────────────────────────
    _buildRenderer() {
      const size = this.container.clientWidth || 400;
      this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
      this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      this.renderer.setSize(size, size);
      this.renderer.shadowMap.enabled = true;
      this.renderer.shadowMap.type    = THREE.PCFSoftShadowMap;
      this.container.appendChild(this.renderer.domElement);
    }

    _buildScene() {
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0x13162a);
      this.scene.fog        = new THREE.Fog(0x13162a, 22, 40);

      this.camera = new THREE.PerspectiveCamera(48, 1, 0.1, 100);
      this._resetCamera();
    }

    _buildBoard() {
      // outer border / table
      const borderGeo = new THREE.BoxGeometry(9.6, 0.18, 9.6);
      const borderMat = new THREE.MeshLambertMaterial({ color: 0x6b3a1f });
      const border    = new THREE.Mesh(borderGeo, borderMat);
      border.position.y   = -0.06;
      border.receiveShadow = true;
      this.scene.add(border);

      // 64 squares
      for (let r = 0; r < 8; r++) {
        for (let f = 0; f < 8; f++) {
          const light = (r + f) % 2 === 0;
          const geo = new THREE.BoxGeometry(1, 0.12, 1);
          const mat = new THREE.MeshLambertMaterial({
            color: light ? 0xf0d9b5 : 0xb58863,
          });
          const sq = new THREE.Mesh(geo, mat);
          sq.position.set(f - 3.5, 0, r - 3.5);
          sq.receiveShadow = true;
          this.scene.add(sq);
        }
      }

      // rank / file labels (a–h, 1–8) as small canvas sprites
      const FILES = 'abcdefgh';
      for (let i = 0; i < 8; i++) {
        this.scene.add(this._labelSprite(FILES[i], i - 3.5, -4.6));
        this.scene.add(this._labelSprite(String(i + 1),  -4.6, i - 3.5));
      }
    }

    _labelSprite(text, x, z) {
      const c = document.createElement('canvas');
      c.width  = 64; c.height = 64;
      const ctx = c.getContext('2d');
      ctx.font = 'bold 40px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = '#c9a84c';
      ctx.fillText(text, 32, 32);
      const mat  = new THREE.SpriteMaterial({ map: new THREE.CanvasTexture(c), transparent: true });
      const sp   = new THREE.Sprite(mat);
      sp.scale.set(0.55, 0.55, 1);
      sp.position.set(x, 0.1, z);
      return sp;
    }

    _buildLights() {
      this.scene.add(new THREE.AmbientLight(0xffffff, 0.65));

      const key = new THREE.DirectionalLight(0xfffbe8, 0.9);
      key.position.set(4, 12, 5);
      key.castShadow               = true;
      key.shadow.mapSize.width     = 1024;
      key.shadow.mapSize.height    = 1024;
      key.shadow.camera.near       = 0.5;
      key.shadow.camera.far        = 40;
      key.shadow.camera.left       = -8;
      key.shadow.camera.right      =  8;
      key.shadow.camera.top        =  8;
      key.shadow.camera.bottom     = -8;
      this.scene.add(key);

      const fill = new THREE.DirectionalLight(0xcce8ff, 0.3);
      fill.position.set(-4, 6, -4);
      this.scene.add(fill);
    }

    _buildTextures() {
      Object.keys(SYMBOLS).forEach((ch) => {
        this.textures[ch] = makeTexture(ch);
      });
    }

    _buildControls() {
      this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
      this.controls.enableDamping  = true;
      this.controls.dampingFactor  = 0.06;
      this.controls.minPolarAngle  = 0.15;
      this.controls.maxPolarAngle  = Math.PI / 2.05;
      this.controls.minDistance    = 5;
      this.controls.maxDistance    = 18;
      this.controls.target.set(0, 0, 0);
    }

    _resetCamera() {
      this.camera.position.set(0, 8.5, 7.5);
      this.camera.lookAt(0, 0, 0);
      if (this.controls) {
        this.controls.target.set(0, 0, 0);
        this.controls.update();
      }
    }

    // ── position update ────────────────────────────────────────────
    setPosition(fen) {
      // remove old pieces
      this.pieceMeshes.forEach((m) => this.scene.remove(m));
      this.pieceMeshes = [];

      const rows = (fen || START_FEN).split(' ')[0].split('/');
      rows.forEach((row, rankIdx) => {
        let fileIdx = 0;
        for (const ch of row) {
          if (isNaN(ch)) {
            const tex = this.textures[ch];
            if (tex) {
              const mat    = new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false });
              const sprite = new THREE.Sprite(mat);
              sprite.scale.set(0.88, 0.88, 1);
              const boardRow = 7 - rankIdx;
              sprite.position.set(fileIdx - 3.5, 0.52, boardRow - 3.5);
              this.scene.add(sprite);
              this.pieceMeshes.push(sprite);
            }
            fileIdx++;
          } else {
            fileIdx += parseInt(ch, 10);
          }
        }
      });
    }

    // ── animation loop ─────────────────────────────────────────────
    _animate() {
      requestAnimationFrame(() => this._animate());
      this.controls.update();
      this.renderer.render(this.scene, this.camera);
    }

    // ── responsive resize ──────────────────────────────────────────
    _setupResize() {
      const ro = new ResizeObserver(() => {
        const size = this.container.clientWidth;
        if (size < 10) return;
        this.renderer.setSize(size, size);
        this.camera.aspect = 1;
        this.camera.updateProjectionMatrix();
      });
      ro.observe(this.container);
    }
  }

  // ── export ────────────────────────────────────────────────────────
  window.Chess3DBoard = Chess3DBoard;
})();
