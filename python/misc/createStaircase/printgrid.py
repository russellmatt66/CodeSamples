import requests
from bs4 import BeautifulSoup

# Replace with your Google Doc URL
# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'

# Fetch and parse the document
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize a dictionary to store characters by coordinates
grid = {}

# Find all table rows in the document
for row in soup.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) >= 3:
        try:
            x = int(cells[0].get_text(strip=True))
            char = cells[1].get_text(strip=True)
            y = int(cells[2].get_text(strip=True))
            grid[(x, y)] = char
        except ValueError:
            continue  # Ignore rows with non-integer coordinates

# Determine the grid size
max_x = max(k[0] for k in grid.keys()) if grid else 0
max_y = max(k[1] for k in grid.keys()) if grid else 0

# Print the grid
for y in range(max_y + 1):
    # line = ''.join(grid.get((x, max_y - y), ' ') for x in range(max_x + 1))
    line = ''.join(grid.get((x, y), ' ') for x in range(max_x + 1))
    print(line)
