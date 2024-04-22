import pprint
from app import app, db
from models.contribution_model import ContributionModel
from models.women_model import WomenProfileModel
from models.user_model import UserModel

with app.app_context():

    try:
        print('Connected to the DB 🎉')
        db.drop_all()
        db.create_all()

        # ? Seeding a user
        print('-------- SEEDING USERS --------')
        Marine_Crouzet = UserModel(
            username='Marine Crou',
            email='m@gmail.com',
            password="Hello123$",
            role="super_admin"
        )

        Emily = UserModel(
            username="Emily Potter",
            email = 'e@e.com',
            password= "harrypotter1234",
            role="contributor"
        )

        Marine_Crouzet.save()
        Emily.save()


        # ? Seeding women profiles
        print('-------- SEEDING WOMEN PROFILES--------')
        Maya_Angelou = WomenProfileModel(name= 'Maya Angelou', is_featured_month= False, user_id=Marine_Crouzet.id)
        Maya_Angelou.save()
        Marie_Curie = WomenProfileModel(name='Marie Curie', is_featured_month= False, user_id=Marine_Crouzet.id)
        Marie_Curie.save()
        Rosa_Parks = WomenProfileModel(name='Rosa Parks', is_featured_month= False, user_id=Marine_Crouzet.id)
        Rosa_Parks.save()
        Malala_Yousafzai = WomenProfileModel(name= 'Malala Yousafzai', is_featured_month= True, user_id=Emily.id)
        Malala_Yousafzai.save()
        Amelia_Earhart = WomenProfileModel(name='Amelia Earhart', is_featured_month= False, user_id=Emily.id)
        Amelia_Earhart.save()
        Ada_Lovelace = WomenProfileModel(name = 'Ada Lovelace',is_featured_month= False, user_id=Emily.id)
        Ada_Lovelace.save()
        Lea_Roback = WomenProfileModel(name = 'Léa Roback',is_featured_month= False, user_id=Marine_Crouzet.id)
        Lea_Roback.save()
        Hedy_Lamarr = WomenProfileModel(name = 'Hedy Lamarr',is_featured_month= False, user_id=Marine_Crouzet.id)
        Hedy_Lamarr.save()
        Margaret_Hamilton = WomenProfileModel(name = 'Margaret Hamilton',is_featured_month= False, user_id=Marine_Crouzet.id)
        Margaret_Hamilton.save()
        Grace_Hopper = WomenProfileModel(name = 'Grace Hopper',is_featured_month= False, user_id=Marine_Crouzet.id)
        Grace_Hopper.save()



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
            field="Literature and Civil Rights Activism",
            woman_id=Maya_Angelou.id,
            user_id=Emily.id,
            status="Approved"
            )
        Maya_Angelou.save()
        pprint.pp(Maya_Angelou.name)

        Marie_Curie = ContributionModel(
            contribution_type="Image Upload/Edit",
            name="Marie Curie",
            date_of_birth='November 7, 1867',
            nationality = 'Polish by birth, naturalized-French',
            img='https://media.lesechos.com/api/v1/images/view/661e92400fadd56b5a60a9e5/1280x720-webp/marie-curie.webp',
            bio="Marie Curie was a pioneering physicist and chemist who became the first woman to win a Nobel Prize and the only person to win Nobel Prizes in two different sciences (Physics and Chemistry). Born in Warsaw, Poland, on November 7, 1867, Curie's research was crucial in the development of x-rays in surgery. Along with her husband Pierre, she discovered polonium and radium, furthering the study of atomic structure.",
            achievements="Scientific Breakthroughs: Discovery of Polonium and Radium. Nobel Prizes in Physics (1903) and Chemistry (1911).",
            additionnal_content="",
            field="Physics and Chemistry",
            woman_id=Marie_Curie.id,  # Assuming `profile_2` is the WomenProfileModel instance for Marie Curie
            user_id=Marine_Crouzet.id,
            status="Approved"
            )
        Marie_Curie.save()
        
        Rosa_Parks = ContributionModel(
            contribution_type="Bio Edit",
            name="Rosa Parks",
            date_of_birth='February 4, 1913',
            nationality = 'American',
            img='https://www.licra.org/wp-content/uploads/2019/12/rosa-2-1.jpg',
            bio="Rosa Parks was an African American civil rights activist whose refusal to surrender her seat to a white passenger on a segregated bus in Montgomery, Alabama, spurred a citywide boycott. Born on February 4, 1913, in Tuskegee, Alabama, her act of defiance became a pivotal symbol of the Civil Rights Movement, leading to the end of legal segregation in America.",
            achievements="The Montgomery Bus Boycott, a pivotal event in the Civil Rights Movement.",
            additionnal_content="",
            status="Approved",
            field="Civil Rights",
            woman_id=Rosa_Parks.id,
            user_id=Marine_Crouzet.id
        )
        Rosa_Parks.save()

        Malala_Yousafzai = ContributionModel(
            contribution_type="Historical Context Addition",
            name="Malala Yousafzai",
            date_of_birth= 'July 12, 1997',
            nationality ='Pakistani',
            img='data:image/webp;base64,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',
            bio="Malala Yousafzai is a Pakistani activist for female education and the youngest Nobel Prize laureate. She was born on July 12, 1997, in Mingora, Pakistan. Malala spoke out against the Taliban's prohibition on the education of girls, which led to an assassination attempt on her life in 2012. Surviving the attack, she continued to speak out on the importance of education for girls worldwide.",
            achievements="Nobel Peace Prize winner in 2014 for her struggle against the suppression of children and young people and for the right of all children to education.",
            additionnal_content="",
            field="Education and Women's Rights",
            woman_id=Malala_Yousafzai.id,
            user_id=Emily.id,
            status="Approved"
        )
        Malala_Yousafzai.save()

        Amelia_Earhart = ContributionModel(
            contribution_type="Correction Submission",
            name="Amelia Earhart",
            date_of_birth='July 24, 1897',
            nationality='American',
            img='https://static.nationalgeographic.fr/files/styles/image_3200/public/d5xxm2.jpg?w=1900&h=1442',
            bio="Amelia Earhart was an American aviation pioneer and author. Born on July 24, 1897, in Atchison, Kansas, she became the first female aviator to fly solo across the Atlantic Ocean, earning the U.S. Distinguished Flying Cross for this record. Earhart was instrumental in the formation of The Ninety-Nines, an organization for female pilots.",
            achievements="First female aviator to fly solo across the Atlantic Ocean.",
            additionnal_content="",
            status="Approved",
            field="Aviation",
            woman_id=Amelia_Earhart.id,
            user_id=Marine_Crouzet.id
        )
        Amelia_Earhart.save()

        Amelia_Earhart_edit2 = ContributionModel(
            contribution_type="Image Upload/Edit",
            name="Amelia Earhart",
            date_of_birth='July 24, 1897',
            nationality='American',
            img='https://static.nationalgeographic.fr/files/styles/image_3200/public/d5xxm2.jpg?w=1900&h=1442',
            bio="Amelia Earhart was an American aviation pioneer and author. Born on July 24, 1897, in Atchison, Kansas, she became the first female aviator to fly solo across the Atlantic Ocean, earning the U.S. Distinguished Flying Cross for this record. Earhart was instrumental in the formation of The Ninety-Nines, an organization for female pilots.",
            achievements="First female aviator to fly solo across the Atlantic Ocean.",
            additionnal_content="",
            status="Approved",
            field="Aviation",
            woman_id=Amelia_Earhart.id, 
            user_id=Emily.id
        )
        Amelia_Earhart_edit2.save()

        Ada_Lovelace = ContributionModel(
            contribution_type="Image Upload/Edit",
            name="Ada Lovelace",
            date_of_birth='December 10, 1815',
            nationality='British',
            img='https://eduscol.education.fr/sti/system/files/images/ressources/pedagogiques/16834/16834-ada-lovelace-portrait-vignette.jpg',
            bio="Ada Lovelace, born on December 10, 1815, in London, England, was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognized as the first algorithm intended to be carried out by a machine, making her the world's first computer programmer.",
            achievements="Recognized as the world's first computer programmer.",
            additionnal_content="Approved",
            status="Approved",
            field="Mathematics and Computer Science",
            woman_id=Ada_Lovelace.id,
            user_id=Emily.id
        )
        Ada_Lovelace.save()

        Lea_Roback = ContributionModel(
            contribution_type="New Profile Creation",
            name="Léa Roback",
            date_of_birth='November 3, 1903',
            nationality='Canadian',
            img='https://upload.wikimedia.org/wikipedia/commons/e/eb/Lea_Roback.jpg',
            bio="Léa Roback (3 November 1903 – 28 August 2000) was a Canadian trade union organizer, social activist, pacifist, and feminist. She campaigned against exclusion, violence, racism and injustice. A polyglot and a suffragist, she was a pioneer of feminism in Quebec.",
            achievements="Social Activist & Feminist",
            additionnal_content="",
            status="Approved",
            field="Aviation",
            woman_id=Lea_Roback.id,
            user_id=Marine_Crouzet.id
        )
        Lea_Roback.save()
        Hedy_Lamarr = ContributionModel(
            contribution_type="New Profile Creation",
            name="Hedy Lamarr",
                date_of_birth='November 9, 1914',
                nationality='Austrian-American',
                img='data:image/webp;base64,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',
                bio="Hedy Lamarr was an Austrian-born American actress and inventor. She developed a radio guidance system for Allied torpedoes during WWII, which used spread spectrum technology that would later form the basis for modern technologies like Wi-Fi and Bluetooth.",
                achievements="Inventor & Actress",
                additionnal_content="",
                status="Approved",
                field="Technology",
                woman_id=Hedy_Lamarr.id,
                user_id=Marine_Crouzet.id
            )
        Hedy_Lamarr.save()

        Margaret_Hamilton = ContributionModel(
            contribution_type="New Profile Creation",
            name="Margaret Hamilton",
            date_of_birth='August 17, 1936',
            nationality='American',
            img='https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Margaret_Hamilton_1995.jpg/480px-Margaret_Hamilton_1995.jpg',
            bio="Margaret Hamilton is an American computer scientist, systems engineer, and business owner. She was the Director of the Software Engineering Division of the MIT Instrumentation Laboratory, which developed on-board flight software for NASA's Apollo space program.",
            achievements="Led Apollo Software Development",
            additionnal_content="",
            status="Approved",
            field="Space Exploration",
            woman_id=Margaret_Hamilton.id,
            user_id=Marine_Crouzet.id
        )
        Margaret_Hamilton.save()

        Grace_Hopper = ContributionModel(
            contribution_type="New Profile Creation",
            name="Grace Hopper",
            date_of_birth='December 9, 1906',
            nationality='American',
            img='https://news.yale.edu/sites/default/files/styles/horizontal_image/public/d6_files/YaleNews_hopper-grace.UNIVAC.102635875-CC_0.jpg?itok=4HL3ETlO',
            bio="Grace Hopper was an American computer scientist and United States Navy rear admiral. A pioneer in the field, she was one of the first programmers of the Harvard Mark I computer, and she developed the first compiler for a computer programming language.",
            achievements="Computer Scientist & Navy Rear Admiral",
            additionnal_content="",
            status="Approved",
            field="Computing",
            woman_id=Grace_Hopper.id,
            user_id=Marine_Crouzet.id
        )
        Grace_Hopper.save()
        
        print('SEED SUCCESSFULL 🎉 🎉 🎉 🎉')
    except Exception as e:
        print(e)