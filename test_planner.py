from agents.planner_agent import planla

while True:
    komut = input("Komut: ")

    if komut == "çık":
        break

    print(planla(komut))