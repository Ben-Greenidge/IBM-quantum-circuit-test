import os

from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    token=os.environ["api_key"],
    instance=os.environ["crn"],
)
