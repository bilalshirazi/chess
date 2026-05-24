/* Chess Openings Academy — board controller */

(function () {
  const START_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';

  let board    = null;
  let board3d  = null;
  let flipped  = (OPENING_DATA.color || '').toLowerCase() === 'black';
  let highlightsOn = true;
  let currentLineIndex = 0;
  let currentStepIndex = -1;

  // ---------- helpers ----------

  function currentLine()  { return OPENING_DATA.lines[currentLineIndex]; }
  function currentSteps() { return currentLine().steps; }
  function currentFen()   { return currentStepIndex < 0 ? START_FEN : currentSteps()[currentStepIndex].fen; }

  // ---------- move highlight: extract from/to via chess.js ----------

  function getMoveSquares(idx) {
    if (idx < 0) return { from: null, to: null };
    const steps   = currentSteps();
    const step    = steps[idx];
    const prevFen = idx === 0 ? START_FEN : steps[idx - 1].fen;
    const chess   = new Chess(prevFen);
    // Strip move-number prefix ("1. " or "1... ") to get bare SAN
    const san     = (step.san || '').replace(/^\d+\.+\s*/, '');
    const move    = chess.move(san);
    return move ? { from: move.from, to: move.to } : { from: null, to: null };
  }

  // ---------- 2D highlights ----------

  function applyHighlights2D(from, to) {
    // Remove any existing overlays
    document.querySelectorAll('.sq-hl').forEach(function (el) { el.remove(); });
    if (!highlightsOn || !from) return;

    [{ sq: from, cls: 'sq-hl sq-hl-from' }, { sq: to, cls: 'sq-hl sq-hl-to' }].forEach(function (h) {
      const squareEl = document.querySelector('#chessboard [data-square="' + h.sq + '"]');
      if (!squareEl) return;
      const overlay  = document.createElement('div');
      overlay.className = h.cls;
      squareEl.appendChild(overlay);
    });
  }

  // ---------- piece theme ----------

  const PIECE_UNICODE = {
    wP:'♙', wR:'♖', wN:'♘', wB:'♗', wQ:'♕', wK:'♔',
    bP:'♟', bR:'♜', bN:'♞', bB:'♝', bQ:'♛', bK:'♚',
  };

  function pieceDataURL(piece) {
    const canvas  = document.createElement('canvas');
    canvas.width  = 80; canvas.height = 80;
    const ctx     = canvas.getContext('2d');
    const isWhite = piece[0] === 'w';
    ctx.font         = 'bold 58px serif';
    ctx.textAlign    = 'center';
    ctx.textBaseline = 'middle';
    ctx.lineWidth    = 3.5;
    ctx.strokeStyle  = isWhite ? '#3a3a3a' : '#c0c0c0';
    ctx.strokeText(PIECE_UNICODE[piece], 40, 43);
    ctx.fillStyle = isWhite ? '#f5f5f0' : '#1a1a1a';
    ctx.fillText(PIECE_UNICODE[piece], 40, 43);
    return canvas.toDataURL();
  }

  // ---------- board init ----------

  function initBoard(fen) {
    if (board) board.destroy();
    board = Chessboard('chessboard', {
      position:    fen || START_FEN,
      pieceTheme:  pieceDataURL,
      draggable:   false,
      orientation: flipped ? 'black' : 'white',
    });
  }

  // ---------- render ----------

  function renderMoveList() {
    const list  = document.getElementById('moveList');
    list.innerHTML = '';
    const steps = currentSteps();
    steps.forEach(function (step, idx) {
      const san   = step.san || '';
      const match = san.match(/^(\d+)\./);
      if (match) {
        const numChip = document.createElement('span');
        numChip.className   = 'move-chip move-number';
        numChip.textContent = match[1] + '.';
        list.appendChild(numChip);
      }
      const chip = document.createElement('span');
      chip.className   = 'move-chip' + (idx === currentStepIndex ? ' active' : '');
      chip.textContent = san.replace(/^\d+\.\.\.\s*/, '').replace(/^\d+\.\s*/, '');
      chip.dataset.idx = idx;
      chip.addEventListener('click', function () { goToStep(idx); });
      list.appendChild(chip);
    });
  }

  function renderExplanation() {
    const box = document.getElementById('explanationBox');
    if (currentStepIndex < 0) {
      box.innerHTML = '<p>Press ▶ to start stepping through the moves, or click any move in the list.</p>';
      return;
    }
    const step = currentSteps()[currentStepIndex];
    const san  = step.san || step.move;
    box.innerHTML =
      '<strong style="color:var(--accent-2,#e8c97a);font-size:1.05rem;">' + san + '</strong>' +
      '<p style="margin-top:0.5rem;">' + step.explanation + '</p>';
  }

  function renderCounter() {
    const el    = document.getElementById('moveCounter');
    const steps = currentSteps();
    if (currentStepIndex < 0) {
      el.textContent = 'Start position · ' + steps.length + ' moves in this line';
    } else {
      el.textContent = 'Move ' + (currentStepIndex + 1) + ' of ' + steps.length;
    }
  }

  function renderAll() {
    const fen = currentFen();
    board.position(fen, true);
    if (board3d) board3d.setPosition(fen);

    const { from, to } = getMoveSquares(currentStepIndex);
    // Small delay so chessboard.js finishes placing pieces before we overlay
    setTimeout(function () { applyHighlights2D(from, to); }, 80);
    if (board3d) board3d.highlight(from, to, highlightsOn);

    renderMoveList();
    renderExplanation();
    renderCounter();
  }

  // ---------- navigation ----------

  function goToStep(idx) {
    const steps = currentSteps();
    if (idx < 0)             idx = -1;
    if (idx >= steps.length) idx = steps.length - 1;
    currentStepIndex = idx;
    renderAll();
  }

  function goToStart() { goToStep(-1); }
  function goToPrev()  { goToStep(currentStepIndex - 1); }
  function goToNext()  { goToStep(currentStepIndex + 1); }
  function goToEnd()   { goToStep(currentSteps().length - 1); }

  // ---------- flip ----------

  function flipBoard() {
    flipped = !flipped;
    initBoard(currentFen());
    if (board3d) board3d.flip(flipped);
    document.getElementById('btnFlip').textContent = flipped ? '⬆ White side' : '⬆ Black side';
    // Re-apply highlights after flip redraws the board
    const { from, to } = getMoveSquares(currentStepIndex);
    setTimeout(function () { applyHighlights2D(from, to); }, 80);
  }

  // ---------- highlights toggle ----------

  function toggleHighlights() {
    highlightsOn = !highlightsOn;
    const btn = document.getElementById('btnHighlight');
    btn.classList.toggle('active', highlightsOn);
    btn.title = highlightsOn ? 'Hide move highlights' : 'Show move highlights';
    const { from, to } = getMoveSquares(currentStepIndex);
    applyHighlights2D(from, to);
    if (board3d) board3d.highlight(from, to, highlightsOn);
  }

  // ---------- keyboard ----------

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') goToNext();
    if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   goToPrev();
    if (e.key === 'Home') goToStart();
    if (e.key === 'End')  goToEnd();
  });

  // ---------- init ----------

  document.addEventListener('DOMContentLoaded', function () {
    initBoard(START_FEN);

    if (window.Chess3DBoard) {
      board3d = new Chess3DBoard('chessboard3d');
      board3d.flip(flipped);
    }

    renderAll();

    document.getElementById('btnStart').addEventListener('click', goToStart);
    document.getElementById('btnPrev').addEventListener('click', goToPrev);
    document.getElementById('btnNext').addEventListener('click', goToNext);
    document.getElementById('btnEnd').addEventListener('click', goToEnd);
    document.getElementById('btnFlip').addEventListener('click', flipBoard);
    document.getElementById('btnHighlight').addEventListener('click', toggleHighlights);

    const resetBtn = document.getElementById('btnReset3d');
    if (resetBtn && board3d) {
      resetBtn.addEventListener('click', function () { board3d._resetCamera(); });
    }

    document.querySelectorAll('.tab-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        switchLine(parseInt(btn.dataset.lineIndex));
      });
    });
  });

  // ---------- variation tabs ----------

  function switchLine(lineIdx) {
    currentLineIndex = lineIdx;
    currentStepIndex = -1;
    document.querySelectorAll('.tab-btn').forEach(function (btn) {
      btn.classList.toggle('active', parseInt(btn.dataset.lineIndex) === lineIdx);
    });
    initBoard(START_FEN);
    renderAll();
  }
})();
