from contextlib import contextmanager


@contextmanager
def notification(subject, *args, **kwargs):
    try:
        yield subject(*args, **kwargs)
    finally:
        pass

@contextmanager
def notification_before(subject, *args, **kwargs):
    try:
        subject.notify(*args, **kwargs)
        yield
    finally:
        pass

@contextmanager
def notification_after(subject, *args, **kwargs):
    try:
        yield
    finally:
        subject.notify(*args, **kwargs)

