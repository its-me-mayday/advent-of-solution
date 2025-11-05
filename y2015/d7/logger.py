# logger.py
"""
Logger unico per progetti Python.
- LOG_LEVEL=DEBUG|INFO|WARNING|ERROR|CRITICAL   (default: INFO)
- LOG_FORMAT=text|json                          (default: text)
- LOG_DATEFMT=... (strftime)                    (default: %Y-%m-%dT%H:%M:%S%z)
- LOG_NAME=app                                  (default: app)
"""
from __future__ import annotations
import json
import logging
import os
import sys
from datetime import datetime, timezone
from typing import Any, Dict

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        event: Dict[str, Any] = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        std_keys = {
            "name","msg","args","levelname","levelno","pathname","filename","module",
            "exc_info","exc_text","stack_info","lineno","funcName","created","msecs",
            "relativeCreated","thread","threadName","processName","process",
        }
        extras = {k: v for k, v in record.__dict__.items() if k not in std_keys}
        if extras:
            event.update(extras)
        if record.exc_info:
            event["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(event, ensure_ascii=False)

def _text_formatter() -> logging.Formatter:
    fmt = os.getenv("LOG_FMT", "%(asctime)s %(levelname)s %(name)s: %(message)s")
    datefmt = os.getenv("LOG_DATEFMT", "%Y-%m-%dT%H:%M:%S%z")
    return logging.Formatter(fmt=fmt, datefmt=datefmt)

_configured = False

def get_logger(name: str | None = None) -> logging.Logger:
    global _configured
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    fmt = os.getenv("LOG_FORMAT", "text").lower()
    default_name = os.getenv("LOG_NAME", "app")
    logger_name = name or default_name

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    if not _configured:
        root = logging.getLogger()
        for h in list(root.handlers):
            root.removeHandler(h)

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter() if fmt == "json" else _text_formatter())
        root.addHandler(handler)
        root.setLevel(level)
        _configured = True

    logger.propagate = True  # lasciamo al root il singolo handler
    return logger

if __name__ == "__main__":
    log = get_logger("demo")
    log.debug("debug message (vedrai solo se LOG_LEVEL=DEBUG)")
    log.info("service started", extra={"service": "demo", "version": "0.1.0"})
    try:
        1/0
    except ZeroDivisionError:
        log.exception("failure computing result", extra={"op": "division"})
