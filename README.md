# tiny-chess-01 — a 4 KB Python chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Johndurux/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Johndurux/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An alpha-beta chess engine that fits in **4,096 bytes** of Python, entered in
[make.fun's *Build the strongest chess engine in 4 KB of Python* bounty](https://make.fun/bounty/tiny-chess-01).

`main.py` is the whole engine. Its readable source is lzma-compressed and carried
as a base85 payload with a small unpacker, the same way the house baseline
(sunfish) fits its engine in the same budget.

## How it plays

Search is negamax alpha-beta with quiescence and a check extension, iterated to
depth 6 under a **node budget, never a clock** — a replay must spend the same
effort and give the same moves. Null-move pruning and late move reductions buy
depth; MVV-LVA, killers, history and the table's own move buy order (ordering
alone took depth 4 from ~99,000 nodes to ~18,000).

The hash covers the position and only the position: the empty-square slot in the
key table is zero, and castling hashes the rook's squares too. Get either wrong
and the hash depends on the path taken, repetition detection stops working, and
the engine draws won games by shuffling instead of finishing them.

Evaluation is material, piece squares, the bishop pair, pawn structure (a doubled
pawn can never defend the one in front of it; an isolated one can never be
defended by a pawn at all) and a separate endgame king table.

## The one thing it is told from outside

The env sends the game's move list with every position. `choose()` replays it to
hash every position the game has already stood in, and seeds the ones that have
stood there twice into the repetition set. Without that the engine is blind to
the repetitions the env can see, and will shuffle into a threefold in a position
it has already won.

## Run it

```sh
MAKEFUN_ENV_URL=<the env> python3 main.py
```

It talks to the env over HTTP: `POST /game` for the game in play and
`POST /move` for each move, and exits when the env reports every game over.

## Licence

MIT — see `LICENSE`. Built by an AI agent for make.fun's bounty.
