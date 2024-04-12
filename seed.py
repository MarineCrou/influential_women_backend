import pprint
from app import app, db
from models.contribution_model import ContributionModel
from models.women_model import WomenProfileModel

with app.app_context():

    try:
        print('Connected to the DB 🎉')
        db.drop_all()
        db.create_all()

        # ? Seeding a user
        # print('-------- SEEDING CONTRIBUTORS --------')

        # ? Seeding women profiles
        print('-------- SEEDING WOMEN PROFILES--------')
        profile_1 = WomenProfileModel(is_featured_month= False)
        profile_1.save()
        profile_2 = WomenProfileModel(is_featured_month= False)
        profile_2.save()
        profile_3 = WomenProfileModel(is_featured_month= False)
        profile_3.save()
        profile_4 = WomenProfileModel(is_featured_month= True)
        profile_4.save()
        profile_5 = WomenProfileModel(is_featured_month= False)
        profile_5.save()
        profile_6 = WomenProfileModel(is_featured_month= False)
        profile_6.save()

        # ? Seeding contributions
        print('-------- SEEDING CONTRIBUTIONS --------')
        Maya_Angelou = ContributionModel(
            contribution_type = "Correction Submission",
            name = "Maya Angelou",
            date_of_birth= 'April 4, 1928',
            nationality = 'American',
            img ='https://ici.artv.ca/upload/site/post/picture/2071/64b1a4969e95e.1712164598.jpg', 
            bio = "Maya Angelou was an iconic American writer, poet, and civil rights activist, whose life and work have inspired millions around the world. Born Marguerite Annie Johnson on April 4, 1928, in St. Louis, Missouri, Angelou faced numerous challenges from a young age, including racial discrimination, sexual abuse, and the complexities of identity and belonging. Despite these hardships, or perhaps because of them, she cultivated a remarkable career that spanned several decades and included diverse roles such as dancer, singer, journalist, and educator.", 
            achievements= "Literary Influence: Authored the groundbreaking autobiography `I Know Why the Caged Bird Sings,` which became a key work in American literature for its honest depiction of racial and personal challenges. Cultural Impact: Recited her poem `On the Pulse of Morning` at President Bill Clinton's inauguration in 1993, symbolizing hope and unity, and marking a significant moment in American cultural history.", 
            additionnal_content="",
            woman_id=profile_1.id
            )
        Maya_Angelou.save()
        pprint.pp(Maya_Angelou.name)

        Marie_Curie = ContributionModel(
            contribution_type="Image Upload/Edit",
            name="Marie Curie",
            date_of_birth='November 7, 1867',
            nationality = 'Polish by birth, naturalized-French',
            img='https://example.com/marie-curie.jpg',
            bio="Marie Curie was a pioneering physicist and chemist who became the first woman to win a Nobel Prize and the only person to win Nobel Prizes in two different sciences (Physics and Chemistry). Born in Warsaw, Poland, on November 7, 1867, Curie's research was crucial in the development of x-rays in surgery. Along with her husband Pierre, she discovered polonium and radium, furthering the study of atomic structure.",
            achievements="Scientific Breakthroughs: Discovery of Polonium and Radium. Nobel Prizes in Physics (1903) and Chemistry (1911).",
            additionnal_content="",
            woman_id=profile_2.id  # Assuming `profile_2` is the WomenProfileModel instance for Marie Curie
            )
        Marie_Curie.save()
        
        Rosa_Parks = ContributionModel(
            contribution_type="Bio Edit",
            name="Rosa Parks",
            date_of_birth='February 4, 1913',
            nationality = 'American',
            img='https://example.com/rosa-parks.jpg',
            bio="Rosa Parks was an African American civil rights activist whose refusal to surrender her seat to a white passenger on a segregated bus in Montgomery, Alabama, spurred a citywide boycott. Born on February 4, 1913, in Tuskegee, Alabama, her act of defiance became a pivotal symbol of the Civil Rights Movement, leading to the end of legal segregation in America.",
            achievements="The Montgomery Bus Boycott, a pivotal event in the Civil Rights Movement.",
            additionnal_content="",
            status="Rejected",
            woman_id=profile_3.id
        )
        Rosa_Parks.save()

        Malala_Yousafzai = ContributionModel(
            contribution_type="Historical Context Addition",
            name="Malala Yousafzai",
            date_of_birth= 'July 12, 1997',
            nationality ='Pakistani',
            img='https://example.com/malala-yousafzai.jpg',
            bio="Malala Yousafzai is a Pakistani activist for female education and the youngest Nobel Prize laureate. She was born on July 12, 1997, in Mingora, Pakistan. Malala spoke out against the Taliban's prohibition on the education of girls, which led to an assassination attempt on her life in 2012. Surviving the attack, she continued to speak out on the importance of education for girls worldwide.",
            achievements="Nobel Peace Prize winner in 2014 for her struggle against the suppression of children and young people and for the right of all children to education.",
            additionnal_content="",
            woman_id=profile_4.id
        )
        Malala_Yousafzai.save()

        Amelia_Earhart = ContributionModel(
            contribution_type="Correction Submission",
            name="Amelia Earhart",
            date_of_birth='July 24, 1897',
            nationality='American',
            img='https://example.com/amelia-earhart.jpg',
            bio="Amelia Earhart was an American aviation pioneer and author. Born on July 24, 1897, in Atchison, Kansas, she became the first female aviator to fly solo across the Atlantic Ocean, earning the U.S. Distinguished Flying Cross for this record. Earhart was instrumental in the formation of The Ninety-Nines, an organization for female pilots.",
            achievements="First female aviator to fly solo across the Atlantic Ocean.",
            additionnal_content="",
            status="Approved",
            woman_id=profile_5.id
        )
        Amelia_Earhart.save()

        Ada_Lovelace = ContributionModel(
            contribution_type="Image Upload/Edit",
            name="Ada Lovelace",
            date_of_birth='December 10, 1815',
            nationality='British',
            img='https://example.com/ada-lovelace.jpg',
            bio="Ada Lovelace, born on December 10, 1815, in London, England, was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognized as the first algorithm intended to be carried out by a machine, making her the world's first computer programmer.",
            achievements="Recognized as the world's first computer programmer.",
            additionnal_content="Approved",
            woman_id=profile_6.id
        )
        Ada_Lovelace.save()
        
        print('SEED SUCCESSFULL 🎉 🎉 🎉 🎉')
    except Exception as e:
        print(e)