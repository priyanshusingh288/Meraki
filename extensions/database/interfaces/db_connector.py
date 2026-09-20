from abc import ABC, abstractmethod
from typing import Any ,dict,list,Optional,Tuple

class databaseConnecter(ABC):
    """abstract base class for db connection"""

    @abstractmethod
    async def connect(self) -> None:
        """connection or intialize th econnection from here to the database"""
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """diconnect all connection to the databse or connection pool"""

        pass

    @abstractmethod
    async def execute(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> Any:
        """opertions like insert delete and update"""

        pass

    @abstractmethod
    async def fetch_all(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> list[dict[str, Any]]:
        """Execute a read query and return all matching records as a list of dictionaries.
        return: list of dicts mapping the rows and columns"""
        pass

    @abstractmethod
    async def fetch_one(self, query: str, params: Optional[tuple] = None) -> Optional[dict[str, Any]]:
        """Execute a read query and return the first matching record."""
        pass