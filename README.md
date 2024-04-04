# DigitalDetective

FinalRecon is an all in one automatic web reconnaissance tool written in python. Goal of FinalRecon is to provide an overview of the target in a short amount of time while maintaining the accuracy of results. Instead of executing several tools one after another it can provide similar results keeping dependencies small and simple.

## Features

Digital Detective provides detailed information such as :

* Header Information

* Whois

* SSL Certificate Information

* Crawler
  * html
    * CSS
    * Javascripts
    * Internal Links
    * External Links
    * Images
  * robots
  * sitemaps
  * Links inside Javascripts
  * Links from Wayback Machine from Last 1 Year

* DNS Enumeration
  * A, AAAA, ANY, CNAME, MX, NS, SOA, TXT Records
  * DMARC Records

* Subdomain Enumeration
  * Data Sources
    * BuffOver
    * crt.sh
    * ThreatCrowd
    * AnubisDB
    * ThreatMiner
    * Facebook Certificate Transparency API
      * Auth Token is Required for this source, read Configuration below
    * VirusTotal
    	* API Key is Required
    * Shodan
      * API Key is Required
    * CertSpotter

* Directory Searching
  * Support for File Extensions

* Wayback Machine
    * URLs from Last 5 Years

* Port Scan
  * Fast
  * Top 1000 Ports
 
## Installation
```bash
git clone https://github.com/hitanshkadakia/DigitalDetective.git
cd DigitalDetective
cd digital detective
pip3 install -r requirements.txt
```


# Check headers

python3 finalrecon.py --headers <url>

# Check ssl Certificate

python3 finalrecon.py --sslinfo <url>

# Check whois Information

python3 finalrecon.py --whois <url>

# Crawl Target

python3 finalrecon.py --crawl <url>

# Directory Searching

python3 finalrecon.py --dir <url> -e txt,php -w /path/to/wordlist

# full scan

python3 finalrecon.py --full <url>



https://github.com/hitanshkadakia/DigitalDetective.git
