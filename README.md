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
Week 3: Tire Life Prediction (ML Project #1)
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
---

## 🤖 Week 3 — Tire Life Prediction (ML Project #1)

This week turns tire degradation into a supervised ML problem.

### 🎯 Problem

Given information about a lap (tire age, stint, race phase), predict the
expected lap time. The goal is to:

- Quantify how strongly lap time depends on tire age
- Compare predictability of different cars (Ferrari vs Red Bull)
- Build models that could be used in pit-window and stint-length decisions

### 📘 Notebook

**`notebooks/03_tire_life_prediction.ipynb`**

Contains:

1. Data preparation (reusing the cleaned laps from Week 2)
2. **Model 1 — Linear Regression**
   - Baseline relationship: `LapTimeSeconds ~ TyreLife`
   - Interpretable degradation slope (seconds per lap of tire age)
3. **Model 2 — Random Forest Regression**
   - Non-linear degradation modeling
   - Captures more complex patterns (fuel burn, local fluctuations)
   - Better performance on stable cars (e.g. VER on HARD)

### 📂 Saved Models (`/models`)

Example artifacts:

- `linreg_2024_bahrain_VER_HARD.pkl`
- `linreg_2024_bahrain_LEC_HARD.pkl`
- `rf_2024_bahrain_VER_HARD.pkl`
- `rf_2024_bahrain_LEC_HARD.pkl`

These can be loaded with `joblib` for future simulation notebooks
(e.g. strategy optimization or pit-window prediction).

### 🧠 Key Insights

- Red Bull (VER) exhibits predictable, low-noise degradation:
  - Both Linear Regression and Random Forest achieve low MAE
  - R² is positive, indicating that tire age explains a meaningful part of lap time variance

- Ferrari (LEC) shows noisier, less predictable tire behavior:
  - Higher MAE, negative R² for both models
  - Degradation is less linear and more influenced by setup/thermal swings

This difference in **predictability** is itself a strategic factor:
teams with stable long-run performance can be modeled more accurately and
therefore run more reliable strategy simulations.

### Modeling Constraints

To ensure physical realism, tire degradation slopes are constrained to be
non-negative. This prevents the optimizer from exploiting statistical noise
(e.g., lap time improvements on older tires due to track evolution or fuel burn-off).

This constraint stabilizes strategy optimization and reflects real-world
Formula 1 tire behavior.
