import asyncio


async def main():
    print("#######")
    #await func1("****")
    task=asyncio.create_task(func1("func1_input"))
    print("finished main")
    return 5
async def func1(txt):
    print(txt)
    await asyncio.sleep(1)
    print("finished func1")


a=asyncio.run(main())
print(a)