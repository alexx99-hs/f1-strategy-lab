# F1 Strategy Lab

An experimental lab for analyzing Formula 1 race strategy using Python, FastF1, and data from recent seasons (2021–2024).

## Goals

- Download and organize official timing & telemetry data using [FastF1](https://theoehrly.github.io/Fast-F1/).
- Explore tyre strategy, stint lengths, safety car impact, and pit stop timings.
- Build reusable tools and visualizations that resemble what real F1 strategy teams might use.

## Structure

- `data/` – cached and exported race data (laps, telemetry, etc.)
- `notebooks/` – exploratory Jupyter notebooks (starting with `01_data_download.ipynb`)
- `src/` – helper scripts for data loading and analysis (to be added later)

## Status

Week 1: 🔄 Setting up environment and collecting baseline data.

## Environment

You can install the basic dependencies with:

```bash
pip install -r requirements.txt 

### Full Dataset Storage

Because F1 timing data and FastF1 cache files can be very large,
the complete dataset (all seasons 2021–2024) is stored externally
in Google Drive during development.

This repository includes only a small set of example CSV files in `data/`
to make the notebooks runnable and keep the project lightweight.
