# Convert celcius to fahrenheit

import sys
import logging
logging.basicConfig(
    filename="c2f_batch.log",
    level=logging.DEBUG
)

try:
    c = float(sys.argv[1])
    f = c * 9 / 5 + 32
    print(f"{c} celcius is {f} fahrenheit.")
    logging.info(f"{c} celcius is {f} fahrenheit.")

except ValueError:
    logging.exception(f"ERROR!: {sys.argv[1]} is not an number")

