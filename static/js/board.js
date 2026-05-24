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

  // ---------- move info: from/to squares + capture flag ----------

  function getMoveInfo(idx) {
    if (idx < 0) return { from: null, to: null, isCapture: false };
    const steps   = currentSteps();
    const step    = steps[idx];
    const prevFen = idx === 0 ? START_FEN : steps[idx - 1].fen;
    const chess   = new Chess(prevFen);
    const san     = (step.san || '').replace(/^\d+\.+\s*/, '');
    const move    = chess.move(san);
    if (!move) return { from: null, to: null, isCapture: false };
    const isCapture = move.flags.indexOf('c') !== -1 || move.flags.indexOf('e') !== -1;
    return { from: move.from, to: move.to, isCapture };
  }

  // ---------- 2D highlights ----------

  function applyHighlights2D(from, to) {
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
    const canvas = document.createElement('canvas');
    const canvasSize = 96;
    canvas.width = canvas.height = canvasSize;
    const ctx = canvas.getContext('2d');
    const isWhite = piece[0] === 'w';

    // iOS Safari can fall back to a different font for individual chess glyphs
    // (notably the black pawn), causing inconsistent visual sizes. Use a symbol
    // font stack and scale glyphs to fit a consistent box.
    const glyph = PIECE_UNICODE[piece] + '\uFE0E'; // force text presentation when available
    const fontFamily =
      '"Apple Symbols","Segoe UI Symbol","Noto Sans Symbols2","Noto Sans Symbols",' +
      '"DejaVu Sans","Arial Unicode MS",serif';
    const baseFontSize = 68;
    // Leave extra headroom so stroke + shadow never get clipped by the canvas bounds.
    const padding = 18;
    const targetBox = canvasSize - padding * 2;

    ctx.textAlign = 'left';
    ctx.textBaseline = 'alphabetic';

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

    // Shadow makes white pieces visible on light squares
    ctx.lineJoin      = 'round';
    ctx.lineCap       = 'round';
    ctx.shadowColor   = 'rgba(0,0,0,0.55)';
    ctx.shadowBlur    = Math.max(2, Math.round(fontSize / 18));
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = Math.max(1, Math.round(fontSize / 56));
    ctx.lineWidth    = Math.max(3, Math.round(fontSize / 14));
    ctx.strokeStyle  = isWhite ? '#1a1a1a' : '#d0d0d0';
    const finalMetrics = ctx.measureText(glyph);
    const hasBoxes =
      finalMetrics.actualBoundingBoxLeft != null &&
      finalMetrics.actualBoundingBoxRight != null &&
      finalMetrics.actualBoundingBoxAscent != null &&
      finalMetrics.actualBoundingBoxDescent != null;
    const width = hasBoxes
      ? (finalMetrics.actualBoundingBoxLeft + finalMetrics.actualBoundingBoxRight)
      : targetBox;
    const height = hasBoxes
      ? (finalMetrics.actualBoundingBoxAscent + finalMetrics.actualBoundingBoxDescent)
      : targetBox;
    const x = hasBoxes ? ((canvasSize - width) / 2 + finalMetrics.actualBoundingBoxLeft) : (canvasSize / 2);
    const y = hasBoxes ? ((canvasSize - height) / 2 + finalMetrics.actualBoundingBoxAscent) : (canvasSize / 2);
    if (!hasBoxes) {
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
    }
    ctx.strokeText(glyph, x, y);
    ctx.fillStyle = isWhite ? '#ffffff' : '#111111';
    ctx.fillText(glyph, x, y);
    return canvas.toDataURL('image/png');
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
    setTimeout(addExtraNotation, 50);
  }

  function addExtraNotation() {
    const boardEl = document.getElementById('chessboard');
    if (!boardEl) return;
    boardEl.querySelectorAll('.sq-xnote').forEach(function (el) { el.remove(); });
    const files = flipped ? 'hgfedcba'.split('') : 'abcdefgh'.split('');
    const ranks = flipped ? ['1','2','3','4','5','6','7','8'] : ['8','7','6','5','4','3','2','1'];
    // File labels on top and bottom rows
    for (let f = 0; f < 8; f++) {
      [ranks[0], ranks[7]].forEach(function (rank) {
        const sq = boardEl.querySelector('[data-square="' + files[f] + rank + '"]');
        if (!sq) return;
        const el = document.createElement('span');
        el.className = 'sq-xnote sq-xnote-file';
        el.textContent = files[f];
        sq.appendChild(el);
      });
    }
    // Rank labels on left and right columns
    for (let r = 0; r < 8; r++) {
      [files[0], files[7]].forEach(function (file) {
        const sq = boardEl.querySelector('[data-square="' + file + ranks[r] + '"]');
        if (!sq) return;
        const el = document.createElement('span');
        el.className = 'sq-xnote sq-xnote-rank';
        el.textContent = ranks[r];
        sq.appendChild(el);
      });
    }
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
      chip.addEventListener('click', function () { goToStep(idx, true); });
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

    const { from, to } = getMoveInfo(currentStepIndex);
    setTimeout(function () { applyHighlights2D(from, to); }, 80);
    if (board3d) board3d.highlight(from, to, highlightsOn);

    renderMoveList();
    renderExplanation();
    renderCounter();
  }

  // ---------- navigation ----------

  function goToStep(idx, withSound) {
    const steps = currentSteps();
    if (idx < 0)             idx = -1;
    if (idx >= steps.length) idx = steps.length - 1;
    currentStepIndex = idx;
    if (withSound && idx >= 0 && window.ChessSounds) {
      const { isCapture } = getMoveInfo(idx);
      ChessSounds.play(isCapture ? 'capture' : 'move');
    }
    renderAll();
  }

  function goToStart() { goToStep(-1); }
  function goToPrev()  { goToStep(currentStepIndex - 1); }
  function goToNext()  { goToStep(currentStepIndex + 1, true); }
  function goToEnd()   { goToStep(currentSteps().length - 1); }

  // ---------- flip ----------

  function flipBoard() {
    flipped = !flipped;
    initBoard(currentFen());
    if (board3d) board3d.flip(flipped);
    document.getElementById('btnFlip').textContent = flipped ? '⬆ White side' : '⬆ Black side';
    const { from, to } = getMoveInfo(currentStepIndex);
    setTimeout(function () { applyHighlights2D(from, to); }, 80);
    setTimeout(addExtraNotation, 50);
  }

  // ---------- highlights toggle ----------

  function toggleHighlights() {
    highlightsOn = !highlightsOn;
    const btn = document.getElementById('btnHighlight');
    btn.classList.toggle('active', highlightsOn);
    const { from, to } = getMoveInfo(currentStepIndex);
    applyHighlights2D(from, to);
    if (board3d) board3d.highlight(from, to, highlightsOn);
  }

  // ---------- sound toggle ----------

  function toggleSound() {
    if (!window.ChessSounds) return;
    const on = ChessSounds.toggle();
    const btn = document.getElementById('btnSound');
    btn.classList.toggle('active', on);
    btn.textContent = on ? '🔊 Sound' : '🔇 Sound';
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
    document.getElementById('btnSound').addEventListener('click', toggleSound);

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
    setTimeout(addExtraNotation, 50);
  }
})();
