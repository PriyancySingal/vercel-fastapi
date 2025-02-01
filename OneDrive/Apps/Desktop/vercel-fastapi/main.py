from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock marks data for the students
student_marks = {
    "Alice": 90,
    "Bob": 80,
    "Charlie": 70,
    "David": 60,
    "Eve": 85,
}

@app.get("/api")
def get_marks(name: list[str]):
    marks = [student_marks.get(n, "Not Found") for n in name]
    return JSONResponse(content={"marks": marks})
