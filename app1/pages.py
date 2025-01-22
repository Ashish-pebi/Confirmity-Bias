from otree.api import Page


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


# 2
class Demographics(Page):
    template_name = 'app1/Demographics.html'
    form_model = "player"
    form_fields = ['age', 'gender', 'Income']


# 3
class Info(Page):
    form_model = "player"
    form_fields = ['Choice']

    def vars_for_template(self):
        headers = ['<span style="font-size: 1.5em;">Violet Party</span>',
                   '<span style="font-size: 1.5em;">Yellow Party</span>']
        rows = [
            [' <ul><li><strong>A sound healthcare system</strong> - A single-payer health care system covering all medical needs '
             'and free medical care for children under the age of 18 and elders over the age of 65',
             '<ul><li><strong>Fostering Innovation</strong> - Tax incentives and grants for startups and small businesses, '
             'simplifying business regulation, scholarships, and in-hand experience for students '
             'interested in entrepreneurial careers.'],
            ['<ul><li><strong> Housing for all</strong>- Expanding public housing programs, subsidies, and ceilings to help people '
             'from unprecedented shocks, inflation, etc',
             '<ul><li><strong> Prioritising Infrastructure and Technology</strong> - Investing in cutting-edge technologies '
             'including Artificial Intelligence, Biotechnology, and clean energy. An intensive boost to '
             'the infrastructure keeping the limits of the environment in mind.'],
            ['<ul><li><strong> Free and Quality Education</strong> - Free and Quality education from kindergarten to college and '
             'rigorous vocational training along with increased funding for schools',
             '<ul><li><strong>Educational reforms</strong>- Underlining STEM (science, technology, English, and Math) education '
             'and teaching individuals media literacy. Granting people a lifelong learning opportunity '
             'to update their knowledge reserve. Continuous education, even after being placed, '
             'is needed to ensure job mobility.'],
            ['<ul><li><strong> Greener jobs and Income support</strong> - Creation of more eco-friendly jobs and safety nets for '
             'workers to safeguard their jobs. Also, strict rules to enhance the work-life balance of '
             'the laborforce.',
             '<ul><li><strong> Trade and Globalisation</strong>  - A reasonable push to exports, mitigating the trade balance. '
             'Also acquiring a commanding position in the international arena regarding the thumping '
             'global issues.']
        ]
        return {'headers': headers, 'rows': rows}


#4
class Info2(Page):
    template_name = 'app1/Info2.html'
    form_model = "player"
    form_fields = ['NoElec', 'LoyalSwing']


#5
class Info3(Page):

    form_model = 'player'
    form_fields = ['Manifesto']


class Info3(Page):
    form_model = 'player'
    form_fields = ['Manifesto']

    def vars_for_template(self):
        choice = self.player.Choice
        print(f"Player Choice in Info3: {choice}")
        if choice =="Yellow Party":
            additional_text = (
                '<div class="boxed-text">'
                '<ul>'
                '<li><strong>Breaking News:</strong> 60% of the youngsters believe the Yellow Party can foster a bright future by investing in technology and infrastructure. They also believe that international trade can foster entrepreneurial ventures.</li>'
                '</ul>'
                '</div>'
            )
        else:
            additional_text = (
                '<div class="boxed-text">'
                '<ul>'
                '<li><strong>Breaking News:</strong> 68% of the middle-income class strictly believe the Violet Party could make their lives a lot easier due to the safety nets and income support.</li>'
                '</ul>'
                '</div>'
            )
        print(f"Debug: additional_text is: {additional_text}")
        return {'additional_text': additional_text}


#6
class Info4(Page):
    form_model = "player"
    form_fields = ['item1A']

    def vars_for_template(self):
        if self.player.Choice =="Yellow Party":
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -50% of voters believe the Yellow manifesto is lopsided and capital-oriented. They find the Yellow Manifesto"
                " as a fertile ground for the rich to be richer at the cost of the poor. "  '</div>')
        else:
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -46% of the voters seem skeptical of the "
                "promises of the violet party as their manifesto does not"
                " venture into the plans to generate income.""</div>")
        return {'additional_text': additional_text}


#7
class Info5(Page):
    form_model = "player"
    form_fields = ['item1B']

    def vars_for_template(self):
        if self.player.Choice =="Yellow Party":
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -43% of the students find the STEM emphasis discriminatory and could crowd out several other valuable "
                "disciplines. They also speculate that the Yellow Manifesto could narrow down job markets and widen "
                "income differentials across jobs. "  '</div>')
        else:
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -The Yellow Party criticized the Violet Manifesto as being too utopian and impractical. They label "
                "such an intent as a 'cheap trick' to canvas votes. "  '</div>')
        return {'additional_text': additional_text}


#8
class Info6(Page):
    form_model = "player"
    form_fields = ['item1C']

    def vars_for_template(self):
        if self.player.Choice =="Yellow Party":
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -The Violet Party asserts that the Yellow Party won't be a party for the people but only a minor "
                "fraction of the people. They also question the absence of job security and policies to safeguard "
                "welfare in the workplace in the opposition's manifesto. "  '</div>')
        else:
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -52% of the voters are certain that the violet party intends to increase the tax rates if "
                "they come into power. "  '</div>')
        return {'additional_text': additional_text}


#9
class Info7(Page):
    form_model = "player"
    form_fields = ['item1D']

    def vars_for_template(self):
        if self.player.Choice =="Yellow Party":
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -The opposition hails the Yellow Party as the'beneficiary of the rich'. They also "
                "assert that the Yellow Party could rampantly raise the country's corruption rates and "
                "wealth accumulation. "  '</div>')
        else:
            additional_text = (
                '<div class="boxed-text">'"<ul><li><strong>Breaking News</strong> -The opposition party hails the Violet Party as a 'freebie party', and warns people that "
                "the Violet Party is dabbling with human emotions."  '</div>')
        return {'additional_text': additional_text}


#10
class Info8(Page):
    form_model = "player"
    form_fields = ['FinalQn']

class Thankyou(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    Introduction,
    Demographics,
    Info,
    Info2,
    Info3,
    Info4,
    Info5,
    Info6,
    Info7,
    Info8,
    Thankyou]
