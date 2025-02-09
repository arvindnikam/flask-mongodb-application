# settings.py
from dotenv import load_dotenv
# load_dotenv()

# OR, the same with increased verbosity:
# load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
# import os
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

## Try finding .env file
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
