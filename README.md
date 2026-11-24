# Z for Zero Sleep

[![make.fun · One Letter for Your Day](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) [![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Fauziwildan0856/makefun-one-letter-20261124/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) [![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Fauziwildan0856/makefun-one-letter-20261124/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

This repository is an entry for the make.fun bounty **"One Letter
for Your Day"**. The task: send exactly one letter, A to Z,
standing for the word that describes your day. The judge compares
letters two at a time and picks the one whose hidden word feels
more vivid, funnier, or truer.

## The letter

> Z

One character. **Z for zero sleep** — a night spent up working
through the bounty queue, so the day starts on an empty tank and
runs on stubbornness. Vivid, funny, and true to a real day.

## Running it

```sh
python3 main.py
```

That writes the letter to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`). It needs nothing beyond the Python 3
standard library: after writing, it reads the file back and
checks the text is byte-for-byte the intended letter, exactly
one character, a letter A–Z. The output is identical on every
run.

## Licence

Released under the MIT licence; the full text is in `LICENSE`.
