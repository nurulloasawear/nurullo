from colorama import Fore, Style


class Yakka:
    def __init__(self, ism):
        self.ism = ism


class Ishtirokchi:
    def __init__(self, ishtirokchilar):
        self.ishtirokchilar = ishtirokchilar
        self.ball = 0

    def get_display_ism(self):
        return self.ishtirokchilar[0].ism


class Jamoa(Ishtirokchi):
    def __init__(self, jamoa_azolari, jamoa_nomi, sport_turi):
        super().__init__(ishtirokchilar=jamoa_azolari)
        self.jamoa_nomi = jamoa_nomi
        self.sport_turi = sport_turi

    def get_display_ism(self):
        return f"{self.jamoa_nomi} team"


class YakkaIshtirokchi(Ishtirokchi):
    def __init__(self, ishtirokchi):
        super().__init__(ishtirokchilar=[ishtirokchi])


class Musobaqa:
    def __init__(self, ism, ball):
        self.ism = ism
        self.ball = ball

    def musobaqani_boshlash(self, competitor):
        for ishtirokchi in competitor.ishtirokchilar:
            print(f"{ishtirokchi.ism} ishtirokchi, olgan ballni kiriting: ")
            ball = int(input())
            competitor.ball += ball


def ishtirokchilarni_olish(soni):
    print("\n-----------------------------")
    print(f"{Fore.CYAN}Ishtirokchilarni qo'shish ({soni} ishtirokchi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Ishtirokchilarni qo'shishni toxtatish uchun 'stop' yoki 'exit' deb kiriting.{Style.RESET_ALL}")
    print("-----------------------------")

    ishtirokchilar = []
    for i in range(soni):
        print(f"{Fore.CYAN}Ishtirokchi ismini kiriting {i + 1}:{Style.RESET_ALL} ")
        ism = input()

        if ism.lower() == "stop" or ism.lower() == "exit":
            print(f"{Fore.YELLOW}Ishtirokchilarni qo'shish toxtatildi!{Style.RESET_ALL}")
            break

        ishtirokchi = YakkaIshtirokchi(Yakka(ism))
        ishtirokchilar.append(ishtirokchi)
        print(f"{Fore.GREEN}{ism} Ishtirokchi qo'shildi!{Style.RESET_ALL}")

    return ishtirokchilar


def jamoalarni_olish(team_soni, ishtirokchi_soni):
    print("\n-----------------------------")
    print(f"{Fore.CYAN}Adding teams ({team_soni} teams){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Enter {ishtirokchi_soni} name for each team.{Style.RESET_ALL}")
    print("-----------------------------")

    ishtirokchilar = []
    for i in range(team_soni):
        print(f"{Fore.CYAN}\n-----------------------------{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Enter the name of team {i + 1}:{Style.RESET_ALL} ")
        jamoa_nomi = input()

        print(f"{Fore.CYAN}Sport type for team {i + 1}:{Style.RESET_ALL} ")
        sport_turi = input()

        jamoa_azolari = []
        for j in range(ishtirokchi_soni):
            print(f"{Fore.CYAN}Enter the name of team {i + 1}, competitor {j + 1}:{Style.RESET_ALL} ")
            ishtirokchi_ism = input()
            jamoa_azolari.append(Yakka(ishtirokchi_ism))
            print(f"{Fore.GREEN}{ishtirokchi_ism} has been added to the team {jamoa_nomi}!{Style.RESET_ALL}")

        team_competitor = Jamoa(jamoa_azolari, jamoa_nomi, sport_turi)
        ishtirokchilar.append(team_competitor)

    return ishtirokchilar


def musobaqalarni_olish(soni):
    print("\n-----------------------------")
    print(f"{Fore.CYAN}Adding challenges ({soni} challenges){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Each challenge must be rated with 5 ball!{Style.RESET_ALL}")
    print("-----------------------------")

    challenges = []
    for i in range(soni):
        print(f"{Fore.CYAN}Enter the name of challenge {i + 1}:{Style.RESET_ALL}")
        ism = input()
        print(f"{Fore.CYAN}How many point is the challenge worth?:{Style.RESET_ALL}")
        ball = float(input())
        challenge = Musobaqa(ism, ball)
        challenges.append(challenge)
        print(f"{Fore.GREEN}Musobaqa {i + 1} muaffaqiyatli qo'shildi.{Style.RESET_ALL}")

    return challenges


def initiate_challenge_round(ishtirokchilar, challenges):
    print(f"\n{Fore.CYAN}Challange is in progress!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{len(ishtirokchilar)} ishtirokchilar{Style.RESET_ALL}")

    for challenge in challenges:
        print(f"\n{Fore.CYAN}For {challenge.ism}:{Style.RESET_ALL}")
        for ishtirokchi in ishtirokchilar:
            print(f"{Fore.GREEN}{ishtirokchi.get_display_ism()} has started{Style.RESET_ALL} ")
            challenge.musobaqani_boshlash(ishtirokchi)


def display_results(ishtirokchilar):
    ordered_ishtirokchilar = sorted(ishtirokchilar, key=lambda x: x.ball, reverse=True)

    print(f"\n{Fore.GREEN}Winners:{Style.RESET_ALL}")

    position = 1
    for ishtirokchi in ordered_ishtirokchilar:
        print(f"{Fore.YELLOW}{position}-th place {ishtirokchi.get_display_ism()} + {ishtirokchi.ball}{Style.RESET_ALL}")
        position += 1


def main():
    print(f"{Fore.CYAN}***Turnirga xush kelibsiz***{Style.RESET_ALL}")
    response = ""

    ishtirokchilar = []
    challenges = []

    while True:
        print("\n-----------------------------")
        print(f"{Fore.BLUE}1. Ishtirokchilar qo'shish{Style.RESET_ALL}")
        print(f"{Fore.GREEN}2. Jamoa qo'shish{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Musobaqa qo'shish{Style.RESET_ALL}")
        print(f"{Fore.CYAN}4. Musobaqa boshlash{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}5. G'olibni aniqlash{Style.RESET_ALL}")
        print(f"{Fore.RED}6. Chiqish{Style.RESET_ALL}")
        print("-----------------------------")
        response = input(f"{Fore.CYAN}Funksiyani tanlang:{Style.RESET_ALL} ")

        if response == "1":
            ishtirokchilar += ishtirokchilarni_olish(20)
        elif response == "2":
            ishtirokchilar += jamoalarni_olish(4, 5)
        elif response == "3":
            challenges += musobaqalarni_olish(5)
        elif response == "4":
            if not ishtirokchilar or not challenges:
                print(f"{Fore.RED}Participants or challenges haven't been added yet.{Style.RESET_ALL}")
            else:
                initiate_challenge_round(ishtirokchilar, challenges)
                print(f"The challenge has been completed.")
        elif response == "5":
            if not ishtirokchilar:
                print(f"{Fore.RED}Participants haven't been added yet.{Style.RESET_ALL}")
            else:
                display_results(ishtirokchilar)
        elif response == "6":
            print(f"{Fore.MAGENTA}Program has ended. Goodbye.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Incorrect choice. Please try again.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
