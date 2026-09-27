from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id":101, "name":"Harsh", "city": "Bengaluru", "risk":"low"},
    {"id":102, "name":"John snow", "city": "Winterfell", "risk":"Moderate"},
    {"id":103, "name":"Dexter", "city": "California", "risk":"High"},
    {"id":104, "name":"Jake Reacher", "city": "Dallas", "risk":"High"},
]

@app.get("/customers")
def get_customer(city:str, risk:str):
    filtered = [
        c for c in all_customers
        if c["city"] == city and c["risk"] == risk
    ]
    return {
        "city":city,
        "risk":risk,
        "count": len(filtered),
        "results":filtered,
    }