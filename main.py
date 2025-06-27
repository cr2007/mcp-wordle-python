from datetime import date
from typing import TypedDict

import requests
from fastmcp import FastMCP

mcp = FastMCP("WordleMCP")

class WordleAPIData(TypedDict):
    id:                int
    solution:          str
    print_date:        str
    days_since_launch: int
    editor:            str


@mcp.tool(
        name="get_wordle_solution",
        description="Fetches the Wordle of a particular date provided between 2021-05-19 to 23 days future",
        annotations={"readOnlyHint": True}
)
async def get_wordle_data(date: str = date.today().isoformat()) -> WordleAPIData:
    """
    Retrieves Wordle puzzle data for a specified date.
    
    This function fetches the complete Wordle solution and associated metadata
    for any given date within the supported range.
    
    Args:
        date (str, optional): Target date in YYYY-MM-DD format. If not provided,
            defaults to the current date.
    
    Returns:
        dict: JSON response containing:
            - solution: The 5-letter Wordle answer
            - puzzle_id: Sequential puzzle number
            - metadata: Additional puzzle information (editor, days since launch, etc.)
    
    Note:
        - Date format must be YYYY-MM-DD (ISO 8601)
        - Available date range: 2021-05-19 (Wordle launch) to 23 days future
        - Returns error for dates outside supported range
    """

    url: str = f"https://www.nytimes.com/svc/wordle/v2/{date}.json"

    # Make the GET request to the Wordle API
    return requests.get(url, timeout=300).json()


if __name__ == "__main__":
    mcp.run()
