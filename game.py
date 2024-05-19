#!/usr/bin/env python


def cinput(prompt: str | None = None) -> str:
    if prompt:
        print(prompt)
    return input().strip().lower()


def ask_yes(question: str) -> bool:
    return cinput(question) == "yes"


def ask_character(name: str) -> None:
    if ask_yes(f"Is your character {name}?"):
        print("Guessed right another time :)")
    else:
        print("That's embarrassing, let's try again.")


def main() -> None:
    # Friend Guesser
    print("Welcome, I'm AkinatorGuyyy!")
    print(
        "Today I will manage to guess your friend! (As long as moon put them in the Database lol)"
    )
    print("Please answer the following questions with 'yes' or 'no'\n")

    # Questions
    if ask_yes("Is your character a male?"):
        if ask_yes("Does your character have way too many alt accounts?"):
            ask_character("Robadog")
        elif ask_yes("Is your character part of Cookiecraft?"):
            if ask_yes("Does your character live in Europe?"):
                if ask_yes("Does your character make YouTube videos?"):
                    if ask_yes("Did your character show their face yet?"):
                        ask_character("Walnutty")
                    elif ask_yes("Does your character live in the Netherlands?"):
                        ask_character("MoonGuyyy")
                    else:
                        ask_character("EitiFrie")
                elif ask_yes("Is your character Swedish?"):
                    ask_character("guahlg")
                else:
                    ask_character("XPierceFire")
            elif ask_yes("Is there an animal in your character's name?"):
                ask_character("ZebraColl")
            elif ask_yes("Does your character have over 1000 subscribers on YouTube?"):
                ask_character("Arbythor")
            else:
                ask_character("Jakerbricks")
        elif ask_yes("Is your character part of the Eternals SMP?"):
            if ask_yes("Did your character show their face yet?"):
                if ask_yes("Does your character live in Europe?"):
                    ask_character("Yukii")
                elif ask_yes("Does your character live in Australia?"):
                    ask_character("StumpsMC")
                elif ask_yes("Does your character have over 1000 subscribers?"):
                    if ask_yes("Is your character associated with a penguin?"):
                        ask_character("CommanderNate")
                    elif ask_yes(
                        "Does your character have a lot of red in their profile picture?"
                    ):
                        ask_character("OddManMC")
                    else:
                        ask_character("Gager")
                elif ask_yes("Does your character skate?"):
                    ask_character("UnderscoreBails")
                elif ask_yes("Is your character a crazy scientist?"):
                    ask_character("MikeyMac")
                elif ask_yes(
                    "Did your character build a massive mansion on the Eternals SMP?"
                ):
                    ask_character("BiglyShronk")
                else:
                    ask_character("ProKitMan")
            elif ask_yes("Does your character have their own survival series?"):
                if ask_yes("Does your character have anything to do with the moon?"):
                    ask_character("MoonGuyyy")
                else:
                    ask_character("Guy Tries")
            elif ask_yes("Does your character draw their own thumbnails?"):
                ask_character("Skraby")
            else:
                ask_character("Veseon")
        elif ask_yes("Does your character code?"):
            if ask_yes("Did your character make Onfim?"):
                ask_character("RestitutorOrbis")
            else:
                ask_character("TurtleGamer")
        elif ask_yes("Has your character revealed their voice yet?"):
            ask_character("LyricWheat")
        elif ask_yes("Does your character live in Europe?"):
            if ask_yes("Does your character love tents?"):
                ask_character("Tentoring")
            else:
                ask_character("ChessGuyyy")
        elif ask_yes("Does your character make YouTube videos?"):
            ask_character("FireFox")
        else:
            ask_character("Mathchag")
    elif ask_yes("Is your character part of the Eternals SMP?"):
        if ask_yes("Does your character have red hair?"):
            ask_character("RedGabs")
        elif ask_yes("Does your character have a secret extra personality?"):
            ask_character("ArmorBlue")
        else:
            ask_character("Sarnose")
    else:
        ask_character("Choco/thulasii")


if __name__ == "__main__":
    main()
