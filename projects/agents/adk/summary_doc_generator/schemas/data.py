from pydantic import BaseModel, Field

class personal_data(BaseModel):
    name : str = Field(description="the user name")
    email: str = Field(description="The user email")

class complete_data(BaseModel):
    user_data : personal_data = Field(description="The user information")
    problem : str = Field(description="the user problem")
    tips : str = Field(description="Tips for solve the problem")