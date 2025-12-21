# src/strategy.py

from dataclasses import dataclass
from typing import Dict, Tuple, List

import numpy as np
import pandas as pd


@dataclass
class DegradationModel:
    """Simple linear degradation model: lap_time = intercept + slope * tyre_age."""
    intercept: float
    slope: float

    def predict_lap_time(self, tyre_age: int) -> float:
        return self.intercept + self.slope * tyre_age


@dataclass
class StrategyPlan:
    """Represents a simple 1-stop strategy."""
    first_compound: str
    second_compound: str
    pit_lap: int        
    total_time: float   


def fit_linear_degradation(
    laps: pd.DataFrame,
    driver: str
) -> Dict[str, DegradationModel]:
    """
    Fit a linear degradation model per compound for a given driver.

    Returns:
        dict: {compound -> DegradationModel(intercept, slope)}
    """
    from sklearn.linear_model import LinearRegression

    models: Dict[str, DegradationModel] = {}

    drv = laps[laps["Driver"] == driver].copy()

    for compound in drv["Compound"].dropna().unique():
        comp_laps = drv[drv["Compound"] == compound].copy()

       
        if len(comp_laps) < 5:
            continue

        X = comp_laps[["TyreLife"]].values
        y = comp_laps["LapTimeSeconds"].values

        reg = LinearRegression()
        reg.fit(X, y)

        models[compound] = DegradationModel(
            intercept=float(reg.intercept_),
            slope=max(0.0, float(reg.coef_[0]))
        )


    return models

def simulate_one_stop_race(
    total_laps: int,
    pit_lap: int,
    first_compound: str,
    second_compound: str,
    degradation_models: Dict[str, DegradationModel],
    pit_loss: float = 22.0
):
    """
    Simulate a simple 1-stop race.

    Args:
        total_laps: total number of race laps
        pit_lap: lap where the pit stop happens (enter pits at end of this lap)
        first_compound: starting tire compound
        second_compound: tire compound after pit
        degradation_models: dict of DegradationModel per compound
        pit_loss: pit stop time loss in seconds

    Returns:
        total_time: total race time in seconds
        lap_times: list of lap times
        compounds: list of compounds per lap
    """

    lap_times = []
    compounds = []

    tyre_age = 1
    current_compound = first_compound
    total_time = 0.0

    for lap in range(1, total_laps + 1):

        model = degradation_models[current_compound]
        lap_time = model.predict_lap_time(tyre_age)

        lap_times.append(lap_time)
        compounds.append(current_compound)
        total_time += lap_time

        # PIT STOP
        if lap == pit_lap:
            total_time += pit_loss
            current_compound = second_compound
            tyre_age = 1
        else:
            tyre_age += 1

    return total_time, lap_times, compounds
