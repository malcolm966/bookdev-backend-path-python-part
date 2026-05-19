def hours_to_seconds(hours:int):
    return hours * 60 * 60


def test(hours):
    secs = hours_to_seconds(hours)
    print(f"hours is {hours}, secs is {secs}")


test(1)
test(2)