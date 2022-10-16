import requests
import pymysql


def parse_data():
    r = requests.get("https://map.ke.com/proxyApi/i.c-pc-webapi.ke.com/map/initdata?cityId=310000&dataSource=ESF")
    records = r.json()
    lines = records["data"]["subway"]["options"]
    results = []
    for li in lines:
        line_num = li["name"]  # 1号线
        # print(lines[0])
        for rec in li["options"]:
            results.append({
                "line": line_num,
                "station": rec["name"],
                "station_code": rec["id"]
            })

    print(results[0])
    return results


def insert_sql(results):
    conn = pymysql.connect(
        host="rm-uf6mav88a70rf99w3to.mysql.rds.aliyuncs.com",
        user="gaohan",
        passwd="GAOhan1234567",
        database="lualu",
        autocommit=True
    )
    cursor = conn.cursor()
    for r in results:
        # sql2 = f"""SELECT count(*) FROM subway where line = '{r["line"]}' and station_code ='{r["station_code"]}' """
        # cursor.execute(sql2)
        # ret1 = cursor.fetchone()
        # print(ret1)
        # if len(ret1) == 1:
        sql = f"""INSERT into subway (line,station,station_code) values ('{r["line"]}', '{r["station"]}', '{r["station_code"]}')"""
        cursor.execute(sql)
    cursor.close()


if __name__ == "__main__":
    results = parse_data()
    insert_sql(results)
