# Museum of the Year 3000

A one-line museum label from the year 3000 for a make.fun bounty, with a 2 USDC prize pool for the top 10 entries.

[![Museum of the Year 3000](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Nadanese93/museum-of-the-year-3000/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Nadanese93/museum-of-the-year-3000/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

## What it does

`main.py` validates the museum-label entry (one line, 1–200 characters, not blank) and writes it byte-exactly to `MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline. Python 3, standard library only, deterministic, no network, no randomness.

## Usage

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
