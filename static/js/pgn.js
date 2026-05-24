/* Chess Academy — PGN viewer controller */

(function () {
  const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

  let board        = null;
  let board3d      = null;
  let flipped      = false;
  let highlightsOn = true;
  let steps        = [];
  let current      = -1;

  // ── PGN parsing ────────────────────────────────────────────────
  function loadPGN(pgnText) {
    const chess = new Chess();
    const ok    = chess.load_pgn(pgnText.trim());
    if (!ok) return { error: 'Could not parse PGN. Please check the format and try again.' };

    const headers = chess.header();
    const history = chess.history();

    if (history.length === 0) return { error: 'PGN parsed but contains no moves.' };

    const replay = new Chess();
    const parsed = [];
    history.forEach(function (san, idx) {
      const moveNum  = Math.floor(idx / 2) + 1;
      const isWhite  = idx % 2 === 0;
      const fullSAN  = isWhite ? moveNum + '. ' + san : moveNum + '… ' + san;
      replay.move(san);
      parsed.push({ san: fullSAN, fen: replay.fen(), moveNum, isWhite });
    });

    return { steps: parsed, headers };
  }

  // ── move info: from/to squares + capture flag ──────────────────

  function getMoveInfo(idx) {
    if (idx < 0 || idx >= steps.length) return { from: null, to: null, isCapture: false };
    const step    = steps[idx];
    const prevFen = idx === 0 ? START_FEN : steps[idx - 1].fen;
    const chess   = new Chess(prevFen);
    const san     = step.san.replace(/^\d+\.+\s*/, '');
    const move    = chess.move(san);
    if (!move) return { from: null, to: null, isCapture: false };
    const isCapture = move.flags.indexOf('c') !== -1 || move.flags.indexOf('e') !== -1;
    return { from: move.from, to: move.to, isCapture };
  }

  function applyHighlights2D(from, to) {
    document.querySelectorAll('.sq-hl').forEach(function (el) { el.remove(); });
    if (!highlightsOn || !from) return;
    [{ sq: from, cls: 'sq-hl sq-hl-from' }, { sq: to, cls: 'sq-hl sq-hl-to' }].forEach(function (h) {
      const squareEl = document.querySelector('#chessboard [data-square="' + h.sq + '"]');
      if (!squareEl) return;
      const overlay = document.createElement('div');
      overlay.className = h.cls;
      squareEl.appendChild(overlay);
    });
  }

  // ── board init ─────────────────────────────────────────────────
  function initBoard(fen) {
    if (board) board.destroy();
    board = Chessboard('chessboard', {
      position:    fen || START_FEN,
      pieceTheme:  pieceDataURL,
      draggable:   false,
      orientation: flipped ? 'black' : 'white',
    });
  }

  const PIECE_UNICODE = {
    wP:'♙', wR:'♖', wN:'♘', wB:'♗', wQ:'♕', wK:'♔',
    bP:'♟', bR:'♜', bN:'♞', bB:'♝', bQ:'♛', bK:'♚',
  };
  function pieceDataURL(piece) {
    const canvas = document.createElement('canvas');
    canvas.width = canvas.height = 80;
    const ctx = canvas.getContext('2d');
    const isWhite = piece[0] === 'w';

    const glyph = PIECE_UNICODE[piece] + '\uFE0E'; // force text presentation when available
    const fontFamily =
      '"Apple Symbols","Segoe UI Symbol","Noto Sans Symbols2","Noto Sans Symbols",' +
      '"DejaVu Sans","Arial Unicode MS",serif';
    const baseFontSize = 56;
    const padding = 10;
    const targetBox = 80 - padding * 2;

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    ctx.font = '600 ' + baseFontSize + 'px ' + fontFamily;
    const metrics = ctx.measureText(glyph);
    const measuredWidth = (metrics.actualBoundingBoxLeft != null && metrics.actualBoundingBoxRight != null)
      ? (metrics.actualBoundingBoxLeft + metrics.actualBoundingBoxRight)
      : metrics.width;
    const measuredHeight = (metrics.actualBoundingBoxAscent != null && metrics.actualBoundingBoxDescent != null)
      ? (metrics.actualBoundingBoxAscent + metrics.actualBoundingBoxDescent)
      : baseFontSize;
    const safeWidth = Math.max(measuredWidth, 1);
    const safeHeight = Math.max(measuredHeight, 1);
    const scale = Math.min(targetBox / safeWidth, targetBox / safeHeight, 1);
    const fontSize = Math.max(1, Math.floor(baseFontSize * scale));
    ctx.font = '600 ' + fontSize + 'px ' + fontFamily;

    ctx.shadowColor   = 'rgba(0,0,0,0.55)';
    ctx.shadowBlur    = Math.max(2, Math.round(fontSize / 18));
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = Math.max(1, Math.round(fontSize / 56));
    ctx.lineWidth = Math.max(3, Math.round(fontSize / 14));
    ctx.strokeStyle = isWhite ? '#1a1a1a' : '#d0d0d0';
    ctx.strokeText(glyph, 40, 42);
    ctx.fillStyle = isWhite ? '#ffffff' : '#111111';
    ctx.fillText(glyph, 40, 42);
    return canvas.toDataURL('image/png');
  }

  // ── render ─────────────────────────────────────────────────────
  function currentFen() {
    return current < 0 ? START_FEN : steps[current].fen;
  }

  function renderAll() {
    const fen = currentFen();
    board.position(fen, true);
    if (board3d) board3d.setPosition(fen);

    const { from, to } = getMoveInfo(current);
    setTimeout(function () { applyHighlights2D(from, to); }, 80);
    if (board3d) board3d.highlight(from, to, highlightsOn);
    renderMoveList();
    renderExplanation();
    renderCounter();
  }

  function renderMoveList() {
    const list = document.getElementById('moveList');
    list.innerHTML = '';

    steps.forEach(function (step, idx) {
      if (step.isWhite) {
        const num = document.createElement('span');
        num.className   = 'move-chip move-number';
        num.textContent = step.moveNum + '.';
        list.appendChild(num);
      }
      const chip = document.createElement('span');
      chip.className   = 'move-chip' + (idx === current ? ' active' : '');
      chip.textContent = step.san.replace(/^\d+[.…]+\s*/, '');
      chip.dataset.idx = idx;
      chip.addEventListener('click', function () { goTo(idx, true); });
      list.appendChild(chip);
    });

    const active = list.querySelector('.move-chip.active');
    if (active) active.scrollIntoView({ block: 'nearest' });
  }

  function renderExplanation() {
    const box = document.getElementById('explanationBox');
    if (current < 0) {
      box.innerHTML = '<p>Use ▶ or arrow keys to step through the game.</p>';
      return;
    }
    const step = steps[current];
    box.innerHTML =
      '<strong style="color:var(--accent-2,#e8c97a);font-size:1.05rem;">' + step.san + '</strong>' +
      '<p style="margin-top:0.4rem;color:var(--text-muted);">' +
        (step.isWhite ? 'White' : 'Black') + ' · Move ' + step.moveNum +
      '</p>';
  }

  function renderCounter() {
    const el = document.getElementById('moveCounter');
    if (current < 0) {
      el.textContent = 'Start · ' + steps.length + ' moves';
    } else {
      el.textContent = 'Move ' + (current + 1) + ' of ' + steps.length;
    }
  }

  // ── navigation ─────────────────────────────────────────────────
  function goTo(idx, withSound) {
    if (idx < -1)            idx = -1;
    if (idx >= steps.length) idx = steps.length - 1;
    current = idx;
    if (withSound && idx >= 0 && window.ChessSounds) {
      const { isCapture } = getMoveInfo(idx);
      ChessSounds.play(isCapture ? 'capture' : 'move');
    }
    renderAll();
  }

  function goToStart() { goTo(-1); }
  function goToPrev()  { goTo(current - 1); }
  function goToNext()  { goTo(current + 1, true); }
  function goToEnd()   { goTo(steps.length - 1); }

  function flipBoard() {
    flipped = !flipped;
    initBoard(currentFen());
    if (board3d) board3d.flip(flipped);
    document.getElementById('btnFlip').textContent = flipped ? '⬆ White side' : '⬆ Black side';
    const { from, to } = getMoveInfo(current);
    setTimeout(function () { applyHighlights2D(from, to); }, 80);
  }

  function toggleHighlights() {
    highlightsOn = !highlightsOn;
    const btn = document.getElementById('btnHighlight');
    btn.classList.toggle('active', highlightsOn);
    const { from, to } = getMoveInfo(current);
    applyHighlights2D(from, to);
    if (board3d) board3d.highlight(from, to, highlightsOn);
  }

  function toggleSound() {
    if (!window.ChessSounds) return;
    const on = ChessSounds.toggle();
    const btn = document.getElementById('btnSound');
    btn.classList.toggle('active', on);
    btn.textContent = on ? '🔊 Sound' : '🔇 Sound';
  }

  // ── game header ────────────────────────────────────────────────
  function renderGameHeader(headers) {
    const el = document.getElementById('pgnGameHeader');
    const parts = [];
    if (headers.White || headers.Black) {
      parts.push('<strong>' + (headers.White || '?') + '</strong> vs <strong>' + (headers.Black || '?') + '</strong>');
    }
    if (headers.Event && headers.Event !== '?') parts.push(headers.Event);
    if (headers.Date  && headers.Date  !== '????.??.??') parts.push(headers.Date);
    if (headers.Result) parts.push(headers.Result);
    el.innerHTML = parts.length ? '<p class="pgn-game-info">' + parts.join(' · ') + '</p>' : '';
  }

  // ── game load ──────────────────────────────────────────────────
  function startGame(pgnText) {
    const result = loadPGN(pgnText);
    if (result.error) {
      const err = document.getElementById('pgnError');
      err.textContent = result.error;
      err.style.display = 'block';
      return;
    }

    steps   = result.steps;
    current = -1;

    document.getElementById('pgnInputSection').style.display = 'none';
    document.getElementById('pgnError').style.display = 'none';
    document.getElementById('boardSection').style.display = '';

    renderGameHeader(result.headers);
    initBoard(START_FEN);

    if (window.Chess3DBoard && !board3d) {
      board3d = new Chess3DBoard('chessboard3d');
      board3d.flip(flipped);
    }

    renderAll();
  }

  // ── keyboard ───────────────────────────────────────────────────
  document.addEventListener('keydown', function (e) {
    if (document.getElementById('boardSection').style.display === 'none') return;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') goToNext();
    if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   goToPrev();
    if (e.key === 'Home') goToStart();
    if (e.key === 'End')  goToEnd();
  });

  // ── init ───────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('pgnFileInput').addEventListener('change', function (e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function (ev) {
        document.getElementById('pgnText').value = ev.target.result;
      };
      reader.readAsText(file);
    });

    document.getElementById('pgnLoadBtn').addEventListener('click', function () {
      startGame(document.getElementById('pgnText').value);
    });

    document.getElementById('btnLoadAnother').addEventListener('click', function () {
      document.getElementById('boardSection').style.display = 'none';
      document.getElementById('pgnInputSection').style.display = '';
      if (board) { board.destroy(); board = null; }
    });

    document.getElementById('btnStart').addEventListener('click', goToStart);
    document.getElementById('btnPrev').addEventListener('click', goToPrev);
    document.getElementById('btnNext').addEventListener('click', goToNext);
    document.getElementById('btnEnd').addEventListener('click', goToEnd);
    document.getElementById('btnFlip').addEventListener('click', flipBoard);
    document.getElementById('btnHighlight').addEventListener('click', toggleHighlights);
    document.getElementById('btnSound').addEventListener('click', toggleSound);
    document.getElementById('btnReset3d').addEventListener('click', function () {
      if (board3d) board3d._resetCamera();
    });
  });
})();
