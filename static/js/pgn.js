/* Chess Academy — PGN viewer controller */

(function () {
  const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

  let board    = null;
  let board3d  = null;
  let flipped  = false;
  let steps    = [];   // [{san, fen, moveNum, isWhite}]
  let current  = -1;  // -1 = start position

  // ── PGN parsing ────────────────────────────────────────────────
  function loadPGN(pgnText) {
    const chess = new Chess();
    const ok    = chess.load_pgn(pgnText.trim());
    if (!ok) return { error: 'Could not parse PGN. Please check the format and try again.' };

    const headers = chess.header();
    const history = chess.history();

    if (history.length === 0) return { error: 'PGN parsed but contains no moves.' };

    // Replay to collect FENs
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

  // Canvas-rendered Unicode piece theme (no external images)
  var PIECE_UNICODE = {
    wP:'♙', wR:'♖', wN:'♘', wB:'♗', wQ:'♕', wK:'♔',
    bP:'♟', bR:'♜', bN:'♞', bB:'♝', bQ:'♛', bK:'♚',
  };
  function pieceDataURL(piece) {
    var c = document.createElement('canvas');
    c.width = c.height = 80;
    var ctx = c.getContext('2d');
    var isW = piece[0] === 'w';
    ctx.font = 'bold 58px serif';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.lineWidth = 3.5;
    ctx.strokeStyle = isW ? '#3a3a3a' : '#c0c0c0';
    ctx.strokeText(PIECE_UNICODE[piece], 40, 43);
    ctx.fillStyle = isW ? '#f5f5f0' : '#1a1a1a';
    ctx.fillText(PIECE_UNICODE[piece], 40, 43);
    return c.toDataURL();
  }

  // ── render ─────────────────────────────────────────────────────
  function currentFen() {
    return current < 0 ? START_FEN : steps[current].fen;
  }

  function renderAll() {
    const fen = currentFen();
    board.position(fen, true);
    if (board3d) board3d.setPosition(fen);
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
      // Strip the "1. " or "1… " prefix for the chip label
      chip.textContent = step.san.replace(/^\d+[.…]+\s*/, '');
      chip.dataset.idx = idx;
      chip.addEventListener('click', function () { goTo(idx); });
      list.appendChild(chip);
    });

    // Scroll active chip into view
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
  function goTo(idx) {
    if (idx < -1)           idx = -1;
    if (idx >= steps.length) idx = steps.length - 1;
    current = idx;
    renderAll();
  }

  function goToStart() { goTo(-1); }
  function goToPrev()  { goTo(current - 1); }
  function goToNext()  { goTo(current + 1); }
  function goToEnd()   { goTo(steps.length - 1); }

  function flipBoard() {
    flipped = !flipped;
    initBoard(currentFen());
    if (board3d) board3d.flip(flipped);
    document.getElementById('btnFlip').textContent = flipped ? '⬆ White side' : '⬆ Black side';
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
    // File upload
    document.getElementById('pgnFileInput').addEventListener('change', function (e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function (ev) {
        document.getElementById('pgnText').value = ev.target.result;
      };
      reader.readAsText(file);
    });

    // Load button
    document.getElementById('pgnLoadBtn').addEventListener('click', function () {
      startGame(document.getElementById('pgnText').value);
    });

    // Load another
    document.getElementById('btnLoadAnother').addEventListener('click', function () {
      document.getElementById('boardSection').style.display = 'none';
      document.getElementById('pgnInputSection').style.display = '';
      if (board) { board.destroy(); board = null; }
    });

    // Nav buttons
    document.getElementById('btnStart').addEventListener('click', goToStart);
    document.getElementById('btnPrev').addEventListener('click', goToPrev);
    document.getElementById('btnNext').addEventListener('click', goToNext);
    document.getElementById('btnEnd').addEventListener('click', goToEnd);
    document.getElementById('btnFlip').addEventListener('click', flipBoard);
    document.getElementById('btnReset3d').addEventListener('click', function () {
      if (board3d) board3d._resetCamera();
    });
  });
})();
