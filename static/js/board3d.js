/* Chess Openings Academy — Three.js 3D board with GLB piece models */

(function () {
  const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

  // FEN char (lowercase) -> GLB filename stem
  const FILE_MAP = {
    p: 'ChessPiecePawn',   r: 'ChessPieceRook',
    n: 'ChessPieceKnight', b: 'ChessPieceBishop',
    q: 'ChessPieceQueen',  k: 'ChessPieceKing',
  };

  // Respects the GitHub Pages sub-path (e.g. /chess/static/models/)
  const MODELS_BASE = (window.STATIC_BASE || '/static') + '/models/';

  // Scale all pieces so the tallest fits in TARGET_HEIGHT board units
  const TARGET_HEIGHT = 0.82;

  // ── Chess3DBoard ──────────────────────────────────────────────────
  class Chess3DBoard {
    constructor(containerId) {
      this.container = document.getElementById(containerId);
      if (!this.container) return;

      this.pieceMeshes = [];
      this.models      = {};   // type -> { white: Group, black: Group }
      this.pendingFen  = null;
      this.loaded      = false;

      this._buildRenderer();
      this._buildScene();
      this._buildBoard();
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

    // ── renderer / scene ─────────────────────────────────────────
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

    // ── board geometry ────────────────────────────────────────────
    _buildBoard() {
      // Outer wood border
      const bGeo = new THREE.BoxGeometry(9.6, 0.18, 9.6);
      const bMat = new THREE.MeshLambertMaterial({ color: 0x6b3a1f });
      const border = new THREE.Mesh(bGeo, bMat);
      border.position.y    = -0.06;
      border.receiveShadow = true;
      this.scene.add(border);

      // 64 squares
      for (let r = 0; r < 8; r++) {
        for (let f = 0; f < 8; f++) {
          const light = (r + f) % 2 === 0;
          const sq = new THREE.Mesh(
            new THREE.BoxGeometry(1, 0.12, 1),
            new THREE.MeshLambertMaterial({ color: light ? 0xf0d9b5 : 0xb58863 })
          );
          sq.position.set(f - 3.5, 0, r - 3.5);
          sq.receiveShadow = true;
          this.scene.add(sq);
        }
      }

      // Coordinate labels
      const FILES = 'abcdefgh';
      for (let i = 0; i < 8; i++) {
        this.scene.add(this._labelSprite(FILES[i],    i - 3.5, -4.65));
        this.scene.add(this._labelSprite(String(i+1), -4.65,   i - 3.5));
      }
    }

    _labelSprite(text, x, z) {
      const c = document.createElement('canvas');
      c.width = c.height = 64;
      const ctx = c.getContext('2d');
      ctx.font         = 'bold 40px sans-serif';
      ctx.textAlign    = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle    = '#c9a84c';
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
      key.castShadow                = true;
      key.shadow.mapSize.width      = 1024;
      key.shadow.mapSize.height     = 1024;
      key.shadow.camera.near        = 0.5;
      key.shadow.camera.far         = 40;
      key.shadow.camera.left        = -8;
      key.shadow.camera.right       =  8;
      key.shadow.camera.top         =  8;
      key.shadow.camera.bottom      = -8;
      this.scene.add(key);

      const fill = new THREE.DirectionalLight(0xcce8ff, 0.35);
      fill.position.set(-4, 6, -4);
      this.scene.add(fill);
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
      const loader = new THREE.GLTFLoader();
      const types  = Object.keys(FILE_MAP);
      let remaining = types.length;

      types.forEach(type => {
        const url = `${MODELS_BASE}${FILE_MAP[type]}.glb`;
        loader.load(
          url,
          (gltf) => {
            this.models[type] = this._extractVariants(gltf);
            if (--remaining === 0) callback();
          },
          undefined,
          (err) => {
            console.warn('Failed to load', url, err);
            if (--remaining === 0) callback();
          }
        );
      });
    }

    // Split one GLB (which contains both white + black piece) into two Groups
    _extractVariants(gltf) {
      const white = new THREE.Group();
      const black = new THREE.Group();

      gltf.scene.children.forEach(child => {
        let isWhite = false;
        child.traverse(obj => {
          if (obj.isMesh && obj.material) {
            if ((obj.material.name || '').includes('White')) isWhite = true;
          }
        });

        const clone = child.clone(true);
        clone.position.x = 0;   // remove the small side-by-side X offset
        (isWhite ? white : black).add(clone);
      });

      // Normalise both to TARGET_HEIGHT and lift off the board surface
      [white, black].forEach(group => {
        const box  = new THREE.Box3().setFromObject(group);
        const h    = box.max.y - box.min.y;
        if (h > 0) group.scale.setScalar(TARGET_HEIGHT / h);

        // Re-measure after scale, then lift so base is at y = 0.07
        const b2 = new THREE.Box3().setFromObject(group);
        group.position.y = 0.07 - b2.min.y;
      });

      return { white, black };
    }

    // ── position update ───────────────────────────────────────────
    setPosition(fen) {
      if (!this.loaded) { this.pendingFen = fen; return; }

      this.pieceMeshes.forEach(m => this.scene.remove(m));
      this.pieceMeshes = [];

      const rows = (fen || START_FEN).split(' ')[0].split('/');
      rows.forEach((row, rankIdx) => {
        let fileIdx = 0;
        for (const ch of row) {
          if (isNaN(ch)) {
            const isWhite = ch === ch.toUpperCase();
            const type    = ch.toLowerCase();
            const variant = this.models[type];

            if (variant) {
              const piece = (isWhite ? variant.white : variant.black).clone(true);
              piece.position.x = fileIdx - 3.5;
              piece.position.z = (7 - rankIdx) - 3.5;
              // position.y is already baked in from _extractVariants
              piece.traverse(o => { if (o.isMesh) o.castShadow = true; });
              this.scene.add(piece);
              this.pieceMeshes.push(piece);
            }
            fileIdx++;
          } else {
            fileIdx += parseInt(ch, 10);
          }
        }
      });
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

    // ── loader overlay ────────────────────────────────────────────
    _hideLoader() {
      const el = document.getElementById('board3d-loader');
      if (el) el.remove();
    }

    // ── render loop ───────────────────────────────────────────────
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
