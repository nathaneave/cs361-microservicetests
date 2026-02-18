import requests
DAYOFWEEK_PORT = 8000
DEADLINECHECKER_PORT = 8001
TIMEZONECONVERTER_PORT = 8002

def test_dayofweek_validdate_noholiday():
    url = 'http://127.0.0.1:' + str(DAYOFWEEK_PORT) + '/dayofweek?event_date=2026-01-02'
    req = requests.get(url)
    print("event_date=2026-01-02")
    print("TEST dayofweek - valid date (not a holiday) - response status:", req.status_code)
    print("TEST dayofweek - valid date (not a holiday) - response text:", req.text)

def test_dayofweek_validdate_holiday():
    url = 'http://127.0.0.1:' + str(DAYOFWEEK_PORT) + '/dayofweek?event_date=2026-01-01'
    req = requests.get(url)
    print("event_date=2026-01-01")
    print("TEST dayofweek - valid date (holiday) - response status:", req.status_code)
    print("TEST dayofweek - valid date (holiday) - response text:", req.text)

def test_dayofweek_invaliddate():
    url = 'http://127.0.0.1:' + str(DAYOFWEEK_PORT) + '/dayofweek?event_date=2026-01'
    req = requests.get(url)
    print("event_date=2026-01")
    print("TEST dayofweek - valid date (holiday) - response status:", req.status_code)
    print("TEST dayofweek - valid date (holiday) - response text:", req.text)


def test_deadlinechecker_validdate_future():
    url = 'http://127.0.0.1:' + str(DEADLINECHECKER_PORT) + '/deadline_checker?event_date=2026-03-01'
    req = requests.get(url)
    print("event_date=2026-03-01")
    print("TEST deadlinechecker - valid future date - response status:", req.status_code)
    print("TEST deadlinechecker - valid future date - response text:", req.text)

def test_deadlinechecker_validdate_past():
    url = 'http://127.0.0.1:' + str(DEADLINECHECKER_PORT) + '/deadline_checker?event_date=2026-02-01'
    req = requests.get(url)
    print("event_date=2026-02-01")
    print("TEST deadlinechecker - valid past date - response status:", req.status_code)
    print("TEST deadlinechecker - valid past date - response text:", req.text)

def test_deadlinechecker_invaliddate():
    url = 'http://127.0.0.1:' + str(DEADLINECHECKER_PORT) + '/deadline_checker?event_date=INVALID'
    req = requests.get(url)
    print("event_date=INVALID")
    print("TEST deadlinechecker - invalid date - response status:", req.status_code)
    print("TEST deadlinechecker - invalid date - response text:", req.text)


def test_timezoneconverter_validinput_forward():
    url = 'http://127.0.0.1:' + str(TIMEZONECONVERTER_PORT) + '/timezone_converter?event_time=2026-03-02T08:00:00&from_timezone=UTC-08:00&to_timezone=UTC-05:00'
    req = requests.get(url)
    print("event_time=2026-03-02T08:00:00 | from_timezone=UTC-08:00 | to_timezone=UTC-05:00")
    print("TEST timezoneconverter - valid input (8AM PST to EST) - response status:", req.status_code)
    print("TEST timezoneconverter - valid input (8AM PST to EST) - response text:", req.text)

def test_timezoneconverter_validinput_backward():
    url = 'http://127.0.0.1:' + str(TIMEZONECONVERTER_PORT) + '/timezone_converter?event_time=2026-04-01T12:00:00&from_timezone=UTC-05:00&to_timezone=UTC-08:00'
    req = requests.get(url)
    print("event_time=2026-04-01T12:00:00 | from_timezone=UTC-05:00 | to_timezone=UTC-08:00")
    print("TEST timezoneconverter - valid input (12PM EST to PST) - response status:", req.status_code)
    print("TEST timezoneconverter - valid input (12PM EST to PST) - response text:", req.text)

def test_timezoneconverter_invalidtime():
    url = 'http://127.0.0.1:' + str(TIMEZONECONVERTER_PORT) + '/timezone_converter?event_time=2026-04&from_timezone=UTC-05:00&to_timezone=UTC-08:00'
    req = requests.get(url)
    print("event_time=2026-04 | from_timezone=UTC-05:00 | to_timezone=UTC-08:00")
    print("TEST timezoneconverter - invalid date/time - response status:", req.status_code)
    print("TEST timezoneconverter - invalid date/time - response text:", req.text)

def test_timezoneconverter_invalidtimezone():
    url = 'http://127.0.0.1:' + str(TIMEZONECONVERTER_PORT) + '/timezone_converter?event_time=2026-05-08T09:00:00&from_timezone=UTCINVALID&to_timezone=UTC-08:00'
    req = requests.get(url)
    print("event_time=2026-05-08T09:00:00 | from_timezone=UTCINVALID | to_timezone=UTC-08:00")
    print("TEST timezoneconverter - invalid timezone - response status:", req.status_code)
    print("TEST timezoneconverter - invalid timezone - response text:", req.text)


print("----------- BEGIN dayofweek TESTS -----------")
test_dayofweek_validdate_noholiday()
print()
test_dayofweek_validdate_holiday()
print()
test_dayofweek_invaliddate()
print("----------- END dayofweek TESTS -----------")

print()

print("----------- BEGIN deadlinechecker TESTS -----------")
test_deadlinechecker_validdate_future()
print()
test_deadlinechecker_validdate_past()
print()
test_deadlinechecker_invaliddate()
print("----------- END deadlinechecker TESTS -----------")

print()

print("----------- BEGIN timezoneconverter TESTS -----------")
test_timezoneconverter_validinput_forward()
print()
test_timezoneconverter_validinput_backward()
print()
test_timezoneconverter_invalidtime()
print()
test_timezoneconverter_invalidtimezone()
print("----------- END timezoneconverter TESTS -----------")

