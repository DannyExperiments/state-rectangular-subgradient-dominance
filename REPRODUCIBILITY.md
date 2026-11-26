# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay checks 300 active-gradient mixtures, 2,400 fixed-model comparisons, eight active row selections and 13 weight choices in the three-state example using rational arithmetic. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/occupancy-rows-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font paths. [Build the paper](paper/BUILD.md).
