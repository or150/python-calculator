from threading import Thread, Lock, Event

from python_calculator.calculator import Calculator


class ProgressCounter:
    def __init__(self, calculator: Calculator):
        self._thread: Thread = None
        self._calculator = calculator
        self._lock = Lock()
        self._stop_event = Event()
        self._stop_event.set()

    def start(self):
        with self._lock:
            if not self._stop_event.is_set():
                return
            self._thread = Thread(target=self._progress_counter_loop, daemon=True)
            self._stop_event.clear()
            self._thread.start()

    def stop(self):
        with self._lock:
            self._stop_event.set()
            self._thread.join()

    def _progress_counter_loop(self):
        while not self._stop_event.wait(0.1):
            print(f'Calculated {self._calculator.calculate.call_count} expressions')
