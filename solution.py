import sys
import requests
from bs4 import BeautifulSoup

# Fix Unicode output on Windows
sys.stdout.reconfigure(encoding="utf-8")


def print_secret_message(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    points = []

    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            cells = row.find_all(["td", "th"])

            if len(cells) != 3:
                continue

            values = [cell.get_text(strip=True) for cell in cells]

            try:
                x = int(values[0])
                character = values[1]
                y = int(values[2])
                points.append((x, y, character))
            except ValueError:
                continue

    if not points:
        raise ValueError("No valid character coordinates found.")

    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)

    grid = [[" "] * (max_x + 1) for _ in range(max_y + 1)]

    for x, y, character in points:
        grid[y][x] = character

    for y in range(max_y, -1, -1):
        print("".join(grid[y]))


url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_secret_message(url)