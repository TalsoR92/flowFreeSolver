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


class Opti:
    """
    A class to represent the optimization settings
    """
    def __init__(self, 
                 check_reachable: CheckReachable = CheckReachable.NONE, 
                 reachability_check_method: ReachabilityCheckMethod = ReachabilityCheckMethod.DFS):
        
        if not isinstance(check_reachable, CheckReachable): # Validate if check_reachable is a valid value from the CheckReachable enumeration
            raise ValueError("check_reachable must be a value from the CheckReachable enumeration")
            
        if not isinstance(reachability_check_method, ReachabilityCheckMethod): # Validate if reachability_check_method is a valid value from the ReachabilityCheckMethod enumeration
            raise ValueError("reachability_check_method must be a value from the ReachabilityCheckMethod enumeration")
        
        self.check_reachable = check_reachable
        self.reachability_check_method = reachability_check_method