from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routers import vectors, matrices, primes, geometry, triangle_solver, irrationals, cas, pythagorean

app = FastAPI(title="The Elephant Calculator API", docs_url="/api/docs", redoc_url="/api/redoc")

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
    status_code = 400 if isinstance(exc, ValueError) else 500
    error_type = ''.join([' ' + char if char.isupper() else char for char in exc.__class__.__name__]).strip()
    return JSONResponse(
        status_code=status_code,
        content={
            "detail": str(exc),
            "error_type": error_type,
            "path": str(request.url)
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
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
