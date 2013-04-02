README for percent displayer in various languages

Author: Quinten Palmer

- 1.0 Install
- 1.1 Clean
- 1.2 Run
- 1.3 Other commands
- 2.0 Settings
- 2.1 Example setting.txt

1.0
To install type:
> ./percent.sh install

1.1
To clean up the install, type:
> ./percent.sh clean

1.2
To run any of the various percent displays, type:
> ./percent python

> ./percent shell

> ./percent java

> ./percent c

1.3
To view the help text, type:
> ./percent help

To view the time test, type:
> ./percent time

2.0
To change the number that it counts to and the frequency of each tick, edit settings.txt

The first line is the number to count to (pretty simple)
The second line changes how often the tick happens (it is in milliseconds)

2.1
Example settings.txt:
> 100

> 1000

Will count up to 100, ticking every second
