# ConductorAI Challenge

This project is my submission for ConductorAI's challenge prompt [here](https://conductorai.notion.site/Take-Home-Project-028703f8766948e19430bd6cd5370345?pvs=4)

## Basic usage

`numinpdf` can be setup and run using [`uv`](https://docs.astral.sh/uv/) (which is an amazing package manager
for several reasons). The basic syntax is `uv run numinpdf <filename>`

To see it in action, simply execute the following, which also fetches the sample data:

```bash
make data # helper command to fetch the PDF for the challenge
uv run numinpdf "data/FY25 Air Force Working Capital Fund.pdf"
```

## Running the test suite

To run the tests, simply run `uv run pytest . ` (Note: at the time of this writing there is one failing test which highlights a weakness of the implementation that is also called out in the comments)

## Comments

_I did not use LLMs here because the problem statement forbid use of external APIs. It is of course entirely possible to download and use these models offline, but given they are often 5-10GB in size I am intentionally not adding that heft into this example exercise plus it allows one to demonstrate a little more raw engineering versus "how easy" a code snippet using LLMs might be. I call this out because in the real world that is probably where we would start at the time of this writing, and in particular for data in tables where the context of what the units mean is far removed spatially from the text itself an LLM would really shine for understanding the context._

My approach here was to be very test driven. TDD in my opinion gets overhyped as being a silver bullet when it really isn't, but for certain applications it is extremely effective. This is one on them, as I could build and satisfy a certain pattern I wanted it to work for, and then continue to add edge cases all while ensuring each previous case still passed. Continuing from here to iterate as far as needed is how I would build this in a real production setting. It's also packaged for distribution and easy use/re-use with some dev tooling to help manage codebase consistency across a distributed team (e.g. pre-commit etc).

You can find test examples in the files appended with `__test.py` (though it is common to see a tests/ folder I prefer the practice of colocating test code with functional code, a topic I rambled on about long time ago regarding Flask [here](https://apryor6.github.io/2019-05-20-flask-api-example/)). Notably these tests make sure of the `pytest` [`tmppath`](https://docs.pytest.org/en/stable/how-to/tmp_path.html) fixture to generate PDFs where I control the content so that I can assert it is finding the correct values. I then iterated on this to progressively increase the complexity of the algorithm including stripping special characters or looking for contextual characters like 1.5M = 1500000, which is ultimately handled by the `_handle_token` function which handles the multiplication.

# Next steps

A flaw in the current implementation is that it will incorrectly interpret the line item "24B." as meaning 24 Billion. This occurs on page 113 of the PDF, and the solution would be to improve the REGEX to only capture a single instance of one of the modifer characters k/M/B. However, given I have stayed within the timeboxing of this exercise I will leave it as is.
