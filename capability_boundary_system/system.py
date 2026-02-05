from .schema import CapabilityBoundary

class CapabilityBoundarySystem:
    name = "capability_boundary_system"

    def boundaries(self) -> CapabilityBoundary:
        return CapabilityBoundary(prohibited_capabilities=set())
