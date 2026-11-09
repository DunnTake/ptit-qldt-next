# ptit-qldt-next

Tells you the next class of PTIT.

How it works:
1. User types in qldt account user and password (this only needs to be completed once)
2. extract.py opens qldt on a separate hidden browser to log in and wait for "w-locdstkbtuanusertheohocky" API, then converts the API to a separate .json file in the folder
3. parser.py parses the qldt_calendar.json file to find the next session, writes the result onto result.html
4. server.py opens a local server for result.html

main.py starts the entire process and re-run parser.py every 5 minutes

Note: I originally built this project because i believed the traditional method of checking the schedule was annoying. Back then, the scope was to make an entire independent calendar based on the student schedule data acquired by the qldt API. I have since re-scoped it to just be a webpage that tells you when the next class starts. However, in the future, i would still like to be able to make a full-fledged calendar that is more convenient than both the official website and my current version. If you would like to do this yourself, parser.py handles the parsing, start there.
