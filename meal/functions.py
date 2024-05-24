import datetime

def orderTrxIdGen():
    x = datetime.datetime.now()
    yy = x.strftime("%Y")
    mm = x.strftime("%m")
    dd = x.strftime("%d")
    hh = x.strftime("%H")
    mm = x.strftime("%M")
    ss = x.strftime("%S")
    id = str("tx-" + yy + mm + dd + hh + mm + ss)
    return id