"""Agent Registry - Dynamic agent discovery, registration, and dependency management."""
from typing import Type
from app.agents.base_agent import BaseAgent


class AgentCapability:
    """Declares what context fields an agent requires and produces."""
    
    def __init__(
        self,
        agent_class: Type[BaseAgent],
        required_fields: list[str],
        optional_fields: list[str],
        produces_fields: list[str],
        depends_on: list[str] = None,
        priority: int = 0,
    ):
        self.agent_class = agent_class
        self.required_fields = required_fields
        self.optional_fields = optional_fields
        self.produces_fields = produces_fields
        self.depends_on = depends_on or []
        self.priority = priority  # Higher = runs first


class AgentRegistry:
    """Registry for dynamically discovering and managing agents.
    
    Agents register themselves with their capability declarations.
    The orchestrator uses this to determine which agents to run
    based on available context and dependency ordering.
    """
    
    def __init__(self):
        self._registry: dict[str, AgentCapability] = {}
    
    def register(self, name: str, capability: AgentCapability):
        """Register an agent with its capability declaration."""
        self._registry[name] = capability
    
    def get_runnable_agents(self, context: dict) -> list[str]:
        """Return agents whose required fields are satisfied by context."""
        runnable = []
        for name, cap in self._registry.items():
            if all(field in context for field in cap.required_fields):
                runnable.append(name)
        return runnable
    
    def get_execution_order(self, agent_names: list[str]) -> list[list[str]]:
        """Return agents grouped into execution waves based on dependencies.
        
        Wave 1: agents with no dependencies
        Wave 2: agents depending on Wave 1 outputs
        ... and so on (topological sort)
        """
        waves = []
        resolved = set()
        remaining = set(agent_names)
        
        while remaining:
            wave = []
            for name in list(remaining):
                cap = self._registry[name]
                if all(dep in resolved for dep in cap.depends_on if dep in agent_names):
                    wave.append(name)
            
            if not wave:
                # Circular dependency — run all remaining
                wave = list(remaining)
            
            for name in wave:
                remaining.discard(name)
                resolved.add(name)
            
            waves.append(sorted(wave, key=lambda n: -self._registry[n].priority))
        
        return waves
    
    def get_capability(self, name: str) -> AgentCapability | None:
        return self._registry.get(name)
    
    def list_agents(self) -> list[str]:
        return list(self._registry.keys())
