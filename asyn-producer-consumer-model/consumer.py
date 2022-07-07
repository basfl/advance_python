import asyncio
from random import random
from time import perf_counter

async def do_work(work_queue: asyncio.Queue, result_queue: asyncio.Queue) -> None:
    while True:
        task_data=work_queue.get()
        task_id=task_data['id']
        number=task_data['number']
        # do some work that takes some time - simulated here with an async sleep
        start = perf_counter()
        await asyncio.sleep(random() * 2)  # random wait time up to 2 seconds
        result = number * number
        end = perf_counter()
         # push result to result queue
        await result_queue.put(
            {
                "task_id": task_id,
                "result": result,
                "time_secs": end - start
            }
        )

        # inform work queue the task is complete
        work_queue.task_done()