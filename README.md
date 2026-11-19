# chess4k

A tiny deterministic chess engine that fits in 4096 bytes, built for the make.fun
[tiny-chess-01](https://make.fun/bounty/tiny-chess-01) bounty.

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ucupverz/chess4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard)
[![reward](https://make.fun/badge/tiny-chess-01/ucupverz/chess4k/reward.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard)

## What it is

`main.py` is a self-contained Python 3 program, standard library only. It plays
full games of chess against the make.fun environment: it reads the current game
state over HTTP, searches, and returns one legal move in UCI form.

No model calls, no network access beyond the environment, no randomness. The
same position always produces the same move.

## How it works

The shipped file is a compressed payload. The readable source travels in the
submission bundle under `packs/` and expands to a single module:

- **Board** — 0x88 mailbox, 128 squares, occupied squares kept in a set.
- **Move generation** — pawns (double push, en passant, promotion), knights,
  bishops, rooks, queens, king, and both castling sides.
- **Search** — iterative deepening alpha-beta with a principal variation, a
  transposition table keyed by Zobrist hash, killer moves and a history
  heuristic for ordering.
- **Quiescence** — captures, promotions and en passant only, so the search
  never stops in the middle of a trade.
- **Evaluation** — material plus piece-square tables and a bishop-pair bonus.
- **Budget** — a fixed node budget per move rather than a wall-clock timer, so
  the result is identical on any machine.

## Run it

The program expects `MAKEFUN_ENV_URL` to point at a make.fun environment.

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python main.py
```

It polls `/game`, and while the game is on `your_move` it posts its choice to
`/move`. When the environment reports `done`, it exits.

To reproduce the shipped file from source:

```sh
makefun compress engine.py --out main.py
```

## Layout

| path | what |
| --- | --- |
| `main.py` | the entry, 4096-byte limit |
| `README.md` | this file |
| `LICENSE` | MIT |

## License

MIT. See `LICENSE`.
