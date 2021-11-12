# https://github.com/richeyphu/pyurlfuzzer
import httpx
import asyncio


async def request(urls: list):
    length = len(urls)
    for i, _u in enumerate(urls):
        async with httpx.AsyncClient() as client:
            tasks = (client.get(url) for url in _u)
            reqs = await asyncio.gather(*tasks)
        for r in reqs:
            status = r.status_code
            loading_bar(i + 1, length)
            if status != 404:
                print(f"\rURL={r.url}\t\t{status=}")


def getUrlList():
    with open('common.txt') as file:
        return [f"http://{target}/{line.rstrip()}" for line in file.readlines()]


def splitList(lst: list, n: int):
    # return [lst[i::n] for i in range(n)]
    k, m = divmod(len(lst), n)
    return list((lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)))


def loading_bar(n, l):
    print("\rFuzzing : {} ({:.2f}%)".format("█" * round(n / l * 100 / 2), n / l * 100), end="")


def test_conn(tar):
    try:
        httpx.get("http://{}".format(tar))
    except Exception as e:
        print("ERROR: {}".format(e))
        exit()


def main():
    global target
    target = input("Input target : ")
    test_conn(target)
    urls = getUrlList()
    max_conn = input("Max requests per time : ")
    max_conn = int(max_conn) if max_conn.isnumeric() else 10
    div = int(len(urls) / max_conn)
    splited_urls = splitList(urls, div)

    print('-' * 70)
    asyncio.run(request(splited_urls))
    # asyncio.run(request(urls))
    print('\r' + '-' * 70)

    print("Fuzzing Completed!")


if __name__ == '__main__':
    main()
