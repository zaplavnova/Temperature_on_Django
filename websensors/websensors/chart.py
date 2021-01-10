#!/usr/bin/env python3

def get(request):
    import pandas as pd
    import django
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    import psycopg2

    conn = psycopg2.connect(dbname="temperature", user="postgres", password="enot115735", host="localhost", port="5432")
    cursor = conn.cursor()

    sql = "SELECT temp1, temp2, temp3, ts FROM TEMPERATURE ORDER BY ts;"

    cursor.execute(sql)
    tmp = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(tmp, columns=["temp1", "temp2", "temp3", "ts"])

    fig = Figure()
    ax = fig.add_subplot(111)

    ax.plot(df.ts, df.temp1)
    ax.plot(df.ts, df.temp2)
    ax.plot(df.ts, df.temp3)
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type="image/png")
    canvas.print_png(response)
    return response
