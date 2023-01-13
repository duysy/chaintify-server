class Config:
    BASE_DOMAIN = ""

    HOST = 'db'
    USER = 'root'
    NAME = 'django'
    PASSWORD = 'django'
    PORT = '5432'

    # HOST = 'localhost'
    # BASE_GETAWAY = "https://8285-2a09-bac1-7ac0-30-00-19b-18e.ap.ngrok.io/ipfs"
    # URL_API_IPFS = "/ip4/127.0.0.1/tcp/5001"

    # BASE_GETAWAY = "https://8285-2a09-bac1-7ac0-30-00-19b-18e.ap.ngrok.io/ipfs"
    # URL_API_IPFS = "/dns/ipfs/tcp/5001/http"

    BASE_GETAWAY = "http://103.39.125.95:8080/ipfs"
    URL_API_IPFS = "/dns/ipfs/tcp/5001/http"

    ALCHEMY_KEY = "Gnp3tbW0Wp0tJpdhVz1ZRtB9bqgYG03O"
    CHAINTIFY_CONTRACT_ADDRESS = "0xab091A35E9bf7D997a1DF8961cE76A1edf4a4530"
    RPC_URL = f"https://polygon-mumbai.g.alchemy.com/v2/{ALCHEMY_KEY}"
