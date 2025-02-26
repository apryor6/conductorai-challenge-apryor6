# ConductorAI Challenge

This project is my submission for ConductorAI's challenge prompt [here](A submission for ConductorAI's challenge posted https://conductorai.notion.site/Take-Home-Project-028703f8766948e19430bd6cd5370345?pvs=4)

## Basic usage

`numinpdf` can be setup and run using [`uv`](https://docs.astral.sh/uv/) (which is an amazing package manager
for several reasons). The basic syntax is `uv run numinpdf <filename>`

To see it in action, simply execute the following:

```
make data # helper command to fetch the PDF for the challenge
uv run numinpdf "data/FY25 Air Force Working Capital Fund.pdf"
```

## Comments

- My approach here was to be very test driven. TDD in my opinion gets overhyped as being a silver bullet when it really isn't, but for certain applications it is extremely effective. This is one on them, as I could build and satisfy a certain pattern I wanted it to work for, and then continue to add edge cases all while ensuring each previous case still passed. Continuing from here to iterate as far as needed is how I would build this in a real production setting. It's also packaged for distribution and easy use/re-use with some dev tooling to help manage codebase consistency across a distributed team (e.g. pre-commit etc)
