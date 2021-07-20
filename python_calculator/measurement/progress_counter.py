from threading import Thread, Lock, Event


class ProgressCounter:
    def __init__(self):
        self._thread: Thread = None
        self._lock = Lock()
        self._stop_event = Event()
        self._stop_event.set()
        self._call_count = 0

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

    def increment_call_count(self, value: int = 1):
        self._call_count += value

    @property
    def call_count(self):
        return self._call_count

    def _progress_counter_loop(self):
        while not self._stop_event.wait(0.1):
            print(f'Calculated {self._call_count} expressions')
