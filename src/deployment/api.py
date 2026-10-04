from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title='Steel Inspection Vision AI')

class Health(BaseModel):
    service: str='steel-inspection'
    status: str='ok'

@app.get('/health',response_model=Health)
def health(): return Health()
