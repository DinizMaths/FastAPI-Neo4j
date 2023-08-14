from fastapi  import FastAPI, HTTPException
from database import driver


app = FastAPI()


def execute_query(query):
  with driver.session() as session:
    result = session.run(query)

    return result.data()


@app.get("/")
def read_root():
  return {"message": "Welcome to FastAPI with Neo4j integration!"}

@app.get("/execute-query/{query}")
def execute_query_endpoint(query: str):
  try:
    result = execute_query(query)

    return {"result": result}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))