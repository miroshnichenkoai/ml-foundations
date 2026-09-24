"""Module for data preprocessing and splitting operations."""

from dataclasses import dataclass

import numpy as np


def split_data(
    data: np.typing.NDArray[np.int_],
) -> tuple[np.typing.NDArray[np.int_], np.typing.NDArray[np.int_]]:
    """Split data into train and test sets."""
    length = len(data)
    train_data = data[: int(length * 0.8)]
    test_data = data[int(length * 0.8) :]
    return train_data, test_data


@dataclass(frozen=True)
class TrainConfig:
    """Configuration for training."""

    seed: int
    lr: float
    steps: int

    def set_rng(self) -> np.random.Generator:
        """Random number generator."""
        return np.random.default_rng(self.seed)
