class Config:
    DEBUG = False
    BASE_DOMAIN = ""

    HOST_DB = 'db'
    USER_DB = 'root'
    NAME_DB = 'django'
    PASSWORD_DB = 'django'
    PORT_DB = '5432'

    # HOST_DB = 'localhost'
    # BASE_GETAWAY = "https://2200-171-255-132-157.ap.ngrok.io/ipfs"
    # URL_API_IPFS = "/ip4/127.0.0.1/tcp/5001"

    # BASE_GETAWAY = "https://8285-2a09-bac1-7ac0-30-00-19b-18e.ap.ngrok.io/ipfs"
    # URL_API_IPFS = "/dns/ipfs/tcp/5001/http"

    BASE_GETAWAY = "https://ipfs.chaintify.space/ipfs"
    URL_API_IPFS = "/dns/ipfs/tcp/5001/http"

    ALCHEMY_KEY = "Gnp3tbW0Wp0tJpdhVz1ZRtB9bqgYG03O"
    CHAINTIFY_CONTRACT_ADDRESS = "0x1ad1A82aA0AA9FCB53Dd2d265Eb79B06265097E3"
    RPC_URL = f"https://polygon-mumbai.g.alchemy.com/v2/{ALCHEMY_KEY}"
