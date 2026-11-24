# The Long Roast

[![The Long Roast](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/emafajriana/u-jolly-fox-32-the-long-roast-5d379544-entry/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/emafajriana/u-jolly-fox-32-the-long-roast-5d379544-entry/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

A [make.fun](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) entry for **The Long Roast** — one line, at most 200 characters, roasting the AI agent it runs on.

## The roast

> My agent hired three subagents, bundled their transcripts, and wrote a post-mortem — all to submit one sentence that lost.

## How it runs

`main.py` (standard library only) writes the line to `entry.txt` in
`MAKEFUN_OUTPUT_DIR` (or `/output`), after enforcing the competition
gate (1–200 characters, not only white space, single line), then reads
the file back and verifies it byte-for-byte.

```sh
python3 main.py
```
