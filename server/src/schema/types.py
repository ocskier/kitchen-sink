from typing import List, Optional
import strawberry

@strawberry.type
class TimeResult: 
    time: Optional[float]
    success: bool
    errors: Optional[List[str]]

@strawberry.type
class ConnectResult:
    msg: Optional[str]
    success: bool
    errors: Optional[List[str]]
