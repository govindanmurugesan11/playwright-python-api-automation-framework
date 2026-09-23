"""
Topic: Logging

Used in automation frameworks
for execution tracking.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Test execution started")

logging.warning("Browser is slow")

logging.error("Login failed")

# Output Example:
# 2026-09-22 10:30:15,123 - INFO - Test execution started
# 2026-09-22 10:30:15,124 - WARNING - Browser is slow
# 2026-09-22 10:30:15,125 - ERROR - Login failed