# OrbitCrate Bridge

Telemetry bridge between OrbitCrate sensor rigs and the warehouse.

`catalog_ref: orbitcrate` - this repository backs the capability-registry entry
`catalog/orbitcrate.md`.

## Availability

Integration partners run trial builds under the vendor agreement. Promotion to
the public channel is handled by the OrbitCrate launch program; `main` tracks
internal development only. The authoritative channel state is committed by CI
in `distribution.json`.

## Layout

- `src/` bridge and protocol adapters
- `tests/` unit tests
- `results/` field notes
