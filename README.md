# Spotify music recommendation

This is a Flask-based web application that allows users to generate Spotify playlists based on artist recommendations.

## Installation

The project requires Python 3.7 or above. Follow these steps to install and run the project:

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Create a virtual environment and activate it:

   On Unix or MacOS:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

   On Windows:

   ```bash
   python3 -m venv env
   .\env\Scripts\activate
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the project:

```bash
python3 app.py
```

## Environment Variables

To run this project, you will need to add the following environment variables:

1.  `SPOTIFY_CLIENT_ID`: Your Spotify client ID
2.  `SPOTIFY_CLIENT_SECRET`: Your Spotify client secret
3.  `SPOTIFY_REDIRECT_URI`: Your Spotify redirect URI

## Features

- Search for an artist
- Get a recommendation list based on selected artists
- Create a new playlist on Spotify based on the recommendation list
