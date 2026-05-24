"""
Chess openings data: moves, variations, and explanations for novice learners.
Each opening is a dict with metadata and a list of lines (main + variations).
Each line has a list of steps: {move, fen, explanation}.
"""

OPENINGS = {
    "colle-system": {
        "id": "colle-system",
        "name": "The Colle System",
        "emoji": "♙",
        "color": "White",
        "tagline": "A solid, reliable White system built around d4 + e3",
        "overview": "The Colle System is a quiet but deadly opening for White. White builds a rock-solid "
        "pawn centre with d4 and e3, develops the knight to f3, and often launches a powerful "
        "kingside attack once castled. It is perfect for beginners because the piece development "
        "follows a clear, repeatable recipe — you don't need to memorise long theory. Edgar "
        "Colle, a Belgian master of the 1920s, popularised this system, and it remains a "
        "favourite weapon at club level today.",
        "key_ideas": [
            "Control the centre with pawns on d4 and e3",
            "Develop the knight to f3 to attack the centre",
            "Castle kingside quickly for king safety",
            "Launch a kingside attack with moves like e4 at the right moment",
            "The bishop on d3 points dangerously at the kingside",
        ],
        "lines": [
            {
                "id": "main",
                "name": "Main Line",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1",
                        "explanation": "White opens with 1.d4 — claiming the centre. This is the "
                        "foundation of all d4 openings including the Colle.",
                    },
                    {
                        "move": "d5",
                        "san": "1... d5",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq d6 0 2",
                        "explanation": "Black mirrors White's idea — staking a claim in the centre "
                        "too. This is Black's most natural reply.",
                    },
                    {
                        "move": "e3",
                        "san": "2. e3",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 2",
                        "explanation": "The hallmark Colle move — both pawns come first. e3 solidifies "
                        "the centre and opens the diagonal for the dark-squared bishop.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4P3/PPP2PPP/RNBQKBNR w KQkq - 1 3",
                        "explanation": "Black develops naturally. The knight on f6 defends d5 and "
                        "controls the centre.",
                    },
                    {
                        "move": "Nf3",
                        "san": "3. Nf3",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 2 3",
                        "explanation": "Now the knight develops to f3, attacking d5 and preparing to castle. "
                        "With both pawns already in place, the Colle setup is underway.",
                    },
                    {
                        "move": "e6",
                        "san": "3... e6",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "Black solidifies the centre. e6 is very natural — it supports "
                        "d5 and prepares to develop the dark-squared bishop.",
                    },
                    {
                        "move": "Bd3",
                        "san": "4. Bd3",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "The bishop comes to its ideal square — d3. From here it eyes "
                        "the h7 pawn (a common target in kingside attacks) and supports "
                        "a future e4 advance.",
                    },
                    {
                        "move": "c5",
                        "san": "4... c5",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq c6 0 5",
                        "explanation": "Black challenges White's centre immediately with c5. This is a "
                        "very common and principled response.",
                    },
                    {
                        "move": "c3",
                        "san": "5. c3",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/2PBPN2/PP3PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "White reinforces d4 with c3 — keeping the pawn centre solid. "
                        "White is in no hurry to complicate things.",
                    },
                    {
                        "move": "Nc6",
                        "san": "5... Nc6",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P4/2PBPN2/PP3PPP/RNBQK2R w KQkq - 1 6",
                        "explanation": "Black develops the queen's knight. Both sides are building up "
                        "their forces logically.",
                    },
                    {
                        "move": "Nbd2",
                        "san": "6. Nbd2",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQK2R b KQkq - 2 6",
                        "explanation": "White develops the queen's knight to d2 rather than c3 (which "
                        "is blocked by the pawn). From d2 it can hop to f1 or e4 "
                        "later.",
                    },
                    {
                        "move": "Bd6",
                        "san": "6... Bd6",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQK2R w KQkq - 3 7",
                        "explanation": "Black mirrors White's setup — bishop to d6 is very natural "
                        "here.",
                    },
                    {
                        "move": "O-O",
                        "san": "7. O-O",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQ1RK1 b kq - 4 7",
                        "explanation": "Castle! The king is safe. White's plan is now to play e4 at "
                        "the right moment, opening lines toward Black's king. The Colle "
                        "attack is brewing.",
                    },
                ],
            },
            {
                "id": "colle-attack",
                "name": "The Colle Attack (e4 break)",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1",
                        "explanation": "White opens with d4, setting up the Colle System.",
                    },
                    {
                        "move": "d5",
                        "san": "1... d5",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq d6 0 2",
                        "explanation": "Black contests the centre.",
                    },
                    {
                        "move": "e3",
                        "san": "2. e3",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 2",
                        "explanation": "Both pawns first — the Colle approach. e3 solidifies the centre.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4P3/PPP2PPP/RNBQKBNR w KQkq - 1 3",
                        "explanation": "Black develops symmetrically.",
                    },
                    {
                        "move": "Nf3",
                        "san": "3. Nf3",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 2 3",
                        "explanation": "Now the knight — the Colle setup is taking shape.",
                    },
                    {
                        "move": "e6",
                        "san": "3... e6",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "Black supports d5.",
                    },
                    {
                        "move": "Bd3",
                        "san": "4. Bd3",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "Bishop to d3 — the ideal square, pointing at h7.",
                    },
                    {
                        "move": "Be7",
                        "san": "4... Be7",
                        "fen": "rnbqk2r/ppp1bppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq - 2 5",
                        "explanation": "Black prepares to castle.",
                    },
                    {
                        "move": "O-O",
                        "san": "5. O-O",
                        "fen": "rnbqk2r/ppp1bppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQ1RK1 b kq - 3 5",
                        "explanation": "White castles kingside. The Colle setup is nearly complete.",
                    },
                    {
                        "move": "O-O",
                        "san": "5... O-O",
                        "fen": "rnbq1rk1/ppp1bppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQ1RK1 w KQ - 4 6",
                        "explanation": "Both kings have castled. Now White unleashes the classic Colle "
                        "plan...",
                    },
                    {
                        "move": "Nbd2",
                        "san": "6. Nbd2",
                        "fen": "rnbq1rk1/ppp1bppp/4pn2/3p4/3P4/3BPN2/PPPN1PPP/R1BQ1RK1 b kq - 5 6",
                        "explanation": "The queen's knight joins the party. From d2 it can swing to "
                        "f1, then g3 or e5 — building up the kingside attack.",
                    },
                    {
                        "move": "c5",
                        "san": "6... c5",
                        "fen": "rnbq1rk1/pp2bppp/4pn2/2pp4/3P4/3BPN2/PPPN1PPP/R1BQ1RK1 w - - 0 7",
                        "explanation": "Black strikes in the centre — the natural counter.",
                    },
                    {
                        "move": "c3",
                        "san": "7. c3",
                        "fen": "rnbq1rk1/pp2bppp/4pn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQ1RK1 b - - 0 7",
                        "explanation": "A key preparatory move. c3 shores up d4 so that after e4, "
                        "if Black advances c4, the bishop can safely retreat to c2 "
                        "with no loss of tempo. Never play e4 without c3 first!",
                    },
                    {
                        "move": "Nc6",
                        "san": "7... Nc6",
                        "fen": "r1bq1rk1/pp2bppp/2n1pn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQ1RK1 w - - 1 8",
                        "explanation": "Black develops the queen's knight, reinforcing d5 and c5.",
                    },
                    {
                        "move": "e4",
                        "san": "8. e4",
                        "fen": "r1bq1rk1/pp2bppp/2n1pn2/2pp4/3PP3/2PB1N2/PP1N1PPP/R1BQ1RK1 b - - 0 8",
                        "explanation": "The Colle pawn break! With c3 already in place, e4 is safe. "
                        "The bishop on d3 now attacks h7 with lethal force. Black must be "
                        "very careful — this is where beginner opponents often get into "
                        "serious trouble.",
                    },
                ],
            },
            {
                "id": "colle-zukertort",
                "name": "Colle-Zukertort (b3 + Bb2)",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "White opens with d4 — the Colle-Zukertort starts just like the "
                        "normal Colle.",
                    },
                    {
                        "move": "Nf6",
                        "san": "1... Nf6",
                        "fen": "rnbqkb1r/pppppppp/5n2/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 1 2",
                        "explanation": "Black plays 1...Nf6 — flexible, keeping options open.",
                    },
                    {
                        "move": "e3",
                        "san": "2. e3",
                        "fen": "rnbqkb1r/pppppppp/5n2/8/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 2",
                        "explanation": "2.e3 — both pawns first, the Colle-Zukertort way.",
                    },
                    {
                        "move": "e6",
                        "san": "2... e6",
                        "fen": "rnbqkb1r/pppp1ppp/4pn2/8/3P4/4P3/PPP2PPP/RNBQKBNR w KQkq - 0 3",
                        "explanation": "2...e6 — Black prepares d5.",
                    },
                    {
                        "move": "Nf3",
                        "san": "3. Nf3",
                        "fen": "rnbqkb1r/pppp1ppp/4pn2/8/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 1 3",
                        "explanation": "3.Nf3 — the knight joins after the pawns are set.",
                    },
                    {
                        "move": "d5",
                        "san": "3... d5",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "3...d5 — Black claims the centre.",
                    },
                    {
                        "move": "Bd3",
                        "san": "4. Bd3",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "4.Bd3 — bishop to its ideal square.",
                    },
                    {
                        "move": "c5",
                        "san": "4... c5",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq - 0 5",
                        "explanation": "4...c5 — Black challenges White's pawn.",
                    },
                    {
                        "move": "b3",
                        "san": "5. b3",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/1P1BPN2/P1P2PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "5.b3! — The Zukertort move! Instead of c3, White prepares Bb2, "
                        "aiming the bishop powerfully at the kingside along the long "
                        "diagonal. This is what makes the Colle-Zukertort distinct from "
                        "the regular Colle.",
                    },
                    {
                        "move": "Nc6",
                        "san": "5... Nc6",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P4/1P1BPN2/P1P2PPP/RNBQK2R w KQkq - 1 6",
                        "explanation": "5...Nc6 — Black develops naturally.",
                    },
                    {
                        "move": "Bb2",
                        "san": "6. Bb2",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P4/1P1BPN2/PBP2PPP/RN1QK2R b KQkq - 2 6",
                        "explanation": "6.Bb2 — the bishop arrives on b2, pointed straight at g7. "
                        "Combined with the Bd3, White now has two bishops aimed at "
                        "Black's kingside.",
                    },
                    {
                        "move": "Bd6",
                        "san": "6... Bd6",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P4/1P1BPN2/PBP2PPP/RN1QK2R w KQkq - 3 7",
                        "explanation": "6...Bd6 — Black develops the bishop.",
                    },
                    {
                        "move": "Nbd2",
                        "san": "7. Nbd2",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P4/1P1BPN2/PBPN1PPP/R2QK2R b KQkq - 4 7",
                        "explanation": "7.Nbd2 — the queen's knight joins, ready to support an e4 "
                        "advance.",
                    },
                    {
                        "move": "O-O",
                        "san": "7... O-O",
                        "fen": "r1bq1rk1/pp3ppp/2nbpn2/2pp4/3P4/1P1BPN2/PBPN1PPP/R2QK2R w KQ - 5 8",
                        "explanation": "7...O-O — Black castles.",
                    },
                    {
                        "move": "O-O",
                        "san": "8. O-O",
                        "fen": "r1bq1rk1/pp3ppp/2nbpn2/2pp4/3P4/1P1BPN2/PBPN1PPP/R2Q1RK1 b - - 6 8",
                        "explanation": "8.O-O — White castles. The Colle-Zukertort battery (Bd3, Bb2, "
                        "Nbd2, Nf3) is fully primed for e4 and a devastating kingside "
                        "attack.",
                    },
                ],
            },
            {
                "id": "colle-kings-indian",
                "name": "Colle vs King's Indian",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "1.d4 — White opens.",
                    },
                    {
                        "move": "Nf6",
                        "san": "1... Nf6",
                        "fen": "rnbqkb1r/pppppppp/5n2/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 1 2",
                        "explanation": "1...Nf6 — Black plays the knight first, keeping options open.",
                    },
                    {
                        "move": "e3",
                        "san": "2. e3",
                        "fen": "rnbqkb1r/pppppppp/5n2/8/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 2",
                        "explanation": "2.e3 — both pawns first, the Colle way.",
                    },
                    {
                        "move": "g6",
                        "san": "2... g6",
                        "fen": "rnbqkb1r/pppppp1p/5np1/8/3P4/4P3/PPP2PPP/RNBQKBNR w KQkq - 0 3",
                        "explanation": "2...g6 — Black signals the King's Indian: fianchetto the "
                        "bishop on g7 and aim for ...e5.",
                    },
                    {
                        "move": "Nf3",
                        "san": "3. Nf3",
                        "fen": "rnbqkb1r/pppppp1p/5np1/8/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 1 3",
                        "explanation": "3.Nf3 — White sticks with the Colle System regardless of what "
                        "Black plays.",
                    },
                    {
                        "move": "Bg7",
                        "san": "3... Bg7",
                        "fen": "rnbqk2r/ppppppbp/5np1/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 1 4",
                        "explanation": "3...Bg7 — the King's Indian bishop, powerful on the long "
                        "diagonal.",
                    },
                    {
                        "move": "Bd3",
                        "san": "4. Bd3",
                        "fen": "rnbqk2r/ppppppbp/5np1/8/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq - 2 4",
                        "explanation": "4.Bd3 — White sets up the Colle battery.",
                    },
                    {
                        "move": "O-O",
                        "san": "4... O-O",
                        "fen": "rnbq1rk1/ppppppbp/5np1/8/3P4/3BPN2/PPP2PPP/RNBQK2R w KQ - 3 5",
                        "explanation": "4...O-O — Black castles, safe behind the fianchetto.",
                    },
                    {
                        "move": "O-O",
                        "san": "5. O-O",
                        "fen": "rnbq1rk1/ppppppbp/5np1/8/3P4/3BPN2/PPP2PPP/RNBQ1RK1 b - - 4 5",
                        "explanation": "5.O-O — White castles too.",
                    },
                    {
                        "move": "d6",
                        "san": "5... d6",
                        "fen": "rnbq1rk1/ppp1ppbp/3p1np1/8/3P4/3BPN2/PPP2PPP/RNBQ1RK1 w - - 0 6",
                        "explanation": "5...d6 — Black prepares the ...e5 central push.",
                    },
                    {
                        "move": "Nbd2",
                        "san": "6. Nbd2",
                        "fen": "rnbq1rk1/ppp1ppbp/3p1np1/8/3P4/3BPN2/PPPN1PPP/R1BQ1RK1 b - - 1 6",
                        "explanation": "6.Nbd2 — White completes development.",
                    },
                    {
                        "move": "Nbd7",
                        "san": "6... Nbd7",
                        "fen": "r1bq1rk1/pppnppbp/3p1np1/8/3P4/3BPN2/PPPN1PPP/R1BQ1RK1 w - - 2 7",
                        "explanation": "6...Nbd7 — Black develops, eyeing the e5 square.",
                    },
                    {
                        "move": "c3",
                        "san": "7. c3",
                        "fen": "r1bq1rk1/pppnppbp/3p1np1/8/3P4/2PBPN2/PP1N1PPP/R1BQ1RK1 b - - 0 7",
                        "explanation": "7.c3 — White solidifies the centre before pushing e4.",
                    },
                    {
                        "move": "e5",
                        "san": "7... e5",
                        "fen": "r1bq1rk1/pppn1pbp/3p1np1/4p3/3P4/2PBPN2/PP1N1PPP/R1BQ1RK1 w - - 0 8",
                        "explanation": "7...e5! — the King's Indian central break! Black fights for "
                        "the centre.",
                    },
                    {
                        "move": "e4",
                        "san": "8. e4",
                        "fen": "r1bq1rk1/pppn1pbp/3p1np1/4p3/3PP3/2PB1N2/PP1N1PPP/R1BQ1RK1 b - - 0 8",
                        "explanation": "8.e4! — White strikes back. Both sides have space and active "
                        "pieces. The Colle handles the King's Indian very well — White "
                        "has a familiar plan while Black must navigate the sharp "
                        "centre.",
                    },
                ],
            },
        ],
    },
    "london-system": {
        "id": "london-system",
        "name": "The London System",
        "emoji": "🏰",
        "color": "White",
        "tagline": "A beginner-friendly setup with Bf4 and a solid pawn chain",
        "overview": "The London System is one of the easiest ways to reach a playable position as White. "
        "White starts with d4, develops the bishop to f4 before locking it in, and builds a sturdy "
        "centre with e3 and c3. Because White's plan is more about setup than memorising theory, "
        "it is a popular choice for improving players. The London can also become aggressive when "
        "White strikes with e4 or attacks on the kingside.",
        "key_ideas": [
            "Play d4 and develop the bishop to f4 early",
            "Support the centre with e3 and c3",
            "Develop knights to f3 and d2, then castle",
            "Use the bishop on f4 to pressure e5 and support an e4 break",
            "Stay flexible: the same setup works against many Black defenses",
        ],
        "lines": [
            {
                "id": "main",
                "name": "Main Line (vs ...d5)",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "White claims space in the centre with 1.d4.",
                    },
                    {
                        "move": "d5",
                        "san": "1... d5",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2",
                        "explanation": "Black meets the challenge by taking space in the centre too.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "Develop and prepare to castle. The knight also eyes e5 and d4.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "Black develops and increases control of the centre.",
                    },
                    {
                        "move": "Bf4",
                        "san": "3. Bf4",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P1B2/5N2/PPP1PPPP/RN1QKB1R b KQkq - 3 3",
                        "explanation": "The London bishop. White develops it outside the pawn chain.",
                    },
                    {
                        "move": "e6",
                        "san": "3... e6",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P1B2/5N2/PPP1PPPP/RN1QKB1R w KQkq - 0 4",
                        "explanation": "A solid reply: Black supports d5 and prepares to develop smoothly.",
                    },
                    {
                        "move": "e3",
                        "san": "4. e3",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P1B2/4PN2/PPP2PPP/RN1QKB1R b KQkq - 0 4",
                        "explanation": "White builds a sturdy pawn chain and opens lines for development.",
                    },
                    {
                        "move": "c5",
                        "san": "4... c5",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P1B2/4PN2/PPP2PPP/RN1QKB1R w KQkq - 0 5",
                        "explanation": "Black challenges the centre from the side, a common plan against London setups.",
                    },
                    {
                        "move": "c3",
                        "san": "5. c3",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P1B2/2P1PN2/PP3PPP/RN1QKB1R b KQkq - 0 5",
                        "explanation": "Reinforce d4 and prepare a later e4 push.",
                    },
                    {
                        "move": "Nc6",
                        "san": "5... Nc6",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P1B2/2P1PN2/PP3PPP/RN1QKB1R w KQkq - 1 6",
                        "explanation": "Black develops and adds more pressure to the centre.",
                    },
                    {
                        "move": "Nbd2",
                        "san": "6. Nbd2",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P1B2/2P1PN2/PP1N1PPP/R2QKB1R b KQkq - 2 6",
                        "explanation": "The knight supports e4 and keeps the position flexible.",
                    },
                    {
                        "move": "Bd6",
                        "san": "6... Bd6",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P1B2/2P1PN2/PP1N1PPP/R2QKB1R w KQkq - 3 7",
                        "explanation": "Black challenges the bishop on f4 and develops with tempo.",
                    },
                    {
                        "move": "Bg3",
                        "san": "7. Bg3",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P4/2P1PNB1/PP1N1PPP/R2QKB1R b KQkq - 4 7",
                        "explanation": "Retreat and keep the bishop pair. White is ready to castle.",
                    },
                    {
                        "move": "O-O",
                        "san": "7... O-O",
                        "fen": "r1bq1rk1/pp3ppp/2nbpn2/2pp4/3P4/2P1PNB1/PP1N1PPP/R2QKB1R w KQ - 5 8",
                        "explanation": "Black castles and finishes development.",
                    },
                    {
                        "move": "Bd3",
                        "san": "8. Bd3",
                        "fen": "r1bq1rk1/pp3ppp/2nbpn2/2pp4/3P4/2PBPNB1/PP1N1PPP/R2QK2R b KQ - 6 8",
                        "explanation": "Develop and support an eventual e4 break in the centre.",
                    },
                    {
                        "move": "b6",
                        "san": "8... b6",
                        "fen": "r1bq1rk1/p4ppp/1pnbpn2/2pp4/3P4/2PBPNB1/PP1N1PPP/R2QK2R w KQ - 0 9",
                        "explanation": "Black prepares to develop the bishop to b7, pressuring the centre from afar.",
                    },
                ],
            },
            {
                "id": "vs-kings-indian",
                "name": "Vs King's Indian Setup (...g6)",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "White starts with d4, aiming for a solid setup.",
                    },
                    {
                        "move": "Nf6",
                        "san": "1... Nf6",
                        "fen": "rnbqkb1r/pppppppp/5n2/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 1 2",
                        "explanation": "Black develops and keeps options open.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkb1r/pppppppp/5n2/8/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq - 2 2",
                        "explanation": "Develop and prepare to castle.",
                    },
                    {
                        "move": "g6",
                        "san": "2... g6",
                        "fen": "rnbqkb1r/pppppp1p/5np1/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3",
                        "explanation": "Black heads for a King's Indian fianchetto.",
                    },
                    {
                        "move": "Bf4",
                        "san": "3. Bf4",
                        "fen": "rnbqkb1r/pppppp1p/5np1/8/3P1B2/5N2/PPP1PPPP/RN1QKB1R b KQkq - 1 3",
                        "explanation": "White sticks to London principles: develop the bishop early.",
                    },
                    {
                        "move": "Bg7",
                        "san": "3... Bg7",
                        "fen": "rnbqk2r/ppppppbp/5np1/8/3P1B2/5N2/PPP1PPPP/RN1QKB1R w KQkq - 2 4",
                        "explanation": "Black completes the fianchetto, putting pressure on the centre.",
                    },
                    {
                        "move": "e3",
                        "san": "4. e3",
                        "fen": "rnbqk2r/ppppppbp/5np1/8/3P1B2/4PN2/PPP2PPP/RN1QKB1R b KQkq - 0 4",
                        "explanation": "A calm move that supports d4 and opens lines for development.",
                    },
                    {
                        "move": "O-O",
                        "san": "4... O-O",
                        "fen": "rnbq1rk1/ppppppbp/5np1/8/3P1B2/4PN2/PPP2PPP/RN1QKB1R w KQ - 1 5",
                        "explanation": "Black castles, putting the king to safety.",
                    },
                    {
                        "move": "h3",
                        "san": "5. h3",
                        "fen": "rnbq1rk1/ppppppbp/5np1/8/3P1B2/4PN1P/PPP2PP1/RN1QKB1R b KQ - 0 5",
                        "explanation": "A useful waiting move: it stops ...Ng4 ideas and keeps White flexible.",
                    },
                    {
                        "move": "d6",
                        "san": "5... d6",
                        "fen": "rnbq1rk1/ppp1ppbp/3p1np1/8/3P1B2/4PN1P/PPP2PP1/RN1QKB1R w KQ - 0 6",
                        "explanation": "Black supports a future ...e5 central break.",
                    },
                    {
                        "move": "Be2",
                        "san": "6. Be2",
                        "fen": "rnbq1rk1/ppp1ppbp/3p1np1/8/3P1B2/4PN1P/PPP1BPP1/RN1QK2R b KQ - 1 6",
                        "explanation": "White prepares to castle and keeps the position solid.",
                    },
                    {
                        "move": "Nbd7",
                        "san": "6... Nbd7",
                        "fen": "r1bq1rk1/pppnppbp/3p1np1/8/3P1B2/4PN1P/PPP1BPP1/RN1QK2R w KQ - 2 7",
                        "explanation": "Black develops and supports the e5 push.",
                    },
                    {
                        "move": "O-O",
                        "san": "7. O-O",
                        "fen": "r1bq1rk1/pppnppbp/3p1np1/8/3P1B2/4PN1P/PPP1BPP1/RN1Q1RK1 b - - 3 7",
                        "explanation": "White castles too. The London aims for this safe, developed setup.",
                    },
                    {
                        "move": "e5",
                        "san": "7... e5",
                        "fen": "r1bq1rk1/pppn1pbp/3p1np1/4p3/3P1B2/4PN1P/PPP1BPP1/RN1Q1RK1 w - - 0 8",
                        "explanation": "Black grabs space in the centre. White can respond with calm development or a timely e4 break later.",
                    },
                ],
            },
        ],
    },
    "dutch-defense": {
        "id": "dutch-defense",
        "name": "The Dutch Defense",
        "emoji": "♟",
        "color": "Black",
        "tagline": "Black fights back aggressively against 1.d4",
        "overview": "The Dutch Defense is Black's fighting reply to 1.d4. Instead of matching White's "
        "central pawn with 1...d5, Black plays 1...f5 — an ambitious move that grabs space on "
        "the kingside and signals Black's intent to attack. The Dutch is famously aggressive "
        "and can lead to wildly unbalanced positions. World Champions Mikhail Botvinnik and "
        "Magnus Carlsen have used it. For beginners, it teaches the important concept of flank "
        "attacks and asymmetrical play.",
        "key_ideas": [
            "Black immediately stakes space on the kingside with ...f5",
            "Black aims to build a kingside attack while White typically plays on the queenside",
            "The e5 square becomes a powerful outpost for Black's pieces",
            "The Stonewall variation (pawns on d5, e6, f5, c6) creates a fortress",
            "Be careful — f5 slightly weakens the e5 and g5 squares for Black",
        ],
        "lines": [
            {
                "id": "classical",
                "name": "Classical Dutch",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1",
                        "explanation": "White plays 1.d4 — claiming central space.",
                    },
                    {
                        "move": "f5",
                        "san": "1... f5",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq f6 0 2",
                        "explanation": "1...f5! This is the Dutch Defense. Black immediately stakes "
                        "kingside space. It's bold and slightly risky — the e5 square "
                        "is weakened — but highly aggressive.",
                    },
                    {
                        "move": "c4",
                        "san": "2. c4",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2",
                        "explanation": "White expands on the queenside — the most ambitious response. "
                        "c4 is the mainline reply, fighting for the centre.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 1 3",
                        "explanation": "Black develops the knight to f6 — controlling e4 and d5. "
                        "Natural and flexible.",
                    },
                    {
                        "move": "Nc3",
                        "san": "3. Nc3",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 2 3",
                        "explanation": "White develops the queen's knight, putting more pressure on "
                        "the centre.",
                    },
                    {
                        "move": "e6",
                        "san": "3... e6",
                        "fen": "rnbqkb1r/pppp2pp/4pn2/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 0 4",
                        "explanation": "Black plays e6 — supporting f5, opening the diagonal for the "
                        "dark-squared bishop, and preparing d5. This is the Classical "
                        "Dutch setup.",
                    },
                    {
                        "move": "Nf3",
                        "san": "4. Nf3",
                        "fen": "rnbqkb1r/pppp2pp/4pn2/5p2/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 1 4",
                        "explanation": "White develops the king's knight to its natural square.",
                    },
                    {
                        "move": "Be7",
                        "san": "4... Be7",
                        "fen": "rnbqk2r/ppppb1pp/4pn2/5p2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5",
                        "explanation": "The bishop comes to e7 — a solid development, preparing to "
                        "castle. This is the hallmark of the Classical Dutch.",
                    },
                    {
                        "move": "g3",
                        "san": "5. g3",
                        "fen": "rnbqk2r/ppppb1pp/4pn2/5p2/2PP4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq - 0 5",
                        "explanation": "White prepares to fianchetto the bishop on g2 — a powerful "
                        "diagonal that will put pressure on Black's position for the "
                        "whole game.",
                    },
                    {
                        "move": "O-O",
                        "san": "5... O-O",
                        "fen": "rnbq1rk1/ppppb1pp/4pn2/5p2/2PP4/2N2NP1/PP2PP1P/R1BQKB1R w KQ - 1 6",
                        "explanation": "Black castles — king safety is always important! From here "
                        "Black will aim for ...d6 and eventually ...e5 to seize the "
                        "initiative.",
                    },
                ],
            },
            {
                "id": "stonewall",
                "name": "Stonewall Variation",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1",
                        "explanation": "White opens with d4.",
                    },
                    {
                        "move": "f5",
                        "san": "1... f5",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq f6 0 2",
                        "explanation": "The Dutch Defense again — 1...f5.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "A quieter approach — White develops the knight.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "Black develops naturally.",
                    },
                    {
                        "move": "g3",
                        "san": "3. g3",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/3P4/5NP1/PPP1PP1P/RNBQKB1R b KQkq - 0 3",
                        "explanation": "White goes for the fianchetto setup — a common way to fight "
                        "the Dutch.",
                    },
                    {
                        "move": "e6",
                        "san": "3... e6",
                        "fen": "rnbqkb1r/pppp2pp/4pn2/5p2/3P4/5NP1/PPP1PP1P/RNBQKB1R w KQkq - 0 4",
                        "explanation": "Black builds the Stonewall pawn chain. e6 prepares d5.",
                    },
                    {
                        "move": "Bg2",
                        "san": "4. Bg2",
                        "fen": "rnbqkb1r/pppp2pp/4pn2/5p2/3P4/5NP1/PPP1PPBP/RNBQK2R b KQkq - 1 4",
                        "explanation": "The bishop goes to g2 — the fianchetto is complete. It "
                        "controls a long diagonal.",
                    },
                    {
                        "move": "d5",
                        "san": "4... d5",
                        "fen": "rnbqkb1r/ppp3pp/4pn2/3p1p2/3P4/5NP1/PPP1PPBP/RNBQK2R w KQkq d6 0 5",
                        "explanation": "The Stonewall! Black has pawns on d5, e6, and f5 — a solid "
                        "pawn wall. This structure is very resilient and gives Black a "
                        "clear plan.",
                    },
                    {
                        "move": "O-O",
                        "san": "5. O-O",
                        "fen": "rnbqkb1r/ppp3pp/4pn2/3p1p2/3P4/5NP1/PPP1PPBP/RNBQ1RK1 b kq - 2 5",
                        "explanation": "White castles — both sides are safe. The game enters a "
                        "strategic battle: White's fianchetto bishop vs. Black's solid "
                        "Stonewall.",
                    },
                    {
                        "move": "Bd6",
                        "san": "5... Bd6",
                        "fen": "rnbqk2r/ppp3pp/3bpn2/3p1p2/3P4/5NP1/PPP1PPBP/RNBQ1RK1 w kq - 3 6",
                        "explanation": "Black develops the bishop to d6 — a wonderful square in the "
                        "Stonewall. From here it supports a potential kingside attack "
                        "and eyes h2. Black will castle next and then launch the "
                        "attack!",
                    },
                ],
            },
            {
                "id": "leningrad-dutch",
                "name": "Leningrad Variation",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "1.d4 — White opens.",
                    },
                    {
                        "move": "f5",
                        "san": "1... f5",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2",
                        "explanation": "1...f5 — the Dutch Defense.",
                    },
                    {
                        "move": "c4",
                        "san": "2. c4",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 2",
                        "explanation": "2.c4 — White expands on the queenside.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 1 3",
                        "explanation": "2...Nf6 — Black develops.",
                    },
                    {
                        "move": "Nc3",
                        "san": "3. Nc3",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 2 3",
                        "explanation": "3.Nc3 — White develops.",
                    },
                    {
                        "move": "g6",
                        "san": "3... g6",
                        "fen": "rnbqkb1r/ppppp2p/5np1/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 0 4",
                        "explanation": "3...g6! — The Leningrad Dutch! Black combines the Dutch (f5) "
                        "with King's Indian ideas (g6/Bg7). This is the most "
                        "aggressive and popular Dutch variation, used by World "
                        "Champions including Magnus Carlsen.",
                    },
                    {
                        "move": "Nf3",
                        "san": "4. Nf3",
                        "fen": "rnbqkb1r/ppppp2p/5np1/5p2/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 1 4",
                        "explanation": "4.Nf3 — White develops normally.",
                    },
                    {
                        "move": "Bg7",
                        "san": "4... Bg7",
                        "fen": "rnbqk2r/ppppp1bp/5np1/5p2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5",
                        "explanation": "4...Bg7 — the Leningrad bishop, incredibly powerful pointing "
                        "down the long diagonal.",
                    },
                    {
                        "move": "g3",
                        "san": "5. g3",
                        "fen": "rnbqk2r/ppppp1bp/5np1/5p2/2PP4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq - 0 5",
                        "explanation": "5.g3 — White answers with a fianchetto of their own.",
                    },
                    {
                        "move": "O-O",
                        "san": "5... O-O",
                        "fen": "rnbq1rk1/ppppp1bp/5np1/5p2/2PP4/2N2NP1/PP2PP1P/R1BQKB1R w KQ - 1 6",
                        "explanation": "5...O-O — Black castles.",
                    },
                    {
                        "move": "Bg2",
                        "san": "6. Bg2",
                        "fen": "rnbq1rk1/ppppp1bp/5np1/5p2/2PP4/2N2NP1/PP2PPBP/R1BQK2R b KQ - 2 6",
                        "explanation": "6.Bg2 — both fianchetto bishops face each other, creating a "
                        "fascinating diagonal battle.",
                    },
                    {
                        "move": "d6",
                        "san": "6... d6",
                        "fen": "rnbq1rk1/ppp1p1bp/3p1np1/5p2/2PP4/2N2NP1/PP2PPBP/R1BQK2R w KQ - 0 7",
                        "explanation": "6...d6 — Black solidifies the structure and prepares ...e5.",
                    },
                    {
                        "move": "O-O",
                        "san": "7. O-O",
                        "fen": "rnbq1rk1/ppp1p1bp/3p1np1/5p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 b - - 1 7",
                        "explanation": "7.O-O — White castles.",
                    },
                    {
                        "move": "c6",
                        "san": "7... c6",
                        "fen": "rnbq1rk1/pp2p1bp/2pp1np1/5p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - - 0 8",
                        "explanation": "7...c6 — Black prepares ...d5 or attacking ideas. The "
                        "Leningrad is rich, complex, and favoured by attacking players "
                        "at all levels.",
                    },
                ],
            },
            {
                "id": "staunton-gambit",
                "name": "Staunton Gambit (2.e4)",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "1.d4 — White opens.",
                    },
                    {
                        "move": "f5",
                        "san": "1... f5",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2",
                        "explanation": "1...f5 — the Dutch Defense.",
                    },
                    {
                        "move": "e4",
                        "san": "2. e4",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/3PP3/8/PPP2PPP/RNBQKBNR b KQkq - 0 2",
                        "explanation": "2.e4!? — The Staunton Gambit! White immediately sacrifices a "
                        "pawn to blow open the centre before Black can castle. Named "
                        "after Howard Staunton, one of the strongest players of the "
                        "19th century.",
                    },
                    {
                        "move": "fxe4",
                        "san": "2... fxe4",
                        "fen": "rnbqkbnr/ppppp1pp/8/8/3Pp3/8/PPP2PPP/RNBQKBNR w KQkq - 0 3",
                        "explanation": "2...fxe4 — Black accepts. Declining is too passive.",
                    },
                    {
                        "move": "Nc3",
                        "san": "3. Nc3",
                        "fen": "rnbqkbnr/ppppp1pp/8/8/3Pp3/2N5/PPP2PPP/R1BQKBNR b KQkq - 1 3",
                        "explanation": "3.Nc3 — White develops with tempo, attacking the e4 pawn "
                        "immediately.",
                    },
                    {
                        "move": "Nf6",
                        "san": "3... Nf6",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/8/3Pp3/2N5/PPP2PPP/R1BQKBNR w KQkq - 2 4",
                        "explanation": "3...Nf6 — Black defends and develops.",
                    },
                    {
                        "move": "Bg5",
                        "san": "4. Bg5",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/6B1/3Pp3/2N5/PPP2PPP/R2QKBNR b KQkq - 3 4",
                        "explanation": "4.Bg5! — pinning the knight on f6 and increasing pressure on "
                        "e4. White's development advantage is growing rapidly.",
                    },
                    {
                        "move": "Nc6",
                        "san": "4... Nc6",
                        "fen": "r1bqkb1r/ppppp1pp/2n2n2/6B1/3Pp3/2N5/PPP2PPP/R2QKBNR w KQkq - 4 5",
                        "explanation": "4...Nc6 — Black defends e4 again with a piece.",
                    },
                    {
                        "move": "d5",
                        "san": "5. d5",
                        "fen": "r1bqkb1r/ppppp1pp/2n2n2/3P2B1/4p3/2N5/PPP2PPP/R2QKBNR b KQkq - 0 5",
                        "explanation": "5.d5! — White advances, attacking the knight on c6 and trying "
                        "to open more lines.",
                    },
                    {
                        "move": "Ne5",
                        "san": "5... Ne5",
                        "fen": "r1bqkb1r/ppppp1pp/5n2/3Pn1B1/4p3/2N5/PPP2PPP/R2QKBNR w KQkq - 1 6",
                        "explanation": "5...Ne5 — the knight retreats to a strong central square.",
                    },
                    {
                        "move": "Qd4",
                        "san": "6. Qd4",
                        "fen": "r1bqkb1r/ppppp1pp/5n2/3Pn1B1/3Qp3/2N5/PPP2PPP/R3KBNR b KQkq - 2 6",
                        "explanation": "6.Qd4 — White attacks both e4 and e5 at once. The Staunton "
                        "Gambit gives White enormous piece activity. A great opening "
                        "for learning how development advantage compensates for "
                        "material.",
                    },
                ],
            },
            {
                "id": "anti-dutch-bg5",
                "name": "Hopton Attack (2.Bg5)",
                "steps": [
                    {
                        "move": "d4",
                        "san": "1. d4",
                        "fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "1.d4 — White opens.",
                    },
                    {
                        "move": "f5",
                        "san": "1... f5",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2",
                        "explanation": "1...f5 — the Dutch Defense.",
                    },
                    {
                        "move": "Bg5",
                        "san": "2. Bg5",
                        "fen": "rnbqkbnr/ppppp1pp/8/5pB1/3P4/8/PPP1PPPP/RN1QKBNR b KQkq - 1 2",
                        "explanation": "2.Bg5! — The Hopton Attack (Anti-Dutch). White sidesteps all "
                        "Dutch theory with an immediate bishop development. Black must "
                        "react carefully.",
                    },
                    {
                        "move": "h6",
                        "san": "2... h6",
                        "fen": "rnbqkbnr/ppppp1p1/7p/5pB1/3P4/8/PPP1PPPP/RN1QKBNR w KQkq - 0 3",
                        "explanation": "2...h6 — Black chases the bishop. The most natural response.",
                    },
                    {
                        "move": "Bh4",
                        "san": "3. Bh4",
                        "fen": "rnbqkbnr/ppppp1p1/7p/5p2/3P3B/8/PPP1PPPP/RN1QKBNR b KQkq - 1 3",
                        "explanation": "3.Bh4 — the bishop retreats but stays active, eyeing g5.",
                    },
                    {
                        "move": "g5",
                        "san": "3... g5",
                        "fen": "rnbqkbnr/ppppp3/7p/5pp1/3P3B/8/PPP1PPPP/RN1QKBNR w KQkq - 0 4",
                        "explanation": "3...g5!? — Black chases the bishop again with a pawn, but "
                        "this seriously weakens the kingside.",
                    },
                    {
                        "move": "Bg3",
                        "san": "4. Bg3",
                        "fen": "rnbqkbnr/ppppp3/7p/5pp1/3P4/6B1/PPP1PPPP/RN1QKBNR b KQkq - 1 4",
                        "explanation": "4.Bg3 — the bishop steps back calmly.",
                    },
                    {
                        "move": "f4",
                        "san": "4... f4",
                        "fen": "rnbqkbnr/ppppp3/7p/6p1/3P1p2/6B1/PPP1PPPP/RN1QKBNR w KQkq - 0 5",
                        "explanation": "4...f4 — Black pushes the bishop away once more! But Black's "
                        "kingside is now riddled with holes.",
                    },
                    {
                        "move": "e3",
                        "san": "5. e3",
                        "fen": "rnbqkbnr/ppppp3/7p/6p1/3P1p2/4P1B1/PPP2PPP/RN1QKBNR b KQkq - 0 5",
                        "explanation": "5.e3 — White strikes at Black's overextended pawns.",
                    },
                    {
                        "move": "fxg3",
                        "san": "5... fxg3",
                        "fen": "rnbqkbnr/ppppp3/7p/6p1/3P4/4P1p1/PPP2PPP/RN1QKBNR w KQkq - 0 6",
                        "explanation": "5...fxg3 — forced.",
                    },
                    {
                        "move": "hxg3",
                        "san": "6. hxg3",
                        "fen": "rnbqkbnr/ppppp3/7p/6p1/3P4/4P1P1/PPP2PP1/RN1QKBNR b KQkq - 0 6",
                        "explanation": "6.hxg3 — White recaptures, opening the h-file. Black has "
                        "gained space but White has a permanent target on the "
                        "kingside. A fascinating positional battle that teaches about "
                        "pawn weaknesses!",
                    },
                ],
            },
        ],
    },
    "rousseau-gambit": {
        "id": "rousseau-gambit",
        "name": "The Rousseau Gambit",
        "emoji": "⚔",
        "color": "Black",
        "tagline": "A sharp, aggressive counter-gambit in the Italian Game",
        "overview": "The Rousseau Gambit (also called the Ponziani-Steinitz Gambit) is a wild and "
        "aggressive counter-attack by Black. After 1.e4 e5 2.Nf3 Nc6, when White plays 3.Bc4 "
        "(Italian Game), Black responds with the shocking 3...f5!? — offering a pawn to seize "
        "the initiative. The idea is to unbalance the game immediately and create attacking "
        "chances. It is risky but great fun, and the tactics can confuse unprepared opponents "
        "quickly.",
        "key_ideas": [
            "Black sacrifices pawn stability for immediate activity with ...f5",
            "If White captures with exf5, Black opens the e-file for an attack",
            "The e5 pawn becomes a battering ram in the centre",
            "White needs precise play to defuse the gambit — many beginners fail",
            "Black aims to develop rapidly and attack before White consolidates",
        ],
        "lines": [
            {
                "id": "main",
                "name": "Main Line (White declines)",
                "steps": [
                    {
                        "move": "e4",
                        "san": "1. e4",
                        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
                        "explanation": "White opens with 1.e4 — the most popular first move, "
                        "staking central ground immediately.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 2",
                        "explanation": "Black replies symmetrically with 1...e5 — meeting fire with "
                        "fire.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "White develops the knight and attacks e5 immediately. A key "
                        "principle: attack in the opening!",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "Black defends e5 with the knight — also a key principle: "
                        "develop while defending.",
                    },
                    {
                        "move": "Bc4",
                        "san": "3. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3",
                        "explanation": "3.Bc4 — the Italian Game! The bishop goes to c4, pointing "
                        "at f7 — Black's weakest point. This is one of the oldest "
                        "openings in chess.",
                    },
                    {
                        "move": "f5",
                        "san": "3... f5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq f6 0 4",
                        "explanation": "3...f5!? — The Rousseau Gambit! Black immediately "
                        "counter-attacks with f5, threatening to take on e4. This is "
                        "Black's fighting spirit — instead of passive defence, Black "
                        "attacks!",
                    },
                    {
                        "move": "d3",
                        "san": "4. d3",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/3P1N2/PPP2PPP/RNBQK2R b KQkq - 0 4",
                        "explanation": "White declines to capture and plays d3 — a solid response. "
                        "White supports e4 and prepares to develop the remaining "
                        "pieces. This is actually the safest approach.",
                    },
                    {
                        "move": "Nf6",
                        "san": "4... Nf6",
                        "fen": "r1bqkb1r/pppp2pp/2n2n2/4pp2/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 1 "
                        "5",
                        "explanation": "Black develops the knight to f6 — adding pressure to e4 and "
                        "developing rapidly.",
                    },
                    {
                        "move": "Nc3",
                        "san": "5. Nc3",
                        "fen": "r1bqkb1r/pppp2pp/2n2n2/4pp2/2B1P3/2NP1N2/PPP2PPP/R1BQK2R b KQkq - 2 "
                        "5",
                        "explanation": "White develops the queen's knight — putting more defenders "
                        "around the centre.",
                    },
                    {
                        "move": "fxe4",
                        "san": "5... fxe4",
                        "fen": "r1bqkb1r/pppp2pp/2n2n2/4p3/2B1p3/2NP1N2/PPP2PPP/R1BQK2R w KQkq - 0 "
                        "6",
                        "explanation": "Black captures on e4! Now White must deal with the threat. "
                        "The position is sharp and double-edged — exactly what Black "
                        "was hoping for with the Rousseau Gambit.",
                    },
                ],
            },
            {
                "id": "accepted",
                "name": "Gambit Accepted (White takes f5)",
                "steps": [
                    {
                        "move": "e4",
                        "san": "1. e4",
                        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
                        "explanation": "1.e4 — White opens the game.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 2",
                        "explanation": "1...e5 — Black mirrors.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "2.Nf3 — attacking e5.",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "2...Nc6 — defending e5.",
                    },
                    {
                        "move": "Bc4",
                        "san": "3. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3",
                        "explanation": "3.Bc4 — the Italian Game.",
                    },
                    {
                        "move": "f5",
                        "san": "3... f5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq f6 0 4",
                        "explanation": "3...f5!? — The Rousseau Gambit! Black offers the f5 pawn or "
                        "forces the e4 pawn to advance.",
                    },
                    {
                        "move": "exf5",
                        "san": "4. exf5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pP2/2B5/5N2/PPPP1PPP/RNBQK2R b KQkq - 0 4",
                        "explanation": "White accepts the gambit! Taking on f5 looks natural — "
                        "White is up a pawn. But now Black opens the e-file with a "
                        "powerful response...",
                    },
                    {
                        "move": "e4",
                        "san": "4... e4",
                        "fen": "r1bqkbnr/pppp2pp/2n5/5P2/2B1p3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 5",
                        "explanation": "4...e4! Black advances the e-pawn, attacking the knight on "
                        "f3. White's knight must move — and meanwhile Black is "
                        "gaining time and opening lines.",
                    },
                    {
                        "move": "Ne5",
                        "san": "5. Ne5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4NP2/2B1p3/8/PPPP1PPP/RNBQK2R b KQkq - 1 5",
                        "explanation": "The knight jumps to e5, attacking the knight on c6 and "
                        "keeping some stability. White hopes the extra pawn on f5 "
                        "will count in the long run.",
                    },
                    {
                        "move": "Qh4",
                        "san": "5... Qh4",
                        "fen": "r1b1kbnr/pppp2pp/2n5/4NP2/2B1p2q/8/PPPP1PPP/RNBQK2R w KQkq - 2 6",
                        "explanation": "5...Qh4! A devastating attack! The queen comes to h4 with "
                        "check threats and enormous pressure. White's king is in "
                        "real danger. Black has full compensation for the pawn — "
                        "this is why the Rousseau Gambit is so dangerous!",
                    },
                ],
            },
            {
                "id": "rousseau-nc3",
                "name": "4.Nc3 — Critical Refutation",
                "steps": [
                    {
                        "move": "e4",
                        "san": "1. e4",
                        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "1.e4 — White opens.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
                        "explanation": "1...e5 — Black mirrors.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "2.Nf3 — White attacks e5.",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "2...Nc6 — Black defends.",
                    },
                    {
                        "move": "Bc4",
                        "san": "3. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3",
                        "explanation": "3.Bc4 — the Italian Game.",
                    },
                    {
                        "move": "f5",
                        "san": "3... f5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4",
                        "explanation": "3...f5 — the Rousseau Gambit!",
                    },
                    {
                        "move": "Nc3",
                        "san": "4. Nc3",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq - 1 4",
                        "explanation": "4.Nc3! — The critical refutation. Instead of the quiet d3, "
                        "White develops with tempo and immediately challenges the "
                        "centre. Most strong players consider this White's best "
                        "response to the Rousseau Gambit.",
                    },
                    {
                        "move": "fxe4",
                        "san": "4... fxe4",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4p3/2B1p3/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 0 5",
                        "explanation": "4...fxe4 — Black captures, opening lines.",
                    },
                    {
                        "move": "Nxe4",
                        "san": "5. Nxe4",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4p3/2B1N3/5N2/PPPP1PPP/R1BQK2R b KQkq - 0 5",
                        "explanation": "5.Nxe4 — White recaptures with the knight, placing it "
                        "centrally.",
                    },
                    {
                        "move": "d5",
                        "san": "5... d5",
                        "fen": "r1bqkbnr/ppp3pp/2n5/3pp3/2B1N3/5N2/PPPP1PPP/R1BQK2R w KQkq - 0 6",
                        "explanation": "5...d5! — the only good response — Black must "
                        "counter-attack in the centre immediately or fall behind in "
                        "development.",
                    },
                    {
                        "move": "Bxd5",
                        "san": "6. Bxd5",
                        "fen": "r1bqkbnr/ppp3pp/2n5/3Bp3/4N3/5N2/PPPP1PPP/R1BQK2R b KQkq - 0 6",
                        "explanation": "6.Bxd5 — White takes the d5 pawn.",
                    },
                    {
                        "move": "Qxd5",
                        "san": "6... Qxd5",
                        "fen": "r1b1kbnr/ppp3pp/2n5/3qp3/4N3/5N2/PPPP1PPP/R1BQK2R w KQkq - 0 7",
                        "explanation": "6...Qxd5 — Black recaptures with the queen, centralising "
                        "it.",
                    },
                    {
                        "move": "Nc3",
                        "san": "7. Nc3",
                        "fen": "r1b1kbnr/ppp3pp/2n5/3qp3/8/2N2N2/PPPP1PPP/R1BQK2R b KQkq - 1 7",
                        "explanation": "7.Nc3 — White attacks the queen, gaining a tempo.",
                    },
                    {
                        "move": "Qd8",
                        "san": "7... Qd8",
                        "fen": "r1bqkbnr/ppp3pp/2n5/4p3/8/2N2N2/PPPP1PPP/R1BQK2R w KQkq - 2 8",
                        "explanation": "7...Qd8 — the queen retreats. White has clear piece "
                        "activity and easy development. This is why 4.Nc3 is "
                        "considered the toughest test of the Rousseau Gambit.",
                    },
                ],
            },
        ],
    },
    "scotch-gambit": {
        "id": "scotch-gambit",
        "name": "The Scotch Gambit",
        "emoji": "♞",
        "color": "White",
        "tagline": "White sacrifices a pawn for rapid development and attack",
        "overview": "The Scotch Gambit is an exciting, swashbuckling opening where White sacrifices a pawn "
        "to gain rapid development and attacking chances. After 1.e4 e5 2.Nf3 Nc6 3.d4, White "
        "opens the centre. After Black captures 3...exd4, instead of recapturing with the "
        "knight (Scotch Game), White plays 4.Bc4 — the Scotch Gambit! White offers the d4 pawn "
        "in exchange for a huge lead in development. This opening teaches the fundamental chess "
        "principle: time and activity are worth material.",
        "key_ideas": [
            "White gives up the d4 pawn to gain several tempi (moves) of development",
            "Rapid development and king safety are the rewards for the gambit",
            "The open centre benefits White's better-developed pieces",
            "Attacking f7 (Black's weakest square) is a common tactical theme",
            "The Dubois-Réti Defense and Max Lange Attack are key variations",
        ],
        "lines": [
            {
                "id": "main",
                "name": "Main Line",
                "steps": [
                    {
                        "move": "e4",
                        "san": "1. e4",
                        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
                        "explanation": "1.e4 — White takes the centre with the king's pawn.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 2",
                        "explanation": "1...e5 — Black answers with symmetry.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "2.Nf3 — White attacks e5.",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "2...Nc6 — Black defends naturally.",
                    },
                    {
                        "move": "d4",
                        "san": "3. d4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3",
                        "explanation": "3.d4! White strikes in the centre immediately — this is the "
                        "key idea that distinguishes the Scotch Gambit from the "
                        "Italian Game. White challenges Black to take the pawn.",
                    },
                    {
                        "move": "exd4",
                        "san": "3... exd4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "3...exd4 — Black accepts, capturing the d4 pawn. This opens "
                        "the centre and is practically forced — declining is passive.",
                    },
                    {
                        "move": "Bc4",
                        "san": "4. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "4.Bc4! — The Scotch Gambit! Instead of winning back the pawn "
                        "immediately, White develops the bishop to c4. This attacks f7 "
                        "and develops rapidly. White is a pawn down but already has "
                        "active pieces.",
                    },
                    {
                        "move": "Bc5",
                        "san": "4... Bc5",
                        "fen": "r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5",
                        "explanation": "4...Bc5 — Black develops the bishop, holding onto the extra "
                        "pawn. Now comes the key Scotch Gambit move...",
                    },
                    {
                        "move": "c3",
                        "san": "5. c3",
                        "fen": "r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/2P2N2/PP3PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "5.c3! White attacks the d4 pawn immediately, trying to "
                        "recapture the centre. This forces Black to make a decision.",
                    },
                    {
                        "move": "Nf6",
                        "san": "5... Nf6",
                        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b5/2BpP3/2P2N2/PP3PPP/RNBQK2R w KQkq - 1 6",
                        "explanation": "5...Nf6 — Black develops the knight and attacks e4. Black is "
                        "trying to hold the extra pawn while also developing.",
                    },
                    {
                        "move": "e5",
                        "san": "6. e5",
                        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1P3/2Bp4/2P2N2/PP3PPP/RNBQK2R b KQkq - 0 6",
                        "explanation": "6.e5! White pushes the pawn forward, attacking the f6 knight. "
                        "This is an energetic move — White is playing dynamically "
                        "rather than trying to regain the pawn immediately.",
                    },
                    {
                        "move": "d5",
                        "san": "6... d5",
                        "fen": "r1bqk2r/ppp2ppp/2n2n2/2bpP3/2Bp4/2P2N2/PP3PPP/RNBQK2R w KQkq d6 0 7",
                        "explanation": "6...d5! Black counter-attacks in the centre. This is the "
                        "recommended defence — Black gives back material to free the "
                        "position.",
                    },
                    {
                        "move": "Bb5",
                        "san": "7. Bb5",
                        "fen": "r1bqk2r/ppp2ppp/2n2n2/1B1pP3/3p4/2P2N2/PP3PPP/RNBQK2R b KQkq - 1 7",
                        "explanation": "7.Bb5 — the bishop pins the knight on c6, which was defending "
                        "d5. White is building up pressure systematically. This is the "
                        "Max Lange Attack territory — one of the most analyzed gambits "
                        "in chess history!",
                    },
                ],
            },
            {
                "id": "dubois-reti",
                "name": "Dubois-Réti Defense",
                "steps": [
                    {
                        "move": "e4",
                        "san": "1. e4",
                        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
                        "explanation": "1.e4 — opening the game.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 2",
                        "explanation": "1...e5 — symmetrical.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "2.Nf3",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "2...Nc6",
                    },
                    {
                        "move": "d4",
                        "san": "3. d4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3",
                        "explanation": "3.d4 — the Scotch Gambit begins.",
                    },
                    {
                        "move": "exd4",
                        "san": "3... exd4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "3...exd4 — capturing the pawn.",
                    },
                    {
                        "move": "Bc4",
                        "san": "4. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "4.Bc4 — the Scotch Gambit move.",
                    },
                    {
                        "move": "Nf6",
                        "san": "4... Nf6",
                        "fen": "r1bqkb1r/pppp1ppp/2n2n2/8/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5",
                        "explanation": "4...Nf6! — The Dubois-Réti Defense! Instead of Bc5, Black "
                        "immediately attacks e4 with the knight. This is a fighting "
                        "response.",
                    },
                    {
                        "move": "e5",
                        "san": "5. e5",
                        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4P3/2Bp4/5N2/PPP2PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "5.e5 — White attacks the knight, pushing forward "
                        "aggressively.",
                    },
                    {
                        "move": "d5",
                        "san": "5... d5",
                        "fen": "r1bqkb1r/ppp2ppp/2n2n2/3pP3/2Bp4/5N2/PPP2PPP/RNBQK2R w KQkq d6 0 6",
                        "explanation": "5...d5! Black hits back in the centre — attacking both the e5 "
                        "pawn and the c4 bishop. The game becomes very sharp and "
                        "tactical.",
                    },
                    {
                        "move": "Bb5",
                        "san": "6. Bb5",
                        "fen": "r1bqkb1r/ppp2ppp/2n2n2/1B1pP3/3p4/5N2/PPP2PPP/RNBQK2R b KQkq - 1 6",
                        "explanation": "6.Bb5 — pinning the knight on c6. White maintains pressure "
                        "and the position crackles with tactics. Both players need to "
                        "play very accurately here. This is excellent training for "
                        "tactical vision!",
                    },
                ],
            },
            {
                "id": "max-lange",
                "name": "Max Lange Attack",
                "steps": [
                    {
                        "move": "e4",
                        "san": "1. e4",
                        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "1.e4 — White opens.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
                        "explanation": "1...e5 — symmetrical.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "2.Nf3 — attacking e5.",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "2...Nc6 — defending.",
                    },
                    {
                        "move": "d4",
                        "san": "3. d4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq - 0 3",
                        "explanation": "3.d4 — the Scotch Gambit.",
                    },
                    {
                        "move": "exd4",
                        "san": "3... exd4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "3...exd4 — capturing.",
                    },
                    {
                        "move": "Bc4",
                        "san": "4. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "4.Bc4 — Scotch Gambit.",
                    },
                    {
                        "move": "Bc5",
                        "san": "4... Bc5",
                        "fen": "r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5",
                        "explanation": "4...Bc5 — Black develops the bishop.",
                    },
                    {
                        "move": "O-O",
                        "san": "5. O-O",
                        "fen": "r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQ1RK1 b kq - 3 5",
                        "explanation": "5.O-O — White castles rather than playing c3, prioritising "
                        "rapid development. This is the path to the Max Lange Attack.",
                    },
                    {
                        "move": "Nf6",
                        "san": "5... Nf6",
                        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b5/2BpP3/5N2/PPP2PPP/RNBQ1RK1 w kq - 4 6",
                        "explanation": "5...Nf6 — Black develops the knight and attacks e4.",
                    },
                    {
                        "move": "e5",
                        "san": "6. e5",
                        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1P3/2Bp4/5N2/PPP2PPP/RNBQ1RK1 b kq - 0 6",
                        "explanation": "6.e5! — White attacks the f6 knight. This is the Max Lange "
                        "Attack! One of the most deeply analysed gambits in chess "
                        "history, beloved by attacking players since the 1850s.",
                    },
                    {
                        "move": "d5",
                        "san": "6... d5",
                        "fen": "r1bqk2r/ppp2ppp/2n2n2/2bpP3/2Bp4/5N2/PPP2PPP/RNBQ1RK1 w kq d6 0 7",
                        "explanation": "6...d5 — Black must counter-attack.",
                    },
                    {
                        "move": "exf6",
                        "san": "7. exf6",
                        "fen": "r1bqk2r/ppp2ppp/2n2P2/2bp4/2Bp4/5N2/PPP2PPP/RNBQ1RK1 b kq - 0 7",
                        "explanation": "7.exf6 — White captures the knight, giving Black a damaged "
                        "pawn structure but opening the position dramatically.",
                    },
                    {
                        "move": "dxc4",
                        "san": "7... dxc4",
                        "fen": "r1bqk2r/ppp2ppp/2n2P2/2b5/2pp4/5N2/PPP2PPP/RNBQ1RK1 w kq - 0 8",
                        "explanation": "7...dxc4 — Black takes the bishop.",
                    },
                    {
                        "move": "Re1+",
                        "san": "8. Re1+",
                        "fen": "r1bqk2r/ppp2ppp/2n2P2/2b5/2pp4/5N2/PPP2PPP/RNBQR1K1 b kq - 1 8",
                        "explanation": "8.Re1+ — check! The rook enters the game with decisive force. "
                        "Black's king is in serious danger. White has a ferocious "
                        "attack for the sacrificed material. This is chess at its most "
                        "exciting!",
                    },
                ],
            },
            {
                "id": "scotch-declined-d5",
                "name": "4...d5 — Declining the Gambit",
                "steps": [
                    {
                        "move": "e4",
                        "san": "1. e4",
                        "fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",
                        "explanation": "1.e4 — White opens.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
                        "explanation": "1...e5 — symmetrical.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "2.Nf3 — attacking e5.",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "2...Nc6 — defending.",
                    },
                    {
                        "move": "d4",
                        "san": "3. d4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq - 0 3",
                        "explanation": "3.d4 — the Scotch Gambit.",
                    },
                    {
                        "move": "exd4",
                        "san": "3... exd4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "3...exd4 — capturing.",
                    },
                    {
                        "move": "Bc4",
                        "san": "4. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "4.Bc4 — Scotch Gambit.",
                    },
                    {
                        "move": "d5",
                        "san": "4... d5",
                        "fen": "r1bqkbnr/ppp2ppp/2n5/3p4/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 0 5",
                        "explanation": "4...d5!? — Declining! Black immediately strikes back in the "
                        "centre, offering to return the pawn for rapid development and "
                        "a solid position. A principled choice.",
                    },
                    {
                        "move": "exd5",
                        "san": "5. exd5",
                        "fen": "r1bqkbnr/ppp2ppp/2n5/3P4/2Bp4/5N2/PPP2PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "5.exd5 — White captures.",
                    },
                    {
                        "move": "Qxd5",
                        "san": "5... Qxd5",
                        "fen": "r1b1kbnr/ppp2ppp/2n5/3q4/2Bp4/5N2/PPP2PPP/RNBQK2R w KQkq - 0 6",
                        "explanation": "5...Qxd5 — Black recaptures with the queen, centralising it "
                        "and keeping the extra d4 pawn.",
                    },
                    {
                        "move": "O-O",
                        "san": "6. O-O",
                        "fen": "r1b1kbnr/ppp2ppp/2n5/3q4/2Bp4/5N2/PPP2PPP/RNBQ1RK1 b kq - 1 6",
                        "explanation": "6.O-O — White castles, trusting that rapid development is "
                        "worth more than the pawn.",
                    },
                    {
                        "move": "Be6",
                        "san": "6... Be6",
                        "fen": "r3kbnr/ppp2ppp/2n1b3/3q4/2Bp4/5N2/PPP2PPP/RNBQ1RK1 w kq - 2 7",
                        "explanation": "6...Be6 — Black develops the bishop and challenges White's "
                        "bishop on c4.",
                    },
                    {
                        "move": "Re1",
                        "san": "7. Re1",
                        "fen": "r3kbnr/ppp2ppp/2n1b3/3q4/2Bp4/5N2/PPP2PPP/RNBQR1K1 b kq - 3 7",
                        "explanation": "7.Re1 — White puts the rook on the open e-file with "
                        "initiative.",
                    },
                    {
                        "move": "Qd7",
                        "san": "7... Qd7",
                        "fen": "r3kbnr/pppq1ppp/2n1b3/8/2Bp4/5N2/PPP2PPP/RNBQR1K1 w kq - 4 8",
                        "explanation": "7...Qd7 — Black steps the queen aside. The d4 pawn gives "
                        "Black a small advantage in material, but White has full "
                        "compensation through development. A rich, balanced "
                        "middlegame.",
                    },
                ],
            },
        ],
    },
}
