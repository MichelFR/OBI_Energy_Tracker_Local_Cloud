"""Discover nearby OBI Bluetooth Low Energy devices."""
import asyncio
from bleak import BleakScanner

async def scan() -> int:
    """Scan for five seconds and list devices whose name starts with ``OBI-``."""
    timeout_seconds = 5
    print(f"Scanning for Bluetooth devices for {timeout_seconds} seconds:")

    devices = await BleakScanner.discover(timeout=timeout_seconds)
    obi_devices = [device for device in devices if device.name and device.name.startswith("OBI-")]

    for device in obi_devices:
        print(device)

    if not obi_devices:
        print("No OBI devices found")
    else:
        print(f"Found {len(obi_devices)} OBI device(s)")

    return 0

if __name__ == "__main__":
    raise SystemExit(asyncio.run(scan()))
