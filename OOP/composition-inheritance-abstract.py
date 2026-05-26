from abc import ABC, abstractmethod
from collections import namedtuple
from dataclasses import dataclass
from datetime import date
from os import getenv
from pathlib import Path
from typing import Any, List, Optional
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup  # type: ignore

TMP = getenv("TMP", "/tmp")
TODAY = date.today()
Candidate = namedtuple("Candidate", "name votes")
LeaderBoard = namedtuple(
    "LeaderBoard", "Candidate Average Delegates Contributions Coverage"
)
Poll = namedtuple(
    "Poll",
    "Poll Date Sample Biden Sanders Gabbard Spread",
)


@dataclass
class File:
    """File represents a filesystem path.

    Variables:
        name: str -- The filename that will be created on the filesystem.
        path: Path -- Path object created from the name passed in.

    Methods:
        [property]
        data: -> Optional[str] -- If the file exists, it returns its contents.
            If it does not exist, it returns None.
    """
    name: str
    path: Path = None  # type: ignore[assignment]

    def __post_init__(self):
        if self.path is None:
            self.path = Path(f"{TMP}/{TODAY}_{self.name}")

    def file_exists(self) -> bool:
        return self.path.exists()

    @property
    def data(self):
        if self.file_exists():
            with open(self.path) as f:
                return f.read()
        return None

@dataclass
class Web:
    """Web object.

    Web is an object that downloads the page from the url that is passed
    to it and stores it in the File instance that is passed to it. If the
    File already exists, it just reads the file, otherwise it downloads it
    and stores it in File.

    Variables:
        url: str -- The url of the web page.
        file: File -- The File object to store the page data into.

    Methods:
        [property]
        data: -> Optional[str] -- Reads the text from File or retrieves it from the
            web if it does not exists.

        [property]
        soup: -> Soup -- Parses the data from File and turns it into a BeautifulSoup
            object.
    """
    url: str
    file: File

    @property
    def data(self) -> Optional[str]:
        """Reads the data from the File object.

        First it checks if the File object has any data. If it doesn't, it retrieves
        it and saves it to the File. It then reads it from the File and returns it.

        Returns:
            Optional[str] -- The string data from the File object.
        """
        if self.file.data is None:
            urlretrieve(self.url, self.file.path)
        return self.file.data

    @property
    def soup(self) -> Soup:
        """Converts string data from File into a BeautifulSoup object.

        Returns:
            Soup -- BeautifulSoup object created from the File.
        """
        return Soup(self.data, "html.parser")


class Site(ABC):
    """Site Abstract Base Class.

    Defines the structure for the objects based on this class and defines the interfaces
    that should be implemented in order to work properly.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        [abstractmethod]
        parse_rows: -> Union[List[LeaderBoard], List[Poll]] -- Parses a BeautifulSoup
            table element and returns the text found in the td elements as
            namedtuples.

        [abstractmethod]
        polls: -> Union[List[LeaderBoard], List[Poll]] -- Does the parsing of the table
            and rows for you. It takes the table index number if given, otherwise
            parses table 0.

        [abstractmethod]
        stats: -- Formats the results from polls into a more user friendly
            representation.
    """
    web: Web

    def find_table(self, loc: int = 0) -> str:
        """Finds the table elements from the Soup object

        Keyword Arguments:
            loc {int} -- Parses the Web object for table elements and
                returns the first one that it finds unless an integer representing
                the required table is passed. (default: {0})

        Returns:
            str -- The html table
        """
        tables = self.web.soup.find_all('table')
        return tables[loc]

    @abstractmethod
    def parse_rows(self, table: Soup) -> List[Any]: ...
    """Abstract Method
    
    Parses the row data from the html table.

    Arguments:
        table {Soup} -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as NamedTuple.

    Returns:
        List[NamedTuple] -- List of NamedTuple that were created from the
            table data.
    """

    @abstractmethod
    def polls(self, table: int = 0) -> List[Any]: ...
    """Abstract Method

    Parses the data

    The find_table and parse_rows methods are called for you and the table index
    that is passed to it is used to get the correct table from the soup object.

    Keyword Arguments:
        table {int} -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.
            (default: {0})

    Returns:
        List[NamedTuple] -- List of NamedTuple that were created from the
            table data.
    """
    
    @abstractmethod
    def stats(self, loc: int = 0): ...
    """Abstract Method
    
    Produces the stats from the polls.

    Keyword Arguments:
        loc {int} -- Formats the results from polls into a more user friendly
        representation.
    """

@dataclass
class RealClearPolitics(Site):
    """RealClearPolitics object.

    RealClearPolitics is a custom class to parse a Web instance from the
    realclearpolitics website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[Poll] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as Poll namedtuples.

        polls: -> List[Poll] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            RealClearPolitics
            =================
                Biden: 214.0
              Sanders: 142.0
              Gabbard: 6.0

    """

    web: Web

    def parse_rows(self, table: Soup) -> List[Poll]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as Poll namedtuples.

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        rows = []
        for tr in table.find_all('tr')[1:]:
            cells = [td.get_text(" ", strip=True) for td in tr.find_all('td')]
            if len(cells) != len(Poll._fields):
                continue
            # Convert numeric polling columns (Biden, Sanders, Gabbard) to float;
            # "--" means no value reported, treat as 0.0.
            for i in (3, 4, 5):
                cells[i] = 0.0 if cells[i] == "--" else float(cells[i])
            rows.append(Poll(*cells))
        return rows
            

    def polls(self, table: int = 0) -> List[Poll]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        tbl = self.find_table(table)
        return self.parse_rows(tbl)
       
    
    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.

        """
        rows = self.polls(loc)
        biden_stat = sanders_stat = gabbard_stat = 0.0
        # Skip the RCP Average row (first data row), sum the rest.
        for row in rows[1:]:
            biden_stat += row.Biden
            sanders_stat += row.Sanders
            gabbard_stat += row.Gabbard

        title = "RealClearPolitics"
        divider = "=" * len(title)
        width = max(len("Biden"), len("Sanders"), len("Gabbard"))
        format_text = (
            f"\n{title}\n{divider}\n"
            f"{'Biden':>{width}}: {biden_stat}\n"
            f"{'Sanders':>{width}}: {sanders_stat}\n"
            f"{'Gabbard':>{width}}: {gabbard_stat}\n"
        )
        print(format_text)
        return format_text


@dataclass
class NYTimes(Site):
    """NYTimes object.

    NYTimes is a custom class to parse a Web instance from the nytimes website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[LeaderBoard] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as LeaderBoard namedtuples.

        polls: -> List[LeaderBoard] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            NYTimes
            =================================

                               Pete Buttigieg
            ---------------------------------
            National Polling Average: 10%
                   Pledged Delegates: 25
            Individual Contributions: $76.2m
                Weekly News Coverage: 3

    """

    web: Web

    def parse_rows(self, table: Soup) -> List[LeaderBoard]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as LeaderBoard namedtuples.

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
            the table data.
        """
        rows = []
        for tr in table.find_all('tr'):
            # Skip candidates who have dropped out of the race.
            tr_classes = tr.get('class', [])
            if 'g-cand-out' in tr_classes:
                continue

            candidate = average = delegates = contributions = coverage = None
            for td in tr.find_all('td'):
                td_classes = td.get('class', [])
                if 'g-cand-info' in td_classes:
                    # The td contains the full name followed by the last name;
                    # keep only the first text node (full name).
                    candidate = td.get_text("|", strip=True).split("|")[0]
                elif 'g-poll_avg' in td_classes:
                    # "29" and "%" are separate text nodes; join with no separator.
                    average = td.get_text("", strip=True)
                elif 'g-delegates' in td_classes:
                    delegates = int(td.get_text("", strip=True))
                elif 'g-total_indiv_contrib' in td_classes:
                    contributions = td.get_text("", strip=True)
                elif 'g-news_coverage_most_recent' in td_classes:
                    # Value looks like "#1"; strip the '#' and convert to int.
                    coverage = int(td.get_text("", strip=True).lstrip("#"))

            if all(v is not None for v in (candidate, average, delegates, contributions, coverage)):
                rows.append(LeaderBoard(
                    Candidate=candidate,
                    Average=average,
                    Delegates=delegates,
                    Contributions=contributions,
                    Coverage=coverage,
                ))
        return rows

    def polls(self, table: int = 0) -> List[LeaderBoard]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
                the table data.
        """
        tbl = self.find_table(table)
        return self.parse_rows(tbl)

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        rows = self.polls(loc)
        title = "NYTimes"
        eq_divider = "=" * 33
        dash_divider = "-" * 33
        label_width = len("Individual Contributions")  # 24

        parts = ["", title, eq_divider, ""]
        for row in rows:
            parts.append(f"{row.Candidate:>33}")
            parts.append(dash_divider)
            parts.append(f"{'National Polling Average':>{label_width}}: {row.Average}")
            parts.append(f"{'Pledged Delegates':>{label_width}}: {row.Delegates}")
            parts.append(f"{'Individual Contributions':>{label_width}}: {row.Contributions}")
            parts.append(f"{'Weekly News Coverage':>{label_width}}: {row.Coverage}")
            parts.append("")

        format_text = "\n".join(parts)
        print(format_text)
        return format_text


def gather_data():
    rcp_file = File("realclearpolitics.html")
    rcp_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_realclearpolitics.html"
    )
    rcp_web = Web(rcp_url, rcp_file)
    rcp = RealClearPolitics(rcp_web)
    rcp.stats(3)

    nyt_file = File("nytimes.html")
    nyt_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_nytimes.html"
    )
    nyt_web = Web(nyt_url, nyt_file)
    nyt = NYTimes(nyt_web)
    nyt.stats()

if __name__ == "__main__":
    gather_data()
