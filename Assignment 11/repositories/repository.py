from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")   # Entity type
ID = TypeVar("ID") # ID type (int or str)


class Repository(ABC, Generic[T, ID]):
    """
    Generic Repository Interface for CRUD operations.
    
    This abstracts storage details behind an interface, allowing us to easily
    swap between in-memory, database, filesystem, etc.
    """
    
    @abstractmethod
    def save(self, entity: T) -> None:
        """Create or Update an entity"""
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find entity by ID"""
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """Return all entities"""
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete entity by ID"""
        pass