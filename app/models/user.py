from dataclasses import dataclass
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class User(BaseModel):
    user_id: Optional[UUID] = None  
    email: str
    username: str
    user_password: str
    phone_number: Optional[str] = None
    profile_pic_url: Optional[str] = None
    metadata: Optional[Dict] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None