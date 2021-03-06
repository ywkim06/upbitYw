import time
import pyupbit
import datetime

access = "ukwfJwgAt9QnFiTACJFmrNImRdCF0QBXf30Ld9eb"
secret = "7KxUxD3jvQr9Nzxhzk4HuGtAxzW7mOI076uFcQAx"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time1 = get_start_time("KRW-XRP")
        end_time1 = start_time1 + datetime.timedelta(days=1)

        if start_time1 - datetime.timedelta(minutes=60) < now < end_time1 - datetime.timedelta(seconds=610):
            target_price = get_target_price("KRW-XRP", 0.030)
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XRP", krw*0.9995)
        else:
            btc = get_balance("XRP")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-XRP", btc*0.9995)

        start_time2 = get_start_time("KRW-BTT")
        end_time2 = start_time2 + datetime.timedelta(days=1)

        if start_time2 - datetime.timedelta(seconds=610) < now < end_time2 - datetime.timedelta(seconds=620):
            target_price = get_target_price("KRW-BTT", 0.464)
            current_price = get_current_price("KRW-BTT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTT", krw*0.9995)
        else:
            btc = get_balance("BTT")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTT", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
