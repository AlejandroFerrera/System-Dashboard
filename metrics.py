import psutil
from typing import Dict


class Metrics:
    """Class to gather system metrics using psutil."""

    @staticmethod
    def get_cpu_usage_by_core(interval: float = 1.0) -> Dict[str, float]:
        """
        Get the CPU usage percentage over a specified interval.

        :param interval: Interval over which to calculate CPU usage.
        :return: CPU usage percentage by core or total.
        """
        cpu_usage = psutil.cpu_percent(interval=interval, percpu=True)

        return {f"core_{i}": usage for i, usage in enumerate(cpu_usage)}

    @staticmethod
    def get_cpu_usage(interval: float = 1.0) -> float:
        """
        Get the total CPU usage percentage over a specified interval.

        :param interval: Interval over which to calculate CPU usage.
        :return: Total CPU usage percentage.
        """
        return psutil.cpu_percent(interval=interval)

    @staticmethod
    def get_memory_info() -> Dict[str, float]:
        """
        Get the system's virtual memory information.

        :return: Dictionary with memory information.
        """
        memory_usage = psutil.virtual_memory()

        return {
            "total": memory_usage.total,
            "available": memory_usage.available,
            "percent": memory_usage.percent,
            "used": memory_usage.used,
            "free": memory_usage.free,
        }
