import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import ContextManager


@dataclass
class ExecutionTimeMeasurement:
    execution_time: int = field(default=0)


class ExecutionTimeCounter:
    def __init__(self):
        self._measurements = []

    @contextmanager
    def measure(self) -> ContextManager[ExecutionTimeMeasurement]:
        measurement = ExecutionTimeMeasurement()

        start = time.time()
        try:
            yield measurement
        finally:
            end = time.time()
            measurement.execution_time = end - start
            self._measurements.append(measurement.execution_time)

    @property
    def average_execution_time(self):
        return sum(self._measurements) / len(self._measurements)

    @property
    def total_execution_time(self):
        return sum(self._measurements)
