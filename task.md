# Ad Statistics
​
## About the task
​
The goal of this task is not to see who can write the best code, but
to get an understanding of how you solve problems and think about
code.
​
- You can use any programming language you feel comfortable with
- We will only use this task as a basis for discussion in your interview,
  so there isn't any pre-defined "correct" way to solve this
- If you are unsure about something; make an assumption and run with it
​
## Solution
We value creativity, so if you think of some fun or interesting way to
solve this which might be a bit unconventional - go for it!
​
The solution is meant to be a basis for discussion so we do not recommend 
using external libraries as then those would also be a part of the discussion,
and it also complicates running the program on our side :)
## Task
​
You are given a file (`ads.txt`) containing FINN ads on the format:
​
```
adId,adType,adPrice
```
​
- `adId` is often called "FINN-kode" and is a unique ID per ad. This is always a whole number.
- `adType` is the "vertical", think of it like a category, on FINN. For example car, house, boat, lamps, etc. 
  This is always text.
- `adPrice` is the asking price of the object. This is a number, but it can have decimals.
​
Your product manager currently wants to know 4 things per adType:
​
- How many ads are there per type?
- What is the cheapest ad per type?
- What is the most expensive ad per type?
- How many ads are duplicated?
​
You are asked to provide this information in a text file named `adStats.txt`.
​
The format is not super strict, but you are given an example:
​
```
AdType: car
Current amount of ads: 1
Duplicated ads: 2
Lowest value ad: 1134123 (839100kr)
Highest value ad: 1134123 (839100kr)
​
AdType: boat
Current amount of ads: 3
Duplicated ads: 0
Lowest value ad: 123566512 (810kr)
Highest value ad: 124124 (91233kr)
```
​
## Delivery
​
Please make sure to include all required files, and instructions, for running your code in your delivery.
​
Good luck 😊
