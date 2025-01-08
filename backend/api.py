from fastapi import FastAPI, Request
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
    print(f"Exception type: {type(exc)}")  # Debugging output
    print(f"{exc}")
    print(f"Request path: {request.url}")
    status_code = 400 if isinstance(exc, ValueError) else 500
    return JSONResponse(
        status_code=status_code,
        content={
            "detail": str(exc),
            "error_type": exc.__class__.__name__,
            "path": str(request.url)
        },
    )

# For testing purposes
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
