from nada_dsl import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("telemetry")

def nada_main():
    telemetry_id = "telemetry_id_123"
    logger.info(f"Telemetry enabled with ID: {telemetry_id}")
    
    party1 = Party(name="Party1")
    
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    sum_int = my_int1 + my_int2
    
    return [
        Output(sum_int, "sum_output", party1)
    ]

nada_main()
