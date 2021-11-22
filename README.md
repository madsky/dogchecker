# dogchecker
Specific HTML parser with SMS notifications via boto3

Probably adaptable if you have a similar need, definitely room to improve it.

Basically it pulls a webpage (in this instance a pets4homes search string and then parses the HTML for a specific value that I needed. If that value had changed since the last time it ran, it would send out an SMS alerting someone to it. Set at a conservative 15 minute delay, which can be shortened. 

Our use case here was that we wanted a puppy but the prices were very inflated and every time we saw a more reasonably priced advert, it was always too late. This script resulted in the latest addition to our family.

Maybe it can useful to someone else.
