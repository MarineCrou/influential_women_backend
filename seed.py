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
            img='hdata:image/webp;base64,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',
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
            bio="Léa Roback (3 November 1903 – 28 August 2000) was a Canadian trade union organizer,[2] social activist, pacifist, and feminist. She campaigned against exclusion, violence, racism and injustice.[3] A polyglot and a suffragist, she was a pioneer of feminism in Quebec.",
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
                img='https://upload.wikimedia.org/wikipedia/commons/a/ad/Hedy_Lamarr_in_The_Heavenly_Body_1944.jpg',
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
            img='https://upload.wikimedia.org/wikipedia/commons/a/ad/Commodore_Grace_M._Hopper%2C_USN_%28covered%29.jpeg',
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