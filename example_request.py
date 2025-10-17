import requests

API_URL = "http://127.0.0.1:8000/predict"

# Sample payload matching all required model features.
PAYLOAD = {
    "inflacion_cl": 4.1,
    "inflacion_us": 2.4,
    "tpm_cl": 6.25,
    "tpm_us": 4.0,
    "ipc_cl": 120.5,
    "ipc_us": 130.8,
    "sp500": 4300.6,
    "ipsa": 5200.1,
    "tpm_cl_cat": 2,
    "tpm_us_cat": 1,
    "tpm_cl_is_0": 0,
    "tpm_us_is_0": 0,
    "tpm_cl_is_1": 1,
    "tpm_us_is_1": 0,
    "tpm_cl_is_2": 0,
    "tpm_us_is_2": 1,
    "tpm_cl_change": 0.15,
    "tpm_us_change": -0.1,
    "new_max_sp500": 0,
    "new_max_ipsa": 1,
    "new_max_usdclp": 0,
    "tpm_diff": 1.25,
    "tpm_diff_pos": 1,
}


def main() -> None:
    response = requests.get(API_URL, params=PAYLOAD, timeout=10)
    response.raise_for_status()
    print(response.json())


if __name__ == "__main__":
    main()
