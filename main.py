import logging
from util.ytm_log import setup_logger
from util.ytm_auth import authenticate_youtube
from util.ytm_sort import display_items, get_playlists, sort_all_playlists

# -------------------- Logging Setup --------------------
LOG_FILE = "ytm-sorter.log"
logger = setup_logger(__name__, log_file=LOG_FILE)
modules = {"util"}

for name in logging.root.manager.loggerDict:
    # Keep logs for __name__ and any module in 'modules' or submodules
    if name != __name__ and not any(
        name == mod or name.startswith(mod + ".") for mod in modules
    ):
        setup_logger(name, level=logging.ERROR)
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
