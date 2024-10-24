from pydantic import BaseModel


class InputData(BaseModel):
    Sex: str
    Length: float
    Diameter: float
    Height: float
    Whole_height: float
    Shucked_weight: float
    Viscera_weight: float
    Shell_weight: float


class PredictionOut(BaseModel):
    age: float
