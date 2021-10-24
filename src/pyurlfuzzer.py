import requests


def req(d):
    r = requests.post("http://{}/{}".format(target, d))
    status = r.status_code
    if status != 404:
        print(f"\t{status=}")


def run():
    with open('common.txt') as file:
        file = list(file)
        l = len(file)
        for i, line in enumerate(file):
            ln = line.rstrip()
            req(ln)
            loading_bar(i + 1, l, ln)


def loading_bar(n, l, ln):
    print("\rFuzzing : {} ({:.2f}%)\tpath=/{}".format("█" * round(n / l * 100 / 2), n / l * 100, ln), end="")


def test_conn(tar):
    try:
        requests.post("http://{}".format(tar))
    except Exception as e:
        print("ERROR: {}".format(e))
        exit()


if __name__ == '__main__':
    target = input("Input target : ")
    test_conn(target)
    print('-' * 50)
    run()
