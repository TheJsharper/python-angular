from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Project 00",
    description="A simple FastAPI application for demonstration purposes.",
    version="1.0.0",
)

list_technologies = [
    {
        "id": 1,
        "title": "Python",
        "description": "A high-level programming language.",
        "content": "Python is widely used in web development, data science, and AI.",
    },
    {
        "id": 2,
        "title": "FastAPI",
        "description": "A modern web framework for building APIs with Python.",
        "content": "FastAPI is based on standard Python type hints and offers automatic docs.",
    },
    {
        "id": 3,
        "title": "Django",
        "description": "A high-level Python web framework.",
        "content": "Django follows the MTV pattern and includes a built-in ORM.",
    },
    {
        "id": 4,
        "title": "Angular",
        "description": "A TypeScript-based front-end framework by Google.",
        "content": "Angular uses components, modules, and services to build SPAs.",
    },
    {
        "id": 5,
        "title": "TypeScript",
        "description": "A strongly typed superset of JavaScript.",
        "content": "TypeScript compiles to plain JavaScript and adds optional static typing.",
    },
    {
        "id": 6,
        "title": "PostgreSQL",
        "description": "An open-source relational database system.",
        "content": "PostgreSQL supports advanced data types and performance optimization.",
    },
    {
        "id": 7,
        "title": "Docker",
        "description": "A platform for developing and running containerized applications.",
        "content": "Docker uses containers to bundle code and dependencies together.",
    },
    {
        "id": 8,
        "title": "Redis",
        "description": "An in-memory data structure store.",
        "content": "Redis is used as a database, cache, and message broker.",
    },
    {
        "id": 9,
        "title": "Git",
        "description": "A distributed version control system.",
        "content": "Git tracks changes in source code and enables collaboration.",
    },
    {
        "id": 10,
        "title": "Linux",
        "description": "An open-source Unix-like operating system kernel.",
        "content": "Linux powers the majority of web servers and cloud infrastructure.",
    },
]


@app.get("/")
async def read_root():
    return {"message": "Welcome to Project 00!"}


@app.get("/technologies")
async def get_technologies(
    query: str = Query(None, description="Filter technologies by title or description")
):
    if query:
        filtered_technologies = [
            tech
            for tech in list_technologies
            if query.lower() in tech["title"].lower()
            or query.lower() in tech["description"].lower()
        ]
        return {"technologies": filtered_technologies}
    return {"technologies": list_technologies}


@app.get("/technologies/{technology_id}")
async def get_technology_by_id(technology_id: int, include_content: bool = Query(True, description="Include content in the response")):
    if technology_id <= 0:
        return JSONResponse(content={"error": "Invalid technology ID"}, status_code=400)

    if technology_id > len(list_technologies):
        return JSONResponse(content={"error": "Technology not found"}, status_code=404)

    technology = next(
        (tech for tech in list_technologies if tech["id"] == technology_id), None
    )

    if technology:
        if not include_content:
            technology = {key: value for key, value in technology.items() if key != "content"}

        return {"technology": technology}
    return JSONResponse(content={"error": "Technology not found"}, status_code=404)
