import logging
import os

from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from elephant_calculator_api.routers import (
    cas,
    geometry,
    irrationals,
    matrices,
    primes,
    pythagorean,
    triangle_solver,
    vectors,
)

logger = logging.getLogger("elephant_calculator_api")

app = FastAPI(title="The Elephant Calculator API", docs_url="/api/docs", redoc_url="/api/redoc")

# Same-origin deployments use the Next.js proxy and need no CORS. To serve the
# API standalone to a browser on another origin, set ELEPHANT_CORS_ORIGINS to a
# comma-separated list of allowed origins (e.g. "https://app.example.com").
_cors_origins = [o.strip() for o in os.environ.get("ELEPHANT_CORS_ORIGINS", "").split(",") if o.strip()]
if _cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_cors_origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )

api_prefix = "/api"
app.include_router(vectors.router, prefix=f"{api_prefix}/vectors", tags=["Vectors"])
app.include_router(matrices.router, prefix=f"{api_prefix}/matrices", tags=["Matrices"])
app.include_router(primes.router, prefix=f"{api_prefix}/primes", tags=["Prime Numbers"])
app.include_router(geometry.router, prefix=f"{api_prefix}/geometry", tags=["Geometry"])
app.include_router(triangle_solver.router, prefix=f"{api_prefix}/triangles", tags=["Triangle Solver"])
app.include_router(irrationals.router, prefix=f"{api_prefix}/irrationals", tags=["High-Precision"])
app.include_router(cas.router, prefix=f"{api_prefix}/cas", tags=["CAS"])
app.include_router(pythagorean.router, prefix=f"{api_prefix}/pythagorean", tags=["Pythagorean Triple Generator"])

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # ValueErrors are the calculator's way of signalling bad input, so they
    # carry a helpful message and map to 400. Anything else is unexpected:
    # log the real error but return a generic message so internals don't leak.
    if isinstance(exc, ValueError):
        return JSONResponse(
            status_code=400,
            content={
                "detail": str(exc),
                "error_type": "Value Error",
                "path": str(request.url),
            },
        )

    logger.exception("Unhandled error while processing %s", request.url)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal error occurred while processing the request.",
            "error_type": "Internal Server Error",
            "path": str(request.url),
        },
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    message = "; ".join([err.get("msg", "Validation error") for err in exc.errors()])
    return JSONResponse(
        status_code=400,
        content={
            "detail": message,
            "error_type": "Validation Error",
            "path": str(request.url)
        },
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "error_type": f"HTTP {exc.status_code}",
            "path": str(request.url)
        },
    )

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={
            "detail": exc.detail,
            "error_type": "HTTP 404",
            "path": str(request.url)
        },
    )

# For testing purposes
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "elephant_calculator_api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
