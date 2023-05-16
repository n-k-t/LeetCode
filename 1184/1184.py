class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # Check if the start and destination are equal, return zero if they are. If not, and 
        # the start is at a later index than the destination, then swap the start and destination. 
        # This allows the list to always be sliced properly.
        if start == destination:
            return 0
        elif start > destination:
            start, destination = destination, start

        # Slices that follow the bus route clockwise or counterclockwise.
        cw = sum(distance[start:destination])
        ccw = sum(distance[destination:] + distance[:start])

        # Return the minimum length route. 
        return min(cw, ccw)