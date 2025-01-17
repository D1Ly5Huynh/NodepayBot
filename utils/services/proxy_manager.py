import aiohttp
import ssl

from urllib.parse import urlparse
from utils.settings import logger, Fore


# Load proxies from a file
def load_proxies():
    try:
        with open('proxies.txt', 'r') as file:
            proxies = file.read().splitlines()

        if not proxies:
            logger.warning(f"{Fore.CYAN}00{Fore.RESET} - {Fore.YELLOW}No proxies found in proxies.txt. Running without proxies{Fore.RESET}")

        return proxies
    
    except FileNotFoundError:
        logger.warning(f"{Fore.CYAN}00{Fore.RESET} - {Fore.YELLOW}File proxies.txt not found. Running without proxies{Fore.RESET}")
        return []

    except Exception as e:
        logger.error(f"{Fore.CYAN}00{Fore.RESET} - {Fore.RED}Error loading proxies:{Fore.RESET} {e}")
        return []

# Prompt the user to decide whether to use proxies


# Map tokens to proxies, assigning None if proxies are insufficient


# Extract the hostname (IP address) from a given proxy URL


# Create SSL context to allow self-signed certificates
def create_ssl_context():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    return ssl_context

# Get the public IP address, optionally through a proxy


# Resolves IP or proxy for the account
async def resolve_ip(account):
    try:
        if account.proxy and account.proxy.startswith("http"):
            return await get_ip_address(account.proxy)
        else:
            return await get_ip_address()
    except Exception as e:
        logger.error(f"{Fore.CYAN}{account.index:02d}{Fore.RESET} - {Fore.RED}Failed to resolve proxy or IP address:{Fore.RESET} {e}")
        return "Unknown"
