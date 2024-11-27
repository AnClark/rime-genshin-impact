# By default we assume the configuration is located at a variable
#     called "exports".
# You can change this with `-n any_name` in the CLI.

from mw2fcitx.tweaks.moegirl import tweaks


exports = {
    # Source configurations.
    "source": {
        # MediaWiki api.php path, if to fetch titles from online.
        "api_path": "https://wiki.biligame.com/ys/api.php",
        # Title file path, if to fetch titles from local file. (optional)
        # Only works if api_path is absent.
        "file_path": "titles.txt",
        "kwargs": {
            # Title number limit for online fetching. (optional)
            # Only works if api_path is provided.
            #"title_limit": 120,
            # Title list export path. (optional)
            "output": "titles.txt"
        }
    },
    # Tweaks configurations as an list.
    # Every tweak function accepts a list of titles and return
    #     a list of title.
    "tweaks":
        tweaks,
    # Converter configurations.
    "converter": {
        # opencc is a built-in converter.
        # For custom converter functions, just give the function itself.
        "use": "opencc",
        "kwargs": {}
    },
    # Generator configurations.
    "generator": [{
        # rime is a built-in generator.
        # For custom generator functions, just give the function itself.
        "use": "rime",
        "kwargs": {
            # Explicitly specify dictionary name, otherwise it will be "moegirl".
            "name": "GenshinImpact",
            # Destination dictionary filename. (optional)
            "output": "GenshinImpact.dict.yml"
        }
    }]
}

