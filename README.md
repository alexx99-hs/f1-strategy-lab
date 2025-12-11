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
Week 2: 🏎️Exploratory Tire Degradation Analysis.

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

---
🏎️ Week 2 — Exploratory Tire Degradation Analysis

This week focuses on understanding how lap time evolves as tires age during a race.  
Using data from the 2024 Bahrain Grand Prix, I explored driver pace, tire compound behavior, and team-level degradation differences.

### 🔍 Goals
- Analyze how lap time changes with tire wear  
- Compare soft vs hard tire behavior  
- Build degradation trendlines using linear modeling  
- Compare Ferrari vs Red Bull long-run performance  

### 📘 Notebook  
**`notebooks/02_tire_degradation_analysis.ipynb`**  
Contains all analysis steps, visualizations, and strategic interpretation.

### 📊 Key Visualizations (in `figures/`)
- **Lap Time vs Lap Number**  
  Shows overall race pace evolution for each driver.

- **Lap Time by Tire Compound**  
  Highlights differences between Soft and Hard compound behavior.

- **Degradation Curves (Lap Time vs Tyre Age)**  
  Shows how performance drops as tire age increases.

- **Degradation Trendlines (Linear Regression)**  
  Quantifies degradation rate for each compound.

- **Team Comparison: Ferrari vs Red Bull**  
  Direct comparison of Charles Leclerc and Max Verstappen’s degradation profiles.

### 🧠 Strategic Insights (Summary)
- Red Bull (VER) has lower baseline lap times and more stable degradation.  
- Ferrari (LEC) shows steeper degradation on soft tires and higher instability across stints.  
- Hard tires provide more consistent performance but still favor Red Bull.  
- These patterns align with real 2024 Bahrain GP race strategy outcomes.

### 🧩 Skills Demonstrated
- Data cleaning and preparation  
- Race-pace lap filtering  
- Tire degradation modeling  
- Multi-driver comparative analysis  
- Visualization for race strategy understanding  

---

