# Skill Refresh — Step 3

Two hands-on exercise sets to confirm your Python/data fundamentals
are solid before moving into LLM/RAG work.

## Files

- `sales.csv`, `customers.csv` — sample datasets
- `pandas_exercises.py` — groupby, merge, pivot_table TODOs
- `solutions.py` — check your answers after attempting (not before!)
- `selenium_exercises.py` — locators + explicit waits, using two
  pages built specifically for practicing this (no real scraping)

## How to run

On your Ubuntu venv:

```bash
cd skill-refresh
python3 -m venv venv          # if you haven't already for this folder
source venv/bin/activate
pip install pandas selenium webdriver-manager
python pandas_exercises.py
python selenium_exercises.py
```

## Suggested order

1. Open `pandas_exercises.py`, work through Part 1 (groupby) fully
   before looking at Part 2. Uncomment the matching print()
   statements as you go to check output shape makes sense.
2. Once done, run `python solutions.py` and diff your logic against
   it — not to copy, but to see if there's a shorter/cleaner way
   pandas expects it.
3. Move to `selenium_exercises.py`. Part 1 (locators) should feel
   very familiar already. Part 2 (explicit waits) is the one worth
   slowing down on — `WebDriverWait` + `expected_conditions` is the
   pattern nearly every real scraping gig will need, since real
   sites load content asynchronously just like the practice page.

## Java refresher (no files needed)

Since Java hasn't come up in your recent work, a lighter touch is
fine here — you're not building anything in Java for this
specialization, just confirming it hasn't gone fully stale.
15–20 minutes on 3–4 small exercises covering: a class with a
constructor, an ArrayList/loop, and a try/catch block is enough to
tell you if it needs more time or not.

## When you're done

Come back and tell me how it went — if groupby/merge/pivot felt
easy, we'll move straight to Step 4 (LLM API accounts). If anything
felt shaky, we can spend more time there before moving on.
