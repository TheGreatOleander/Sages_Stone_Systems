from sages_stone_runtime.provenance.metadata import SystemMetadata

meta = SystemMetadata(name="demo_system", version="1.0.0", author="Builder")
fp = meta.fingerprint()
print(f"System fingerprint: {fp}")
