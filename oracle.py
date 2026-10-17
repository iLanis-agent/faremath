#!/usr/bin/env python3
# Fare Math oracle - mirrors engine.js float-for-float.
import json, math

def _fixed2(x):
    c = math.floor(x * 100 + 0.5)
    w, r = c // 100, c % 100
    return f"{w}.{r:02d}"

def _check_prices(p, r):
    if not math.isfinite(p) or p <= 0:
        raise ValueError("the pass price must be more than zero")
    if not math.isfinite(r) or r <= 0:
        raise ValueError("the ride price must be more than zero")

def break_even_truth(p, r):
    _check_prices(p, r)
    n = math.ceil(p / r - 1e-9)
    return (f"The ${_fixed2(p)} pass against ${_fixed2(r)} rides breaks even at ride {n} - "
            f"ride {n + 1} onward is free.")

def month_truth(p, r, rides):
    _check_prices(p, r)
    if not math.isfinite(rides) or rides < 0:
        raise ValueError("rides must be zero or more")
    if rides == 0:
        return "Zero rides is zero rides - the pass is a donation."
    total = rides * r
    diff = total - p
    ride_word = "ride" if rides == 1 else "rides"
    head = f"{rides} {ride_word} at ${_fixed2(r)} are ${_fixed2(total)} - "
    if abs(diff) < 0.005:
        return head + f"exactly the ${_fixed2(p)} pass, a wash."
    if diff > 0:
        return head + f"the ${_fixed2(p)} pass saves you ${_fixed2(diff)}."
    return head + f"the ${_fixed2(p)} pass costs ${_fixed2(-diff)} more than the rides."

def commute_truth(rpd, days):
    if not math.isfinite(rpd) or rpd < 0:
        raise ValueError("rides per day must be zero or more")
    if not math.isfinite(days) or days < 1:
        raise ValueError("days must be at least 1")
    total = rpd * days
    r_word = "ride" if rpd == 1 else "rides"
    d_word = "day" if days == 1 else "days"
    t_word = "ride" if total == 1 else "rides"
    return (f"{rpd} {r_word} a day for {days} {d_word} is {total} {t_word} - "
            f"count the vacation days honestly.")

CASES = [
    ("breakEvenTruth", (86, 2.75)),
    ("breakEvenTruth", (10, 2.50)),
    ("breakEvenTruth", (86, 0)),
    ("breakEvenTruth", (0, 2.75)),
    ("monthTruth", (86, 2.75, 22)),
    ("monthTruth", (86, 2.75, 40)),
    ("monthTruth", (10, 2.50, 4)),
    ("monthTruth", (86, 2.75, 0)),
    ("monthTruth", (86, 2.75, -1)),
    ("commuteTruth", (2, 20)),
    ("commuteTruth", (1, 1)),
    ("commuteTruth", (2, 0)),
]

FNS = {"breakEvenTruth": break_even_truth, "monthTruth": month_truth, "commuteTruth": commute_truth}

out = []
for name, args in CASES:
    try:
        expected = FNS[name](*args)
    except ValueError as e:
        expected = "ERR:" + str(e)
    out.append({"fn": name, "args": list(args), "expected": expected})

with open("expected.json", "w") as f:
    f.write(json.dumps(out, indent=2) + "\n")
print(f"{len(out)} cases written")
