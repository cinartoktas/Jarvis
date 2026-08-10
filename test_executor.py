from agents.planner_agent import planla
from agents.executor_agent import execute

while True:

    komut = input("Komut: ")

    if komut.lower() == "çık":
        break

    plan = planla(komut)

    print("\nPLAN:")
    print(plan)

    print("\nSONUÇ:")

    sonuc = execute(plan)

    for satir in sonuc:
        print("-", satir)