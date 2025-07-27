import logging
from ytm_util.ytm_log import setup_logger, set_third_party_logging_level
from ytm_util.ytm_auth import authenticate_youtube
from ytm_util.ytm_sort import get_playlists, sort_all_playlists

# -------------------- Logging Setup --------------------
logger = setup_logger(__name__, disable_console=True)
modules = {__name__, "ytm_util"}

set_third_party_logging_level(modules)
# -------------------------------------------------------


def main():
    try:
        youtube = authenticate_youtube()
        playlists = get_playlists(youtube)
        # Default to sorting by artist
        sort_all_playlists(youtube, playlists)
    except Exception as e:
        logger.critical(f"Critical error in main: {e}")


if __name__ == "__main__":
    main()
