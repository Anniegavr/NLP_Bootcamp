import re
"""The patient enters information about their condition prior to visiting a doc. The doctor shall get this information,
so they could prepare for the incoming patient's visit."""
class Disease:
    def __init__(self, name, symptoms):
        self.name_of_disease = name
        self.symptoms = symptoms

    def recommend_doctor(self):
        name = self.symptoms
        if re.findall("kidney", name):
            print("Oh, you should consult a rheumatologist.")
        elif  re.findall("heart", name) or re.findall("chest", name):
            print("Oh, you should consult a cardiologist.")
        elif  re.findall("lung", name) or re.findall("breath", name):
            print("Oh, you should consult a pulmonologist.")
        elif  re.findall("eye", name):
            print("Oh, you should consult a oculist.")
        elif  re.findall("skin", name):
            print("Oh, you should consult a dermatologist.")
        elif  re.findall("stomach", name):
            print("Oh, you should consult a gastrologist.")
        elif  re.findall("mood", name) or re.findall("thoughts", name) or re.findall("sad", name) or re.findall("stressed", name):
            print("Oh, you should consult a psychologist.")
        elif  re.findall("pain", name) and (re.findall("back", name) or re.findall("muscle", name) or re.findall("bone", name) or re.findall("joint", name)):
            print("Oh, you should consult a traumatologist.")
        print("Follow the link: https://www.mayoclinic.org/diseases-conditions/{}".format(self.name_of_disease)+" to learn more.")
        return


class Injury(Disease):
    def __init__(self, name, symptoms):
        super().__init__(name, symptoms)

    def recommend_trauma_doc(self):
        name = self.symptoms
        if re.findall("pain", name) or re.findall("injury", name) or re.findall("broken", name) or re.findall("scratch", name):
            print("Oh, you should consult a traumatologist.")
        return


class Infection(Disease):
    def __init__(self, name, symptoms):
        super().__init__(name, symptoms)

    def recommend_infection_doctor(self):
        name = self.symptoms
        if re.findall("skin", name) or re.findall("rash", name) or re.findall("swelling", name):
            print("Oh, you should consult a infectionist.")



if __name__ == "__main__":
    problem = ""
    sympts = ""
    condition = Disease(problem, sympts)
    answer = input("Do you know the name of your condition?\n")
    if answer == "no":
        answer = input("Did you get injured? yes/no\n")
        if answer == "yes":
            problem = input("What happened?\n")
            sympts = input("Insert the symptoms. The doctor will read this information prior to consulting you.\n (Write them in one line, separated by comma.)\n")
            tr = Injury(problem, sympts)
            tr.recommend_trauma_doc()
        elif answer == "no":
            answer = input("Do you have an infection?\n")
            if answer == "yes":
                problem = input("What kind of infection?\n")
                sympts = input(
                    "Insert the symptoms. The doctor will read this information prior to consulting you.\n (Write them in one line, separated by comma.)\n")
                infection = Infection(problem, sympts)
                infection.recommend_infection_doctor()
            elif answer == "no":
                problem = input("What part of your body is affected?\n")
                sympts = input(
                    "Insert the symptoms. The doctor will read this information prior to consulting you.\n (Write them in one line, separated by comma.)\n")
                condition = Disease(problem, sympts)
                condition.recommend_doctor()

    elif answer == "yes":
        problem = input("What condition do you have?\n")
        sympts = input("Symptoms?\n (Write them in one line, separated by comma)\n")
        condition = Disease(problem, sympts)
        condition.recommend_doctor()
