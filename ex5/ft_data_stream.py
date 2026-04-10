import random
from typing import Generator


def gen_event() -> Generator[tuple, None, None]:
    names = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim',
               'release']

    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield (name, action)


def consume_event(name_action_list: list) -> Generator[tuple, None, None]:
    while name_action_list:
        tuple_picked = random.choice(name_action_list)
        name_action_list.remove(tuple_picked)
        yield tuple_picked


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")

    events_list = []
    name_action = ()
    for i in range(10):
        name, action = next(generator)
        events_list.append((name, action))
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")
