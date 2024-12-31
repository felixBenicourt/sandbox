import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_id():
    id_number = random.randint(00000, 99999)
    logging.info(f"PIPE ID TICKET: TDSD-{id_number}")
    return id_number

id_number = generate_id()
