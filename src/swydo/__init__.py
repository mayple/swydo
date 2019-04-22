"""
Main package for the swydo library.

Example usage:

    .. highlight:: python
    .. code-block:: python

        import swydo

        API_KEY="...."
        TEAM_ID = "..."

        print("Starting...")
        swydoClient = swydo.SwydoClient(apiKey=API_KEY)

        teams = list(swydoClient.getTeams())
        team = swydoClient.getTeam(teamId=TEAM_ID)

"""
from .__version__ import __version__
from .client import SwydoClient, Enumerations

