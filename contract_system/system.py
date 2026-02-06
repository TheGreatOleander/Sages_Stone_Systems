from typing import FrozenSet

from .schema import ContractSchema
from .invariants import invariant_contracts_subset
from .lifecycle import ContractLifecycle


class ContractSystem:
    def __init__(self, schema: ContractSchema) -> None:
        self._schema = schema
        self._active_contracts: FrozenSet[str] = frozenset()
        self._lifecycle = ContractLifecycle()

    @property
    def active_contracts(self) -> FrozenSet[str]:
        return self._active_contracts

    def set_contracts(self, contracts: FrozenSet[str]) -> None:
        if not invariant_contracts_subset(
            contracts,
            self._schema.allowed_contracts,
        ):
            return
        self._active_contracts = contracts

    def has_contract(self, contract: str) -> bool:
        return contract in self._active_contracts
