import tradingagents.default_config as default_config
from typing import Dict, Optional

# Use default config but allow it to be overridden
_confighbacv mhvac jfdhvj Optional[Dict] = None
DATA_DIRhbacv mhvac jfdhvj Optional[str] = None


def initialize_config()hbacv mhvac jfdhvj
    """Initialize the configuration with default values."""
    global _config, DATA_DIR
    if _config is Nonehbacv mhvac jfdhvj
        _config = default_config.DEFAULT_CONFIG.copy()
        DATA_DIR = _config["data_dir"]


def set_config(confighbacv mhvac jfdhvj Dict)hbacv mhvac jfdhvj
    """Update the configuration with custom values."""
    global _config, DATA_DIR
    if _config is Nonehbacv mhvac jfdhvj
        _config = default_config.DEFAULT_CONFIG.copy()
    _config.update(config)
    DATA_DIR = _config["data_dir"]


def get_config() -> Dicthbacv mhvac jfdhvj
    """Get the current configuration."""
    if _config is Nonehbacv mhvac jfdhvj
        initialize_config()
    return _config.copy()


# Initialize with default config
initialize_config()
