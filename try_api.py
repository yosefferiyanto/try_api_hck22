from fastapi import FastAPI, HTTPException

app = FastAPI()

data = {"name": "shopping cart",
        "columns": ["prod_name", "price", "num_items"],
        "items": {}}


@app.get("/")
def root():
    return {"message": "Welcome to Toko H8 Shopping Cart! There are some features that you can explore",
            "menu": {1: "See shopping cart (/cart)",
                     2: "Add item (/add) - You may need request",
                     3: "Edit shopping cart (/edit/id)",
                     4: "Delete item from shopping cart (/del/id)",
                     5: "Calculate total price (/total)",
                     6: "Exit (/exit)"}
            }


@app.get("/cart")
def show():
    return data


@app.post("/add")
def add_item(added_item: dict):
    id = len(data["items"].keys()) + 1
    data["items"][id] = added_item
    return f"Item successfully added into your cart with ID {id}"


@app.put("/edit/{id}")
def update_cart(id: int, updated_cart: dict):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        data["items"][id].update(updated_cart)
        return {"message": f"Item with ID {id} has been updated successfully."}


@app.delete("/del/{id}")
def remove_row(id: int):
    if id not in data['items'].keys():
        raise HTTPException(status_code=404, detail=f"Item with ID {id} not found")
    else:
        data["items"].pop(id)
        return {"message": f"Item with ID {id} has been deleted successfully."}


@app.get("/total")
def get_total():
    # Calculate total price by iterating through items and summing "price" values
    total_price = sum(item["price"] * item["num_items"] for item in data["items"].values())
    return {"total_price": total_price}


@app.get("/exit")
def exit():
    return {"message": "Thank you for using Toko H8 Shopping Cart! See you next time."}