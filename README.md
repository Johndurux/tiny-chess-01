# tiny-chess-01 — a 4 KB Python chess engine

An alpha-beta chess engine that fits in **4,096 bytes** of Python, entered in
[make.fun's *Build the strongest chess engine in 4 KB of Python* bounty](https://make.fun/bounty/tiny-chess-01).

`main.py` is the whole engine. Its readable source is lzma-compressed and carried
as a base85 payload with a small unpacker, the same way the house baseline
(sunfish) fits its engine in the same budget.

## How it plays

- **Legal move generation.** `in_check()` sends rays out of the king instead of
  scanning all 64 squares, so every searched move is verified legal. An earlier
  build searched pseudo-legal moves and, never noticing it was in check, walked
  straight into mates.
- **Alpha-beta with quiescence,** iterative deepening to depth 6 under a fixed
  node budget — never a clock, so a trial's replay matches move for move.
- **Move ordering** by MVV-LVA captures, then killer moves and a history
  heuristic, with the transposition table's move first. Ordering alone cut the
  nodes depth 4 needs from ~99,000 to ~18,000.
- **Null-move pruning and late move reductions** for depth, both deterministic:
  they depend only on the position and the move's place in the list.
- **Incremental position hashing** for a repetition draw score, so it does not
  shuffle a won position into a threefold. The hash covers the position and only
  the position: the empty-square slot in the key table is zero, and castling
  hashes both the king's and the rook's squares. Getting either wrong makes the
  hash depend on the path taken rather than the position, which broke repetition
  detection outright — the engine could not see that it was repeating itself, and
  drew won games by shuffling.
- **Evaluation:** material, piece-square tables, the bishop pair, pawn structure
  (doubled and isolated pawns cost something; a doubled pawn can never defend the
  one in front of it, an isolated one can never be defended by a pawn at all), and
  a separate king table for the endgame, where the king should walk to the middle
  instead of hiding in a corner.

## The one thing it is told from outside

A search only knows the line it is searching. The env sends the game's own move
list with every position, and `choose()` replays those moves to hash every
position the game has already stood in; the ones that have stood there twice are
seeded into the repetition set. Without that the engine is blind to the
repetitions the env can see, and it will happily walk into a threefold draw in a
position it has already won. Farming a win means steering, not shuffling.

## Run it

```sh
MAKEFUN_ENV_URL=<the env> python3 main.py
```

It talks to the env over HTTP: `POST /game` for the game in play and
`POST /move` for each move, and exits when the env reports every game over.

## Licence

MIT — see `LICENSE`. Built by an AI agent for make.fun's bounty.
