from enum import Enum

class CheckReachable(Enum):
    """
    Enumeration for different conditions when the reachability check is performed
    """
    NONE = 0               # No reachability check
    END_PATH = 1           # Check at the end of the path
    NEAR_2_POINTS = 2      # Check when near 2 points
    NEAR_3_THINGS = 3      # Check when near 3 points or borders
    EVERY_CASE = 4         # Check at every case/position

class ReachabilityCheckMethod(Enum):
    """
    Enumeration for different methods to check reachability
    """
    DFS = 0                 # Use Depth-First Search (DFS) for reachability check
    SHORTEST_PATH_FIRST = 1 # Check using the shortest path first
    
class PathTestingOrder(Enum):
    """
    Enumeration for different orders to test paths
    """
    NORMAL = 0              # Test paths in the normal order
    ASCENDING = 1           # Test paths in ascending order
    DESCENDING = 2          # Test paths in descending order

class BorderCellAccessibility(Enum):
    """
    Enumeration for different conditions when checking edge cell accessibility
    """
    NONE = 0                # No check for edge cell accessibility
    CHECK = 1               # Check edge cell accessibility

class SurroundingCellBlockedCheck(Enum):
    """
    Enumeration for different conditions when checking if surrounding cells are blocked
    """
    NONE = 0                # No check for surrounding cell blocked
    CHECK = 1               # Check if surrounding cells are blocked

class Opti:
    """
    A class to represent the optimization settings
    """
    def __init__(self, 
                 check_reachable: CheckReachable = CheckReachable.NONE, 
                 reachability_check_method: ReachabilityCheckMethod = ReachabilityCheckMethod.DFS,
                 path_testing_order: PathTestingOrder = PathTestingOrder.NORMAL,
                 border_cell_accessibility: BorderCellAccessibility = BorderCellAccessibility.NONE,
                 surrounding_cell_blocked_check: SurroundingCellBlockedCheck = SurroundingCellBlockedCheck.NONE):
        
        if not isinstance(check_reachable, CheckReachable): # Validate if check_reachable is a valid value from the CheckReachable enumeration
            raise ValueError("check_reachable must be a value from the CheckReachable enumeration")
            
        if not isinstance(reachability_check_method, ReachabilityCheckMethod): # Validate if reachability_check_method is a valid value from the ReachabilityCheckMethod enumeration
            raise ValueError("reachability_check_method must be a value from the ReachabilityCheckMethod enumeration")
        
        if not isinstance(path_testing_order, PathTestingOrder): # Validate if path_testing_order is a valid value from the PathTestingOrder enumeration
            raise ValueError("path_testing_order must be a value from the PathTestingOrder enumeration")
        
        if not isinstance(border_cell_accessibility, BorderCellAccessibility): # Validate if border_cell_accessibility is a valid value from the BorderCellAccessibility enumeration
            raise ValueError("border_cell_accessibility must be a value from the BorderCellAccessibility enumeration")
            
        if not isinstance(surrounding_cell_blocked_check, SurroundingCellBlockedCheck): # Validate if surrounding_cell_blocked_check is a valid value from the SurroundingCellBlockedCheck enumeration
            raise ValueError("surrounding_cell_blocked_check must be a value from the SurroundingCellBlockedCheck enumeration")
        
        self.check_reachable = check_reachable
        self.reachability_check_method = reachability_check_method
        self.path_testing_order = path_testing_order
        self.border_cell_accessibility = BorderCellAccessibility.NONE
        self.surrounding_cell_blocked_check = SurroundingCellBlockedCheck.NONE