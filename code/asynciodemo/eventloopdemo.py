# coding=utf-8

import asyncio

import datetime


# def hello_world(loop):
#     print('Hello World')
#     loop.stop()
#
# loop = asyncio.get_event_loop()
# loop.call_soon(hello_world, loop)
# loop.run_forever()
# loop.close()



def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()

loop = asyncio.get_event_loop()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

loop.run_forever()
loop.close()