from otree.api import (models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


class Constants(BaseConstants):
    name_in_url ='Political_Decision_Making'
    players_per_group = None
    num_rounds = 1
    StandardChoices = [
        [1, 'Disagree strongly'],
        [2, 'Disagree a little'],
        [3, 'Neither agree nor disagree'],
        [4, 'Agree a little'],
        [5, 'Agree strongly'],
    ]

    Survey1Choices = StandardChoices


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    #Part 1 - Demographics Page 2
    age = models.IntegerField(
        label="What is your age?",
                                min=15, max=125)

    gender = models.StringField(
        label="What is your gender?",
                                choices=[["Male", "Male"],
                                         ["Female", "Female"],
                                         ["Prefer not to say", "Prefer not to say"]
                                         ]
                                )

    Income = models.StringField(
        label="What is your income range?",
                                choices=[["Less than 48,500$ per year", "Less than 48,500$ per year"],
                                         ["Between 48,500$ and 145,500$ per year", "Between 48,500$ and 145,500$ per year"],
                                         ["Greater than 145,500$ per year", "Greater than 145,500$ per year"]
                                         ]
                                )

    #Part 2 - The Table and Choice Page 3

    """from tabulate import tabulate

    table_data = [['Violet Party', 'Yellow Party'],

                  [
                      'A sound healthcare system -\n''A single-payer health care system covering all medical needs and\nfree medical care for children under the age of 18 and\nelders over the age of 65',
                      'Fostering Innovation -\nTax incentives and grants for startups and\nsmall businesses,\nsimplifying business regulation,\nscholarships, and\nin-hand experience for students interested\nin entrepreneurial careers.'],
                  [
                      'Housing for all -\nExpanding public housing programs,\nsubsidies, andceilings to help people from\nunprecedented shocks, inflation, etc',
                      'Prioritising Infrastructure and Technology -\nInvesting in cutting-edge technologies including\nArtificial Intelligence, Biotechnology, and clean energy.\nAn intensive boost to the infrastructure\nkeeping the limits of the environment in mind.'],
                  [
                      'Free and Quality Education -\nFree and Quality education\nfrom kindergarten to college and \nrigorous vocational training \nalong with increased funding for schools',
                      'Educational reforms -\nUnderlining STEM (science, technology, English, and Math) education\nand teaching individuals media literacy.\nGranting people a lifelong learning opportunity\nto update their knowledge reserve.\nContinuous education, even after being placed,\nis needed to ensure job mobility.'],
                  [
                      'Greener jobs and Income support - \nCreation of more eco-friendly jobs and safety nets\nfor workers to safeguard their jobs.\nAlso, strict rules to enhance the\nwork-life balance of the labor force.',
                      'Trade and Globalisation -\nA reasonable push to exports,\nmitigating the trade balance.\nAlso acquiring a commanding position in\nthe international arena regarding\nthe thumping global issues. ']
                  ]
    print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))"""

    Choice = models.StringField(
        label="The manifestoes of two hypothetical political parties are given above. Carefully read the passage and decide who you would prefer to rule you.",
                                choices=[["Violet Party", "Violet Party"],
                                         ["Yellow Party", "Yellow Party"]
                                         ]
                                )

  #Part 3 Question Regarding Confirmity Bias Page 4

    NoElec = models.StringField(
        label="How many Elections have you taken part in?",
                                choices=[["1-3", "1-3"],
                                         ["3-5", "3-5"],
                                         ["5-7", "5-7"],
                                         ["More than Seven", "More than Seven"]
                                         ]
                                )
  #Page 5
    LoyalSwing = models.StringField(
        label="Do you consider yourself a swing voter or a loyal voter?",
                                    choices=[["Swing Voter", "Swing Voter"],
                                             ["Loyal Voter", "Loyal Voter"]
                                             ]
                                    )
 #Page 6
    Manifesto = models.StringField(
        label="<ul><li><strong>Question 1</strong>-You always thoroughly read and verify a party's manifesto before voting for them.",
        choices=[["Yes", "Yes"],
                 ["No", "No"],
                 ["I depend on newspapers, broadcasts and social media instead", "I depend on newspapers, broadcasts and social media instead"],
                 ["I depend on my dear ones", "I depend on my dear ones"],
                 ["I collect information from media and dear ones", "I collect information from media and dear ones"]
                 ]
    )


    # More Questions Page 7

    item1A = models.IntegerField(
        label='<ul><li><strong>Question 2</strong>-You have felt guilty for switching sides in an election',
        choices=Constants.Survey1Choices
    )
 # Page 8
    item1B = models.IntegerField(
        label='<ul><li><strong>Question 3</strong>-You are concerned about the sentiments of your dear ones if you switch sides in an election',
        choices=Constants.Survey1Choices
    )
# Page 9
    item1C = models.IntegerField(
        label='<ul><li><strong>Question 4</strong>-You have voted for a party you are unfamiliar with just because your dear ones chose that party',
        choices=Constants.Survey1Choices
    )
  #Page10
    item1D = models.IntegerField(
        label='<ul><li><strong>Question 5</strong>-Your priority is to be loyal to a political party',
        choices=Constants.Survey1Choices
    )

    # Part - 5 Final Question

    FinalQn = models.StringField(
            label="Now, you are allowed to reaffirm your choice. After reading the questionnaire and the glimpses of news, would you like to lock in your initial choice or change it? ",

            choices=[["Yellow Party", "Yellow Party"],
                     ["Violet Party", "Violet Party"]
                     ]
        )

#Part - 4, Pop-up Signals

""" import tkinter

    # If Violet Party
# Page 5
    window1 = tkinter.Tk()
    window1.title("Decision Making")
    label = tkinter.Label(window1,
                          text="68% of the middle-income class strictly believe the violet party\ncould make their lives a lot easier due to the safety nets\nand income support.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window1.mainloop()
#Page 6
    window2 = tkinter.Tk()
    window2.title("Decision Making")
    label = tkinter.Label(window2,
                          text="46% of the voters seem skeptical of the promises of the violet party\nas their manifesto does not venture into the plans\nto generate income.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window2.mainloop()
#Page 7
    window3 = tkinter.Tk()
    window3.title("Decision Making")
    label = tkinter.Label(window3,
                          text="52% of the voters are certain that the violet party intends to increase\nthe tax rates if they come into power.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window3.mainloop()
#Page 8
    window4 = tkinter.Tk()
    window4.title("Decision Making")
    label = tkinter.Label(window4,
                          text="The Yellow Party criticized the Violet Manifesto as being too utopian and\nimpractical. They label such an intent as a\n'cheap trick' to canvas votes.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window4.mainloop()
# Page 9
    window5 = tkinter.Tk()
    window5.title("Decision Making")
    label = tkinter.Label(window5,
                          text="The opposition party hails the Violet Party as a 'freebie party', and warns\npeople that the Violet Party is dabbling with\nhuman emotions.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window5.mainloop()

    # If Yellow Party
# Page 5
    window6 = tkinter.Tk()
    window6.title("Decision Making")
    label = tkinter.Label(window6,
                          text="60% of the youngsters believe the Yellow Party can foster a bright future by investing\nin technology and infrastructure. They also believe\nthat international trade can foster entrepreneurial ventures.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window6.mainloop()
#Page 6
    window7 = tkinter.Tk()
    window7.title("Decision Making")
    label = tkinter.Label(window7,
                          text="43% of the students find the STEM emphasis discriminatory and crowd out several other valuable\ndisciplines. They also speculate that the Yellow Manifesto could\nnarrow down job markets and widen income differentials across jobs.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window7.mainloop()
#Page 7
    window8 = tkinter.Tk()
    window8.title("Decision Making")
    label = tkinter.Label(window8,
                          text="50% of voters believe the manifesto is lopsided and capital-oriented. They find the Yellow Manifesto\nas a fertile ground for the rich to be richer at the cost of the poor.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window8.mainloop()
# Page 8
    window9 = tkinter.Tk()
    window9.title("Decision Making")
    label = tkinter.Label(window9,
                          text="The Violet Party asserts that the Yellow Party won't be a party for the people but only a minor fraction\nof the people. They also question the absence of job security\nand policies to safeguard welfare in the workplace in the opposition's manifesto.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window9.mainloop()
# Page 9
    window10 = tkinter.Tk()
    window10.title("Decision Making")
    label = tkinter.Label(window10,
                          text="The opposition hails the Yellow Party as the country's 'beneficiary of the rich'. They also assert that the Yellow\nParty could rampantly raise the country's corruption rates and\nwealth accumulation.",
                          font=('Times New Roman', 14, 'bold'),
                          fg='black',
                          bg='white'
                          )
    label.pack()
    window10.mainloop()"""

