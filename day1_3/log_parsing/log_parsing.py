from datetime import datetime


def get_datetime(line):
    return datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')


def main():
    shutdown_events = []
    for line in open('messages.log', 'r'):
        if 'Shutdown initiated' in line:
            shutdown_events.append(get_datetime(line))

    print(shutdown_events[-1] - shutdown_events[0])


if __name__ == '__main__':
    main()
