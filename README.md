# chess4k

A tiny chess engine for the make.fun bounty [tiny-chess-01](https://make.fun/bounty/tiny-chess-01): iterative-deepening alpha-beta under a fixed 40k-node budget per move, 0x88 board, quiescence search, transposition table, killer/history ordering and piece-square evaluation. Fully deterministic (no clock, no randomness), Python 3.13 standard library only, packed as an lzma payload with its unpacker in one 4 KB `main.py`.

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ucupverz/chess4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard)

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python main.py
```
