from pydantic import BaseModel, Field
from typing import Annotated

class Ollama_driving(BaseModel):

    age: Annotated[int, Field(
        ..., 
        gt=0, lt=100, 
        description="Enter Age (1-99).", 
        examples=[21]
    )]

    gender: Annotated[int, Field(
        ..., 
        ge=0, le=1, 
        description="Gender (0 = Female, 1 = Male).", 
        examples=[0]
    )]

    day: Annotated[int, Field(
        ..., 
        ge=1, le=31, 
        description="Joining Day (1-31).", 
        examples=[24]
    )]

    month: Annotated[int, Field(
        ..., 
        ge=1, le=12, 
        description="Joining Month (1-12).", 
        examples=[12]
    )]

    year: Annotated[int, Field(
        ..., 
        ge=1990, le=2026, 
        description="Joining Year (1990-2026).", 
        examples=[2018]
    )]

    education_level: Annotated[int, Field(
        ..., 
        ge=0, le=5, 
        description="Education Level (0-5).", 
        examples=[2]
    )]

    income: Annotated[int, Field(
        ..., 
        ge=0, le=1000000, 
        description="Income (0 - 10L).", 
        examples=[57387]
    )]

    joining_designation: Annotated[int, Field(
        ..., 
        ge=0, le=10, 
        description="Joining Designation Level (0-10).", 
        examples=[1]
    )]

    grade: Annotated[int, Field(
        ..., 
        ge=0, le=10, 
        description="Grade Level (0-10).", 
        examples=[1]
    )]

    total_business_value: Annotated[int, Field(
        ..., 
        ge=0, 
        description="Total Business Value (>=0).", 
        examples=[665480]
    )]

    quarterly_rating: Annotated[int, Field(
        ..., 
        ge=1, le=5, 
        description="Quarterly Rating (1-5).", 
        examples=[2]
    )]