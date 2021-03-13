from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()

# https method [ get,post,put,patch,delete]
# command database [find,insert,update,delete]


@app.get("/")  # select
def index():
    return JSONResponse(content={"message": "Hello,  World Pai"}, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)


@app.get("/profile/{name}/{age}")  # http://127.0.0.1:3000/profile/wiraphat/21
def get_path_parameter(name: str, age: int):  # get_path_parameter
    return JSONResponse(
        content={"message": f"My name is: {name} age {age}"},
        status_code=200,
    )


@app.get("/example/")  # http://127.0.0.1:3000/example/?start=2&limit=8&name=pai
def get_query_parameter(start: int = 0, limit: int = 0, name: str = ""):
    # get_query_parameter
    # กำหนดค่ากันใส่ค่าผิด
    print("start", start)
    print("limit", limit)
    print("name", name)

    return JSONResponse(
        content={"message": f"profile start: {start} limit: {limit} name: {name}"},
        status_code=200,
    )


@app.get("/books")  # ข้อมูลหนังสือทั้งหมด
def get_books():
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]
    # connect db
    # books = "select * from books"
    return JSONResponse(content={"status": "ok", "date": dict_books}, status_code=200)


@app.get("/books/{book_id}")  # เลือกมาเเค่อันเดียว
def get_books_by_id(book_id: int):
    book = {
        "book_id": 1,
        "book_name": "Harry Potter and Philosopher's Stone",
        "page": 223,
    }
    response = {"status": "ok", "data": book}
    return JSONResponse(content=response, status_code=200)


class createBookPayload(BaseModel):
    id: str
    name: str
    page: int


@app.post("/books")  # post = insert
def create_books(req_body: createBookPayload):
    req_body_dict = req_body.dict()

    id = req_body_dict["id"]
    name = req_body_dict["name"]
    page = req_body_dict["page"]
    book = {
        "id": id,
        "name": name,
        "page": page,
    }
    response = {"status": "ok", "data": book}
    return JSONResponse(content=response, status_code=200)


class updateBookPayload(BaseModel):
    name: str
    page: int


@app.patch("/books/{book_id}")  # update
def update_book_by_id(req_body: updateBookPayload, book_id: str):
    req_body_dict = req_body.dict()

    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print(f"name: {name}, page: {page}")

    update_message = f"Update book id {book_id} is complete !! "
    response = {"status": "ok", "data": update_message}
    return JSONResponse(content=response, status_code=200)


@app.delete("/books/{book_id}")  # delete
def delete_book_by_id(book_id: int):
    delete_message = f"Delete book id {book_id} is complete !! "
    response = {"status": "ok", "date": delete_message}
    return JSONResponse(content=response, status_code=200)
