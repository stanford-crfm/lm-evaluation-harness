import logging
import os


<<<<<<< HEAD
__version__ = "0.4.9"
=======
__version__ = "0.4.9.1"
>>>>>>> de496b80d60c267a2d7eea3b3c1dc40f693daee7


# Lazy-load .evaluator module to improve CLI startup
def __getattr__(name):
    if name == "evaluate":
        from .evaluator import evaluate

        return evaluate
    elif name == "simple_evaluate":
        from .evaluator import simple_evaluate

        return simple_evaluate
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = ["evaluate", "simple_evaluate", "__version__"]
