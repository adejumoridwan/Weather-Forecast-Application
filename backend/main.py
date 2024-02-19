from fastapi import FastAPI, HTTPException
import uvicorn

from model import convert, predict


app = FastAPI()


@app.post(
    "/predict",
    status_code=200,
)
async def get_prediction(weather_variable: str, days: int):
    prediction_list = predict(weather_variable, days)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "weather_variable": weather_variable,
        "forecast": convert(prediction_list),
    }
    return response_object


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
