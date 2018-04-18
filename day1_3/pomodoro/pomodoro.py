import argparse
import sys
import time
from datetime import datetime, timedelta


class Pomodoro:

    def __init__(self, work_time, short_break, long_break):
        self.work_time = work_time
        self.short_break = short_break
        self.long_break = long_break

    def start_pomodoro(self):

        for i in range(9, -1, -1):
            sys.stdout.write('\r')
            sys.stdout.write('Pomodoro starts in {}'.format(i))
            sys.stdout.flush()
            time.sleep(1)

        pomodoro_count = 0
        while True:

            print()
            print('Pomodoro started: {}'.format(datetime.strftime(datetime.now(), '%B, %d %Y-%m-%d %H:%M:%S')))

            td = timedelta(minutes=self.work_time)
            while td > timedelta(seconds=-1):
                sys.stdout.write('\r\t\t{}'.format(td))
                sys.stdout.flush()
                td -= timedelta(seconds=1)
                time.sleep(1)

            if pomodoro_count == 3:
                pomodoro_count = 0
                print('\nLong break: {}'.format(datetime.strftime(datetime.now(), '%B, %d %Y-%m-%d %H:%M:%S')))
                td = timedelta(minutes=self.long_break)
                while td > timedelta(seconds=-1):
                    sys.stdout.write('\r\t\t{}'.format(td))
                    sys.stdout.flush()
                    td -= timedelta(seconds=1)
                    time.sleep(1)
            else:
                print('\nShort break: {}'.format(datetime.strftime(datetime.now(), '%B, %d %Y-%m-%d %H:%M:%S')))
                td = timedelta(minutes=self.short_break)
                while td > timedelta(seconds=-1):
                    sys.stdout.write('\r\t\t{}'.format(td))
                    sys.stdout.flush()
                    td -= timedelta(seconds=1)
                    time.sleep(1)

                pomodoro_count += 1


def main():
    parser = argparse.ArgumentParser(description='Basic Pomodoro application')

    parser.add_argument('-wt', '--work-time',
                        help='work time, default is 25 minutes',
                        default=1,
                        type=int)
    parser.add_argument('-sb', '--short-break',
                        help='short break time, default is 5 minutes',
                        default=1,
                        type=int)
    parser.add_argument('-lg', '--long-break',
                        help='long break time, default is 10 minutes',
                        default=1,
                        type=int)
    args = parser.parse_args()

    p1 = Pomodoro(args.work_time, args.short_break, args.long_break)
    p1.start_pomodoro()

if __name__ == '__main__':
    main()
