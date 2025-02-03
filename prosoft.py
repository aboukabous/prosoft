import os
import shutil
import tempfile
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clear_temp_files():
    # Get the path to the temporary directory
    temp_dir = tempfile.gettempdir()
    logging.info(f"Clearing temporary files in: {temp_dir}")

    try:
        # Iterate through all files and folders in the temp directory
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)

            # Check if it is a file or directory and remove it
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                logging.info(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                logging.info(f"Deleted directory: {item_path}")

        logging.info("Temporary files cleared successfully.")
    except Exception as e:
        logging.error(f"Error while clearing temporary files: {e}")

def clear_windows_temp_files():
    # Get the path to the Windows temp directory
    windows_temp_dir = Path(os.getenv('LOCALAPPDATA')) / 'Temp'
    logging.info(f"Clearing Windows temporary files in: {windows_temp_dir}")

    try:
        # Iterate through all files and folders in the Windows temp directory
        for item in windows_temp_dir.iterdir():
            try:
                if item.is_file() or item.is_symlink():
                    item.unlink()
                    logging.info(f"Deleted file: {item}")
                elif item.is_dir():
                    shutil.rmtree(item)
                    logging.info(f"Deleted directory: {item}")
            except Exception as e:
                logging.error(f"Error while deleting {item}: {e}")

        logging.info("Windows temporary files cleared successfully.")
    except Exception as e:
        logging.error(f"Error while clearing Windows temporary files: {e}")

def main():
    logging.info("ProSoft: Starting system cleanup...")
    clear_temp_files()
    clear_windows_temp_files()
    logging.info("ProSoft: System cleanup completed.")

if __name__ == "__main__":
    main()