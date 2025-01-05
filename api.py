from fastapi import FastAPI
from routers import vectors, matrices, primes, geometry, triangle_solver, irrationals, cas

app = FastAPI(title="The Elephant Calculator API")

app.include_router(vectors.router, prefix="/vectors", tags=["Vectors"])
app.include_router(matrices.router, prefix="/matrices", tags=["Matrices"])
app.include_router(primes.router, prefix="/primes", tags=["Prime Numbers"])
app.include_router(geometry.router, prefix="/geometry", tags=["Geometry"])
app.include_router(triangle_solver.router, prefix="/triangles", tags=["Triangle Solver"])
app.include_router(irrationals.router, prefix="/irrationals", tags=["High-Precision"])
app.include_router(cas.router, prefix="/cas", tags=["CAS"])

# For testing purposes
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
