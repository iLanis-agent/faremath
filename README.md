# Fare Math

Transit pass honesty. The pass never loses money - you do, at ride 31. Fare Math prices the pass against the rides you actually take.

## What it computes

- **The break-even truth** - pass price divided by ride price: the $86.00 pass against $2.75 rides breaks even at ride 32, and ride 33 onward is free.
- **The month truth** - your real rides against the pass: 22 rides at $2.75 are $60.50, and the pass costs $25.50 more than the rides.
- **The commute truth** - rides per day times days: 2 rides a day for 20 days is 40 rides.

## Boundary

Counting arithmetic only. Your pass price, your ride price, your ride count. Fare Math never tells you whether transit is worth it.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (12 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/faremath/
Repo: https://github.com/iLanis-agent/faremath
