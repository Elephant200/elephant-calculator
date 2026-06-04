"""Vercel Python serverless entrypoint for the Elephant Calculator API.

Vercel's Python runtime serves the module-level ASGI ``app``. Because this is a
uv/pnpm monorepo, the API and its calculator package live under workspace
``src`` directories rather than being pip-installed, so we add them to the
import path here. ``requirements.txt`` (repo root) provides the third-party
dependencies, and ``vercel.json`` bundles the source via ``includeFiles``.
"""

import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _src in ("apps/api/src", "packages/calculator/src"):
    _path = os.path.join(_ROOT, _src)
    if _path not in sys.path:
        sys.path.insert(0, _path)

from elephant_calculator_api.main import app  # noqa: E402

# Re-exported for the Vercel Python runtime.
__all__ = ["app"]
