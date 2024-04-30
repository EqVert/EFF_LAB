## Об'єднаємо розрахунок загальної суми та кількості елементів даних,
## які використовуються у методах calculate_total та calculate_average.

class DataAnalyzer:
  def __init__(self, data):
    self.data = data
    self._total = None
    self._count = None

  def _ensure_calculated(self):
    if self._total is None or self._count is None:
      self._total = sum(self.data)
      self._count = len(self.data)

  def calculate_total(self):
    self._ensure_calculated()
    return self._total

  def calculate_average(self):
    self._ensure_calculated()
    return self._total / self._count if self._count else 0

  def calculate_minimum(self):
    return min(self.data) if self.data else None

  def calculate_maximum(self):
    return max(self.data) if self.data else None