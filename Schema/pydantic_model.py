from pydantic import BaseModel,Field
from typing import Annotated

class Ollama_driving(BaseModel):
    age : Annotated[int,Field(...,description="Enter the Age.",examples=[21])]
    gender: Annotated[int, Field(..., description="Enter Gender (0 = Female, 1 = Male).", examples=[0])]
    day: Annotated[int, Field(..., description="Enter Joining Day (1-31).", examples=[24])]
    month: Annotated[int, Field(..., description="Enter Joining Month (1-12).", examples=[12])]
    year: Annotated[int, Field(..., description="Enter Joining Year.", examples=[2018])]
    education_level: Annotated[int, Field(..., description="Enter Education Level.", examples=[2])]
    income: Annotated[int, Field(..., description="Enter Income.", examples=[57387])]
    joining_designation: Annotated[int, Field(..., description="Enter Joining Designation.", examples=[1])]
    grade: Annotated[int, Field(..., description="Enter Grade.", examples=[1])]
    total_business_value: Annotated[int, Field(..., description="Enter Total Business Value.", examples=[665480])]
    quarterly_rating: Annotated[int, Field(..., description="Enter Quarterly Rating (1-5).", examples=[2])]