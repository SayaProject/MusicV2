#!/usr/bin/env python3
from config import Config, strtobool
from os import environ

# Set required env vars first to avoid check() errors
environ["API_ID"] = "17596251"
environ["API_HASH"] = "test_hash"
environ["BOT_TOKEN"] = "test_token"
environ["MONGO_URL"] = "mongodb://test"
environ["LOGGER_ID"] = "12345"
environ["OWNER_ID"] = "12345"
environ["SESSION"] = "test_session"

# Test strtobool helper
print("Testing strtobool helper:")
test_cases = [
    ("true", True),
    ("yes", True),
    ("y", True),
    ("1", True),
    ("on", True),
    ("TRUE", True),
    ("YES", True),
    ("false", False),
    ("no", False),
    ("n", False),
    ("0", False),
    ("off", False),
    ("FALSE", False),
    ("NO", False),
]
for val, expected in test_cases:
    result = strtobool(val)
    print(f"strtobool('{val}') → {result} (expected {expected}) {'✓' if result == expected else '✗'}")

print()
print("Testing Config class:")

# Test 1: Default values (no env vars set)
print("\nTest 1: Default values")
environ.pop("AUTO_END", None)
environ.pop("AUTO_LEAVE", None)
environ.pop("VIDEO_PLAY", None)
config = Config()
print(f"AUTO_END: {config.AUTO_END} (should be False)")
print(f"AUTO_LEAVE: {config.AUTO_LEAVE} (should be False)")
print(f"VIDEO_PLAY: {config.VIDEO_PLAY} (should be True)")
assert config.AUTO_END is False
assert config.AUTO_LEAVE is False
assert config.VIDEO_PLAY is True
print("✓ Test 1 passed!")

# Test 2: True values
print("\nTest 2: True values")
environ["AUTO_END"] = "true"
environ["AUTO_LEAVE"] = "yes"
environ["VIDEO_PLAY"] = "1"
config = Config()
print(f"AUTO_END: {config.AUTO_END} (should be True)")
print(f"AUTO_LEAVE: {config.AUTO_LEAVE} (should be True)")
print(f"VIDEO_PLAY: {config.VIDEO_PLAY} (should be True)")
assert config.AUTO_END is True
assert config.AUTO_LEAVE is True
assert config.VIDEO_PLAY is True
print("✓ Test 2 passed!")

# Test 3: False values
print("\nTest 3: False values")
environ["AUTO_END"] = "false"
environ["AUTO_LEAVE"] = "no"
environ["VIDEO_PLAY"] = "0"
config = Config()
print(f"AUTO_END: {config.AUTO_END} (should be False)")
print(f"AUTO_LEAVE: {config.AUTO_LEAVE} (should be False)")
print(f"VIDEO_PLAY: {config.VIDEO_PLAY} (should be False)")
assert config.AUTO_END is False
assert config.AUTO_LEAVE is False
assert config.VIDEO_PLAY is False
print("✓ Test 3 passed!")

print("\n✅ All tests passed!")

