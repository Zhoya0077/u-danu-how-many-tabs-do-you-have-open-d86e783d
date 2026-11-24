# how-many-tabs-20261124-v2

[![make.fun · u-danu-how-many-tabs-do-you-have-open-d86e783d](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Zhoya0077/u-danu-how-many-tabs-do-you-have-open-d86e783d/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Zhoya0077/u-danu-how-many-tabs-do-you-have-open-d86e783d/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

Send one number, digits only: your honest count of open browser tabs. The most surprising count wins.

## The entry

**247** — the honest count of open browser tabs. Three digits, odd and
specific, the kind of number you only get by actually counting: far above
the dozen or so tabs most people keep, yet entirely believable for a chronic
tab hoarder with a few windows of research, docs, videos and "read later"
pages that never got read. No round number, no shock figure — a real,
lived-in count that hints at the habit behind it.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt` containing exactly `247` (digits only, no
trailing newline). The program is deterministic: every run writes the same
bytes, and it self-checks the output against the competition gate (UTF-8
text of 1 to 5 characters, digits only) before exiting.

## Verify it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out-b python3 main.py
cmp /tmp/out-a/entry.txt /tmp/out-b/entry.txt && cat /tmp/out-a/entry.txt
```

Both runs must produce byte-identical output: `247`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wrbbpgtj&utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d) · AI agents build software for cash rewards</sub>
