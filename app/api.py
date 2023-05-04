from fastapi import FastAPI
from mangum import Mangum
from copykitt import generate_keywords_openai_api_call
from copykitt import generate_snippet_openai_api_call


app = FastAPI()

handler = Mangum(app)


@app.get("/generate_snippet")
async def generate_snippet_api_endpoint(prompt: str):
    snippet = generate_snippet_openai_api_call(prompt)
    return {f'Snippet: {snippet}'}


@app.get("/generate_keyword")
async def generate_keyword_api_endpoint(prompt: str):
    keyword = generate_keywords_openai_api_call(prompt)
    return {f'Keywords: {keyword}'}


@app.get("/generate_copykitt_output")
async def copykitt_api_endpoint(prompt: str):
    keyword = generate_keywords_openai_api_call(prompt)
    snippet = generate_snippet_openai_api_call(prompt)
    return {f'Keywords: {keyword} Snippet: {snippet}'}


# todo
# parameter validation, > pydantics
    # https://www.tutorialspoint.com/fastapi/fastapi_parameter_validation.htm

# DB integration for statistiken der app,

# middleware
#   https://www.tutorialspoint.com/fastapi/fastapi_middleware.htm

# events(boot)
#   https://www.tutorialspoint.com/fastapi/fastapi_event_handlers.htm

# uvicorn api:app --reload
