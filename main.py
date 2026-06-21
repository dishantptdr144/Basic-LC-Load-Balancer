import json
import time
import random

FILE = "servers_usage.json"


def load_data():
    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def process_server(server_name):
    data = load_data()

    # Request start
    data[server_name]["requests"] += 1
    save_data(data)

    print(f"[+] {server_name} handling request")
    print(f"Active Requests: {data[server_name]['requests']}")

    sleep_time = random.randint(3, 5)
    time.sleep(sleep_time)

    # Request complete
    data = load_data()
    data[server_name]["requests"] -= 1
    save_data(data)

    print(f"[-] {server_name} completed request")
    print(f"Active Requests: {data[server_name]['requests']}")

    return {
        "server": server_name,
        "status": "completed",
        "time_taken": sleep_time
    }


def get_best_server():
    data = load_data()

    return min(
        data,
        key=lambda server: data[server]["requests"]
    )


def handle_request():
    best_server = get_best_server()

    print(f"Selected Server: {best_server}")

    return process_server(best_server)


# Test
print(handle_request())