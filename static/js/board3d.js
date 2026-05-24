/* Chess Openings Academy — Three.js 3D board with GLB piece models */

(function () {
  const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

  const FILE_MAP = {
    p: 'ChessPiecePawn',   r: 'ChessPieceRook',
    n: 'ChessPieceKnight', b: 'ChessPieceBishop',
    q: 'ChessPieceQueen',  k: 'ChessPieceKing',
  };

  // Respects the GitHub Pages sub-path set by the template (e.g. /chess/static)
  const MODELS_BASE = (window.STATIC_BASE || '/static') + '/models/';

  const TARGET_HEIGHT = 0.82;

  // ── Chess3DBoard ──────────────────────────────────────────────────
  class Chess3DBoard {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;

      this.pieceMeshes = [];
      this.models      = {};
      this.pendingFen  = null;
      this.loaded      = false;
      this.flipped     = false;

      this._buildRenderer();
      this._buildScene();
      this._buildBoardGroup();   // all geometry in one rotatable group
      this._buildLights();
      this._buildControls();
      this._loadModels(() => {
        this.loaded = true;
        this._hideLoader();
        this.setPosition(this.pendingFen || START_FEN);
      });
      this._animate();
      this._setupResize();
    }

    // ── renderer ──────────────────────────────────────────────────
    _buildRenderer() {
      const size = this.container.clientWidth || 400;
      this.renderer = new THREE.WebGLRenderer({ antialias: true });
      this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      this.renderer.setSize(size, size);
      this.renderer.shadowMap.enabled = true;
      this.renderer.shadowMap.type    = THREE.PCFSoftShadowMap;
      this.container.appendChild(this.renderer.domElement);
    }

    _buildScene() {
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0x13162a);
      this.scene.fog         = new THREE.Fog(0x13162a, 22, 40);
      this.camera = new THREE.PerspectiveCamera(48, 1, 0.1, 100);
      this._resetCamera();
    }

    // ── board geometry — everything in a single group so we can flip it ──
    _buildBoardGroup() {
      this.boardGroup = new THREE.Group();
      this.scene.add(this.boardGroup);

      // Wood border
      const border = new THREE.Mesh(
        new THREE.BoxGeometry(9.6, 0.18, 9.6),
        new THREE.MeshLambertMaterial({ color: 0x6b3a1f })
      );
      border.position.y    = -0.06;
      border.receiveShadow = true;
      this.boardGroup.add(border);

      // 64 squares
      for (let r = 0; r < 8; r++) {
        for (let f = 0; f < 8; f++) {
          const sq = new THREE.Mesh(
            new THREE.BoxGeometry(1, 0.12, 1),
            new THREE.MeshLambertMaterial({ color: (r + f) % 2 === 0 ? 0xf0d9b5 : 0xb58863 })
          );
          sq.position.set(f - 3.5, 0, r - 3.5);
          sq.receiveShadow = true;
          this.boardGroup.add(sq);
        }
      }

      this._buildLabels();
    }

    // Rank/file labels — rebuilt when orientation changes
    _buildLabels() {
      if (this._labelSprites) {
        this._labelSprites.forEach(s => this.boardGroup.remove(s));
      }
      this._labelSprites = [];

      const FILES = this.flipped ? 'hgfedcba' : 'abcdefgh';
      const RANKS = this.flipped
        ? ['1','2','3','4','5','6','7','8']
        : ['8','7','6','5','4','3','2','1'];

      for (let i = 0; i < 8; i++) {
        // File labels along the near edge (z = +4.65)
        const fs = this._labelSprite(FILES[i], i - 3.5, 4.65);
        // Rank labels along the left edge (x = -4.65)
        const rs = this._labelSprite(RANKS[i], -4.65, i - 3.5);
        this.boardGroup.add(fs);
        this.boardGroup.add(rs);
        this._labelSprites.push(fs, rs);
      }
    }

    _labelSprite(text, x, z) {
      const c = document.createElement('canvas');
      c.width = c.height = 64;
      const ctx = c.getContext('2d');
      ctx.font = 'bold 40px sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillStyle = '#c9a84c';
      ctx.fillText(text, 32, 32);
      const sp = new THREE.Sprite(
        new THREE.SpriteMaterial({ map: new THREE.CanvasTexture(c), transparent: true })
      );
      sp.scale.set(0.55, 0.55, 1);
      sp.position.set(x, 0.1, z);
      return sp;
    }

    // ── lighting ──────────────────────────────────────────────────
    _buildLights() {
      this.scene.add(new THREE.AmbientLight(0xffffff, 0.7));
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
      this.scene.add(Object.assign(new THREE.DirectionalLight(0xcce8ff, 0.35), {
        position: new THREE.Vector3(-4, 6, -4)
      }));
    }

    // ── orbit controls ────────────────────────────────────────────
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

    // ── GLB loading ───────────────────────────────────────────────
    _loadModels(callback) {
      const loader    = new THREE.GLTFLoader();
      const types     = Object.keys(FILE_MAP);
      let remaining   = types.length;

      types.forEach(type => {
        const url = `${MODELS_BASE}${FILE_MAP[type]}.glb`;
        loader.load(
          url,
          (gltf) => { this.models[type] = this._extractVariants(gltf); if (--remaining === 0) callback(); },
          undefined,
          (err)  => { console.warn('GLB load failed:', url, err);       if (--remaining === 0) callback(); }
        );
      });
    }

    _extractVariants(gltf) {
      const white = new THREE.Group();
      const black = new THREE.Group();

      gltf.scene.children.forEach(child => {
        let isWhite = false;
        child.traverse(o => { if (o.isMesh && o.material && (o.material.name || '').includes('White')) isWhite = true; });
        const clone = child.clone(true);
        clone.position.x = 0;
        (isWhite ? white : black).add(clone);
      });

      [white, black].forEach(g => {
        const box = new THREE.Box3().setFromObject(g);
        const h   = box.max.y - box.min.y;
        if (h > 0) g.scale.setScalar(TARGET_HEIGHT / h);
        const b2 = new THREE.Box3().setFromObject(g);
        g.position.y = 0.07 - b2.min.y;
      });

      return { white, black };
    }

    // ── position update ───────────────────────────────────────────
    setPosition(fen) {
      if (!this.loaded) { this.pendingFen = fen; return; }

      this.pieceMeshes.forEach(m => this.boardGroup.remove(m));
      this.pieceMeshes = [];

      const rows = (fen || START_FEN).split(' ')[0].split('/');
      rows.forEach((row, rankIdx) => {
        let fileIdx = 0;
        for (const ch of row) {
          if (isNaN(ch)) {
            const isWhite = ch === ch.toUpperCase();
            const variant = this.models[ch.toLowerCase()];
            if (variant) {
              const piece = (isWhite ? variant.white : variant.black).clone(true);
              piece.position.x = fileIdx - 3.5;
              // rankIdx 0 = rank 8 (black back rank) → z=-3.5 (far, top of screen)
              // rankIdx 7 = rank 1 (white back rank) → z=+3.5 (near, bottom = white side)
              piece.position.z = rankIdx - 3.5;
              piece.traverse(o => { if (o.isMesh) o.castShadow = true; });
              this.boardGroup.add(piece);
              this.pieceMeshes.push(piece);
            }
            fileIdx++;
          } else {
            fileIdx += parseInt(ch, 10);
          }
        }
      });
    }

    // ── orientation ───────────────────────────────────────────────
    // flipped=false → white at bottom (default)
    // flipped=true  → black at bottom
    flip(flipped) {
      this.flipped = !!flipped;
      this.boardGroup.rotation.y = this.flipped ? Math.PI : 0;
      this._buildLabels();  // re-render labels for correct a–h / 1–8 order
      this._resetCamera();
    }

    // ── camera reset ──────────────────────────────────────────────
    _resetCamera() {
      this.camera.position.set(0, 8.5, 7.5);
      this.camera.lookAt(0, 0, 0);
      if (this.controls) {
        this.controls.target.set(0, 0, 0);
        this.controls.update();
      }
    }

    _hideLoader() {
      const el = document.getElementById('board3d-loader');
      if (el) el.remove();
    }

    _animate() {
      requestAnimationFrame(() => this._animate());
      this.controls.update();
      this.renderer.render(this.scene, this.camera);
    }

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

  window.Chess3DBoard = Chess3DBoard;
})();
