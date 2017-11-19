# Github Scraper

## Description
This script is intended to quickly scrape github projects.

## Usage
```
python scrape-github.py [technology-list]
```
Here the following arguments are *needed*:
* technology list: the technologies you are trying to scrape, all technologies in this list should be escaped

This will leave you with a file per technology that has the technology's name and in there you will find all github projects that are returned.

## Restrictions
Github will restrict all calls to 1000 repositories. The scraper uses 4 metrics to search both in descending and ascending order:
* search results
* stars
* forks
* recently updated

By running this every x days and making a set you will end up with a maximum amount of repositories while not running into github's restrictions.

### Not a set
It is also worth to note that the resulting list is not a set, entries can appear multiple times.

## Example
```
python scrape-github.py hadoop
```
This will leave you with a 'hadoop' file that has 8000 entries.

```
python scrape-github.py hadoop file+system spark apache+flink data-mining
```
This will leave you with the following files:
* hadoop
* file+system
* spark
* apache+flink
* data-mining
Each of which will contain links to projects that have a link to that technology.
