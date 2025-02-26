# ConductorAI Challenge

This project is my submission for ConductorAI's challenge prompt [here](A submission for ConductorAI's challenge posted https://conductorai.notion.site/Take-Home-Project-028703f8766948e19430bd6cd5370345?pvs=4)

## Basic usage

`numinpdf` can be setup and run using [`uv`](https://docs.astral.sh/uv/) (which is an amazing package manager
for several reasons). The basic syntax is `uv run numinpdf <filename>`

To see it in action, simply execute the following, which also fetches the sample data:

```bash
make data # helper command to fetch the PDF for the challenge
uv run numinpdf "data/FY25 Air Force Working Capital Fund.pdf"
```

## Comments

_I did not use LLMs here because the problem statement forbid use of external APIs. It is of course entirely possible to download and use these models offline, but given they are often 5-10GB in size I am intentionally not adding that heft into this example exercise plus it allows one to demonstrate a little more raw engineering versus "how easy" a code snippet using LLMs might be. I call this out because in the real world that is probably where we would start at the time of this writing._

My approach here was to be very test driven. TDD in my opinion gets overhyped as being a silver bullet when it really isn't, but for certain applications it is extremely effective. This is one on them, as I could build and satisfy a certain pattern I wanted it to work for, and then continue to add edge cases all while ensuring each previous case still passed. Continuing from here to iterate as far as needed is how I would build this in a real production setting. It's also packaged for distribution and easy use/re-use with some dev tooling to help manage codebase consistency across a distributed team (e.g. pre-commit etc).

You can find test examples in the files appended with `__test.py` (though it is common to see a tests/ folder I prefer the practice of colocating test code with functional code, a topic I rambled on about long time ago regarding Flask [here](https://apryor6.github.io/2019-05-20-flask-api-example/)). Notably these tests make sure of the `pytest` [`tmppath`](https://docs.pytest.org/en/stable/how-to/tmp_path.html) fixture to generate PDFs where I control the content so that I can assert it is finding the correct values. I then iterated on this to progressively increase the complexity of the algorithm including stripping special characters or looking for contextual characters like 1.5M = 1500000.
