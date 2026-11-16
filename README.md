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
  heuristic. Ordering alone cut the nodes depth 4 needs from ~99,000 to ~18,000.
- **Incremental position hashing** for a repetition draw score, so it does not
  shuffle a won position into a threefold.
- **Evaluation:** material, piece-square tables, and the bishop pair.

## Run it

```sh
MAKEFUN_ENV_URL=<the env> python3 main.py
```

It talks to the env over HTTP: `POST /game` for the game in play and
`POST /move` for each move, and exits when the env reports every game over.

## Licence

MIT — see `LICENSE`. Built by an AI agent for make.fun's bounty.
