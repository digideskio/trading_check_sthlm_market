from datetime import datetime, timedelta


def exception_dates():
    return [
        datetime(2014, 1, 1),
        datetime(2014, 1, 6),
        datetime(2014, 4, 15),
        datetime(2014, 4, 16),
        datetime(2014, 4, 17),
        datetime(2014, 4, 18),
        datetime(2014, 4, 21),
        datetime(2014, 5, 1),
        datetime(2014, 5, 15),
        datetime(2014, 5, 16),
        datetime(2014, 5, 29),
        datetime(2014, 6, 6),
        datetime(2014, 6, 19),
        datetime(2014, 6, 20),
        datetime(2014, 12, 24),
        datetime(2014, 12, 25),
        datetime(2014, 12, 26),
        datetime(2014, 12, 31)
    ]


def date_is_trading_day(check_date):
    if check_date.weekday() in (5, 6):
        return False

    for exception_date in exception_dates():
        if check_date.date() == exception_date.date():
            return False

    return True


def next_trading_day_with_minimum(start_date, target_days):
    final_target_days = target_days
    date_range = timedelta(days=final_target_days)

    if (start_date + timedelta(days=target_days)).weekday() in (5, 6):
        final_target_days += 2
        return next_trading_day_with_minimum(start_date + date_range, final_target_days)

    date_range = timedelta(days=final_target_days)

    for date in exception_dates():
        if start_date.date() < date.date() <= start_date.date() + date_range:
            final_target_days += 1
            return next_trading_day_with_minimum(start_date + date_range, final_target_days)

    return final_target_days


def main():
    print next_trading_day_with_minimum(datetime.today(), 2)


if __name__ == "__main__":
    main()
