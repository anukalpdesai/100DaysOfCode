import argparse
import sys
import time
from datetime import datetime


class Pomodoro:

    def __init__(self, work_time, short_break, long_break):
        self.work_time = work_time
        self.short_break = short_break
        self.long_break = long_break
        self.max_pomodoro = 1

    def start_pomodoro(self):

        for i in range(9, -1, -1):
            sys.stdout.write('\r')
            sys.stdout.write('Pomodoro starts in {}'.format(i))
            sys.stdout.flush()
            time.sleep(1)

        pomodoro_count = 0
        while pomodoro_count < self.max_pomodoro:
            print()
            print('Pomodoro started: {}'.format(datetime.strftime(datetime.now(), '%B, %d %Y-%m-%d %H:%M:%S')))

            for i in range(1500, 0, -1):
                sys.stdout.write('\r\t\t')
                sys.stdout.write('{:4d}'.format(i))
                sys.stdout.flush()
                time.sleep(1)

            print('Short break: {}'.format(datetime.strftime(datetime.now(), '%B, %d %Y-%m-%d %H:%M:%S')))

            for i in range(600, 0, -1):
                sys.stdout.write('\r\t\t')
                sys.stdout.write('{:3d}'.format(i))
                sys.stdout.flush()
                time.sleep(1)

            pomodoro_count += 1


def main():
    parser = argparse.ArgumentParser(description='Basic Pomodoro application')

    parser.add_argument('-wt', '--work-time',
                        help='work time, default is 25 minutes',
                        default=25,
                        type=int)
    parser.add_argument('-sb', '--short-break',
                        help='short break time, default is 5 minutes',
                        default=5,
                        type=int)
    parser.add_argument('-lg', '--long-break',
                        help='long break time, default is 10 minutes',
                        default=10,
                        type=int)
    args = parser.parse_args()

    p1 = Pomodoro(args.work_time, args.short_break, args.long_break)
    p1.start_pomodoro()

if __name__ == '__main__':
    main()
