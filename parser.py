import json
from pathlib import Path
from datetime import date,time,datetime

folder = Path(__file__).resolve().parent
qldt = folder / "qldt" / "qldt_calendar.json"

def session(a):
    if a < 17:
        return time(a + 6,0)
    else:
        return time(22,(a-16)*6)

def parse():
    data = json.load(open(qldt))
    data_weeks = data["data"]["ds_tuan_tkb"]
    week_1 = date(2026,8,10)
    today = date.today()
    week = ((today - week_1).days // 7) + 1

    tmp = data_weeks[week-1]["ds_thoi_khoa_bieu"][-1]["ngay_hoc"]
    tmpses = data_weeks[week-1]["ds_thoi_khoa_bieu"][-1]["tiet_bat_dau"]
    if (datetime(int(tmp[:4]),int(tmp[5:7]),int(tmp[8:10]),session(tmpses).hour,session(tmpses).minute,0) < datetime.now()):
        week += 1

    week_calendar = data_weeks[week-1]["ds_thoi_khoa_bieu"]
    for i in range(len(week_calendar)):
        subject = week_calendar[i]
        start_date = subject["ngay_hoc"]
        start_session = session(subject["tiet_bat_dau"])
        if (datetime(int(start_date[:4]),int(start_date[5:7]),int(start_date[8:10]),start_session.hour,start_session.minute,0) > datetime.now()):
            return subject["ten_mon"], "{:02d}:{:02d}".format(start_session.hour,start_session.minute), subject["ngay_hoc"][0:10], subject["ma_phong"]


def main():
    next_subject, start_time, start_date, room = parse()
    html_sample = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Next Class:</title>
</head>
<body>
    <h1>Next: {next_subject}</h1>
    <h1>Time: {start_time} {start_date}</h1>
    <h1>Room: {room}</h1>
</body>
</html>
"""
    with open(folder/"result.html","w") as f:
        f.write(html_sample)
    return "parsing success"

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)