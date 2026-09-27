from fastapi import FastAPI

app = FastAPI()

customer_risk_profiles = {
    101: {"name":"Harsh", "risk":"low"},
    102: {"name":"John snow", "risk":"Moderate"},
    103: {"name":"Dexter", "risk":"High"},
}

@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id: int):
    if customer_id not in customer_risk_profiles:
        return {"error":f"customer {customer_id} not found"}

    profile = customer_risk_profiles[customer_id]

    return {
        "customer_id":customer_id,
        "name:" :profile["name"],
        "risk_level:" :profile["risk"],
    }

@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction(model_name:str, customer_id:int):
    return {
        "model":model_name,
        "customer_id": customer_id,
        "prediction": "high_risk",
    }