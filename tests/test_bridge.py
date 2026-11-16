"""Bridge buffering behaviour."""
import asyncio

from orbitcrate.bridge import SensorBridge


class FakeWriter:
    def __init__(self):
        self.flushes = 0

    async def write(self, value):
        return None

    async def flush(self):
        self.flushes += 1

    async def close(self):
        return None


def test_flush_after_batch():
    writer = FakeWriter()
    bridge = SensorBridge(reader=None, writer=writer)
    bridge._buffered = 511
    asyncio.run(bridge.shutdown())
    assert writer.flushes == 1
