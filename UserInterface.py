from FileReader import FileReader
from TravelPlanner import TravelPlanner


def get_input():
    response = input().upper()
    return response


def get_airport_details(reader):
    print("Input the Airport's 3-letter code here: ")
    response = input("\n").upper()
    try:
        reader.airports.get(response).get_details()
    except:
        print("Airport not found")


def get_airport(reader):
    response = input("\n").upper()

    airport = reader.airports.get(response)

    if airport is None:
        print("Airport not found")
    else:
        return airport


def get_aircraft(reader):
    print("Available Aircraft: A319, A320, A321, A330, 737, 747, 757, 767, 777, BAE146, DC8, F50\n"
          "MD11, A400M, C212, V22")
    print("Please input Aircraft Code: ")
    response = input("\n").upper()
    try:
        print(reader.aircraft.get(response))
    except:
        print("Aircraft not found")


def select_aircraft(reader):
    print("Please select a plane for use in planning by its aircraft code.")
    response = input("\n").upper()
    try:
        return reader.aircraft.get(response)
    except:
        print("Aircraft not found")


def main_menu():
    aircraft = None  # Aircraft can be selected and stored throughout menu interaction. Reset when menu opens.

    while True:  # used to ensure the menu cycles.
        reader = FileReader()
        print_menu()
        response = get_input()

        if response == "A":
            get_airport_details(reader)

        elif response == "B":
            get_aircraft(reader)

        elif response == "C":
            aircraft = select_aircraft(reader)
            print(aircraft.code, " has been selected. To change aircraft please run option again")

        elif response == "E":
            if aircraft is None:
                aircraft = select_aircraft(reader)
            destinations = TravelPlanner.plan_journey(reader)
            print(TravelPlanner.journey_details(aircraft, destinations))

        elif response == "D":
            if aircraft is None:
                aircraft = select_aircraft(reader)
            destinations = TravelPlanner.plan_journey(reader)
            result = TravelPlanner.get_shortest_route(destinations, aircraft)
            if result is None:
                print("Aircraft cannot reach all destinations.")
            else:
                print("This is the shortest route between all airports,", result,
                      " Including returning home.")
        elif response == "X":  # breaks out of the infinite loop
            print("Shutting Down. Goodbye!")
            break


def print_menu():
    print("-----------------------------------")
    print("MAIN MENU")
    print("A: Get Airport Information.")
    print("B: Get Aircraft Information.")
    print("C: Select an Aircraft.")
    print("D: Find Shortest Route.")
    print("E: Create User defined flight plan.")
    print("X: ShutDown")
    print("Please Select an Option: \n")


def main():
    main_menu()


if __name__ == '__main__':
    main()
