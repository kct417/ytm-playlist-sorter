# Setting Up OAuth Client ID for Desktop App

TODO: Add detailed instructions with screenshots.

-   https://console.cloud.google.com/
-   APIs & Services -> Credentials
-   Create Credentials -> OAuth client ID
-   Desktop App

# Setup Python Environment

The following steps depend on your operating system:

## Windows

```
.\setup.bat
```

## macOS/Linux

```
./setup.sh
```

# Manual Setup

```
python -m venv .venv
```

The following steps depend on your operating system:

## Windows

```
.venv\Scripts\activate.bat
```

## macOS/Linux

```
source .venv/bin/activate
```

## Install Dependencies

```
pip install -r requirements.txt
```

# Usage

```
python main.py
```

# Limitations

-   Quota limits from YouTube Data API v3 apply.
-   Must have "Manage your YouTube account" permission for playlists.
-   Must have a Google Console project with YouTube Data API v3 enabled.
