from ast import Await
import asyncio
from typing import List


async def produce_work(batch: List[dict], work_queu: asyncio.Queue, producer_complete: asyncio.Event):
    print('start produce work')
    for data in batch:
        await work_queu.put(data)
    producer_complete.set()

    
