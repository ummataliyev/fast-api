import fastapi

app = fastapi.FastAPI()


@app.get('/')
async def get():
    return {'message': 'Hello World'}


@app.post('/')
async def post():
    return {'message': 'Hello World again with Post Request'}


@app.put('/')
async def put():
    return {'message': 'Hello World again with Put Request'}


@app.get('/items')
async def list_items():
    return {'message': "List Items Route!"}


@app.get('/items/{item_id}')
async def get_item(item_id: int):
    return {'message': f"Item ID: {item_id}"}
