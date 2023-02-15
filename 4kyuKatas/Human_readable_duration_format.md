# Human readable duration format
:computer: Join [CodeWars](www.codewars.com/r/v0KX6w) and :point_right: follow [me](https://www.codewars.com/users/gmarte)!

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:
```
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

<details><summary>open to view solution</summary>

### Solution
```python
def format_duration(seconds):
    result = {}
    if seconds <= 0:
        return 'now'
    years = seconds // 31536000  # 31536000
    if years:
        result['years' if years > 1 else 'year'] = years
    days = seconds // 86400 % 365  # 86400
    if days:
        result['days' if days > 1 else 'day'] = days
    hours = (seconds // 3600) % 24  # 3600
    if hours:
        result['hours' if hours > 1 else 'hour'] = hours
    minutes = (seconds % 3600) // 60
    if minutes:
        result['minutes' if minutes > 1 else 'minute'] = minutes
    seconds = seconds % 60
    if seconds:
        result['seconds' if seconds > 1 else 'second'] = seconds
    # return f"{years:2d} years, {days:2d} days, {hours:2d} hours, {minutes:02d} minutes, {seconds:02d} seconds"

    if len(result) > 1:
        resultString = ', '.join(str(y) + ' ' + str(x)
                                 for x, y in list(result.items())[:-1])
        lastkey = list(result.keys())[-1]
        resultString += ' and ' + str(result[lastkey]) + ' ' + str(lastkey)
    else:
        resultString = ', '.join(str(y) + ' ' + str(x)
                                 for x, y in result.items())
    return resultString
```
</details>