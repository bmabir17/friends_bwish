from functools import wraps


def error_handle(logger):
    def decorator(func):
        @wraps(func)
        def _wrapped(self, *args, **kwargs):
            log = getattr(self, logger)
            log.info(f"-- Inside the wrapper for {func.__name__} --")
            try:
                return func(self, *args, **kwargs)
            except Exception:
                log.exception(f"--- Exception occurred at {func.__name__} --- ")
                raise Exception

        return _wrapped

    return decorator