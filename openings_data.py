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
        "tagline": "A solid, reliable opening for White built around d4",
        "overview": (
            "The Colle System is a quiet but deadly opening for White. "
            "White builds a rock-solid pawn centre with d4 and e3, develops the "
            "knight to f3, and often launches a powerful kingside attack once "
            "castled. It is perfect for beginners because the piece development "
            "follows a clear, repeatable recipe — you don't need to memorise long "
            "theory. Edgar Colle, a Belgian master of the 1920s, popularised this "
            "system, and it remains a favourite weapon at club level today."
        ),
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
                        "explanation": "White opens with 1.d4 — claiming the centre. This is the foundation of all d4 openings including the Colle.",
                    },
                    {
                        "move": "d5",
                        "san": "1... d5",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq d6 0 2",
                        "explanation": "Black mirrors White's idea — staking a claim in the centre too. This is Black's most natural reply.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "The knight comes to f3 — developing a piece, attacking the d5 pawn, and preparing to castle. This is a key Colle move.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "Black develops naturally. The knight on f6 defends d5 and controls the centre.",
                    },
                    {
                        "move": "e3",
                        "san": "3. e3",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 0 3",
                        "explanation": "This quiet pawn move is the hallmark of the Colle System. It supports d4, opens the diagonal for the bishop on f1, and keeps the position solid.",
                    },
                    {
                        "move": "e6",
                        "san": "3... e6",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "Black solidifies the centre. e6 is very natural — it supports d5 and prepares to develop the dark-squared bishop.",
                    },
                    {
                        "move": "Bd3",
                        "san": "4. Bd3",
                        "fen": "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "The bishop comes to its ideal square — d3. From here it eyes the h7 pawn (a common target in kingside attacks) and supports a future e4 advance.",
                    },
                    {
                        "move": "c5",
                        "san": "4... c5",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq c6 0 5",
                        "explanation": "Black challenges White's centre immediately with c5. This is a very common and principled response.",
                    },
                    {
                        "move": "c3",
                        "san": "5. c3",
                        "fen": "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/2PBPN2/PP3PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "White reinforces d4 with c3 — keeping the pawn centre solid. White is in no hurry to complicate things.",
                    },
                    {
                        "move": "Nc6",
                        "san": "5... Nc6",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P4/2PBPN2/PP3PPP/RNBQK2R w KQkq - 1 6",
                        "explanation": "Black develops the queen's knight. Both sides are building up their forces logically.",
                    },
                    {
                        "move": "Nbd2",
                        "san": "6. Nbd2",
                        "fen": "r1bqkb1r/pp3ppp/2n1pn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQK2R b KQkq - 2 6",
                        "explanation": "White develops the queen's knight to d2 rather than c3 (which is blocked by the pawn). From d2 it can hop to f1 or e4 later.",
                    },
                    {
                        "move": "Bd6",
                        "san": "6... Bd6",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQK2R w KQkq - 3 7",
                        "explanation": "Black mirrors White's setup — bishop to d6 is very natural here.",
                    },
                    {
                        "move": "O-O",
                        "san": "7. O-O",
                        "fen": "r1bqk2r/pp3ppp/2nbpn2/2pp4/3P4/2PBPN2/PP1N1PPP/R1BQ1RK1 b kq - 4 7",
                        "explanation": "Castle! The king is safe. White's plan is now to play e4 at the right moment, opening lines toward Black's king. The Colle attack is brewing.",
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
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/ppp1pppp/8/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "Knight to f3 — developing and pressuring d5.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "Black develops symmetrically.",
                    },
                    {
                        "move": "e3",
                        "san": "3. e3",
                        "fen": "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 0 3",
                        "explanation": "The Colle move — solid and flexible.",
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
                        "explanation": "Both kings have castled. Now White unleashes the classic Colle plan...",
                    },
                    {
                        "move": "Nbd2",
                        "san": "6. Nbd2",
                        "fen": "rnbq1rk1/ppp1bppp/4pn2/3p4/3P4/3BPN2/PPPN1PPP/R1BQ1RK1 b kq - 5 6",
                        "explanation": "The queen's knight joins the party. From d2 it can swing to f1, then g3 or e5 — building up the kingside attack.",
                    },
                    {
                        "move": "c5",
                        "san": "6... c5",
                        "fen": "rnbq1rk1/pp2bppp/4pn2/2pp4/3P4/3BPN2/PPPN1PPP/R1BQ1RK1 w KQ c6 0 7",
                        "explanation": "Black strikes in the centre — the natural counter.",
                    },
                    {
                        "move": "e4",
                        "san": "7. e4",
                        "fen": "rnbq1rk1/pp2bppp/4pn2/2pp4/3PP3/3B1N2/PPPN1PPP/R1BQ1RK1 b kq e3 0 7",
                        "explanation": "The Colle pawn break! White opens the centre with e4. The bishop on d3 now attacks h7 with lethal force. Black must be very careful. This is where beginner opponents often get into serious trouble.",
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
        "overview": (
            "The Dutch Defense is Black's fighting reply to 1.d4. Instead of "
            "matching White's central pawn with 1...d5, Black plays 1...f5 — an "
            "ambitious move that grabs space on the kingside and signals Black's "
            "intent to attack. The Dutch is famously aggressive and can lead to "
            "wildly unbalanced positions. World Champions Mikhail Botvinnik and "
            "Magnus Carlsen have used it. For beginners, it teaches the important "
            "concept of flank attacks and asymmetrical play."
        ),
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
                        "explanation": "1...f5! This is the Dutch Defense. Black immediately stakes kingside space. It's bold and slightly risky — the e5 square is weakened — but highly aggressive.",
                    },
                    {
                        "move": "c4",
                        "san": "2. c4",
                        "fen": "rnbqkbnr/ppppp1pp/8/5p2/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2",
                        "explanation": "White expands on the queenside — the most ambitious response. c4 is the mainline reply, fighting for the centre.",
                    },
                    {
                        "move": "Nf6",
                        "san": "2... Nf6",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 1 3",
                        "explanation": "Black develops the knight to f6 — controlling e4 and d5. Natural and flexible.",
                    },
                    {
                        "move": "Nc3",
                        "san": "3. Nc3",
                        "fen": "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 2 3",
                        "explanation": "White develops the queen's knight, putting more pressure on the centre.",
                    },
                    {
                        "move": "e6",
                        "san": "3... e6",
                        "fen": "rnbqkb1r/pppp2pp/4pn2/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 0 4",
                        "explanation": "Black plays e6 — supporting f5, opening the diagonal for the dark-squared bishop, and preparing d5. This is the Classical Dutch setup.",
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
                        "explanation": "The bishop comes to e7 — a solid development, preparing to castle. This is the hallmark of the Classical Dutch.",
                    },
                    {
                        "move": "g3",
                        "san": "5. g3",
                        "fen": "rnbqk2r/ppppb1pp/4pn2/5p2/2PP4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq - 0 5",
                        "explanation": "White prepares to fianchetto the bishop on g2 — a powerful diagonal that will put pressure on Black's position for the whole game.",
                    },
                    {
                        "move": "O-O",
                        "san": "5... O-O",
                        "fen": "rnbq1rk1/ppppb1pp/4pn2/5p2/2PP4/2N2NP1/PP2PP1P/R1BQKB1R w KQ - 1 6",
                        "explanation": "Black castles — king safety is always important! From here Black will aim for ...d6 and eventually ...e5 to seize the initiative.",
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
                        "explanation": "White goes for the fianchetto setup — a common way to fight the Dutch.",
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
                        "explanation": "The bishop goes to g2 — the fianchetto is complete. It controls a long diagonal.",
                    },
                    {
                        "move": "d5",
                        "san": "4... d5",
                        "fen": "rnbqkb1r/ppp3pp/4pn2/3p1p2/3P4/5NP1/PPP1PPBP/RNBQK2R w KQkq d6 0 5",
                        "explanation": "The Stonewall! Black has pawns on d5, e6, and f5 — a solid pawn wall. This structure is very resilient and gives Black a clear plan.",
                    },
                    {
                        "move": "O-O",
                        "san": "5. O-O",
                        "fen": "rnbqkb1r/ppp3pp/4pn2/3p1p2/3P4/5NP1/PPP1PPBP/RNBQ1RK1 b kq - 2 5",
                        "explanation": "White castles — both sides are safe. The game enters a strategic battle: White's fianchetto bishop vs. Black's solid Stonewall.",
                    },
                    {
                        "move": "Bd6",
                        "san": "5... Bd6",
                        "fen": "rnbqk2r/ppp3pp/3bpn2/3p1p2/3P4/5NP1/PPP1PPBP/RNBQ1RK1 w kq - 3 6",
                        "explanation": "Black develops the bishop to d6 — a wonderful square in the Stonewall. From here it supports a potential kingside attack and eyes h2. Black will castle next and then launch the attack!",
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
        "overview": (
            "The Rousseau Gambit (also called the Ponziani-Steinitz Gambit) is a "
            "wild and aggressive counter-attack by Black. After 1.e4 e5 2.Nf3 Nc6, "
            "when White plays 3.Bc4 (Italian Game), Black responds with the "
            "shocking 3...f5!? — offering a pawn to seize the initiative. "
            "The idea is to unbalance the game immediately and create attacking "
            "chances. It is risky but great fun, and the tactics can confuse "
            "unprepared opponents quickly."
        ),
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
                        "explanation": "White opens with 1.e4 — the most popular first move, staking central ground immediately.",
                    },
                    {
                        "move": "e5",
                        "san": "1... e5",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 2",
                        "explanation": "Black replies symmetrically with 1...e5 — meeting fire with fire.",
                    },
                    {
                        "move": "Nf3",
                        "san": "2. Nf3",
                        "fen": "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2",
                        "explanation": "White develops the knight and attacks e5 immediately. A key principle: attack in the opening!",
                    },
                    {
                        "move": "Nc6",
                        "san": "2... Nc6",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3",
                        "explanation": "Black defends e5 with the knight — also a key principle: develop while defending.",
                    },
                    {
                        "move": "Bc4",
                        "san": "3. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3",
                        "explanation": "3.Bc4 — the Italian Game! The bishop goes to c4, pointing at f7 — Black's weakest point. This is one of the oldest openings in chess.",
                    },
                    {
                        "move": "f5",
                        "san": "3... f5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq f6 0 4",
                        "explanation": "3...f5!? — The Rousseau Gambit! Black immediately counter-attacks with f5, threatening to take on e4. This is Black's fighting spirit — instead of passive defence, Black attacks!",
                    },
                    {
                        "move": "d3",
                        "san": "4. d3",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/3P1N2/PPP2PPP/RNBQK2R b KQkq - 0 4",
                        "explanation": "White declines to capture and plays d3 — a solid response. White supports e4 and prepares to develop the remaining pieces. This is actually the safest approach.",
                    },
                    {
                        "move": "Nf6",
                        "san": "4... Nf6",
                        "fen": "r1bqkb1r/pppp2pp/2n2n2/4pp2/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 1 5",
                        "explanation": "Black develops the knight to f6 — adding pressure to e4 and developing rapidly.",
                    },
                    {
                        "move": "Nc3",
                        "san": "5. Nc3",
                        "fen": "r1bqkb1r/pppp2pp/2n2n2/4pp2/2B1P3/2NP1N2/PPP2PPP/R1BQK2R b KQkq - 2 5",
                        "explanation": "White develops the queen's knight — putting more defenders around the centre.",
                    },
                    {
                        "move": "fxe4",
                        "san": "5... fxe4",
                        "fen": "r1bqkb1r/pppp2pp/2n2n2/4p3/2B1p3/2NP1N2/PPP2PPP/R1BQK2R w KQkq - 0 6",
                        "explanation": "Black captures on e4! Now White must deal with the threat. The position is sharp and double-edged — exactly what Black was hoping for with the Rousseau Gambit.",
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
                        "explanation": "3...f5!? — The Rousseau Gambit! Black offers the f5 pawn or forces the e4 pawn to advance.",
                    },
                    {
                        "move": "exf5",
                        "san": "4. exf5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4pP2/2B5/5N2/PPPP1PPP/RNBQK2R b KQkq - 0 4",
                        "explanation": "White accepts the gambit! Taking on f5 looks natural — White is up a pawn. But now Black opens the e-file with a powerful response...",
                    },
                    {
                        "move": "e4",
                        "san": "4... e4",
                        "fen": "r1bqkbnr/pppp2pp/2n5/5P2/2B1p3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 5",
                        "explanation": "4...e4! Black advances the e-pawn, attacking the knight on f3. White's knight must move — and meanwhile Black is gaining time and opening lines.",
                    },
                    {
                        "move": "Ne5",
                        "san": "5. Ne5",
                        "fen": "r1bqkbnr/pppp2pp/2n5/4NP2/2B1p3/8/PPPP1PPP/RNBQK2R b KQkq - 1 5",
                        "explanation": "The knight jumps to e5, attacking the knight on c6 and keeping some stability. White hopes the extra pawn on f5 will count in the long run.",
                    },
                    {
                        "move": "Qh4",
                        "san": "5... Qh4",
                        "fen": "r1b1kbnr/pppp2pp/2n5/4NP2/2B1p2q/8/PPPP1PPP/RNBQK2R w KQkq - 2 6",
                        "explanation": "5...Qh4! A devastating attack! The queen comes to h4 with check threats and enormous pressure. White's king is in real danger. Black has full compensation for the pawn — this is why the Rousseau Gambit is so dangerous!",
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
        "overview": (
            "The Scotch Gambit is an exciting, swashbuckling opening where White "
            "sacrifices a pawn to gain rapid development and attacking chances. "
            "After 1.e4 e5 2.Nf3 Nc6 3.d4, White opens the centre. After Black "
            "captures 3...exd4, instead of recapturing with the knight (Scotch "
            "Game), White plays 4.Bc4 — the Scotch Gambit! White offers the d4 "
            "pawn in exchange for a huge lead in development. This opening teaches "
            "the fundamental chess principle: time and activity are worth material."
        ),
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
                        "explanation": "3.d4! White strikes in the centre immediately — this is the key idea that distinguishes the Scotch Gambit from the Italian Game. White challenges Black to take the pawn.",
                    },
                    {
                        "move": "exd4",
                        "san": "3... exd4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4",
                        "explanation": "3...exd4 — Black accepts, capturing the d4 pawn. This opens the centre and is practically forced — declining is passive.",
                    },
                    {
                        "move": "Bc4",
                        "san": "4. Bc4",
                        "fen": "r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4",
                        "explanation": "4.Bc4! — The Scotch Gambit! Instead of winning back the pawn immediately, White develops the bishop to c4. This attacks f7 and develops rapidly. White is a pawn down but already has active pieces.",
                    },
                    {
                        "move": "Bc5",
                        "san": "4... Bc5",
                        "fen": "r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5",
                        "explanation": "4...Bc5 — Black develops the bishop, holding onto the extra pawn. Now comes the key Scotch Gambit move...",
                    },
                    {
                        "move": "c3",
                        "san": "5. c3",
                        "fen": "r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/2P2N2/PP3PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "5.c3! White attacks the d4 pawn immediately, trying to recapture the centre. This forces Black to make a decision.",
                    },
                    {
                        "move": "Nf6",
                        "san": "5... Nf6",
                        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b5/2BpP3/2P2N2/PP3PPP/RNBQK2R w KQkq - 1 6",
                        "explanation": "5...Nf6 — Black develops the knight and attacks e4. Black is trying to hold the extra pawn while also developing.",
                    },
                    {
                        "move": "e5",
                        "san": "6. e5",
                        "fen": "r1bqk2r/pppp1ppp/2n2n2/2b1P3/2Bp4/2P2N2/PP3PPP/RNBQK2R b KQkq - 0 6",
                        "explanation": "6.e5! White pushes the pawn forward, attacking the f6 knight. This is an energetic move — White is playing dynamically rather than trying to regain the pawn immediately.",
                    },
                    {
                        "move": "d5",
                        "san": "6... d5",
                        "fen": "r1bqk2r/ppp2ppp/2n2n2/2bpP3/2Bp4/2P2N2/PP3PPP/RNBQK2R w KQkq d6 0 7",
                        "explanation": "6...d5! Black counter-attacks in the centre. This is the recommended defence — Black gives back material to free the position.",
                    },
                    {
                        "move": "Bb5",
                        "san": "7. Bb5",
                        "fen": "r1bqk2r/ppp2ppp/2n2n2/1B1pP3/3p4/2P2N2/PP3PPP/RNBQK2R b KQkq - 1 7",
                        "explanation": "7.Bb5 — the bishop pins the knight on c6, which was defending d5. White is building up pressure systematically. This is the Max Lange Attack territory — one of the most analyzed gambits in chess history!",
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
                        "explanation": "4...Nf6! — The Dubois-Réti Defense! Instead of Bc5, Black immediately attacks e4 with the knight. This is a fighting response.",
                    },
                    {
                        "move": "e5",
                        "san": "5. e5",
                        "fen": "r1bqkb1r/pppp1ppp/2n2n2/4P3/2Bp4/5N2/PPP2PPP/RNBQK2R b KQkq - 0 5",
                        "explanation": "5.e5 — White attacks the knight, pushing forward aggressively.",
                    },
                    {
                        "move": "d5",
                        "san": "5... d5",
                        "fen": "r1bqkb1r/ppp2ppp/2n2n2/3pP3/2Bp4/5N2/PPP2PPP/RNBQK2R w KQkq d6 0 6",
                        "explanation": "5...d5! Black hits back in the centre — attacking both the e5 pawn and the c4 bishop. The game becomes very sharp and tactical.",
                    },
                    {
                        "move": "Bb5",
                        "san": "6. Bb5",
                        "fen": "r1bqkb1r/ppp2ppp/2n2n2/1B1pP3/3p4/5N2/PPP2PPP/RNBQK2R b KQkq - 1 6",
                        "explanation": "6.Bb5 — pinning the knight on c6. White maintains pressure and the position crackles with tactics. Both players need to play very accurately here. This is excellent training for tactical vision!",
                    },
                ],
            },
        ],
    },
}
