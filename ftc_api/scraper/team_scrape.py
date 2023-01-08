import httpx
from bs4 import BeautifulSoup


class TeamScrape:
    team_id = 0
    name = ""


def get_info(team_id):
    r = httpx.get("https://ftc-events.firstinspires.org/2022/team/" + str(team_id))

    return BeautifulSoup(r.text)


print(get_info(14380).prettify())
